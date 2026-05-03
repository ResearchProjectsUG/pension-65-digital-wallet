# Claim Discipline Audit: Digital Wallet Adoption RDD Paper

---

## [CRITICAL] Issues

---

### CRITICAL-1: Survey weights absent despite population-representative inference claims

The paper states: *"Population-level inference is carried out with the official expansion factor (FACPOB07, renamed FACTOR\_EXPANSION in our cleaned file)"* (§3.1), and reports "population mean: 7.4%" for `TIENE_BILLETERA`.

The data audit explicitly flags: **"No survey weight column found. Results may not be population-representative."**

These are irreconcilable. If `FACTOR_EXPANSION` was dropped during cleaning, every standard error, mean, and population-level claim in the paper rests on unweighted counts from a complex stratified design. The paper never acknowledges this discrepancy, and all references to "population" estimates should be qualified as "sample" estimates until resolved.

---

### CRITICAL-2: Statistically significant placebo result dismissed without valid justification

The paper states: *"Both placebos are economically negligible and consistent with the absence of a discontinuity specific to age 65"* (§4.2).

Table 3 (Panel D) shows the first placebo cutoff (TIENE\_BILLETERA, BW=7.41, N=99,667) has **CI [−0.0083, −0.0062]**, which excludes zero. This is a **statistically significant discontinuity at the placebo cutoff** — the opposite of what the paper claims.

The paper's explanation — *"The left placebo's tight confidence interval reflects an artificially small standard error driven by the placebo using a far-from-cutoff window where there is little local variation"* — is **logically inverted**: scarcity of local variation produces wider, not narrower, standard errors. A valid justification for dismissing this result is never provided. A significant placebo is a direct threat to the RDD validity assumption, and the paper's dismissal is unsubstantiated.

---

### CRITICAL-3: Invalid WLS confidence intervals reported as primary evidence

The paper acknowledges: *"the t-statistic computed in the asymptotic covariate-adjusted WLS specification (t≈−5.1, computed as −0.027/0.005) would suggest rejection at any conventional level, but the randomization p-value reflects the actual permutation distribution"* (§4.1) and identifies the asymptotic SE as wrong due to discrete mass-points.

Despite this, the CI [−0.037, −0.017] derived from that SE appears in **Table 2**, the **abstract**, and the **discussion**. An SE the paper itself characterizes as incorrect has no business anchoring confidence intervals that are then presented to readers. The paper should either report the randomization-inference-compatible interval or explicitly mark the WLS CI as unreliable — not present it as primary output.

---

### CRITICAL-4: Duplicate donut-hole estimates presented as independent robustness checks

Table 3, Panel B:

| Donut | Estimate | SE | CI | BW | N |
|---|---|---|---|---|---|
| 0.5 yr | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |
| 1.0 yr | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |

**Six significant figures identical across two nominally different specifications.** Two distinct exclusion windows cannot produce identical bandwidths, sample sizes, SEs, and point estimates unless the code executed the same specification twice. The paper treats these as two independent robustness data points; they are almost certainly a single result counted twice, inflating the apparent robustness evidence.

---

### CRITICAL-5: McCrary density test result potentially never computed (API extraction bug)

The code review flags that p-value extraction uses `rd_den.p`, but the `rddensity` Python package stores test results in `.test` (a dict), not a `.p` attribute. If `.p` does not exist, the result silently becomes `NaN`.

The paper reports a test statistic of 2.0 and concludes no manipulation. If the statistic was read from a NaN-valued attribute — or if 2.0 is the *statistic* rather than the *p-value*, as a z-statistic of 2.0 would imply marginal rejection at α=0.05 — the no-manipulation assumption is unvalidated. The paper provides no p-value for this test, only the statistic.

---

## [MAJOR] Issues

---

### MAJOR-1: "LATE" label applied to an ITT reduced-form estimand

Section 4.1 states: *"The estimand is the local average treatment effect (LATE) of crossing the eligibility threshold"* and labels equation (1) accordingly.

This is an ITT (reduced-form) RDD estimate, not a LATE in the IV/Wald sense. The paper acknowledges this explicitly elsewhere — *"We do not claim to identify a sharp local average treatment effect on actual program compliers"* — but then uses "LATE" in the formal identification section. LATE has a precise meaning (Wald estimand on compliers) that this paper does not deliver. The methods section should consistently use "ITT" or "intent-to-treat effect at the cutoff."

---

### MAJOR-2: "Sharp RDD" throughout despite acknowledged fuzzy treatment

The abstract, title, and Section 4 heading all call this a **"sharp regression discontinuity."** The paper simultaneously acknowledges: (a) only ~22.5% of age-65 individuals satisfy both eligibility criteria (age + SISFOH); (b) take-up among the jointly eligible is ~75%; (c) *"the design we exploit is best characterized as an intent-to-treat (ITT) RDD."*

The running variable has a sharp cutoff; the treatment probability does not jump from 0 to 1. This is a **fuzzy design** estimated as a reduced form. Calling it "sharp" throughout obscures the core identification limitation. The appropriate label is "fuzzy RDD, estimated as ITT."

---

### MAJOR-3: Extreme-poor subsample effect described as "moderate" when it implies ~114% relative increase

Section 4.4: *"the confidence interval covers zero and the magnitude is moderate (+2.5 percentage points on a baseline rate of approximately 2.2%)."*

A 2.5 pp effect on a 2.2% baseline is a **~114% relative increase** — roughly a doubling of the outcome in the target population. Describing this as "moderate" suppresses information about economic significance. The paper correctly notes the CI covers zero, but mischaracterizes the point estimate's economic scale. The relative-effect framing matters here precisely because this is the relevant population for the policy question.

---

### MAJOR-4: Randomization inference procedure is non-standard for RDD and target specification is ambiguous

The paper describes permuting *treatment assignment* within the age window [55, 75]. Standard Fisher randomization inference for RDD either (a) shifts the cutoff to placebo locations or (b) randomly assigns treatment to individuals within the local bandwidth, preserving local density. Permuting treatment within a 20-year window destroys the local identification structure of the estimand and is not a standard test of the RDD null.

Additionally, the paper conflates two non-equivalent uses of p=0.434: if the permutation test was run on the rdrobust specification (where t≈−0.37), the p-value is unremarkable and there is no "apparent inconsistency." If run on the WLS specification (where t≈−5.1), the contradiction implies the WLS SE is off by nearly an order of magnitude. The paper presents this as one number without specifying which specification it tests.

---

### MAJOR-5: Abstract presents covariate-adjusted estimate alongside baseline without disclosing different bandwidth

The abstract reports: *"Estimates with predetermined covariates yield a small negative effect on ownership (−0.027, SE=0.005)"* immediately after the baseline estimate of −0.006. The abstract does not mention that the covariate-adjusted specification uses bandwidth h=34.2 versus the optimal h*=14.2 — a 2.4× difference. The paper acknowledges in Section 4.1 that these "reflect a different identification window" and "should not be interpreted as variance reduction holding bandwidth constant." Readers of the abstract receive no such warning and will naturally compare the two estimates as if they estimate the same local quantity.

---

### MAJOR-6: Causal policy prescription from null ITT cross-section

The conclusion states: *"institutional digitization of government transfers, on its own, is an insufficient lever for moving vulnerable populations into active digital wallet use"* and *"policy attention on the elderly poor population should focus on the underlying determinants of digital adoption."*

A null ITT result in a cross-sectional survey is consistent with at minimum four mechanisms: (a) truly no effect, (b) effect diluted by low take-up (~22.5% × 75% ≈ 17% compliance rate), (c) effect present only for long-run enrollees undetectable in one cross-section, (d) cohort confounding at the cutoff. The paper acknowledges all four in Section 5.2 but abandons them in the conclusion and reaches actionable causal policy prescriptions (*"pair the institutional channel with behavioral-change components"*) that go beyond what an ITT null on one cross-section can support.

---

## [MINOR] Issues

---

### MINOR-1: "First" contribution claims unverified

Three claims of priority — *"first regression-discontinuity evaluation,"* *"first sharply-identified evidence,"* *"first wave to include digital wallets"* — are asserted without supporting citations. The paper discloses in the acknowledgment footnote that it was autonomously generated, which further reduces confidence in literature priority screening.

---

### MINOR-2: RD plot description internally inconsistent

Section 4.5: *"rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."* A profile with a peak at age 35 cannot decline **monotonically** with age (it must rise from younger ages to reach that peak). The description is contradictory and the age-profile narration (reading from age 50 to 35) is nonstandard.

---

### MINOR-3: WLS fallback due to memory failure presented as methodological parity

Section 4.1 acknowledges the WLS specification was used because *"the local-polynomial rdrobust routine encountered memory limitations."* A computational fallback is not a methodological choice. Presenting WLS alongside rdrobust as two primary specifications implies they are comparably designed; one is the appropriate estimator and the other is a workaround with a different bandwidth and demonstrably wrong asymptotic SEs.

---

### MINOR-4: 25 clusters insufficient for asymptotic cluster-robust SEs, not flagged

The WLS specifications cluster at the department level (25 clusters). The econometrics literature is clear that simple cluster-robust SEs are downward-biased with fewer than ~30 clusters; CR2 or wild-bootstrap corrections are recommended. This limitation is not mentioned.

---

### MINOR-5: "Precisely estimated null" framing relative to base rate

The paper calls results *"tightly bounded"* and *"precisely estimated."* The 95% CI for ownership is [−0.034, 0.031], a width of 6.5 pp around a 7.4% baseline. This rules out effects larger than ±3.4 pp — i.e., a true positive effect of 46% relative size would still lie within the CI. Whether this constitutes precision depends on the policy-relevant minimum detectable effect size, which the paper never motivates.

---

### MINOR-6: Active-use outcome is degenerate zeros in the policy-relevant subpopulation — finding underreported

Section 4.4 notes *"no extreme-poor individual aged 65–75 in our sample reports active wallet use"* in passing, as a technical issue with inference. This is itself a substantive finding: the primary policy-relevant population (elderly extreme-poor) does not use digital wallets actively in the data at all. This should be elevated as a standalone result, not buried as a caveat to degenerate inference.

---

## Summary

```json
{
  "n_critical": 5,
  "n_major": 6,
  "n_minor": 6,
  "causal_overclaiming": [
    "These findings imply that institutional digitization of government transfers, on its own, is an insufficient lever for moving vulnerable populations into active digital wallet use.",
    "The well-documented age gradient in technology adoption appears to dominate any program-specific effect; if Pensión 65 has a positive impact on digital behavior, it is overwhelmed at the population level by underlying cohort differences in digital literacy and smartphone access.",
    "institutional digitization works best when paired with explicit digital-literacy support, smartphone-access subsidies, or in-person enrollment assistance, rather than as a stand-alone lever.",
    "policy attention on the elderly poor population should focus on the underlying determinants of digital adoption---smartphone ownership, internet access, digital literacy training---rather than on institutional accounts alone.",
    "Both placebos are economically negligible and consistent with the absence of a discontinuity specific to age 65."
  ],
  "missing_caveats": [
    "Survey expansion weights are absent from the cleaned data despite claims of population-representative inference; all population-level descriptive statistics are unvalidated.",
    "The first placebo cutoff (age 15) produces a CI that excludes zero; the paper dismisses this with a logically inverted explanation and never addresses the threat to RDD validity.",
    "The WLS confidence intervals [-0.037, -0.017] rest on an SE the paper identifies as incorrect; these intervals should not be reported as valid.",
    "The donut-hole robustness checks at 0.5 and 1.0 years produce identical estimates, SEs, and sample sizes, suggesting a coding error rather than two independent checks.",
    "With ~22.5% joint eligibility and ~75% take-up, the ITT dilutes the effect on compliers by a factor of approximately 0.17; no Lee-Bound or first-stage scaling is provided to bracket the complier effect.",
    "No extreme-poor individual aged 65-75 in the sample actively uses a digital wallet; the active-use outcome is uninformative for the target population and should be reported as a substantive finding, not a technical footnote.",
    "The McCrary density test p-value is potentially NaN due to a confirmed API extraction bug in the code; the no-manipulation assumption may be empirically untested.",
    "The cohort-versus-age confound is acknowledged only in the limitations section; the local-linear estimator attenuates but cannot eliminate this threat and it should be central to the identification discussion."
  ]
}
```