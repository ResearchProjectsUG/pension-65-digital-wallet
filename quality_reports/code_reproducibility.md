## Overall

- The pipeline is **well-structured and methodologically thorough** for an RDD study: it covers McCrary density test, placebo outcomes, bandwidth sensitivity, donut holes, covariate balance, polynomial sensitivity, placebo cutoffs, and permutation inference.
- A hardcoded absolute machine-specific path and a fragile cross-script import are the only blocking reproducibility issues.
- Template artifacts (electoral RDD boilerplate) survived into the output scripts — table notes and axis labels describe an electoral study, not the digital wallet study.
- `TIME_VAR = "None"` (string) is non-idiomatic Python; it happens to be safe because the column check filters it out, but it's a latent trap.
- No master run script, no `requirements.txt`, and no documented execution order — the pipeline cannot be run end-to-end by a new user without reading each file.

---

## Top Findings

- **[CRITICAL]** Hardcoded absolute path — `00_clean.py:16` — `DATA_FILE = "C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv"` breaks on every other machine; the `os.path.join(SCRIPT_DIR, DATA_FILE)` call at line 46 silently ignores SCRIPT_DIR because the path is absolute — replace with a relative path from project root or an environment variable.

- **[CRITICAL]** Fragile cross-script import via `import_module("01_main")` — `02_robustness.py:~60` — Python module names starting with a digit are not valid identifiers; `importlib.import_module` may raise `ModuleNotFoundError` depending on sys.path and Python version — rename to `main01` / `pipeline_main`, or use `importlib.util.spec_from_file_location` with an explicit file path, or inline the shared helpers.

- **[VERIFY]** `rddensity` p-value extraction via `rd_den.p` — `02_robustness.py:~120` — the rddensity Python package stores results in `.test` (a dict/DataFrame) rather than a direct `.p` attribute; if `.p` doesn't exist the McCrary p-value silently becomes `np.nan` and no warning is raised — verify with `rddensity.__version__` and the actual API; likely fix is `rd_den.test['p_jk']` or similar.

- **[VERIFY]** `TIME_VAR = "None"` (string, not `None`) — `00_clean.py:21` — coincidentally safe because `"None" in df.columns` returns False, but any future check using `if TIME_VAR is None` would silently misbehave — replace with Python `None`.

- **[NOTE]** Template boilerplate survives in output scripts — `03_output.py` table notes and figure labels — Table 1 note mentions "municipality-elections where the party's vote share exceeded the electoral threshold"; Table 4 header says "at the Electoral Threshold"; Figure 1 x-axis label reads "Vote Margin" — none of these match the digital wallet / ENAHO study; update all three before any submission.

- **[NOTE]** Auto-`pip install` at runtime — `01_main.py:42–47`, `02_robustness.py:similar` — silently installs `rdrobust` during execution; this is not reproducible (version is unconstrained) and can fail in CI or read-only environments — pin version in `requirements.txt` and remove the runtime install block.

- **[NOTE]** Hardcoded `h_approx = 2.0` for Figure 1 plot window — `03_output.py:~323` — ignores the data-driven optimal bandwidth computed in `01_main.py`; the RD plot may show too little or too much of the running variable — read `h_opt` from `main_results.csv` (the baseline bandwidth column) and use it here.

- **[NOTE]** Effect size `%change` uses full-sample mean — `01_main.py:~155` — `pct_change = 100 * est / abs(mean_val)` divides by the pooled mean; in an RDD the correct denominator is the control-side mean at the threshold (or the control group mean) — use `df.loc[df['treat']==0, outcome].mean()`.

- **[MISSING]** No master run script — pipeline entrypoint is undocumented — a new user has no single command to reproduce results; add `run_all.py` or a `Makefile` that calls `00 → 01 → 02 → 03` in order.

- **[MISSING]** No `requirements.txt` or `environment.yml` — `rdrobust`, `rddensity`, `statsmodels`, `matplotlib`, `pandas`, `numpy` versions are all unconstrained — add pinned requirements.

---

## Strengths

- **Graceful rdrobust → statsmodels fallback** with clear console messaging; results always include a `method` column identifying which estimator ran.
- **NaN/blank cell protection** in all four table generators (`validate_table`), with auto-replacement by `---` and a post-generation content scan.
- **Permutation test uses `np.random.default_rng(42)`** — the only stochastic step in the pipeline is fully seeded.
- **Robustness coverage is comprehensive**: McCrary density, placebo outcomes, bandwidth multipliers (½, 1×, 2×), donut holes, covariate balance restricted to bandwidth, polynomial order (p=1 and p=2), placebo cutoffs, and permutation inference — a strong referee-ready suite.
- **Covariate balance is correctly restricted to the bandwidth window** (`df_bw = df[np.abs(df[RUNNING_VAR]) <= h_opt]`) — a common mistake avoided.
- **BH FDR correction** implemented correctly for multiple hypothesis testing.
- **Consistent centering convention**: `running_centered` used uniformly across all four scripts.

---

## Reproducibility Checklist

- **Relative paths**: CRITICAL — `DATA_FILE` in `00_clean.py` is an absolute machine-specific path; all output paths are relative (good).
- **Random seed**: PASS — permutation test uses `np.random.default_rng(42)`; no other stochastic steps.
- **Outputs generated**: PASS — `clean_data.csv`, `main_results.csv`, `robustness_results.csv`, all tables and figures are explicitly written; `main_results.csv` is pre-created as a placeholder in `00_clean.py`.
- **Dependency management**: MISSING — no `requirements.txt`; runtime pip-install is unconstrained.
- **Run order**: MISSING — no master script; order `00→01→02→03` must be inferred from reading files.
- **Documentation**: MISSING — no README; no inline comments explaining the RDD design choices or threshold rationale.

---

```json
{
  "critical_issues": [
    {
      "file": "00_clean.py",
      "description": "DATA_FILE is a hardcoded absolute path 'C:/Users/jesus/Desktop/...' that breaks on any other machine. os.path.join(SCRIPT_DIR, DATA_FILE) at line 46 silently ignores SCRIPT_DIR because the path is absolute.",
      "fix": "Replace DATA_FILE with a path relative to the project root (e.g., '../../data/enaho_2024_clean.csv') and resolve it as os.path.join(SCRIPT_DIR, DATA_FILE), or accept it as a CLI argument / environment variable."
    },
    {
      "file": "02_robustness.py",
      "description": "import_module('01_main') attempts to import a module whose name starts with a digit, which is not a valid Python identifier. This can raise ModuleNotFoundError depending on sys.path and Python version.",
      "fix": "Rename 01_main.py to main_rdd.py (or pipeline_main.py), update the import, and keep 01_main.py as a thin wrapper if backward compatibility matters. Alternatively, use importlib.util.spec_from_file_location with the explicit file path."
    }
  ],
  "n_critical": 2,
  "n_notes": 6,
  "overall_status": "NEEDS_FIX"
}
```