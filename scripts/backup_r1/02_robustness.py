"""02_robustness.py — RDD robustness template.

All required RDD robustness checks in one file:
1. McCrary/rddensity manipulation test (with figure)
2. Placebo outcomes
3. Bandwidth sensitivity (h/2, h_opt, 2h)
4. Donut-hole specifications
5. Covariate balance AT BANDWIDTH (not full sample)
6. Polynomial order sensitivity
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
PRIMARY_OUTCOME = "TIENE_BILLETERA"
RUNNING_VAR = "running_centered"
CLUSTER_VAR = "DPTO"
COVARIATES = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
PLACEBO_OUTCOMES = ["INTERNET_HOGAR", "SMARTPHONE"]

# ═══════════════════════════════════════════════════════════════════════════════
# FIXED CODE
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "data", "clean")
FIGURES_DIR = os.path.join(SCRIPT_DIR, "..", "..", "paper", "figures")
CLEAN_CSV = os.path.join(DATA_DIR, "clean_data.csv")

os.makedirs(FIGURES_DIR, exist_ok=True)

# Import rdrobust (same pattern as 01_main.py)
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
    except Exception:
        pass

# Import from 01_main.py to reuse the safe RDD runner
sys.path.insert(0, SCRIPT_DIR)
try:
    from importlib import import_module
    main_mod = import_module("01_main")
    run_rdd = main_mod.run_rdd
    _safe_scalar = main_mod._safe_scalar
except Exception:
    # Inline fallback
    def _safe_scalar(obj, idx=0):
        try:
            if hasattr(obj, "iloc"):
                return float(obj.iloc[idx])
            elif hasattr(obj, "__getitem__"):
                return float(obj[idx])
            return float(obj)
        except Exception:
            return np.nan

    def run_rdd(df, outcome, covariates=None, h=None, label="test"):
        """Minimal RDD fallback using statsmodels."""
        import statsmodels.api as sm
        sub = df.dropna(subset=[outcome, RUNNING_VAR]).copy()
        y = sub[outcome].values
        x = sub[RUNNING_VAR].values
        if h is None:
            x_std = np.std(x)
            if x_std < 1e-10:
                return {"outcome": outcome, "specification": label,
                        "estimate": np.nan, "se_robust": np.nan,
                        "ci_lower": np.nan, "ci_upper": np.nan,
                        "bandwidth": 0, "N_eff": 0, "method": "none_zero_variance"}
            h = 1.5 * x_std
        mask = np.abs(x) <= h
        y_bw, x_bw = y[mask], x[mask]
        if len(y_bw) < 10:
            return {"outcome": outcome, "specification": label,
                    "estimate": np.nan, "se_robust": np.nan,
                    "ci_lower": np.nan, "ci_upper": np.nan,
                    "bandwidth": h, "N_eff": 0, "method": "none"}
        treat = (x_bw >= 0).astype(float)
        weights = np.maximum(1 - np.abs(x_bw) / h, 0)
        X = sm.add_constant(np.column_stack([treat, x_bw, treat * x_bw]))
        mod = sm.WLS(y_bw, X, weights=weights).fit(cov_type="HC2")
        ci = mod.conf_int()[1]
        return {"outcome": outcome, "specification": label,
                "estimate": mod.params[1], "se_robust": mod.bse[1],
                "ci_lower": ci[0], "ci_upper": ci[1],
                "bandwidth": h, "N_eff": len(y_bw),
                "N_left": int((x_bw < 0).sum()), "N_right": int((x_bw >= 0).sum()),
                "method": "statsmodels_WLS"}


def main():
    print("=" * 70)
    print("02_robustness.py — RDD Robustness Checks")
    print("=" * 70)

    df = pd.read_csv(CLEAN_CSV)
    print(f"Loaded: {len(df):,} rows x {df.shape[1]} cols")

    all_results = []
    y_all = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])[RUNNING_VAR].values

    # ══════════════════════════════════════════════════════════════════════
    # 1. McCrary / rddensity MANIPULATION TEST
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 1. McCrary/rddensity manipulation test ---")
    print("  Expected: p > 0.05 (no sorting at threshold)")
    mccrary_pval = np.nan
    try:
        from rddensity import rddensity
        rd_den = rddensity(X=y_all, c=0)
        # Extract p-value
        try:
            mccrary_pval = rd_den.p if hasattr(rd_den, "p") else np.nan
        except Exception:
            pass
        print(f"  rddensity p-value: {mccrary_pval}")

        # Save density plot
        try:
            from rddensity import rdplotdensity
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            rdplotdensity(rd_den, X=y_all)
            fig_path = os.path.join(FIGURES_DIR, "figure_mccrary_density.png")
            plt.savefig(fig_path, dpi=150, bbox_inches="tight")
            plt.close("all")
            print(f"  Saved: {fig_path}")
        except Exception as e:
            print(f"  Density plot failed: {e}")
    except ImportError:
        print("  rddensity not installed. Skipping.")
    except Exception as e:
        print(f"  McCrary test failed: {e}")

    all_results.append({
        "test": "mccrary", "outcome": "density", "estimate": mccrary_pval,
        "se_robust": np.nan, "ci_lower": np.nan, "ci_upper": np.nan,
        "bandwidth": np.nan, "N_eff": len(y_all), "method": "rddensity",
    })

    # ══════════════════════════════════════════════════════════════════════
    # 2. PLACEBO OUTCOMES
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 2. Placebo outcomes ---")
    print("  Expected: NULL effect (treatment should not affect placebos)")
    placebo_present = [p for p in PLACEBO_OUTCOMES if p in df.columns]
    if not placebo_present:
        print("  No placebo outcomes found.")

    for pv in placebo_present:
        res = run_rdd(df, pv, label="placebo")
        res["test"] = "placebo"
        all_results.append(res)
        sig = "*" if res.get("ci_lower", -1) > 0 or res.get("ci_upper", 1) < 0 else ""
        print(f"  {pv}: est={res['estimate']:.4f} CI=[{res.get('ci_lower', np.nan):.4f}, "
              f"{res.get('ci_upper', np.nan):.4f}] {sig}")

    # ══════════════════════════════════════════════════════════════════════
    # 3. BANDWIDTH SENSITIVITY
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 3. Bandwidth sensitivity ---")

    # First get optimal bandwidth
    baseline = run_rdd(df, PRIMARY_OUTCOME, label="bw_optimal")
    h_opt = baseline.get("bandwidth", 2.0)
    if np.isnan(h_opt) or h_opt <= 0:
        h_opt = 2.0

    for multiplier, label in [(0.5, "h_half"), (1.0, "h_optimal"), (2.0, "h_double")]:
        h = h_opt * multiplier
        res = run_rdd(df, PRIMARY_OUTCOME, h=h, label=f"bandwidth_{label}")
        res["test"] = f"bandwidth_{label}"
        all_results.append(res)
        print(f"  {label} (h={h:.2f}): est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}] "
              f"N_eff={res.get('N_eff', '?')}")

    # ══════════════════════════════════════════════════════════════════════
    # 4. DONUT-HOLE
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 4. Donut-hole specifications ---")
    for donut in [0.5, 1.0]:
        df_donut = df[np.abs(df[RUNNING_VAR]) >= donut].copy()
        res = run_rdd(df_donut, PRIMARY_OUTCOME, label=f"donut_{donut}")
        res["test"] = f"donut_{donut}"
        all_results.append(res)
        print(f"  Exclude |x|<{donut}: est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}] "
              f"N={len(df_donut)}")

    # ══════════════════════════════════════════════════════════════════════
    # 5. COVARIATE BALANCE AT BANDWIDTH (not full sample)
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n--- 5. Covariate balance at bandwidth (h={h_opt:.2f}) ---")
    print("  Expected: all insignificant (no discontinuity in covariates)")

    # Filter to within bandwidth FIRST, then test
    df_bw = df[np.abs(df[RUNNING_VAR]) <= h_opt].copy()
    print(f"  Observations within bandwidth: {len(df_bw)}")

    cov_avail = [c for c in COVARIATES if c in df_bw.columns]
    for cov in cov_avail:
        res = run_rdd(df_bw, cov, h=h_opt, label="covariate_balance")
        res["test"] = "covariate_balance"
        res["outcome"] = cov
        all_results.append(res)
        sig = " *IMBALANCED*" if (res.get("ci_lower", -1) > 0 or res.get("ci_upper", 1) < 0) else ""
        print(f"  {cov:20s}: est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}]{sig}")

    # ══════════════════════════════════════════════════════════════════════
    # 6. POLYNOMIAL ORDER SENSITIVITY
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 6. Polynomial order sensitivity ---")
    # Linear (p=1) is the baseline. Also report quadratic (p=2).
    if rdrobust_available:
        sub = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])
        y_sub = sub[PRIMARY_OUTCOME].values
        x_sub = sub[RUNNING_VAR].values
        cl_sub = sub[CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None

        for p_order, p_label in [(1, "linear"), (2, "quadratic")]:
            try:
                kwargs = dict(y=y_sub, x=x_sub, p=p_order,
                              kernel="triangular", bwselect="mserd")
                if cl_sub is not None:
                    kwargs["cluster"] = cl_sub
                rd = rdrobust(**kwargs)
                est = _safe_scalar(rd.coef, 0)
                try:
                    ci_lo = float(rd.ci.iloc[-1, 0])
                    ci_hi = float(rd.ci.iloc[-1, 1])
                except Exception:
                    ci_lo = ci_hi = np.nan
                # CI midpoint fallback
                if np.isnan(est) and not np.isnan(ci_lo) and not np.isnan(ci_hi):
                    est = (ci_lo + ci_hi) / 2.0

                bw = float(rd.bws.iloc[0, 0]) if hasattr(rd.bws, "iloc") else np.nan
                n_eff = int(rd.N_h[0]) + int(rd.N_h[1]) if hasattr(rd.N_h, "__getitem__") else 0

                res = {"test": f"polynomial_{p_label}", "outcome": PRIMARY_OUTCOME,
                       "estimate": est, "se_robust": _safe_scalar(rd.se, -1),
                       "ci_lower": ci_lo, "ci_upper": ci_hi,
                       "bandwidth": bw, "N_eff": n_eff, "method": "rdrobust"}
                all_results.append(res)
                print(f"  p={p_order} ({p_label}): est={est:.4f} "
                      f"CI=[{ci_lo:.4f}, {ci_hi:.4f}] N_eff={n_eff}")
            except Exception as e:
                print(f"  p={p_order} ({p_label}): failed ({e})")
    else:
        print("  rdrobust not available — skipping polynomial sensitivity.")

    # ══════════════════════════════════════════════════════════════════════
    # 7. PLACEBO CUTOFF TEST (false cutoffs away from true threshold)
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 7. Placebo cutoff test ---")
    print("  Expected: NULL effect at false cutoffs")

    sub_pc = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR]).copy()
    x_vals = sub_pc[RUNNING_VAR].values
    n_unique_x = len(np.unique(x_vals))

    if n_unique_x < 10:
        print(f"  Running variable has only {n_unique_x} unique values (discrete).")
        print(f"  Placebo cutoff test requires sufficient mass on both sides — may skip some cutoffs.")

    # Test at 25th and 75th percentile of running variable (left and right of cutoff)
    for pctile, label in [(25, "left_placebo"), (75, "right_placebo")]:
        cutoff = np.percentile(x_vals, pctile)
        if abs(cutoff) < 0.1:  # too close to real cutoff
            print(f"  {label}: cutoff={cutoff:.2f} too close to 0. Skipping.")
            continue

        # For discrete running variables: snap cutoff to actual data point
        if n_unique_x < 20:
            unique_sorted = np.sort(np.unique(x_vals))
            cutoff = unique_sorted[np.argmin(np.abs(unique_sorted - cutoff))]

        # Re-center around placebo cutoff
        df_placebo_c = sub_pc.copy()
        df_placebo_c["_running_placebo"] = df_placebo_c[RUNNING_VAR] - cutoff

        # Only use observations on one side of the real cutoff
        if cutoff < 0:
            df_placebo_c = df_placebo_c[df_placebo_c[RUNNING_VAR] < 0]
        else:
            df_placebo_c = df_placebo_c[df_placebo_c[RUNNING_VAR] >= 0]

        if len(df_placebo_c) >= 30:
            # Run RDD at placebo cutoff
            y_pc = df_placebo_c[PRIMARY_OUTCOME].values
            x_pc = df_placebo_c["_running_placebo"].values

            try:
                if rdrobust_available:
                    rd_pc = rdrobust(y=y_pc, x=x_pc, kernel="triangular", bwselect="mserd")
                    est_pc = _safe_scalar(rd_pc.coef, 0)
                    try:
                        ci_lo_pc = float(rd_pc.ci.iloc[-1, 0])
                        ci_hi_pc = float(rd_pc.ci.iloc[-1, 1])
                    except Exception:
                        ci_lo_pc = ci_hi_pc = np.nan
                    if np.isnan(est_pc) and not np.isnan(ci_lo_pc) and not np.isnan(ci_hi_pc):
                        est_pc = (ci_lo_pc + ci_hi_pc) / 2.0

                    sig = " *FAILS*" if (ci_lo_pc > 0 or ci_hi_pc < 0) else ""
                    print(f"  {label} (cutoff={cutoff:.2f}): est={est_pc:.4f}  "
                          f"CI=[{ci_lo_pc:.4f}, {ci_hi_pc:.4f}]{sig}")

                    all_results.append({
                        "test": f"placebo_cutoff_{label}", "outcome": PRIMARY_OUTCOME,
                        "estimate": est_pc, "se_robust": _safe_scalar(rd_pc.se, -1),
                        "ci_lower": ci_lo_pc, "ci_upper": ci_hi_pc,
                        "bandwidth": float(rd_pc.bws.iloc[0, 0]) if hasattr(rd_pc.bws, "iloc") else np.nan,
                        "N_eff": len(df_placebo_c), "method": "rdrobust_placebo_cutoff",
                    })
                else:
                    import statsmodels.api as sm
                    h_pc = 1.5 * np.std(x_pc)
                    mask = np.abs(x_pc) <= h_pc
                    y_bw = y_pc[mask]
                    x_bw = x_pc[mask]
                    if len(y_bw) >= 10:
                        treat = (x_bw >= 0).astype(float)
                        weights = np.maximum(1 - np.abs(x_bw) / h_pc, 0)
                        X_pc = sm.add_constant(np.column_stack([treat, x_bw, treat * x_bw]))
                        mod = sm.WLS(y_bw, X_pc, weights=weights).fit(cov_type="HC2")
                        print(f"  {label} (cutoff={cutoff:.2f}): est={mod.params[1]:.4f}  "
                              f"p={mod.pvalues[1]:.4f}")
            except Exception as e:
                print(f"  {label}: failed ({e})")

    # ══════════════════════════════════════════════════════════════════════
    # 8. PERMUTATION INFERENCE (randomized cutoffs)
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 8. Permutation inference (randomized cutoffs) ---")

    sub_perm = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR]).copy()
    if len(sub_perm) >= 30:
        try:
            import statsmodels.api as sm

            y_perm = sub_perm[PRIMARY_OUTCOME].values
            x_perm = sub_perm[RUNNING_VAR].values

            # Get estimate at true cutoff
            x_std_perm = np.std(x_perm)
            if x_std_perm < 1e-10:
                print("  Running variable has zero variance. Skipping permutation test.")
                raise ValueError("zero variance")
            h_perm = 1.5 * x_std_perm
            mask_real = np.abs(x_perm) <= h_perm
            y_bw_real = y_perm[mask_real]
            x_bw_real = x_perm[mask_real]
            treat_real = (x_bw_real >= 0).astype(float)
            weights_real = np.maximum(1 - np.abs(x_bw_real) / h_perm, 0)
            X_real = sm.add_constant(np.column_stack([treat_real, x_bw_real, treat_real * x_bw_real]))
            mod_real = sm.WLS(y_bw_real, X_real, weights=weights_real).fit()
            t_real = mod_real.tvalues[1]

            # Permute: use random cutoffs
            n_perms = 500
            rng = np.random.default_rng(42)
            x_quantiles = np.percentile(x_perm, np.linspace(10, 90, 50))
            t_perms = []

            for _ in range(n_perms):
                c_fake = rng.choice(x_quantiles)
                x_shifted = x_perm - c_fake
                mask_p = np.abs(x_shifted) <= h_perm
                y_bw_p = y_perm[mask_p]
                x_bw_p = x_shifted[mask_p]
                if len(y_bw_p) < 10:
                    continue
                treat_p = (x_bw_p >= 0).astype(float)
                weights_p = np.maximum(1 - np.abs(x_bw_p) / h_perm, 0)
                X_p = sm.add_constant(np.column_stack([treat_p, x_bw_p, treat_p * x_bw_p]))
                try:
                    mod_p = sm.WLS(y_bw_p, X_p, weights=weights_p).fit()
                    t_perms.append(mod_p.tvalues[1])
                except Exception:
                    pass

            success_rate = len(t_perms) / n_perms if n_perms > 0 else 0
            if len(t_perms) > 100:
                t_perms = np.array(t_perms)
                perm_pval = np.mean(np.abs(t_perms) >= np.abs(t_real))
                print(f"  t_real: {t_real:.3f}")
                print(f"  Permutation p-value ({len(t_perms)} valid, "
                      f"{success_rate:.0%} success rate): {perm_pval:.4f}")
                if success_rate < 0.5:
                    print(f"  WARNING: Low success rate ({success_rate:.0%}). "
                          f"P-value may be unreliable.")

                all_results.append({
                    "test": "permutation_inference", "outcome": PRIMARY_OUTCOME,
                    "estimate": t_real, "se_robust": np.nan,
                    "pvalue": perm_pval,
                    "ci_lower": np.nan, "ci_upper": np.nan,
                    "bandwidth": h_perm, "N_eff": len(sub_perm),
                    "method": f"permutation_{len(t_perms)}",
                })
        except Exception as e:
            print(f"  Permutation inference failed: {e}")

    # ══════════════════════════════════════════════════════════════════════
    # 9. MULTIPLE HYPOTHESIS CORRECTION (BH FDR)
    # ══════════════════════════════════════════════════════════════════════
    print("\n--- 9. Multiple hypothesis correction (BH FDR) ---")
    testable = [r for r in all_results
                if "pvalue" in r and pd.notna(r.get("pvalue")) and r.get("pvalue", 1) < 1]
    if len(testable) > 1:
        pvals = np.array([r["pvalue"] for r in testable])
        n_p = len(pvals)
        ranked = np.argsort(pvals)
        adj = np.empty(n_p)
        for i, rank_idx in enumerate(reversed(ranked)):
            rank = n_p - i
            if i == 0:
                adj[rank_idx] = pvals[rank_idx]
            else:
                adj[rank_idx] = min(pvals[rank_idx] * n_p / rank, adj[ranked[n_p - i]])
        adj = np.minimum(adj, 1.0)
        for i, r in enumerate(testable):
            r["pvalue_bh"] = adj[i]
        print(f"  Corrected {n_p} tests.")

    # ── Save results ──────────────────────────────────────────────────────
    results_df = pd.DataFrame(all_results)
    out_path = os.path.join(DATA_DIR, "robustness_results.csv")
    results_df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path} ({len(results_df)} rows)")

    print("\n" + "=" * 70)
    print("02_robustness.py complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
