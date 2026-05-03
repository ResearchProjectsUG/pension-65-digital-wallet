## Claim Discipline Audit: Pensi\'on 65 RDD Paper

I'll work through the paper systematically, using the evidence packet to verify each claim against what the code actually produced.

---

### [CRITICAL-1] Donut-Hole Specifications Return Identical Results

**Where:** Section 5.2 / Table 3 Panel B

**Claim:** "Donut-hole specifications excluding observations within ±0.5 and ±1.0 years of the cutoff yield estimates of −0.001, removing the small negative point estimate entirely."

**Evidence:** Table 3 Panel B shows both donut specifications — 0.5 and 1.0 — returning **identical** values: Estimate=−0.0014, SE=0.0213, CI=[−0.0388, 0.0449], BW=10.65, N=19,434. A donut exclusion of ±0.5 vs. ±1.0 should drop different observations and produce different bandwidths, sample sizes, and estimates. The duplication is a near-certain sign of a coding error where the second donut-hole was not actually implemented. These robustness checks cannot be used as evidence.

---

### [CRITICAL-2] Placebo Test Has SE=0.0006 and N=99,667 — No Bandwidth Restriction Applied

**Where:** Section 5.2 / Table 3 Panel D

**Claim:** "The left placebo achieves a confidence interval that does not include zero, but the magnitude is similar to the actual cutoff estimate, reinforcing that the signal at age 65 is not specific to the program."

**Evidence:** Table 3 Panel D shows the first TIENE\_BILLETERA placebo row: Estimate=−0.0067, SE=0.0006, CI=[−0.0083, −0.0062], BW=7.41, N=99,667. A SE of 0.0006 with N=99,667 is consistent with an OLS regression run on the *entire* below-threshold sample with no bandwidth restriction — not a local RDD estimator centered on the placebo cutoff. A valid RDD placebo at age 53 should use observations within roughly [43, 63], not the full 99,667-person below-threshold sample. The result therefore reflects a global age-trend estimate, not an RDD discontinuity test. The fact that this "placebo" rejects the null is a design validity threat that the paper waves away with one sentence.

---

### [CRITICAL-3] Heterogeneity Subgroup `het_POBREZA_low` Returns Baseline Estimates

**Where:** Section 5.4 / Table 2

**Claim:** "Effects are uniformly small and statistically null across all subgroups."

**Evidence:** Table 2 row `het_POBREZA_low` shows Estimate=−0.0056, SE=(0.0165), CI=[−0.0336, 0.0310], N/BW=27,809/14.24 — **identical** to the full-sample baseline. Since the full sample has 113,755 individuals and N=27,809 is the within-bandwidth count for the full sample, the poverty subgroup filter was not applied. Claiming null heterogeneity by poverty status is unsupported when the subgroup estimate is numerically indistinguishable from the pooled estimate.

---

### [CRITICAL-4] Permutation p-value of 0.434 Is Irreconcilable With Reported t=−5.999

**Where:** Section 5.1 and 5.2

**Claim:** "Permutation-based randomization inference yields a t-statistic of −5.999 with a randomization p-value of 0.434. The conventional asymptotic test rejects the null at any standard level, but randomization inference...fails to reject."

**Analysis:** If the observed t-statistic is −5.999, then across 500 random permutations of treatment assignment in the age window [55, 75], finding a permuted t-statistic more extreme than −5.999 should occur essentially 0% of the time — not 43.4% of the time. A p-value of 0.434 with |t|=5.999 is self-contradictory unless the permutation test was applied to a **different specification** (almost certainly the baseline rdrobust, where t≈−0.34, and p≈0.434 would be perfectly sensible). The paper presents these numbers back-to-back under the covariate-adjusted discussion, implying they refer to the same specification. This conflation is either a reporting error or a coding error; either way, the claim that "randomization inference fails to reject" cannot be cited as independent evidence in the paper's current form.

---

### [CRITICAL-5] Missing Citation Left Verbatim in Published Text

**Where:** Section 2.3

**Verbatim:** "The closest recent application to our setting uses an age-65 cutoff for cash-transfer eligibility in a Latin American context and documents weak first-stage effects on digital savings [CITATION MISSING — insert \citet{} key]."

This is a placeholder that was never resolved. Beyond the obvious academic-integrity problem, the sentence it belongs to is being used to situate this paper in the literature and to establish the novelty of the contribution. Without knowing what paper is being cited, the reader cannot assess whether that paper already documents the main finding of this one.

---

### [MAJOR-1] The Estimand Is Labeled LATE But Is ITT

**Where:** Section 4.1, Equation (1)

**Claim:** "The estimand is the local average treatment effect (LATE) of crossing the eligibility threshold on each outcome."

**Problem:** In an RDD where treatment D_i = 1{age ≥ 65} represents *eligibility* and program receipt requires additionally being SISFOH-classified as extreme-poor, D_i is not the treatment of interest — it is an assignment mechanism. With ~25% non-take-up (acknowledged in Section 3.5), eligibility ≠ receipt. The correct label for the estimand under imperfect take-up is **intent-to-treat (ITT)**, not LATE. LATE in the IV sense would require using eligibility as an instrument for program receipt. The paper correctly calls this ITT everywhere except in the identification section, where the formula is misleadingly labeled LATE. This inconsistency will invite referee attention.

---

### [MAJOR-2] Covariate-Adjusted Specification Uses WLS With 2.4× Wider Bandwidth, Not rdrobust

**Where:** Section 4.2, Table 2

**Claim:** "We also estimate a covariate-adjusted specification... As discussed by \citet{calonico2019}, covariate adjustment in RDD reduces variance without affecting bias if covariates are continuous at the cutoff."

**Evidence:** Table 2 shows the covariate-adjusted method is `statsmodels_WLS` with BW=34.22 and N=59,649, versus `rdrobust` BW=14.24 and N=27,809 for the baseline. The bandwidth is 2.4 times wider and the estimator is WLS, not the local-polynomial estimator with covariates described in Calonico et al. (2019). The Calonico et al. (2019) result applies to covariates added *within* the rdrobust local-polynomial framework; it does not validate switching to a global WLS. The shift in estimate from −0.006 to −0.027 may partly reflect the wider bandwidth absorbing more of the secular age trend rather than variance reduction from covariates. The paper presents this as a refinement; it is a different estimator with different implicit assumptions.

---

### [MAJOR-3] "Causal Effect of Institutional Access" Overstates What ITT on Eligibility Delivers

**Where:** Section 1

**Verbatim:** "The age-65 eligibility threshold is administratively sharp; this provides a natural experiment for estimating the causal effect of institutional access on digital adoption among the elderly poor."

**Problem:** Three compounding attenuations separate the identified parameter from "institutional access":
1. ~25% of eligibles do not take up the program → ITT dilutes by non-take-up
2. Eligibility requires BOTH age ≥ 65 AND SISFOH extreme-poor status → the age-65 cutoff triggers eligibility for only a subset of age-65 crossers
3. The survey measures wallet ownership across the full general population, not just among program-eligible individuals

The identified effect is the effect of crossing age 65 on the full-population distribution of wallet ownership — not the effect of institutional access. Calling it the "causal effect of institutional access" is a mechanism claim that exceeds the design.

---

### [MAJOR-4] McCrary Density Test Statistic of 2.0 Is Borderline Significant; p-value Absent and Possibly Invalid

**Where:** Section 5.2

**Claim:** "The McCrary-style density test of \citet{cattaneo2018} produces a test statistic of 2.0; while the implementation flags mass-points at integer ages... there is no evidence of bunching specifically at age 65."

**Problems:**
- A z-statistic of 2.0 exceeds the conventional 5% critical value of 1.96. This is borderline rejection of no-manipulation, not clear non-rejection. Describing this as "no evidence" is too strong.
- The code review flags that `rd_den.p` may silently return `np.nan` due to an API mismatch with the rddensity Python package (the correct accessor may be `rd_den.test['p_jk']`). If the p-value is NaN, the paper has no valid density test at all.
- No p-value is reported anywhere in the paper — only the raw statistic.

---

### [MAJOR-5] Survey Weights Flagged as Missing; Population-Level Claims Unsupported

**Where:** Data Audit / Section 3.1 / Abstract

**Data Audit Warning:** "No survey weight column found. Results may not be population-representative."

**Paper Claim:** "Population-level inference is carried out with the official expansion factor (FACPOB07)... Population mean: 7.4%."

The data audit found no weight column in the cleaned data. If FACPOB07 was not actually applied during estimation, the "population mean" figures and the representation of estimates as nationally representative are incorrect. The unweighted mean for TIENE\_BILLETERA implied by the summary table is approximately 7.67% (weighted by cell size), not 7.4%, consistent with weights having some effect. The paper should explicitly confirm that weighted estimation was used and reconcile the data audit warning.

---

### [MAJOR-6] No Power Analysis for "Well-Powered Null" Claim

**Where:** Abstract, Section 1, Section 2.4

**Claim:** "The precisely estimated null... contributes substantively to a literature where well-powered nulls remain underrepresented."

**Problem:** The paper never presents a formal power analysis. The 95% CI for the baseline ownership estimate is [−0.034, 0.031] — a half-width of ~3.25 percentage points on a base rate of 7.4%. Whether this is "well-powered" depends on the minimum economically meaningful effect size, which is never defined. A 3pp change in a 7.4% base-rate outcome is arguably non-trivial (a 40% relative increase), meaning the design may lack power to detect economically important effects. The "well-powered null" framing requires a defensible effect-size benchmark.

---

### [MAJOR-7] Dual Eligibility Criterion Not Adequately Integrated Into ITT Interpretation

**Where:** Sections 3.5 and 6.1

**Claim:** "take-up of Pensi\'on 65 is incomplete (approximately 75% among the eligible). The intent-to-treat estimate dilutes whatever effect exists among actual recipients by the factor of non-take-up."

**Problem:** The dilution is two-stage, not one-stage:
1. Of all adults crossing age 65, only those classified as SISFOH extreme-poor are eligible at all (approximately 30% of age-65 adults per Section 3.5).
2. Of the ~30% who are eligible, approximately 75% actually take up.

So approximately 22.5% of all age-65 crossers are actual recipients. The paper discusses only the second stage of dilution, implying the ITT-to-LATE ratio is ~0.75 when it is closer to ~0.225. This substantially changes the implied effect on compliers under any policy interpretation.

---

### [MINOR-1] Placebo Cutoff Typo: Both Described as "Age 53"

**Where:** Section 5.2

**Verbatim:** "Placebo cutoffs at age 53 (i.e., 12 years below the true cutoff) and age 53 (12 years right)."

The right placebo should be at age 77. The typo is likely harmless, but it makes the description of Panel D ambiguous and the corresponding table entry uninterpretable without inference.

---

### [MINOR-2] Figure Description References Age 35 — Inconsistent With RDD Window

**Where:** Section 5.5

**Verbatim:** "rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."

In the context of an age-65 RDD, the bandwidth window is approximately [51, 79]. Age 35 is outside this window and inconsistent with "declining monotonically with age" (if the peak is at 35, the series declines from 35 through 65, consistent — but a plot focused on [51,79] would not show this). The description is confusing and likely describes a global figure, not the local-linear RDD plot. If the figure shows ages 25–90, describing it accurately is fine, but the caption says "RDD Plot" — an RDD plot conventionally shows the local window.

---

### [MINOR-3] Citation Mismatch: Deming & Noray (2023) Cited for Age Gradient in Digital Adoption

**Where:** Section 5.1

**Claim:** "consistent with the well-documented age gradient in technology adoption \citep{deming2023}"

The Deming & Noray (2023) paper is titled *"Earnings Dynamics, Changing Job Skills, and STEM Careers"* and documents how returns to specific skills evolve over careers. It does not study digital wallet adoption, mobile money, or the age gradient in financial technology. This is likely a citation carried over from a template. The correct citation should reference literature on age gradients in mobile payment or digital financial service adoption (e.g., Suri 2017 or specific survey-based evidence from Peru or LATAM).

---

### [MINOR-4] "First" Contribution Claims Are Unverified

**Where:** Sections 1, 2.4, and 6

**Claim:** "the first regression-discontinuity evaluation of a major government transfer program's effect on digital financial behavior in Peru" / "the first sharply-identified evidence on Pensi\'on 65's effects on digital financial behavior using post-2023 microdata."

These are standard "first" claims that cannot be verified without a comprehensive literature search. Given the concurrent [CITATION MISSING] for what the paper acknowledges is "the closest recent application," the claim of novelty is particularly exposed.

---

### [MINOR-5] Minor Rounding Inconsistencies Between Text and Tables

**Where:** Sections 5.3 and abstract

| Location | Text says | Table shows |
|---|---|---|
| Abstract, ownership CI | [−0.034, 0.031] | [−0.0336, 0.0310] ✓ (rounds correctly) |
| Abstract, use CI | [−0.034, 0.037] | [−0.0338, 0.0368] ✓ |
| Sec 5.3, smartphone CI | [−0.015, 0.086] | [−0.0146, 0.0857] — text rounds to −0.015 but table is −0.0146 |
| Sec 5.3, income CI | [−2,079, 3,172] | [−2078.5952, 3171.9232] ✓ |

The smartphone CI lower bound rounding (−0.015 vs. −0.0146) is trivial but demonstrates less-than-careful transcription.

---

## Summary Table

| # | Severity | Issue |
|---|---|---|
| 1 | [CRITICAL] | Donut-hole 0.5 and 1.0 return identical results — coding error |
| 2 | [CRITICAL] | Placebo runs on N=99,667 with SE=0.0006 — no bandwidth restriction, rejects null |
| 3 | [CRITICAL] | `het_POBREZA_low` returns full-sample baseline — subgroup filter not applied |
| 4 | [CRITICAL] | Permutation p=0.434 incompatible with t=−5.999 under same specification |
| 5 | [CRITICAL] | `[CITATION MISSING]` left verbatim in submitted text |
| 6 | [MAJOR] | Estimand labeled LATE; correct label throughout rest of paper is ITT |
| 7 | [MAJOR] | Covariate-adjusted spec uses WLS + BW=34.22, not Calonico et al. (2019) rdrobust |
| 8 | [MAJOR] | "Causal effect of institutional access" — overstates ITT on eligibility |
| 9 | [MAJOR] | McCrary t=2.0 borderline significant; p-value absent and possibly NaN |
| 10 | [MAJOR] | No survey weight column found; "population mean" claims unsupported |
| 11 | [MAJOR] | No power analysis for "well-powered null" claim |
| 12 | [MAJOR] | Dual eligibility (age + SISFOH) ≈ 22.5% take-up rate, paper implies ~75% |
| 13 | [MINOR] | Both placebos described as "age 53" — typo |
| 14 | [MINOR] | Figure description references age 35 in an age-65 RDD context |
| 15 | [MINOR] | Deming & Noray (2023) cited for age-technology gradient — wrong paper |
| 16 | [MINOR] | Unverified "first" claims |
| 17 | [MINOR] | Minor rounding inconsistency in smartphone CI |

---

```json
{
  "n_critical": 5,
  "n_major": 7,
  "n_minor": 5,
  "causal_overclaiming": [
    "The age-65 eligibility threshold is administratively sharp; this provides a natural experiment for estimating the causal effect of institutional access on digital adoption among the elderly poor.",
    "The estimand is the local average treatment effect (LATE) of crossing the eligibility threshold on each outcome.",
    "crossing the Pensión 65 age-eligibility threshold does not cause a measurable increase in digital wallet ownership or active use among Peruvian adults.",
    "institutional channels for transfer digitization, on their own, do not overcome the age gradient in digital financial behavior at the population level",
    "take-up of Pensión 65 is incomplete (approximately 75% among the eligible). The intent-to-treat estimate dilutes whatever effect exists among actual recipients by the factor of non-take-up."
  ],
  "missing_caveats": [
    "Dual eligibility (age ≥ 65 AND SISFOH extreme-poor) means only ~22.5% of age-65 crossers are actual recipients — not ~75% as implied; the paper discusses only the second-stage dilution.",
    "Covariate-adjusted estimate uses WLS with bandwidth 34.22, not the local-polynomial estimator described in Calonico et al. (2019); the 2.4× wider bandwidth confounds the comparison with the baseline.",
    "McCrary density test statistic of 2.0 is borderline significant at 5%; no p-value is reported and the code-review flags a likely API bug that may have silently returned NaN for the p-value.",
    "No power analysis provided for the 'well-powered null' claim; the CI half-width of ~3.25pp on a 7.4% base rate may not rule out economically meaningful effects.",
    "Integer running variable (completed age in years) creates discrete mass points at every age that undermine the validity of standard density tests and continuity assumptions; the paper acknowledges mass points but does not discuss the implications for identification.",
    "Donut-hole robustness checks are invalid: both the 0.5-year and 1.0-year donut specifications return identical estimates, standard errors, bandwidths, and sample sizes, indicating the exclusion was not actually implemented in the code.",
    "Placebo cutoff test is invalid: the reported SE of 0.0006 with N=99,667 indicates the placebo was estimated on the full below-threshold sample with no bandwidth restriction, not a local RDD window around the placebo cutoff.",
    "The heterogeneity analysis by poverty status is invalid: the het_POBREZA_low row returns values numerically identical to the full-sample baseline, indicating the subgroup filter was not applied.",
    "[CITATION MISSING] left verbatim in the text supporting the novelty claim in Section 2.3."
  ]
}
```