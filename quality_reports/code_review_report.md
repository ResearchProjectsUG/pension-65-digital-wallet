# Code Review Report (Round 1)

## Reproducibility & Quality

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

## Paper-Code Alignment

## Verified Matches

- **Running variable: age centered at 65** → `RUNNING_VAR = "EDAD"`, `THRESHOLD = 65`, `df_rdd["running_centered"] = df_rdd[RUNNING_VAR] - THRESHOLD` → **HIGH** → exact match
- **Primary outcomes: digital wallet adoption** → `OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]` in all four scripts → **HIGH** → consistent throughout
- **MSE-optimal bandwidth** → `bwselect="mserd"` in `run_rdd_rdrobust()` (`01_main.py:51`) → **HIGH** → correct selector
- **Triangular kernel** → `kernel="triangular"` in every rdrobust call → **HIGH** → matches CCT baseline recommendation
- **CCT bias-corrected robust CIs** → `rd.ci.iloc[-1]` extracted in `run_rdd_rdrobust()` (`01_main.py:63-67`); rdrobust returns conventional/robust/bc-robust rows → **MEDIUM** → extraction targets last row (bc-robust), but not verified against rdrobust's row ordering in this Python port
- **Clustering by state/region** → `CLUSTER_VAR = "DPTO"` passed as `cluster=` to rdrobust → **HIGH** → matches design
- **Manipulation/density test** → `rddensity(X=y_all, c=0)` in `02_robustness.py:66-82` → **HIGH** → correct package and cutoff
- **Covariate balance at bandwidth** → `df_bw = df[np.abs(df[RUNNING_VAR]) <= h_opt]` before balance test (`02_robustness.py:155`) → **HIGH** → correctly restricts to bandwidth first
- **Donut-hole robustness** → donut at 0.5 and 1.0 (`02_robustness.py:135-144`) → **HIGH** → implemented
- **All four output files produced** → Tables 1–4 + Figures 1–2 in `03_output.py` + density figure in `02_robustness.py` → **HIGH** → complete set

---

## Items To Verify

- **Fuzzy RDD / 2SLS (LATE)** → `TREATMENT_VAR = ""` in `00_clean.py:16`; no `ivregress`-equivalent anywhere; 01_main.py runs reduced-form only → **NOT FOUND** → code estimates ITT (age≥65 on outcome), never the LATE (P65_receipt_digital on outcome with instrument=age≥65)
- **First stage estimation** → no separate regression of P65_receipt on polynomial(age-65)×1(age≥65); no F-statistic reported → **NOT FOUND** → required before claiming fuzzy RDD is identified
- **P65_receipt / P65_receipt_digital variable** → not defined in any PROJECT-SPECIFIC VARIABLES block; no column mapped → **NOT FOUND** → the endogenous variable for the fuzzy design does not exist in the code
- **Mechanism verification cross-tab** → no cross-tab of P65 receipt by payment modality (digital vs cash) before regression → **NOT FOUND** → checklist flags this as a gate: if <50% digital among 65+, paper cannot proceed
- **Bandwidth sensitivity: 5-point table** → code tests only 3 multipliers (0.5×, 1×, 2×); checklist requires h/2, 2h/3, h, 4h/3, 2h → **LOW** → missing 2h/3 and 4h/3 points
- **CCT ci row ordering** → `rd.ci.iloc[-1]` assumes the last row of rdrobust's CI matrix is the bias-corrected robust CI; Python rdrobust may order rows differently than R → **MEDIUM** → needs unit test against a known dataset
- **INTERNET_HOGAR / SMARTPHONE dual role** → same variables appear in both `COVARIATES` and `PLACEBO_OUTCOMES`; using them as covariates in the main spec and then testing them as placebos conflates adjustment and validation → **MEDIUM** → either exclude from covariates list or use separate placebo variables
- **Kleibergen-Paap F-statistic** → not computed anywhere; required for weak instrument assessment in fuzzy RDD → **NOT FOUND**
- **Permutation p-value uses Silverman bandwidth** → `h_perm = 1.5 * np.std(x_perm)` (`02_robustness.py:196`) is not the MSE-optimal h; permutation and main estimation use different bandwidths → **MEDIUM** → inflate type-I error comparison
- **No heterogeneity table in 03_output.py** → `01_main.py` computes split-sample HTE results and appends to `all_results`, but `03_output.py` has no `make_table_heterogeneity()` function → **LOW** → HTE results are saved to CSV but never rendered to LaTeX
- **Polynomial sensitivity: p=1 and p=2 only** → `02_robustness.py` tests orders 1 and 2; a third-order check is sometimes expected for robustness → **MEDIUM** → minor gap
- **Digital wallet definition** → `TIENE_BILLETERA` / `USA_BILLETERA` are assumed correct but the mapping from raw ENAHO variables to these binary indicators is not shown in `00_clean.py` (they arrive pre-constructed) → **MEDIUM** → construction logic opaque

---

## Likely Discrepancies

- **Sharp vs. Fuzzy RDD — critical**: Paper's checklist requires a fuzzy RDD with `instrument = 1(age≥65)` and `endogenous = P65_receipt_digital`. Code sets `TREATMENT_VAR = ""` and constructs `treat = (running_centered >= 0)`, running a sharp RDD. This estimates ITT, not LATE. If take-up at the cutoff is below 1.0, ITT ≠ LATE and the structural claim fails.

- **No 2SLS anywhere**: The causal chain requires `P65 digital receipt → digital wallet adoption`. Without 2SLS, the code cannot distinguish whether the effect on wallets comes from program receipt or simply from being old enough to qualify.

- **First stage completely absent**: The checklist explicitly requires a first-stage table with jump magnitude, robust SE, and Kleibergen-Paap F ≥ 10. None of this is computed. A reviewer will immediately request it.

- **Mechanism verification gate skipped**: The cross-tab (share of 65+ receiving digital vs. cash payments) that determines whether the paper's causal chain holds is not in the code. If cash dominates, the entire instrument is invalid.

- **Bandwidth sensitivity table shape**: Paper strategy implies a 5-row table (h/2, 2h/3, h, 4h/3, 2h). Code produces 3 rows. Table 3 will not match the text if the paper describes all five multipliers.

- **INTERNET_HOGAR / SMARTPHONE as covariates AND placebos**: Using a variable as a covariate in the outcome equation and then as a placebo outcome in the same dataset is logically inconsistent — the placebo test is supposed to detect pre-existing discontinuities in predetermined variables, but conditioning on them removes that signal.

---

## Coverage Notes

- **Easy to match**: Running variable, threshold, kernel, bandwidth selector, cluster variable, and output file structure are all explicit in the PROJECT-SPECIFIC VARIABLES blocks and translate directly to the fixed code. No ambiguity.
- **Hardest gap**: The fuzzy RDD / 2SLS layer is entirely absent. This is not a configuration issue — it requires a new script or a substantial rewrite of `01_main.py` to add an IV estimation block using `linearmodels.iv` or a manual two-stage implementation.
- **Ambiguous**: Whether `rd.ci.iloc[-1]` correctly retrieves the bias-corrected robust CI depends on the Python rdrobust version's internal DataFrame structure. This should be verified empirically.
- **Silent data dependency**: `00_clean.py` assumes `TIENE_BILLETERA` and `USA_BILLETERA` already exist in `enaho_2024_clean.csv`. The construction of these binary indicators from raw ENAHO payment module variables is not visible in any script, so reproducibility is partial.
- **HTE results are computed but not rendered**: Split-sample heterogeneity estimates exist in the results CSV but have no corresponding LaTeX table, which means they cannot appear in the paper without additional output code.
- **Permutation test bandwidth mismatch**: The permutation inference uses a rule-of-thumb bandwidth while all other tests use MSE-optimal. This makes the permutation p-value not directly comparable to the main estimates.

---

```json
{
  "critical_mismatches": [
    {
      "paper_element": "Fuzzy RDD via 2SLS: instrument=1(age≥65), endogenous=P65_receipt_digital, outcome=digital_wallet_adoption",
      "code_evidence": "TREATMENT_VAR='' in 00_clean.py; 01_main.py runs sharp RDD (ITT only) via rdrobust with no IV stage; P65_receipt_digital not defined anywhere",
      "fix": "Add P65_receipt_digital to 00_clean.py PROJECT-SPECIFIC VARIABLES; add a new 01b_fuzzy.py that runs rdrobust with fuzzy=True or uses linearmodels.iv.IV2SLS with Z=1(age>=65), endog=P65_receipt_digital, exog=covariates; report LATE coefficient alongside ITT"
    },
    {
      "paper_element": "First stage: regress P65_receipt on polynomial(age-65)×1(age≥65); report jump, robust SE, Kleibergen-Paap F",
      "code_evidence": "No first stage regression in any script; no F-statistic computed",
      "fix": "In the new fuzzy estimation script, add a first-stage block using rdrobust(y=P65_receipt_digital, x=running_centered, fuzzy=None) or OLS within bandwidth; extract and print the jump estimate and cluster-robust F-statistic"
    },
    {
      "paper_element": "Mechanism verification: cross-tab P65 receipt by payment modality before any regression",
      "code_evidence": "No cross-tab in 00_clean.py or 01_main.py; TREATMENT_VAR is empty",
      "fix": "In 00_clean.py, after loading data, add: df.groupby('P65_receipt')[['PAGO_DIGITAL','PAGO_CASH']].mean() and print share receiving digital payments among age>=65; halt with sys.exit() if share < 0.5"
    },
    {
      "paper_element": "Bandwidth sensitivity table with 5 multipliers: h/2, 2h/3, h, 4h/3, 2h",
      "code_evidence": "02_robustness.py line 124: only 3 multipliers tested (0.5, 1.0, 2.0)",
      "fix": "Change the list at 02_robustness.py:124 to [(0.5,'h_half'),(0.667,'h_two_thirds'),(1.0,'h_optimal'),(1.333,'h_four_thirds'),(2.0,'h_double')]"
    },
    {
      "paper_element": "INTERNET_HOGAR / SMARTPHONE used as placebo outcomes to validate RDD",
      "code_evidence": "Same variables appear in COVARIATES_BASIC (01_main.py:14) AND PLACEBO_OUTCOMES (02_robustness.py:12); conditioning on them as covariates in the main spec removes the variation the placebo test is meant to detect",
      "fix": "Remove INTERNET_HOGAR and SMARTPHONE from COVARIATES_BASIC and COVARIATES_EXT in 01_main.py, or keep them only as placebos; choose separate predetermined covariates (e.g. POBREZA, INGRESO_PC) for covariate adjustment"
    }
  ],
  "n_mismatches": 5,
  "n_not_found": 4,
  "overall_alignment": "NEEDS_FIX"
}
```

