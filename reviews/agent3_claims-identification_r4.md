## Claim Discipline Audit — Regression Discontinuity Report on Pensión 65 and Digital Wallet Adoption

---

### [CRITICAL-1] "Consistent with zero across every specification" directly contradicts Table 2

**Exact sentence (Discussion §6.1):**
> "The intent-to-treat estimates are small, precisely bounded, and consistent with zero across every specification, bandwidth, and inference procedure we examined."

**What the evidence shows:** Table 2 reports two WLS covariate-adjusted specifications whose 95% confidence intervals for `TIENE_BILLETERA` *exclude* zero:

| Specification | Estimate | CI |
|---|---|---|
| with\_covariates (WLS) | −0.0270 | [−0.0373, **−0.0167**] |
| extended\_covariates (WLS) | −0.0257 | [−0.0363, **−0.0152**] |

Both lower and upper bounds are negative. "Every specification" is therefore factually false — two of the five reported specifications yield a statistically significant negative result on the primary outcome. The paper attempts a post-hoc rescue by invoking the randomization p-value (0.434), but that permutation test was run on the primary rdrobust baseline, not on the WLS specifications. There is no evidence the permutation null was re-run under the WLS data-generating process. The paper cannot simultaneously report Table 2 and claim all estimates are "consistent with zero."

**Required fix:** Rewrite to acknowledge that the covariate-adjusted WLS estimates reject the null under asymptotic inference, and explain precisely why those estimates are discounted in favor of the rdrobust baseline and permutation test — citing the integer running variable and the bandwidth difference, not a blanket "all specifications are null."

---

### [CRITICAL-2] Table 3 vs. Table 4 numerical inconsistency for `INTERNET_HOGAR` — unresolved from Round 3

The same variable (`INTERNET_HOGAR`) appears in both:
- **Table 3, Panel D (Placebo):** BW = 15.23, N = 29,668
- **Table 4 (Covariate Balance):** BW = 14.24, N = 27,809

The sample sizes differ by **1,859 observations**. Neither table contains a footnote explaining why the same outcome is estimated under two different bandwidths. A referee comparing the tables — as Round 3 already flagged — will halt. This is unresolved carry-forward.

---

### [MAJOR-1] Causal language applied to an ITT estimate that cannot isolate the program mechanism

**Exact sentence (Discussion §6.3):**
> "institutional digitization of government transfers should be evaluated against a realistic counterfactual: in the absence of complementary digital-literacy and smartphone-access programs, crossing the eligibility threshold does not, on average, **induce** active wallet adoption."

"Induce" is a causal verb. The paper's design is an ITT RDD at the age-65 threshold — it identifies the combined effect of crossing that threshold across the entire age-65 population, not the effect of Pensión 65 specifically. The ITT absorbs any other discontinuity at age 65 (retirement, reduced labor force participation, Medicare-analog programs, behavioral responses to approaching mortality). The paper correctly notes this elsewhere but then lapses into clean causal language at the policy-implication stage.

The same lapse appears in the Abstract:
> "institutional channels for transfer digitization being insufficient, on their own, to overcome the age gradient"

"Institutional channels for transfer digitization" are never directly observed in ENAHO — the paper observes the age-65 discontinuity. Whether it is the *institutional channel* that is insufficient or some other age-65 correlated change is not identified.

---

### [MAJOR-2] Upper bound on "program effect" ignores the take-up dilution factor

**Exact sentence (Discussion §6.1):**
> "the data support the conclusion that any positive effect of the program on digital adoption, if it exists, is smaller than approximately **3 percentage points in the pooled population**."

Three problems:

1. **"The program" vs. the ITT discontinuity.** The 3 pp figure is the upper bound on the *ITT* estimate — the average across all people crossing age 65, most of whom are not Pensión 65 beneficiaries. Take-up is approximately 75% among the eligible, and only ~22.5% of the age-65 population is jointly eligible (age ≥ 65 *and* SISFOH extreme-poor). The LATE on actual compliers could be many times larger. Bounding the program effect at 3 pp from an ITT estimate is not mathematically valid without an explicit Wald-style scaling.

2. **"In the pooled population."** The estimate is local — identified within ages 50–79 in the MSE-optimal bandwidth, without survey expansion weights. "Pooled population" implies national representativeness that the design does not deliver.

3. **"Positive effect."** The 3 pp bound covers the upper tail of the CI for the *rdrobust baseline*. The WLS covariate-adjusted estimate CI is entirely negative ([−0.0373, −0.0167]). The paper cannot simultaneously bound positive effects at 3 pp and report a precisely negative WLS CI without reconciling the two.

---

### [MAJOR-3] "First RDD evaluation, to our knowledge" — repeated unverifiable claim

This phrase appears in both the **Introduction** (§1, third paragraph) and the **Conclusion** (§6 first paragraph). The hedge "to our knowledge" does not convert an unverifiable claim into a verified one. No systematic literature search is reported. Given that (a) Pensión 65 has operated since 2011, (b) there is an active RDD literature on age-eligibility thresholds in Latin America, and (c) ENAHO microdata are publicly available, the probability that no prior applied economics working paper has examined related discontinuities is not established. If this claim cannot be verified, it should be dropped or softened to "we are not aware of."

---

### [MAJOR-4] WLS "fallback" presented as a robustness specification; its 2.4× wider bandwidth makes it a different estimand

**Exact text (Results §5.1):**
> "this covariate-adjusted specification uses a wider bandwidth (h = 34.2 years) and a weighted least squares (WLS) estimator implemented via statsmodels **as a fallback** when the local-polynomial rdrobust routine encountered memory limitations"

A method chosen because of computational constraints on a specific machine is not a robustness check — it is a forced methodological substitution with a fundamentally different estimand (local effect at the cutoff under h=14.2 vs. a smoothed average over ages 31–79 under h=34.2). The paper acknowledges the bandwidth difference but presents the WLS result in Table 2 alongside the rdrobust baseline as if they are comparable alternative specifications. The claim in the abstract that the covariate-adjusted estimate "is best read as describing the broader age-adoption profile rather than as a refined local effect at the cutoff" confirms the estimands differ — which means the WLS row of Table 2 should not appear as a robustness specification for the rdrobust ITT estimate.

---

### [MAJOR-5] McCrary density test statistic reported without p-value

**Exact sentence (§5.2):**
> "The McCrary-style density test of Cattaneo et al. (2018) produces a test statistic of 2.0"

A test statistic without a p-value or critical value is uninterpretable. Under the rddensity implementation for a variable with integer mass points, the reference distribution is not standard normal. The paper says "there is no evidence of bunching specifically at age 65" but provides no basis for that conclusion beyond asserting a test statistic of 2.0. Depending on the reference distribution, 2.0 may or may not cross conventional significance thresholds. The p-value must be reported.

---

### [MINOR-1] Mechanism claims asserted as explanations, not hypotheses

The paper's three substantive interpretations of the null result (§6.1) are presented with declarative confidence:

> "A null result on this margin would be consistent with prior literature on the dormancy of forced accounts."

> "the secular age gradient in technology adoption is steep enough at age 65 that any program-specific positive effect is overwhelmed by underlying cohort differences"

These are plausible narratives, not tested hypotheses. Neither dormancy (the Bachas et al. mechanism) nor cohort composition (the gradient mechanism) is directly identified in the ENAHO cross-section. The paper should flag these as candidate mechanisms, not as supported findings.

---

### [MINOR-2] "Would face few financial-inclusion incentives" asserted without evidence

**Exact sentence (§3.4, Institutional Background):**
> "The program therefore creates an institutional push toward digital onboarding for a population that, absent the program, **would face few financial-inclusion incentives**."

This claim is stated as established fact. Whether the elderly extreme-poor in Peru face "few" financial-inclusion incentives absent Pensión 65 depends on market structure, family remittances, informal labor, and access to other transfer programs — none of which are measured or cited here. The statement should be hedged: "…a population that arguably faces fewer financial-inclusion incentives from private-market sources."

---

### [MINOR-3] Permutation inference scope is ambiguous

The paper reports one randomization p-value (0.434) on the "primary outcome" and uses it to override the asymptotic WLS CI rejection. But it is not stated whether the permutation test was computed on the rdrobust statistic, the WLS statistic, or both. If it was computed only on the rdrobust statistic (the most natural reading), it does not logically override the WLS CI, and the dismissal of the WLS result as "asymptotic SEs understate uncertainty" remains an assertion rather than a demonstrated fact.

---

### [MINOR-4] Population mean of `USA_BILLETERA` is inconsistent with within-bandwidth mean

The paper states: "`USA_BILLETERA`: Population mean: 15.6%." But Table 1 (full sample) shows `USA_BILLETERA` mean = 17.94% for the control group and 3.19% for the treated group, and the within-bandwidth mean reported in the text is 12.4% (control) / 4.0% (treated). The "population mean" of 15.6% does not match either the full-sample weighted mean (which would require applying `FACTOR_EXPANSION`, noted as absent from the cleaned data in the Data Audit) or the bandwidth-restricted sample mean. The source of this figure should be clarified.

---

```json
{
  "n_critical": 2,
  "n_major": 5,
  "n_minor": 4,
  "causal_overclaiming": [
    "crossing the eligibility threshold does not, on average, induce active wallet adoption",
    "institutional channels for transfer digitization being insufficient, on their own, to overcome the age gradient in digital financial behavior",
    "the intent-to-treat estimates are small, precisely bounded, and consistent with zero across every specification, bandwidth, and inference procedure we examined",
    "the data support the conclusion that any positive effect of the program on digital adoption, if it exists, is smaller than approximately 3 percentage points in the pooled population"
  ],
  "missing_caveats": [
    "The 3 pp upper bound applies to the ITT discontinuity, not the program LATE; the complier effect could be several times larger given ~22.5% joint eligibility rate and ~75% take-up",
    "The permutation p-value scope (rdrobust vs. WLS statistic) is not stated, so it cannot logically override the WLS CI rejection",
    "McCrary test statistic of 2.0 is reported without a p-value; conclusion of no bunching is unsupported",
    "Table 3 and Table 4 report INTERNET_HOGAR under materially different bandwidths (15.23 vs. 14.24) and sample sizes (29,668 vs. 27,809) with no explanation — unresolved from Round 3",
    "The WLS specification is a methodological fallback due to computational constraints, not a robustness check; its 2.4x wider bandwidth identifies a different estimand from the rdrobust baseline"
  ]
}
```