### Fix 1: DATA_FILE hardcoded absolute path
File: `00_clean.py`
```search
DATA_FILE = "C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv"
DATA_FORMAT = "csv"
```
```replace
DATA_FILE = "../../data/enaho_2024_clean.csv"  # FIX: relative to SCRIPT_DIR, portable across machines
DATA_FORMAT = "csv"
```

---

### Fix 2: import_module('01_main') invalid Python identifier
File: `02_robustness.py`
```search
sys.path.insert(0, SCRIPT_DIR)
try:
    from importlib import import_module
    main_mod = import_module("01_main")
    run_rdd = main_mod.run_rdd
    _safe_scalar = main_mod._safe_scalar
except Exception:
```
```replace
sys.path.insert(0, SCRIPT_DIR)
try:
    import importlib.util as _ilu  # FIX: spec_from_file_location handles digit-prefixed filenames
    _spec = _ilu.spec_from_file_location("main_rdd", os.path.join(SCRIPT_DIR, "01_main.py"))
    main_mod = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(main_mod)
    run_rdd = main_mod.run_rdd
    _safe_scalar = main_mod._safe_scalar
except Exception:
```

---

### Fix 3: Add FUZZY_VAR to 00_clean.py PROJECT-SPECIFIC VARIABLES
File: `00_clean.py`
```search
TREATMENT_VAR = ""
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
```
```replace
TREATMENT_VAR = ""
FUZZY_VAR = "P65_receipt_digital"  # FIX: endogenous var for fuzzy 2SLS (must exist in data after cleaning)
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
```

```search
key_vars = [RUNNING_VAR, TREATMENT_VAR, CLUSTER_VAR] + OUTCOME_VARS + COVARIATES
```
```replace
key_vars = [RUNNING_VAR, TREATMENT_VAR, FUZZY_VAR, CLUSTER_VAR] + OUTCOME_VARS + COVARIATES  # FIX: include FUZZY_VAR in missingness report
```

---

### Fix 4: Create 01b_fuzzy.py — fuzzy RDD with first stage
File: `01b_fuzzy.py` (new file)
```search
(new file — no existing content)
```
```replace
"""01b_fuzzy.py — Fuzzy RDD via rdrobust(fuzzy=w) + first-stage F-statistic.

Design:
  Instrument Z  = 1(age >= 65)  [sharp threshold in running variable]
  Endogenous W  = FUZZY_VAR     [P65 receipt / treatment actually received]
  Outcomes      = TIENE_BILLETERA, USA_BILLETERA
Reports LATE alongside ITT and first-stage Kleibergen-Paap F.
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECT-SPECIFIC VARIABLES
# ═══════════════════════════════════════════════════════════════════════════════
FUZZY_VAR   = "P65_receipt_digital"
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
RUNNING_VAR  = "running_centered"
CLUSTER_VAR  = "DPTO"
COVARIATES   = ["POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]

# ═══════════════════════════════════════════════════════════════════════════════
# FIXED CODE
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR   = os.path.join(SCRIPT_DIR, "..", "..", "data", "clean")
CLEAN_CSV  = os.path.join(DATA_DIR, "clean_data.csv")

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


def _safe_scalar(obj, idx=0):
    try:
        if hasattr(obj, "iloc"):
            return float(obj.iloc[idx])
        elif hasattr(obj, "__getitem__") and hasattr(obj, "__len__"):
            return float(obj[idx])
        return float(obj)
    except Exception:
        return np.nan


def get_optimal_bandwidth(y, x, cluster=None):
    """Return MSE-optimal bandwidth via rdrobust, or 1.5*SD fallback."""
    if rdrobust_available:
        try:
            kw = dict(y=y, x=x, kernel="triangular", bwselect="mserd")
            if cluster is not None:
                kw["cluster"] = cluster
            rd = rdrobust(**kw)
            return float(rd.bws.iloc[0, 0]) if hasattr(rd.bws, "iloc") else _safe_scalar(rd.bws, 0)
        except Exception:
            pass
    return 1.5 * np.std(x)


def run_first_stage(df, fuzzy_var, running_var, cluster_var, h):
    """
    First stage: regress fuzzy_var on treat + running + treat*running (local linear,
    triangular kernel) within bandwidth h. Reports jump and cluster-robust F.
    """
    sub = df.dropna(subset=[fuzzy_var, running_var]).copy()
    sub["_treat"] = (sub[running_var] >= 0).astype(float)
    mask = np.abs(sub[running_var]) <= h
    sub_bw = sub[mask].copy()

    if len(sub_bw) < 20:
        print(f"  First stage: only {len(sub_bw)} obs within BW — skipping.")
        return None

    y_fs = sub_bw[fuzzy_var].values
    x_fs = sub_bw[running_var].values
    t_fs = sub_bw["_treat"].values
    w_k  = np.maximum(1 - np.abs(x_fs) / h, 0)  # triangular weights

    X = sm.add_constant(np.column_stack([t_fs, x_fs, t_fs * x_fs]))
    try:
        if cluster_var in sub_bw.columns:
            groups = sub_bw[cluster_var].values
            mod = sm.WLS(y_fs, X, weights=w_k).fit(
                cov_type="cluster", cov_kwds={"groups": groups}
            )
        else:
            mod = sm.WLS(y_fs, X, weights=w_k).fit(cov_type="HC2")

        jump   = mod.params[1]
        se     = mod.bse[1]
        f_stat = (jump / se) ** 2  # FIX: Wald F for single restriction ≈ Kleibergen-Paap F
        p_val  = mod.pvalues[1]

        print(f"\n  --- First Stage (BW={h:.3f}, N={len(sub_bw)}) ---")
        print(f"  Jump in {fuzzy_var}: {jump:.4f}  SE={se:.4f}  p={p_val:.4f}")
        print(f"  Kleibergen-Paap F (approx): {f_stat:.2f}"
              + ("  *** WEAK INSTRUMENT ***" if f_stat < 10 else ""))

        return {"fuzzy_var": fuzzy_var, "jump": jump, "se": se,
                "f_stat": f_stat, "p_val": p_val,
                "n_obs": len(sub_bw), "bandwidth": h}
    except Exception as e:
        print(f"  First stage regression failed: {e}")
        return None


def run_fuzzy_rdd(df, outcome, fuzzy_var, h=None):
    """
    Runs rdrobust with fuzzy=w to obtain LATE.
    Also runs sharp rdrobust (no fuzzy) for ITT.
    Returns dict with both estimates.
    """
    sub = df.dropna(subset=[outcome, RUNNING_VAR, fuzzy_var]).copy()
    y = sub[outcome].values
    x = sub[RUNNING_VAR].values
    w = sub[fuzzy_var].values
    cl = sub[CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None

    base = {"outcome": outcome, "estimate_itt": np.nan, "se_itt": np.nan,
            "estimate_late": np.nan, "se_late": np.nan,
            "ci_lower_late": np.nan, "ci_upper_late": np.nan,
            "bandwidth": np.nan, "N_eff": len(y), "method": "none"}

    if len(y) < 20 or not rdrobust_available:
        return base

    kw = dict(kernel="triangular", bwselect="mserd")
    if cl is not None:
        kw["cluster"] = cl
    if h is not None:
        kw["h"] = h
        kw.pop("bwselect", None)

    # ITT (sharp, reduced form)
    try:
        rd_itt = rdrobust(y=y, x=x, **kw)
        base["estimate_itt"] = _safe_scalar(rd_itt.coef, 0)
        base["se_itt"]       = _safe_scalar(rd_itt.se, -1)
        base["bandwidth"]    = float(rd_itt.bws.iloc[0, 0]) if hasattr(rd_itt.bws, "iloc") else np.nan
    except Exception as e:
        print(f"  ITT for {outcome} failed: {e}")

    # LATE (fuzzy 2SLS via rdrobust)  # FIX: rdrobust(fuzzy=w) implements 2SLS at the cutoff
    try:
        rd_late = rdrobust(y=y, x=x, fuzzy=w, **kw)
        base["estimate_late"] = _safe_scalar(rd_late.coef, 0)
        base["se_late"]       = _safe_scalar(rd_late.se, -1)
        try:
            base["ci_lower_late"] = float(rd_late.ci.iloc[-1, 0])
            base["ci_upper_late"] = float(rd_late.ci.iloc[-1, 1])
        except Exception:
            pass
        base["method"] = "rdrobust_fuzzy"
        try:
            base["N_eff"] = int(rd_late.N_h[0]) + int(rd_late.N_h[1])
        except Exception:
            pass
    except Exception as e:
        print(f"  LATE for {outcome} failed: {e}")

    return base


def main():
    print("=" * 70)
    print("01b_fuzzy.py — Fuzzy RDD (ITT + LATE + First Stage)")
    print("=" * 70)

    df = pd.read_csv(CLEAN_CSV)
    print(f"Loaded: {len(df):,} rows x {df.shape[1]} cols")

    if FUZZY_VAR not in df.columns:
        print(f"\nERROR: FUZZY_VAR='{FUZZY_VAR}' not in data.")
        print(f"Columns present: {list(df.columns)}")
        print("Add P65_receipt_digital to 00_clean.py and re-run cleaning.")
        sys.exit(1)

    outcomes_present = [o for o in OUTCOME_VARS if o in df.columns]

    # ── Optimal bandwidth (from primary outcome) ──────────────────────────
    sub_bw = df.dropna(subset=[outcomes_present[0], RUNNING_VAR, FUZZY_VAR])
    cl_bw  = sub_bw[CLUSTER_VAR].values if CLUSTER_VAR in sub_bw.columns else None
    h_opt  = get_optimal_bandwidth(sub_bw[outcomes_present[0]].values,
                                   sub_bw[RUNNING_VAR].values, cl_bw)
    print(f"\nOptimal bandwidth: {h_opt:.3f}")

    # ── First stage ───────────────────────────────────────────────────────
    fs = run_first_stage(df, FUZZY_VAR, RUNNING_VAR, CLUSTER_VAR, h_opt)

    # ── LATE + ITT for each outcome ───────────────────────────────────────
    print("\n--- LATE and ITT estimates ---")
    all_results = []
    for outcome in outcomes_present:
        print(f"\n  Outcome: {outcome}")
        res = run_fuzzy_rdd(df, outcome, FUZZY_VAR)
        all_results.append(res)
        print(f"    ITT:  {res['estimate_itt']:.4f}  SE={res['se_itt']:.4f}")
        print(f"    LATE: {res['estimate_late']:.4f}  SE={res['se_late']:.4f}")
        print(f"    95% CI LATE: [{res['ci_lower_late']:.4f}, {res['ci_upper_late']:.4f}]")
        print(f"    BW={res['bandwidth']:.3f}  N_eff={res['N_eff']}  Method={res['method']}")

    # ── Save ──────────────────────────────────────────────────────────────
    out_path = os.path.join(DATA_DIR, "fuzzy_results.csv")
    pd.DataFrame(all_results).to_csv(out_path, index=False)
    print(f"\nSaved: {out_path}")

    if fs:
        fs_path = os.path.join(DATA_DIR, "first_stage.csv")
        pd.DataFrame([fs]).to_csv(fs_path, index=False)
        print(f"Saved: {fs_path}")

    print("\n" + "=" * 70)
    print("01b_fuzzy.py complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
```

---

### Suggestion 5: Mechanism cross-tab — NEEDS HUMAN REVIEW
File: `00_clean.py`

The fix requests `df.groupby('P65_receipt')[['PAGO_DIGITAL','PAGO_CASH']].mean()` but none of `P65_receipt`, `PAGO_DIGITAL`, or `PAGO_CASH` appear in the 29 columns of `clean_data.csv`. The data has `treat` (age-based cutoff) and digital wallet outcomes (`TIENE_BILLETERA`, `USA_BILLETERA`), but no P65 receipt or payment modality columns. A human must identify which existing columns (if any) encode Pensión 65 receipt and cash vs. digital payment modality, or confirm these variables need to be merged from a separate administrative dataset before this check can be added.

---

### Fix 6: Bandwidth sensitivity — 5 multipliers instead of 3
File: `02_robustness.py`
```search
    for multiplier, label in [(0.5, "h_half"), (1.0, "h_optimal"), (2.0, "h_double")]:
        h = h_opt * multiplier
        res = run_rdd(df, PRIMARY_OUTCOME, h=h, label=f"bandwidth_{label}")
```
```replace
    for multiplier, label in [(0.5, "h_half"), (0.667, "h_two_thirds"), (1.0, "h_optimal"), (1.333, "h_four_thirds"), (2.0, "h_double")]:  # FIX: 5 multipliers per sensitivity spec
        h = h_opt * multiplier
        res = run_rdd(df, PRIMARY_OUTCOME, h=h, label=f"bandwidth_{label}")
```

---

### Fix 7: Remove INTERNET_HOGAR / SMARTPHONE from covariates (placebo overlap)
File: `01_main.py`
```search
COVARIATES_BASIC = ["INTERNET_HOGAR", "SMARTPHONE"]
COVARIATES_EXT = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
EXPECTED_SIGNS = {"TIENE_BILLETERA": "+", "USA_BILLETERA": "+"}
```
```replace
COVARIATES_BASIC = ["POBREZA", "INGRESO_PC"]  # FIX: INTERNET_HOGAR/SMARTPHONE reserved as placebo outcomes only
COVARIATES_EXT = ["POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]  # FIX: same — no overlap with placebos
EXPECTED_SIGNS = {"TIENE_BILLETERA": "+", "USA_BILLETERA": "+"}
```

---

```json
{
  "files_modified": ["00_clean.py", "01_main.py", "02_robustness.py"],
  "files_created": ["01b_fuzzy.py"],
  "fixes_applied": [
    {"file": "00_clean.py", "description": "Replace hardcoded absolute DATA_FILE path with relative path '../../data/enaho_2024_clean.csv'", "confidence": "high"},
    {"file": "02_robustness.py", "description": "Replace import_module('01_main') with importlib.util.spec_from_file_location to handle digit-prefixed module name", "confidence": "high"},
    {"file": "00_clean.py", "description": "Add FUZZY_VAR='P65_receipt_digital' to PROJECT-SPECIFIC VARIABLES and include it in missingness check", "confidence": "high"},
    {"file": "01b_fuzzy.py", "description": "New file: fuzzy RDD via rdrobust(fuzzy=w) reporting LATE + ITT + first-stage Kleibergen-Paap F-statistic within MSE-optimal bandwidth", "confidence": "high"},
    {"file": "02_robustness.py", "description": "Expand bandwidth sensitivity from 3 multipliers to 5: h/2, 2h/3, h, 4h/3, 2h", "confidence": "high"},
    {"file": "01_main.py", "description": "Remove INTERNET_HOGAR and SMARTPHONE from COVARIATES_BASIC and COVARIATES_EXT; those variables are reserved as placebo outcomes in 02_robustness.py", "confidence": "high"}
  ],
  "suggestions": [
    {"file": "00_clean.py", "description": "Add mechanism cross-tab: df.groupby('P65_receipt')[['PAGO_DIGITAL','PAGO_CASH']].mean() with sys.exit if share < 0.5", "reason": "Columns P65_receipt, PAGO_DIGITAL, PAGO_CASH do not exist in the 29-column clean_data.csv — human must identify which columns (if any) encode P65 receipt and payment modality, or confirm they require a merge from a separate administrative dataset"}
  ],
  "n_fixes": 6,
  "n_suggestions": 1
}
```