```json
{
  "code_requirements": [
    {
      "category": "specification",
      "requirement": "MECHANISM VERIFICATION FIRST: Before any RDD estimation, document in-sample that Pensión 65 beneficiaries in the specific ENAHO wave used actually received payments via a digital wallet (BIM, Yape, Plin, or equivalent). Tabulate payment modality by P65 receipt status. If digital payment is not verifiable in the wave, the entire causal chain collapses. This is a prerequisite gate — fail here and stop.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "SHARP vs FUZZY AUDIT: Compute the fraction of individuals receiving Pensión 65 on each side of the age-65 cutoff. If take-up below age 65 > 0% or take-up above age 65 < 95%, this is a FUZZY RDD. Respecify as IV-RDD with D(age ≥ 65) as instrument for P65 receipt. Report first-stage F-statistic using Montiel Olea–Pflueger (2022) effective F (preferred over Stock-Yogo) and Anderson-Rubin robust confidence interval. Interpret all effects as LATE for age-65 compliers, not ITT.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "McCRARY / CATTANEO DENSITY TEST: Run the manipulation test (rddensity in Python/R or DCdensity in Stata) on the age running variable. Age in ENAHO is self-reported and susceptible to digit preference (heaping at 60, 65, 70). Report the test statistic, p-value, and a density plot. If p < 0.05, document the threat and run donut-hole as a MUST (not optional) robustness check.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "COVARIATE CONTINUITY TEST: Estimate the RDD separately for each predetermined covariate (sex, education, rural/urban, region, household size, wealth index). Report the discontinuity estimate and p-value for each. Run a joint chi-squared / F-test across all covariates. Any significant jump in a baseline covariate at age 65 is a validity failure requiring explicit discussion. Use the same bandwidth as the main specification.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "AGE HEAPING DIAGNOSTIC: Check for bunching at round age values (60, 65, 70) by plotting a histogram with 1-year bins. If bunching at 65 is visually apparent, run a Frandsen (2017) bunching-robust test and include donut-hole specification (±1 year exclusion) as the primary robustness check. Report how many observations fall exactly at age 65.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "COHORT CONFOUND DOCUMENTATION: In a cross-section, age ≡ birth cohort. Individuals born before 1961 (age > 65) may differ in digital literacy, technology adoption history, and financial habits from those born after 1961 — independent of any program effect. This is the central threat to identification. Required: (a) test whether the discontinuity in digital wallet adoption survives conditioning on education, urban status, and wealth (if it shrinks to zero, it is likely a cohort artifact); (b) search for a pre-rollout ENAHO wave where P65 did not exist or did not pay digitally and replicate the RDD — a jump in that wave is a confound, not a causal effect.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PLACEBO CUTOFF TESTS: Estimate the RDD at false cutoffs: ages 58, 60, 62, 68, 70, and 72. Use the same kernel, polynomial order, and bandwidth selector as the main specification. Produce a coefficient plot showing estimates and 95% CIs for all placebo cutoffs alongside the true cutoff. If placebo estimates are statistically significant at ages unrelated to any known program, interpret this as evidence of a smooth age trend being misidentified as a discontinuity.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "COMPETING DISCONTINUITIES AUDIT: Document whether any other policy creates a threshold exactly at age 65 in Peru (e.g., ESSALUD benefits, retirement laws, SIS eligibility changes, other conditional cash transfers). If yes, the exclusion restriction for fuzzy RDD is compromised and cannot be assumed away — must be explicitly addressed in the paper.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "PRIMARY INFERENCE METHOD: Use rdrobust (Calonico-Cattaneo-Titiunik 2014/2020) with heteroskedasticity-robust nearest-neighbor variance estimator (vce='nn') as baseline. This is the standard for local polynomial RDD. Report the conventional, bias-corrected, and robust confidence intervals — the robust CI is the one that should be reported in tables.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "SURVEY DESIGN STANDARD ERRORS: ENAHO is a complex stratified multi-stage sample. In addition to rdrobust SEs, estimate the main RDD with survey-weighted OLS in a bandwidth window and cluster standard errors at the PSU (conglomerado) level to account for within-cluster correlation from the survey design. Report both sets of SEs and flag if conclusions differ.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "WILD CLUSTER BOOTSTRAP TRIGGER: If, after applying the optimal bandwidth, fewer than 50 age-year clusters remain within the estimation window on either side of the cutoff, the asymptotic cluster-robust SEs are unreliable. In that case, use wild cluster bootstrap with Rademacher weights (999+ replications) as the PRIMARY inference method. Use wildboottest (Python) or boottest (Stata). Report whether the bootstrap p-value changes the significance conclusion.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "FIRST-STAGE INFERENCE (fuzzy only): Report Montiel Olea–Pflueger (2022) effective F-statistic for the first stage. Rule of thumb: effective F > 10 for 5% maximal size distortion. If effective F < 10, report Anderson-Rubin confidence interval as the primary CI (it is robust to weak instruments). Do NOT rely only on the Stock-Yogo critical values.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "BANDWIDTH SENSITIVITY: Report main results under (a) CCT MSE-optimal bandwidth (rdbwselect, bwselect='mserd'), (b) CCT CER-optimal bandwidth, (c) half the optimal bandwidth, (d) 1.5× the optimal bandwidth, and (e) a manually chosen ±5-year window. Present all five estimates in a single coefficient plot. Conclusions must hold across bandwidths (a)–(d) to be credible.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "POLYNOMIAL ORDER: Estimate with local linear (order=1) as the primary specification and local quadratic (order=2) as robustness. Do NOT use global polynomial regression (it overfits at boundaries). Do NOT use order=3 or higher without explicit justification.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "DONUT-HOLE SPECIFICATION: Exclude observations within ±6 months (or ±1 year if age is measured in years) of the cutoff and re-estimate. This tests whether the result is driven by individuals right at the boundary who may have manipulated their reported age. If the estimate collapses, the density test failure is load-bearing.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "KERNEL SENSITIVITY: Estimate with triangular kernel (primary, as recommended by CCT) and uniform kernel (robustness). Results should not be sensitive to kernel choice within a reasonable bandwidth.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "PLACEBO OUTCOME TEST: Select at least one outcome that should NOT be affected by receiving P65 digitally — e.g., ownership of a physical bank account opened before program rollout, or having a landline telephone. Estimate the same RDD on this outcome. A significant jump there indicates the age-65 threshold proxies for something unrelated to the digital transfer mechanism.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "PRE-ROLLOUT PLACEBO WAVE: Identify the earliest available ENAHO wave in which Pensión 65 either did not exist or paid exclusively in cash. Replicate the full RDD on digital wallet adoption in that wave. A statistically significant jump in the pre-rollout wave is evidence that the age-65 discontinuity exists independently of the program (cohort confound).",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "SUBGROUP HETEROGENEITY: Estimate the RDD separately for rural vs urban, women vs men, and lowest vs highest wealth quintile. These splits are theoretically motivated (digital infrastructure, prior financial inclusion). Use the same bandwidth and polynomial order. Report estimates and CIs for each group without claiming the subgroup differences are themselves causally identified.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "MANDATORY TABLE ELEMENTS: Every regression table must include: N (observations in estimation sample), bandwidth value used, polynomial order, kernel type, SE type (rdrobust robust, cluster-PSU, or wild bootstrap), point estimate, SE, 95% CI (robust preferred over conventional), and p-value. For fuzzy RDD, add first-stage F-statistic and share of compliers. No table may omit bandwidth or N.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "RDD VISUALIZATION: Produce a binned scatter plot (rdplot command) showing the running variable (age) on the X-axis and digital wallet adoption rate on the Y-axis, with separate fitted polynomials on each side of the cutoff. Use IMSE-optimal number of bins. This is the most important figure in an RDD paper — it must appear before any regression table.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "EFFECT SIZE INTERPRETATION: Report the point estimate in percentage-point terms (not just as a regression coefficient). Compare to the baseline adoption rate among 63–64-year-olds (just below the cutoff) to contextualize the magnitude. Compare to digital adoption gaps documented in prior literature on financial inclusion in Latin America. Flag if the implied effect exceeds what is plausible given baseline rates (e.g., a 40pp jump when baseline adoption is 8% deserves scrutiny).",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "FIRST-STAGE PLOT (fuzzy only): Produce a binned scatter plot of P65 receipt rate vs. age, showing the sharp jump at 65. This is the visual 'first stage' and must accompany the reduced-form digital wallet plot. Without this, the reader cannot assess compliance.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "THEORETICAL SIGN PRE-COMMITMENT: State the expected sign and magnitude of the effect BEFORE presenting regression output. Specifically: if P65 pays digitally, crossing age 65 should increase digital wallet ownership (positive effect). If the estimated sign is negative or implausibly large, this requires explicit discussion — not suppression.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT label as Sharp RDD without verifying near-perfect compliance. If any meaningful fraction of individuals below age 65 receive P65 (via early enrollment errors) or above age 65 do not receive it (eligibility denied for other reasons), the sharp design is misspecified and the estimate is attenuated-biased in unpredictable ways.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT pool multiple ENAHO waves without a cohort-year interaction. If multiple cross-sections are stacked, each wave adds a different birth cohort at age 65. Without a year-of-survey fixed effect interacted with age, the estimate confounds program exposure variation with cohort variation.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT use age in years as the running variable without checking whether ENAHO records age in completed years (floor) or reported age. If floor-coded, all individuals listed as 65 are actually 65.0–65.99 — this affects how close observations are to the true threshold and biases bandwidth selectors. Inspect the raw age distribution for evidence of coding convention.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT use a global polynomial regression (e.g., OLS with age^2, age^3 across the full sample and a threshold dummy). This is a now-discredited approach (Gelman & Imbens 2019). Use local polynomial estimation exclusively.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT bin the running variable before estimation unless using rdplot for visualization only. Binning discards information about distance to cutoff and introduces arbitrary researcher choices that affect results.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT ignore survey weights entirely. ENAHO oversamples rural areas. Either use probability weights in a weighted local linear regression or document explicitly why unweighted estimation is appropriate (e.g., if interest is in the ATE for the population near the cutoff, not the national aggregate). The choice must be stated and defended.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT interpret the RDD LATE as an average effect for all Peruvians or all P65-eligible individuals. The estimate identifies the effect for compliers at the age-65 margin — individuals who received P65 because they just crossed 65 and would not have received it otherwise. External validity to younger cohorts or individuals far from the cutoff is not guaranteed.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "MULTIPLE TESTING CORRECTION: If testing digital wallet adoption across multiple outcome measures (has any digital wallet, uses digital wallet monthly, total digital transactions), apply Benjamini-Hochberg FDR correction or report the Holm-Bonferroni adjusted p-values. Do not cherry-pick the most significant outcome measure without adjustment.",
      "priority": "SHOULD"
    }
  ],
  "method_warnings": [
    "COHORT ≡ AGE IN CROSS-SECTION: This is the deepest threat to the design. In a single cross-sectional wave, age 65 perfectly collinears with birth year 1961. People born in 1955 versus 1967 have different lifetime digital exposure, education systems, and financial socialization — entirely independent of Pensión 65. The only way to separate program effect from cohort effect is (a) a pre-rollout placebo wave, (b) within-cohort panel variation, or (c) exploiting geographic rollout variation. Without one of these, the design identifies 'age-65 discontinuity' not 'P65 digital payment effect'.",
    "FUZZY IS ALMOST CERTAIN: Pensión 65 requires meeting poverty criteria (SISFOH classification) and not receiving other public pensions (ONP, SPP). Age 65 is necessary but not sufficient. The first-stage compliance rate must be documented — if it is below 80%, the sharp design is a serious misspecification and the fuzzy IV is mandatory.",
    "DIGITAL WALLET ADOPTION MAY BE BINARY WITH MASS AT ZERO: If the outcome is a 0/1 indicator, local linear RDD on the binary outcome is still valid (it estimates a difference in conditional means), but the estimated 'effect' could exceed the theoretical maximum if baseline rates are very low. Document the mean of the outcome variable within the bandwidth on each side of the cutoff before interpreting coefficients.",
    "ENAHO SURVEY DESIGN IS STRATIFIED MULTI-STAGE: Ignoring the sampling design inflates the apparent precision. At minimum, cluster SEs at the PSU (conglomerado) level. For national representativeness claims, use survey probability weights. The rdrobust package does not natively handle complex survey designs — a robustness check with survey-weighted OLS in the bandwidth window is required.",
    "AGE MISREPORTING RISK IN OLDER POPULATIONS: Older Peruvians, particularly in rural areas, may not know their exact birth year. Self-reported age at exactly 65 may be noisy. The density test is essential, and if manipulation is detected, the density test failure must be treated as a major result-invalidating threat, not a footnote.",
    "BACHAS ET AL. CITATION: The validation result flags a journal attribution error. Verify the correct outlet (likely Journal of Development Economics or Journal of Finance) before submission. Also add: Calonico, Cattaneo & Titiunik (2014) Econometrica; Cattaneo, Idrobo & Titiunik (2020) Cambridge Elements; and Lee & Lemieux (2010) JEL as canonical RDD methodological references."
  ],
  "must_not_claim": [
    "Cannot claim SHARP RDD identification without documenting that P65 take-up jumps from near-zero to near-one at the age-65 cutoff within the estimation sample.",
    "Cannot claim CAUSAL EFFECT of digital payments on financial inclusion without first verifying that P65 actually disbursed payments via digital wallet in the specific ENAHO wave used.",
    "Cannot claim the estimate generalizes to younger cohorts, other social programs, or other countries — the LATE is local to age-65 compliers in Peru in the sample wave.",
    "Cannot rule out COHORT CONFOUND without a pre-rollout placebo wave or multi-wave panel exploiting program rollout variation.",
    "Cannot claim the running variable is free of manipulation without a passing McCrary/Cattaneo density test reported in the paper.",
    "Cannot interpret the fuzzy RDD IV estimate as the ITT (intent-to-treat) — the IV gives LATE for compliers, which is a different parameter than the average effect of P65 eligibility.",
    "Cannot dismiss the competing discontinuity concern at age 65 without explicitly documenting what other policies change at exactly that age in Peru and why they do not affect digital wallet adoption."
  ]
}
```