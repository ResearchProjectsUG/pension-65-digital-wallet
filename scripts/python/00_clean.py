"""00_clean.py - RDD data cleaning template.

Project-specific variables (in the section below) are filled by Claude.
Everything below the FIXED CODE marker handles known RDD pitfalls and must
not be modified.
"""

import os
import sys
import numpy as np
import pandas as pd

# Reproducibility: pin the RNG so sample-dependent operations (correlation
# tie-breaking, future bootstrap CIs, etc.) produce identical numbers across
# runs.  All downstream scripts inherit this convention.
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECT-SPECIFIC VARIABLES (Claude fills these)
# ═══════════════════════════════════════════════════════════════════════════════
DATA_FILE = "C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv"
DATA_FORMAT = "csv"
RUNNING_VAR = "EDAD"
THRESHOLD = 65
TREATMENT_VAR = ""
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
CLUSTER_VAR = "DPTO"
TIME_VAR = "None"
COVARIATES = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
PLACEBO_OUTCOMES = ["INTERNET_HOGAR", "SMARTPHONE"]

# ═══════════════════════════════════════════════════════════════════════════════
# FIXED CODE (does not change between projects)
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_OUT = os.path.join(SCRIPT_DIR, "..", "..", "data", "clean")
os.makedirs(DATA_OUT, exist_ok=True)

print("=" * 70)
print("00_clean.py — RDD Data Cleaning")
print("=" * 70)

# ── Load data ─────────────────────────────────────────────────────────────────
data_path = os.path.join(SCRIPT_DIR, DATA_FILE)
print(f"Loading: {data_path}")

if DATA_FORMAT == "stata":
    df = pd.read_stata(data_path)
elif DATA_FORMAT == "tab":
    df = pd.read_csv(data_path, sep="\t", encoding="latin-1", low_memory=False)
elif DATA_FORMAT == "parquet":
    df = pd.read_parquet(data_path)
else:
    df = pd.read_csv(data_path, encoding="latin-1", low_memory=False)

print(f"Raw data: {len(df):,} rows x {df.shape[1]} cols")

# ── Missingness table ─────────────────────────────────────────────────────────
print("\n--- Missingness table (key variables) ---")
key_vars = [RUNNING_VAR, TREATMENT_VAR, CLUSTER_VAR] + OUTCOME_VARS + COVARIATES
if TIME_VAR:
    key_vars.append(TIME_VAR)
key_vars = [v for v in key_vars if v and v in df.columns]

for var in key_vars:
    n_miss = df[var].isna().sum()
    pct = 100 * n_miss / len(df)
    print(f"  {var:30s}: {n_miss:6,} missing ({pct:.1f}%)")

# ── Validate running variable exists ──────────────────────────────────────────
if RUNNING_VAR not in df.columns:
    print(f"\nERROR: Running variable '{RUNNING_VAR}' not in data.")
    print(f"Available columns: {list(df.columns[:30])}")
    sys.exit(1)

# ── Filter to RDD sample (running variable non-missing) ──────────────────────
n_before = len(df)
df_rdd = df.dropna(subset=[RUNNING_VAR]).copy()
n_after = len(df_rdd)
print(f"\n--- Filter: running variable non-missing ---")
print(f"  Before: {n_before:,}  After: {n_after:,}  Dropped: {n_before - n_after:,}")

# ── Center running variable at threshold ──────────────────────────────────────
if isinstance(THRESHOLD, (int, float)) and THRESHOLD != 0:
    df_rdd["running_centered"] = df_rdd[RUNNING_VAR] - THRESHOLD
    print(f"  Centered running variable at threshold = {THRESHOLD}")
else:
    df_rdd["running_centered"] = df_rdd[RUNNING_VAR]
    print(f"  Running variable already centered at 0")

# ── Construct treatment indicator ─────────────────────────────────────────────
if TREATMENT_VAR and TREATMENT_VAR in df_rdd.columns:
    print(f"  Using existing treatment variable: {TREATMENT_VAR}")
    df_rdd["treat"] = df_rdd[TREATMENT_VAR].astype(float)
else:
    print(f"  Constructing treatment from running >= 0")
    df_rdd["treat"] = (df_rdd["running_centered"] >= 0).astype(float)

n_treated = int(df_rdd["treat"].sum())
n_control = len(df_rdd) - n_treated
print(f"  Treated: {n_treated:,}  Control: {n_control:,}")

# ── Outcome validation ────────────────────────────────────────────────────────
print("\n--- Outcome validation ---")
outcomes_present = [o for o in OUTCOME_VARS if o in df_rdd.columns]
outcomes_missing = [o for o in OUTCOME_VARS if o not in df_rdd.columns]

if outcomes_missing:
    print(f"  WARNING: Missing outcomes: {outcomes_missing}")
if not outcomes_present:
    print(f"  ERROR: No outcome variables found in data!")
    sys.exit(1)

for var in outcomes_present:
    s = df_rdd[var].dropna()
    corr = df_rdd[[var, "running_centered"]].dropna().corr().iloc[0, 1]
    ctrl_mean = df_rdd.loc[df_rdd["treat"] == 0, var].mean()
    treat_mean = df_rdd.loc[df_rdd["treat"] == 1, var].mean()
    print(f"  {var}: N_valid={len(s)}, ctrl_mean={ctrl_mean:.4f}, "
          f"treat_mean={treat_mean:.4f}, corr_with_running={corr:.4f}")

# ── Top 10 correlates with running variable ───────────────────────────────────
print("\n--- Top 10 variables correlated with running variable ---")
numeric_cols = df_rdd.select_dtypes(include=[np.number]).columns
corrs = {}
for col in numeric_cols:
    if col in ("running_centered", "treat", RUNNING_VAR):
        continue
    try:
        r = df_rdd[["running_centered", col]].dropna().corr().iloc[0, 1]
        if not np.isnan(r):
            corrs[col] = abs(r)
    except Exception:
        pass

for i, (col, r) in enumerate(sorted(corrs.items(), key=lambda x: -x[1])[:10], 1):
    print(f"  {i:2d}. {col:40s} |r| = {r:.4f}")

# ── Panel balance check (if panel data) ──────────────────────────────────────
if TIME_VAR and TIME_VAR in df_rdd.columns and CLUSTER_VAR in df_rdd.columns:
    print(f"\n--- Panel structure ---")
    n_units = df_rdd[CLUSTER_VAR].nunique()
    n_periods = df_rdd[TIME_VAR].nunique()
    ct = pd.crosstab(df_rdd[CLUSTER_VAR], df_rdd[TIME_VAR])
    n_balanced = (ct > 0).all(axis=1).sum()
    print(f"  Units: {n_units}, Periods: {n_periods}")
    print(f"  Balanced: {n_balanced}/{n_units} ({100*n_balanced/n_units:.1f}%)")
    print(f"  Year distribution:")
    print(f"  {df_rdd[TIME_VAR].value_counts().sort_index().to_dict()}")

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = os.path.join(DATA_OUT, "clean_data.csv")
df_rdd.to_csv(out_path, index=False)
print(f"\nSaved: {out_path} ({len(df_rdd):,} rows x {df_rdd.shape[1]} cols)")

# Placeholder results
results_path = os.path.join(DATA_OUT, "main_results.csv")
if not os.path.exists(results_path):
    pd.DataFrame(columns=["outcome", "specification", "estimate", "se_robust",
                           "ci_lower", "ci_upper", "bandwidth", "N_eff", "method"]
                 ).to_csv(results_path, index=False)
    print(f"Saved placeholder: {results_path}")

print("\n" + "=" * 70)
print("00_clean.py complete.")
print("=" * 70)
