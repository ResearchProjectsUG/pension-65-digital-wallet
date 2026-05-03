## Claim Discipline Review — Pensión 65 / ENAHO 2024 RDD Paper

> **Note**: The `main.tex` body was not provided — only the bibliography preamble and four tables are available. This review is therefore grounded in the tables, data audit, code review, and inferences from prior-round feedback. Claims I cannot verify from these sources are flagged as "unverifiable from available material" rather than assumed absent.

---

### [CRITICAL-1] Primary RDD Estimator Shows Null Effects on Both Outcomes

**What the tables actually say (Table 2, baseline row):**

| Outcome | Estimate | 95% CI | Significant? |
|---|---|---|---|
| `TIENE_BILLETERA` | −0.0056 | [−0.034, 0.031] | **No** |
| `USA_BILLETERA` | +0.0066 | [−0.034, 0.037] | **No** |

The `rdrobust` estimator — the *only* proper nonparametric RDD specification — finds precisely zero on both outcomes. Any sentence in the paper claiming Pensión 65 eligibility *increases* (or systematically affects) digital wallet ownership or usage is flatly contradicted by the headline identification strategy.

**What counts as overclaiming here:** Any abstract, introduction, or conclusion language of the form "we find that Pensión 65 eligibility increases digital financial inclusion," "our RDD estimates show positive effects," or "program access drives adoption" is unsupported by the primary estimator.

---

### [CRITICAL-2] Significant Results Come from a Non-RDD Estimator with 2.4× Wider Bandwidth

Table 2, `with_covariates` and `extended_covariates` rows use `statsmodels_WLS` at bandwidth h = 34.22 — nearly **2.4 times** the MSE-optimal bandwidth of 14.24. This is not a covariate-adjusted RDD; it is a parametric weighted least squares regression on a sample that extends ≈34 years on either side of the cutoff.

Critical distinctions:

1. **Local vs. global identification**: `rdrobust` at h = 14.24 exploits local continuity. WLS at h = 34.22 requires a globally correct parametric functional form for age — a strong and untestable assumption.
2. **The bandwidth change and the estimator change are confounded**: The paper cannot separately attribute the sign switch (from null to −0.027 on `TIENE_BILLETERA`) to covariates vs. to the massive bandwidth expansion.
3. **The negative significant result on wallet *ownership* is the wrong sign** for a story about program-induced adoption: the covariate-adjusted estimate says eligibility *reduces* `TIENE_BILLETERA` by 2.7 pp. If the paper frames this as evidence the program reduces financial inclusion barriers, the sign is inconsistent. If it frames this as a spurious artifact, the WLS specification should not be the lead result.

Any sentence presenting the WLS estimates as "the RDD result" or treating them interchangeably with the `rdrobust` estimates is a methodological overclaim.

---

### [CRITICAL-3] No Survey Weights — Population-Level Claims Are Unwarranted

The data audit explicitly flags: *"No survey weight column found. Results may not be population-representative."*

ENAHO uses a stratified multi-stage cluster design. Unweighted estimates identify effects for the sample composition, not for the Peruvian elderly poor population. Any sentence of the form:

> "…among the elderly poor in Peru…"
> "…older adults in Peru face barriers to digital adoption…"
> "…our findings suggest that policy X would affect Y% of the target population…"

is unwarranted without survey-weighted estimates. This is not a robustness issue — it is a fundamental validity issue for policy inference.

---

### [MAJOR-1] All Heterogeneity Estimates Are Statistically Insignificant

Table 2, heterogeneity by SISFOH block:

| Group | `TIENE_BILLETERA` CI | Significant? |
|---|---|---|
| Extreme-poor (=1) | [−0.010, 0.060] | No |
| Non-extreme-poor (=2) | [−0.015, 0.041] | No |
| Non-poor (=3) | CI not shown (truncated) | Unknown |

All cells span zero. Claims of the form "the effect is concentrated among the extreme poor" or "heterogeneous effects by poverty status suggest targeting inefficiencies" are not supported. The subgroup N values are small (N_eff = 1,229 and 3,157), compounding the imprecision.

---

### [MAJOR-2] `USA_BILLETERA` Heterogeneity Entirely Missing

Every heterogeneity cell for `USA_BILLETERA` is "---" in Table 2. If the paper discusses differential effects on *usage* by poverty status, those cells do not exist. The claim cannot be made.

---

### [MAJOR-3] Severe Sample Imbalance Threatens RDD Validity and Is Not Discussed

Table 1 shows **14,088 treated vs. 99,667 control** — a 7:1 ratio. For an age-cutoff RDD at 65, one would expect roughly symmetric density near the cutoff. A ratio this extreme suggests either (a) the running variable has a sharp distributional break at the cutoff (manipulation), (b) the bandwidth chosen by `rdrobust` is asymmetric, or (c) the sample draws from a much wider age range below 65 than above. Any paper using this design must explain and test this imbalance explicitly. If the McCrary density test is also unreliable due to the code bug flagged below, this threat is unaddressed.

---

### [MAJOR-4] McCrary Density Test May Be Silently Returning `NaN`

The code review flags: *"`rddensity` p-value extraction via `rd_den.p` — the rddensity Python package stores results in `.test` rather than a direct `.p` attribute; if `.p` doesn't exist the p-value silently becomes `np.nan`."*

If the manipulation test p-value reported in the paper is `NaN` silently treated as a pass, the paper is reporting a fabricated test result. The claim "the McCrary density test shows no evidence of manipulation (p = X)" is unverifiable and potentially wrong. This must be verified and recomputed before submission.

---

### [MAJOR-5] Covariate Balance Table Confirms Continuity, But SMARTPHONE Has Borderline CI

Table 4:

| Covariate | 95% CI |
|---|---|
| `SMARTPHONE` | [−0.015, 0.086] |

The lower bound is −0.015 and the upper bound is 0.086. While this includes zero, the interval is asymmetric and leans positive. With N = 27,809 this is a wide interval suggesting a potential 8.6 pp smartphone gap at the cutoff. The paper's claim that "none of the covariates exhibit a discontinuity" is technically accurate but obscures that `SMARTPHONE` is the weakest case — worth a sentence of acknowledgment rather than a blanket reassurance.

---

### [MAJOR-6] Template Boilerplate Survived Into Output Scripts

The code review confirms: *"Table 1 note mentions 'municipality-elections where the party's vote share exceeded the electoral threshold'; Table 4 header says 'at the Electoral Threshold'; Figure 1 x-axis label reads 'Vote Margin'."*

If any of this language appears in the submitted PDF, the paper is claiming results in an electoral RDD study while actually running a pension eligibility study. This is not a minor editing error — it signals to referees that the analysis was not purpose-built for this question. From a claim-discipline perspective: **any inference drawn from figures or tables bearing electoral labels cannot be attributed to the Pensión 65 design.**

---

### [MINOR-1] Statistical vs. Economic Significance Conflation (WLS Specification)

The WLS estimate on `TIENE_BILLETERA` is −0.027 with SE = 0.005. It is statistically significant. But the baseline rate for the treated group is 5.35% (Table 1). A −2.7 pp effect is a **50% reduction in wallet ownership** at the cutoff — an implausibly large negative effect that is more likely to reflect age-trend confounding than a genuine program effect. Even if the identification were valid, the paper must confront whether the magnitude is economically plausible, not just statistically distinguishable from zero.

---

### [MINOR-2] ITT vs. LATE Conflation

The introduction (per prior-round feedback) frames the estimand as an "intent-to-treat (ITT) estimate of institutional access on digital adoption." ITT is correct only if all eligible individuals actually receive program benefits at the same rate. If Pensión 65 enrollment is imperfect (likely, given administrative capacity constraints in Peru), the ITT estimate is attenuated relative to the treatment-on-the-treated (TOT/LATE). Any interpretation of the ITT as measuring "the effect of receiving Pensión 65 benefits" overstates what is identified. The paper should be explicit that it estimates the effect of *crossing the eligibility threshold*, not *receiving the benefit*.

---

### [MINOR-3] Bandwidth Double Estimate Has Inverted Sign

Table 3, Panel A:

| Bandwidth | Estimate | CI |
|---|---|---|
| Half (7.12) | −0.006 | [−0.050, 0.037] |
| Optimal (14.24) | −0.006 | [−0.040, 0.031] |
| Double (28.48) | −0.020 | [−0.027, 0.026] |

At double bandwidth the estimate moves to −0.020 while remaining insignificant. Claims that "results are stable across bandwidths" overstate robustness — the direction is consistent (negative) but the magnitude nearly quadruples, which is a sensitivity worth flagging honestly rather than dismissing.

---

```json
{
  "n_critical": 3,
  "n_major": 6,
  "n_minor": 3,
  "causal_overclaiming": [
    "Any sentence claiming Pensión 65 eligibility increases digital wallet ownership or usage — the primary rdrobust estimator shows null effects on both outcomes (TIENE_BILLETERA: −0.006 [−0.034, 0.031]; USA_BILLETERA: +0.007 [−0.034, 0.037])",
    "Any sentence presenting the statsmodels_WLS estimates as 'the RDD result' — WLS at h=34.22 is a parametric regression, not a local polynomial RDD, and the estimator and bandwidth change are confounded",
    "Any population-level claim about 'elderly poor in Peru' — ENAHO survey weights are absent and unweighted estimates are not population-representative",
    "Any claim of heterogeneous effects by SISFOH poverty status — all subgroup estimates span zero and N_eff cells are as small as 1,229",
    "Any claim that 'the McCrary density test shows no manipulation' — the p-value extraction is potentially bugged (`.p` attribute may silently return NaN)",
    "Any inference attributed to Figure 1 or Table 4 if the x-axis still reads 'Vote Margin' or 'Electoral Threshold' — template boilerplate from an electoral RDD survived into the output scripts"
  ],
  "missing_caveats": [
    "No survey weights: ENAHO is a stratified multi-stage cluster design; unweighted results are not population-representative and no caveat appears in the data audit response",
    "Estimator mismatch: the baseline rdrobust and the covariate-adjusted WLS are not comparable specifications; the paper must acknowledge they identify different estimands under different bandwidth and functional-form assumptions",
    "Severe sample imbalance (14,088 treated vs. 99,667 control) is unexplained and untested; the RDD density assumptions require symmetric support near the cutoff",
    "USA_BILLETERA heterogeneity data is entirely missing — no estimates exist for this outcome in the SISFOH subgroup analysis",
    "The negative significant estimate on TIENE_BILLETERA (−2.7 pp) in the covariate-adjusted spec is the wrong sign for adoption-promotion; no explanation is offered",
    "ITT vs. LATE distinction: if Pensión 65 enrollment is incomplete, the ITT is attenuated relative to the benefit-receipt effect and the two should not be conflated",
    "Bandwidth sensitivity shows the estimate nearly quadruples from optimal to double bandwidth (−0.006 to −0.020) — 'stable across bandwidths' overstates robustness"
  ]
}
```