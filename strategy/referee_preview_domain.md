Here is the full referee checklist, calibrated to the specific threats in this design:

```json
{
  "code_requirements": [
    {
      "category": "mechanism_verification",
      "requirement": "Before any regression: cross-tab P65 receipt by payment modality (digital vs cash) for the target ENAHO wave. If the share receiving digital payments in the 65+ group is <50%, the causal chain is broken and the paper cannot proceed as written.",
      "priority": "MUST"
    },
    {
      "category": "first_stage",
      "requirement": "Run fuzzy RDD first stage: regress P65_receipt on polynomial(age-65) × 1(age≥65) using local linear regression. Report jump magnitude, robust SE, and Kleibergen-Paap F-statistic. A sharp RDD is only defensible if take-up at the cutoff is near 1.0; document this explicitly.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Implement fuzzy RDD via 2SLS: instrument = 1(age≥65), endogenous variable = P65_receipt_digital, outcome = digital_wallet_adoption. Local linear specification with triangular kernel as baseline. Report LATE (Local Average Treatment Effect), not ITT alone.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Use CCT (Calonico-Cattaneo-Titiunik 2014) bias-corrected robust confidence intervals, not conventional OLS standard errors. In Python use rdd or rdrobust-equivalent; the raw local-linear coefficient has non-trivial bias at optimal bandwidth.",
      "priority": "MUST"
    },
    {
      "category": "bandwidth",
      "requirement": "Apply MSE-optimal bandwidth selection (CCT or IK selector). Then report results at h/2, 2h/3, h, 4h/3, 2h in a single sensitivity table. The baseline estimate must not be hand-chosen.",
      "priority": "MUST"
    },
    {
      "category": "manipulation_test",
      "requirement": "Run Cattaneo-Jansson-Ma (2018) local-polynomial density test (rddensity equivalent) at the age-65 cutoff. Report the test statistic, p-value, and a histogram/density plot. Heaping at integer age 65 is extremely likely in ENAHO — if the test rejects, add a donut-hole robustness check.",
      "priority": "MUST"
    },
    {
      "category": "age_heaping",
      "requirement": "Audit the age distribution for heaping at multiples of 5 (ages 60, 65, 70). Compute Whipple Index or a simple spike ratio. If heaping is present at 65 specifically, add donut-hole estimates excluding [64.5, 65.5] and [64, 66] as robustness columns.",
      "priority": "MUST"
    },
    {
      "category": "covariate_balance",
      "requirement": "Test for discontinuities at age 65 in ALL pre-determined covariates: sex, years of education, rural dummy, poverty index (IHH or SISFOH score), household size, district-level infrastructure index. None should show a statistically significant jump. Present as a balance table AND as small RDD plots.",
      "priority": "MUST"
    },
    {
      "category": "placebo_cutoffs",
      "requirement": "Estimate the main specification at four placebo cutoffs: 60, 62, 68, 70. Report point estimates and 95% CIs for all four alongside the true cutoff in a single figure. The 65-cutoff estimate must be a clear outlier to be credible.",
      "priority": "MUST"
    },
    {
      "category": "competing_discontinuities",
      "requirement": "Document and test whether any other program or policy generates a discontinuity at age 65 in Peru: SIS/EsSalud transitions, AFP contributory pension, formal retirement age rules. If any co-exist exactly at 65, the exclusion restriction of the IV is violated. Explicitly rule these out or discuss as a limitation.",
      "priority": "MUST"
    },
    {
      "category": "placebo_outcomes",
      "requirement": "Run the RDD on at least three pre-determined/unaffected outcomes: formal employment rate, durable asset ownership, and food expenditure (or equivalent available in ENAHO). None should show a significant jump at 65.",
      "priority": "MUST"
    },
    {
      "category": "polynomial_sensitivity",
      "requirement": "Report results for polynomial orders p=1, p=2, and p=3 in a sensitivity table. The baseline must be p=1 (local linear) per best-practice RDD guidance (Gelman & Imbens 2019 warning against global high-order polynomials).",
      "priority": "MUST"
    },
    {
      "category": "kernel_sensitivity",
      "requirement": "Re-run baseline estimate with triangular, uniform, and Epanechnikov kernels. Triangular is canonical — the others are sensitivity only.",
      "priority": "SHOULD"
    },
    {
      "category": "donut_hole",
      "requirement": "Exclude observations within ±0.5 years and ±1 year of the cutoff and re-estimate. This guards against the possibility that individuals at exactly age 65 self-select into P65 registration through awareness.",
      "priority": "SHOULD"
    },
    {
      "category": "heterogeneity",
      "requirement": "Stratify the main estimate by: (1) sex, (2) rural vs urban, (3) quartile of district-level digital infrastructure or bank branch density. Report as interaction terms or separate subgroup estimates with appropriate multiple-testing correction (Bonferroni or BH-FDR).",
      "priority": "SHOULD"
    },
    {
      "category": "survey_design",
      "requirement": "Apply ENAHO sampling weights (factexp) throughout all descriptive statistics and balance tests. For the RDD regressions, document whether weights are applied and justify the choice — weighted LLR can be inconsistent; follow Solon et al. (2015) guidance.",
      "priority": "SHOULD"
    },
    {
      "category": "rollout_placebo",
      "requirement": "If multiple ENAHO waves are available: estimate the same RDD in waves BEFORE Pensión 65 introduced digital payments. A null effect in the pre-digital wave and a positive effect post-switch is the cleanest evidence for the mechanism.",
      "priority": "SHOULD"
    },
    {
      "category": "reduced_form",
      "requirement": "Report the ITT (reduced form: digital wallet on eligibility indicator) separately from the IV estimate. The ITT is always identified; the IV estimate additionally requires a strong first stage and exclusion restriction.",
      "priority": "SHOULD"
    },
    {
      "category": "confidence_intervals",
      "requirement": "All RDD point estimates must be accompanied by bias-corrected robust confidence intervals (not just p-values). Do not report stars alone — report the full CI.",
      "priority": "MUST"
    },
    {
      "category": "multiple_outcomes",
      "requirement": "If testing digital wallet adoption AND bank account ownership AND mobile money as separate outcomes, apply Romano-Wolf or Benjamini-Hochberg correction for multiple hypotheses. Do not treat each as independent at 5% level.",
      "priority": "SHOULD"
    },
    {
      "category": "cluster_se",
      "requirement": "Cluster standard errors at the district (distrito) level, not individual. ENAHO sampling is clustered at the conglomerado level — use the finer clustering that matches the program's geographic variation in rollout.",
      "priority": "SHOULD"
    },
    {
      "category": "power_analysis",
      "requirement": "Report ex-ante or ex-post minimum detectable effect (MDE) for the chosen bandwidth, given the sample size near the cutoff. An underpowered null result is not informative without this.",
      "priority": "NICE"
    },
    {
      "category": "randomization_inference",
      "requirement": "Optionally supplement asymptotic CIs with permutation-based p-values (Fisher sharp null) by randomly shifting the cutoff across the age distribution. Provides a non-parametric validity check.",
      "priority": "NICE"
    }
  ],

  "data_warnings": [
    "ENAHO records age in integer years: this GUARANTEES heaping at 60, 65, 70. The density test will almost certainly reject. Plan the donut-hole robustness before running any regression.",
    "Pensión 65 is means-tested (SISFOH poverty score), not purely age-gated: the jump in take-up at age 65 will be less than 1.0, making the design fuzzy by construction. Never claim 'sharp RDD' without verifying near-perfect take-up at the cutoff.",
    "Digital payment via Banco de la Nación ('Cuenta DNI' or 'BIM') is NOT the same as Yape/Plin adoption. Carefully distinguish: the outcome should be voluntary digital wallet usage, not just having a government-mandated account. Conflating these measures the mechanism, not the financial inclusion effect.",
    "The year of the ENAHO wave matters critically: Pensión 65 transitioned to digital disbursements in phases (2019–2022). Using a wave before the digital transition makes the entire mechanism void. Verify the exact wave and cross-check with MIDIS administrative records.",
    "ENAHO is cross-sectional: you cannot observe pre-treatment digital wallet status for the same individuals. Any comparison is between cohorts, not the same individuals before and after crossing 65. State this limitation explicitly.",
    "Other programs with discontinuities near age 65 in Peru: Contigo (disability pension, no age cutoff), SIS (health insurance has different age rules), AFP obligatory contributions (cease at retirement). Each must be explicitly ruled out as a co-treatment.",
    "Unit of analysis ambiguity: ENAHO collects financial data at both individual and household level. Clarify whether 'digital wallet adoption' is individual-level (the recipient) or household-level. Spillovers to other household members would be a different estimand.",
    "Geographic rollout heterogeneity: P65 was not available uniformly across all districts simultaneously. Pooling all districts may dilute the first stage. Consider restricting to districts where P65 was operational at survey date, or use rollout timing as an additional instrument.",
    "Survey non-response at age 65: check whether item non-response on the digital payment question is differential near the cutoff. A jump in missingness would bias the RDD estimate.",
    "Proxy respondents: older respondents in ENAHO are sometimes answered by a proxy (spouse or child). Digital wallet questions answered by proxy may have different measurement error — check and flag."
  ],

  "tables_required": [
    "Table 1: Descriptive statistics overall and separately for [60–64] vs [65–70] age groups — means, SDs, and a test of difference. Include running variable, outcome, all covariates, and P65 receipt rate.",
    "Table 2: First-stage RDD — P65 receipt on 1(age≥65) × f(age−65), local linear, triangular kernel, CCT optimal bandwidth. Report jump, robust SE, bias-corrected CI, and Kleibergen-Paap F-statistic.",
    "Table 3: Main RDD results — ITT (reduced form) and LATE (fuzzy IV). Columns: (1) baseline CCT bandwidth, (2) h/2, (3) 2h. Rows: digital wallet, bank account, mobile money (if available). Bias-corrected robust CIs throughout.",
    "Table 4: Bandwidth sensitivity — point estimates and 95% CIs for h/2, 2h/3, h, 4h/3, 2h. Show both ITT and IV.",
    "Table 5: Polynomial order sensitivity — p=1, p=2, p=3 at the CCT optimal bandwidth.",
    "Table 6: Covariate balance at cutoff — one row per covariate (sex, education, rural, poverty index, etc.), showing the RDD estimate and p-value. All should be statistically insignificant.",
    "Table 7: Placebo cutoffs at ages 60, 62, 65 (true), 68, 70 — point estimate and 95% CI for the main outcome at each.",
    "Table 8: Placebo outcomes — RDD estimate on formal employment, asset index, food expenditure. Should all be null.",
    "Table 9: Heterogeneity — main estimate split by sex, rural/urban, and district digital infrastructure quartile.",
    "Table A1 (appendix): Donut-hole robustness — estimates excluding ±0.5y and ±1y around cutoff.",
    "Table A2 (appendix): Kernel sensitivity — triangular (baseline), uniform, Epanechnikov."
  ],

  "figures_required": [
    "Figure 1: RDD plot — scatter of binned means of digital wallet adoption vs age (bins of 0.5 or 1 year), with local linear fits and 95% CI on each side of the cutoff. This is the flagship visual.",
    "Figure 2: First-stage RDD plot — same format as Figure 1, but outcome = P65 receipt. Visually confirm the jump in take-up.",
    "Figure 3: Density/histogram plot — histogram of age with bin width ≤ 1 year, overlaid with the Cattaneo-Jansson-Ma density test result annotated. Visually show heaping (or absence thereof) at 65.",
    "Figure 4: Covariate balance plots — small multiples (one panel per covariate) showing binned means with local linear fits, confirming no jump at 65 in pre-treatment variables.",
    "Figure 5: Bandwidth sensitivity plot — point estimates + 95% CIs for the main IV estimate across a grid of bandwidths from h/2 to 2h. Include the MSE-optimal bandwidth marked with a vertical line.",
    "Figure 6: Placebo cutoffs figure — point estimates + 95% CIs for all five cutoffs (60, 62, 65, 68, 70) plotted side by side. The true cutoff should stand out visually.",
    "Figure 7 (optional): Pre-digital wave vs post-digital wave RDD comparison — overlaid RDD plots showing null effect in the pre-digital ENAHO wave and positive effect post-transition (if multi-wave data is available).",
    "Figure A1 (appendix): Reduced form (ITT) plot — same format as Figure 1 but showing the raw ITT before IV scaling."
  ]
}
```

---

Los tres puntos más críticos de este checklist, en orden de prioridad:

**1. Verificá el mecanismo PRIMERO** — si Pensión 65 no pagaba digitalmente en el año ENAHO que estás usando, todo lo demás es irrelevante. Esto va antes de correr una sola regresión.

**2. El diseño es fuzzy, no sharp** — porque P65 es focalizado por pobreza (SISFOH), no todo el que cruza los 65 recibe el beneficio. El código DEBE implementar el fuzzy RDD con la primera etapa explícita. Llamarlo "sharp" sin documentar take-up ≈ 1.0 es un error que cualquier referee va a cazar.

**3. El heaping en edad entera es casi seguro** — ENAHO registra edad en años enteros. Habrá un pico artificial en exactamente 65. La prueba de densidad muy probablemente rechace, y si no hay robustez con donut-hole, el paper muere en revisión.