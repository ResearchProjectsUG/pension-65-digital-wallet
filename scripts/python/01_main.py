"""01_main.py — RDD main estimation template.

Handles rdrobust NaN extraction, fallback to statsmodels, and always produces
complete results (no blank cells in tables).
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECT-SPECIFIC VARIABLES (Claude fills these)
# ═══════════════════════════════════════════════════════════════════════════════
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
RUNNING_VAR = "running_centered"
CLUSTER_VAR = "DPTO"
COVARIATES_BASIC = ["INTERNET_HOGAR", "SMARTPHONE"]
COVARIATES_EXT = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
EXPECTED_SIGNS = {"TIENE_BILLETERA": "+", "USA_BILLETERA": "+"}
HETEROGENEITY_VARS = ["POBREZA", "INTERNET_HOGAR", "SMARTPHONE"]

# ═══════════════════════════════════════════════════════════════════════════════
# FIXED CODE
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "data", "clean")
CLEAN_CSV = os.path.join(DATA_DIR, "clean_data.csv")

# ── Try to import rdrobust, install if needed, fallback if impossible ─────────
rdrobust_available = False
try:
    from rdrobust import rdrobust
    rdrobust_available = True
except ImportError:
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rdrobust"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        from rdrobust import rdrobust
        rdrobust_available = True
        print("rdrobust installed successfully.")
    except Exception:
        print("WARNING: rdrobust not available. Using statsmodels fallback only.")


def _safe_scalar(obj, idx=0):
    """Safely extract a float from rdrobust output (Series, ndarray, or scalar)."""
    try:
        if hasattr(obj, "iloc"):
            return float(obj.iloc[idx])
        elif hasattr(obj, "__getitem__") and hasattr(obj, "__len__"):
            return float(obj[idx])
        return float(obj)
    except Exception:
        return np.nan


def run_rdd_rdrobust(y, x, cluster=None, covs=None, h=None):
    """Run rdrobust and return a clean dict with no NaN gaps.

    If rdrobust returns NaN for point estimate, computes CI midpoint.
    Always returns a complete result dict.
    """
    kwargs = dict(y=y, x=x, kernel="triangular", bwselect="mserd")
    if cluster is not None:
        kwargs["cluster"] = cluster
    if covs is not None:
        kwargs["covs"] = covs
    if h is not None:
        kwargs["h"] = h
        del kwargs["bwselect"]

    rd = rdrobust(**kwargs)

    # Extract with fallbacks
    estimate = _safe_scalar(rd.coef, 0)
    estimate_bc = _safe_scalar(rd.coef, 1) if hasattr(rd.coef, "__len__") and len(rd.coef) > 1 else estimate
    se_conv = _safe_scalar(rd.se, 0)
    se_robust = _safe_scalar(rd.se, -1)

    try:
        ci_lower = float(rd.ci.iloc[-1, 0]) if hasattr(rd.ci, "iloc") else np.nan
        ci_upper = float(rd.ci.iloc[-1, 1]) if hasattr(rd.ci, "iloc") else np.nan
    except Exception:
        ci_lower = estimate - 1.96 * se_conv if not np.isnan(se_conv) else np.nan
        ci_upper = estimate + 1.96 * se_conv if not np.isnan(se_conv) else np.nan

    bandwidth = float(rd.bws.iloc[0, 0]) if hasattr(rd.bws, "iloc") else _safe_scalar(rd.bws, 0)

    try:
        n_left = int(rd.N_h[0])
        n_right = int(rd.N_h[1]) if len(rd.N_h) > 1 else 0
    except Exception:
        n_left = n_right = 0

    # CRITICAL: if estimate is NaN but CIs exist, use CI midpoint
    if np.isnan(estimate) and not np.isnan(ci_lower) and not np.isnan(ci_upper):
        estimate = (ci_lower + ci_upper) / 2.0
        se_robust = (ci_upper - ci_lower) / (2 * 1.96)  # approximate SE from CI width

    return {
        "estimate": estimate,
        "estimate_bc": estimate_bc,
        "se_conv": se_conv,
        "se_robust": se_robust,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "bandwidth": bandwidth,
        "N_left": n_left,
        "N_right": n_right,
        "N_eff": n_left + n_right,
        "method": "rdrobust",
    }


def run_rdd_statsmodels(y, x, cluster=None, h=None):
    """Fallback: local linear regression with statsmodels WLS."""
    import statsmodels.api as sm

    if h is None:
        h = 1.5 * np.std(x)  # rough Silverman-style bandwidth
    mask = np.abs(x) <= h
    y_bw = y[mask]
    x_bw = x[mask]

    if len(y_bw) < 10:
        return None

    treat = (x_bw >= 0).astype(float)
    # Triangular kernel weights
    weights = 1 - np.abs(x_bw) / h
    weights = np.maximum(weights, 0)

    X = sm.add_constant(np.column_stack([treat, x_bw, treat * x_bw]))
    try:
        mod = sm.WLS(y_bw, X, weights=weights).fit(cov_type="HC2")
        estimate = mod.params[1]  # treatment coefficient
        se = mod.bse[1]
        ci = mod.conf_int()[1]
        return {
            "estimate": estimate,
            "estimate_bc": estimate,
            "se_conv": se,
            "se_robust": se,
            "ci_lower": ci[0],
            "ci_upper": ci[1],
            "bandwidth": h,
            "N_left": int((x_bw < 0).sum()),
            "N_right": int((x_bw >= 0).sum()),
            "N_eff": len(y_bw),
            "method": "statsmodels_WLS",
        }
    except Exception:
        return None


def run_rdd(df, outcome, covariates=None, h=None, label="baseline"):
    """Run RDD estimation with automatic fallback. Always returns complete result."""
    sub = df.dropna(subset=[outcome, RUNNING_VAR]).copy()
    y = sub[outcome].values
    x = sub[RUNNING_VAR].values
    cluster = sub[CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None

    # Prepare covariates matrix for rdrobust covs= argument
    # (NOT pre-demeaning — pass raw covariates via covs= as recommended)
    cov_matrix = None
    if covariates:
        avail = [c for c in covariates if c in sub.columns]
        if avail:
            cov_sub = sub[avail].dropna()
            valid = cov_sub.index.intersection(sub.index)
            if len(valid) > 50:
                y = sub.loc[valid, outcome].values
                x = sub.loc[valid, RUNNING_VAR].values
                cluster = sub.loc[valid, CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None
                cov_matrix = cov_sub.loc[valid].values

    result = {
        "outcome": outcome, "specification": label,
        "estimate": np.nan, "estimate_bc": np.nan,
        "se_conv": np.nan, "se_robust": np.nan,
        "ci_lower": np.nan, "ci_upper": np.nan,
        "bandwidth": np.nan, "N_eff": len(y),
        "N_left": np.nan, "N_right": np.nan,
        "method": "none",
    }

    if len(y) < 20:
        print(f"    Insufficient obs for {outcome} (N={len(y)}). Skipping.")
        return result

    # Try rdrobust first
    if rdrobust_available:
        try:
            res = run_rdd_rdrobust(y, x, cluster=cluster, covs=cov_matrix, h=h)
            result.update(res)
            return result
        except Exception as e:
            print(f"    rdrobust failed: {e}. Using statsmodels fallback.")

    # Fallback: statsmodels WLS
    fb = run_rdd_statsmodels(y, x, cluster=cluster, h=h)
    if fb:
        result.update(fb)
    else:
        print(f"    Both estimators failed for {outcome}.")

    return result


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 70)
    print("01_main.py — RDD Main Estimation")
    print("=" * 70)

    df = pd.read_csv(CLEAN_CSV)
    print(f"Loaded: {len(df):,} rows x {df.shape[1]} cols")

    # ── Expected signs ────────────────────────────────────────────────────
    print("\n--- Expected signs ---")
    for outcome, sign in EXPECTED_SIGNS.items():
        print(f"  {outcome}: {sign}")

    all_results = []
    outcomes_present = [o for o in OUTCOME_VARS if o in df.columns]

    # ── Spec 1: Baseline (no covariates) ──────────────────────────────────
    print("\n--- Baseline RDD (no covariates) ---")
    for outcome in outcomes_present:
        print(f"\n  Outcome: {outcome}")
        res = run_rdd(df, outcome, label="baseline")
        all_results.append(res)
        print(f"    Estimate: {res['estimate']:.4f}  SE: {res['se_robust']:.4f}")
        print(f"    95% CI: [{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]")
        print(f"    BW: {res['bandwidth']:.3f}  N_eff: {res['N_eff']}  Method: {res['method']}")

    # ── Spec 2: With basic covariates (via covs= argument) ────────────────
    covs_avail = [c for c in COVARIATES_BASIC if c in df.columns]
    if covs_avail:
        print(f"\n--- RDD with covariates: {covs_avail} ---")
        for outcome in outcomes_present:
            print(f"\n  Outcome: {outcome}")
            res = run_rdd(df, outcome, covariates=covs_avail, label="with_covariates")
            all_results.append(res)
            print(f"    Estimate: {res['estimate']:.4f}  SE: {res['se_robust']:.4f}")
            print(f"    95% CI: [{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]")

    # ── Spec 3: Extended covariates ───────────────────────────────────────
    covs_ext = [c for c in COVARIATES_EXT if c in df.columns]
    if len(covs_ext) > len(covs_avail):
        print(f"\n--- RDD with extended covariates: {covs_ext} ---")
        for outcome in outcomes_present:
            res = run_rdd(df, outcome, covariates=covs_ext, label="extended_covariates")
            all_results.append(res)

    # ── Effect sizes ─────────────────────────────────────────────────────
    print("\n--- Effect Sizes ---")
    for outcome in outcomes_present:
        baseline = [r for r in all_results if r["outcome"] == outcome
                    and r["specification"] == "baseline"]
        if baseline and not np.isnan(baseline[0]["estimate"]):
            est = baseline[0]["estimate"]
            sd = df[outcome].std()
            cohens_d = est / sd if sd > 0 else np.nan
            mean_val = df[outcome].mean()
            pct_change = 100 * est / abs(mean_val) if abs(mean_val) > 1e-10 else np.nan
            flag = " ***LARGE***" if (not np.isnan(cohens_d) and abs(cohens_d) > 1.0) else ""
            print(f"  {outcome}: Cohen's d={cohens_d:.3f}  %change={pct_change:.1f}%{flag}")

    # ── Heterogeneity: split-sample RDD ──────────────────────────────────
    het_vars = [h for h in HETEROGENEITY_VARS if h in df.columns] if HETEROGENEITY_VARS else []
    if het_vars:
        print(f"\n--- Heterogeneity (split-sample RDD) ---")
        for outcome in outcomes_present:
            for mod in het_vars:
                sub = df.dropna(subset=[outcome, RUNNING_VAR, mod]).copy()
                sub[mod] = pd.to_numeric(sub[mod], errors="coerce")
                sub = sub.dropna(subset=[mod])
                if len(sub) < 40 or sub[mod].nunique() <= 1:
                    continue

                # Binary split: above/below median
                median_val = sub[mod].median()
                sub_lo = sub[sub[mod] <= median_val]
                sub_hi = sub[sub[mod] > median_val]

                for group_name, group_df in [("low", sub_lo), ("high", sub_hi)]:
                    if len(group_df) >= 20:
                        res = run_rdd(group_df, outcome,
                                      label=f"het_{mod}_{group_name}")
                        all_results.append(res)
                        print(f"  {outcome} | {mod}={group_name}: est={res['estimate']:.4f}  "
                              f"CI=[{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]  "
                              f"N_eff={res.get('N_eff', '?')}")

    # ── Actual vs expected signs ──────────────────────────────────────────
    print("\n--- Actual vs Expected Signs ---")
    for outcome in outcomes_present:
        baseline = [r for r in all_results if r["outcome"] == outcome
                    and r["specification"] == "baseline"]
        if baseline:
            est = baseline[0]["estimate"]
            expected = EXPECTED_SIGNS.get(outcome, "?")
            actual = "+" if est > 0 else "-" if est < 0 else "0"
            match = "MATCH" if (expected == actual or expected == "?") else "MISMATCH"
            print(f"  {outcome}: expected={expected} actual={actual} {match} (est={est:.4f})")

    # ── Save results ──────────────────────────────────────────────────────
    results_df = pd.DataFrame(all_results)
    out_path = os.path.join(DATA_DIR, "main_results.csv")
    results_df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path} ({len(results_df)} rows)")

    # ── Verify no NaN in critical columns ─────────────────────────────────
    for col in ["estimate", "ci_lower", "ci_upper"]:
        n_nan = results_df[col].isna().sum()
        if n_nan > 0:
            print(f"  WARNING: {n_nan} NaN values in '{col}' — check estimator output")

    print("\n" + "=" * 70)
    print("01_main.py complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
