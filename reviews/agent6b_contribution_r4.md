## Referee Report

**Paper:** Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption? A Regression Discontinuity Analysis with ENAHO 2024

---

### Part 1 — Central Contribution

The paper provides the first regression-discontinuity estimate of Peru's Pensión 65 cash-transfer program on digital financial inclusion, exploiting the age-65 eligibility cutoff in the 2024 ENAHO survey — the first wave to separately identify digital wallet ownership and use in the microdata.

**Rating: Incremental.** The design is competent and the data are novel (2024 ENAHO with wallet variables), but the contribution is a single-context null result without population-level calibration. Null findings with tight confidence intervals are valuable; this one is somewhat underpowered for the policy interpretation it carries. Appropriate for a development field journal; ambitious for a top-five target.

---

### Part 2 — Identification and Credibility

**Variation used.** The running variable is completed age in years; the cutoff is 65, the minimum age for Pensión 65 eligibility. The design is administratively sharp on the age dimension but acknowledged to be fuzzy with respect to actual program receipt (incomplete take-up, joint SISFOH filter). The authors correctly frame this as an ITT discontinuity.

**Plausibility of exogeneity.** The McCrary density test and the balance table (Table 3, implied) provide the standard evidence. Age heaping in self-reported integer ages is a known concern in LMIC household surveys and is not fully addressed by the local-polynomial density test — the latter is most powerful against smooth bunching, not coarse rounding. This deserves at least a brief empirical check (e.g., compare density mass at age 65 vs. neighboring integers 63, 64, 66, 67).

**Main threat — compound discontinuity.** Age 65 in Peru is not only the Pensión 65 threshold. It coincides with SIS (Seguro Integral de Salud) age-specific coverage rules and, for many workers, informal retirement norms. The paper acknowledges this verbally ("combined effect of program eligibility and any other age-65-specific changes") but makes no attempt to isolate the Pensión 65 channel from these confounds. For a null result this matters less — if everything at the threshold combined is zero, each component is also bounded — but the positive interpretation ("institutional channels are insufficient") requires that the Pensión 65 channel be distinguishable. It is not, in the current design.

**Absence of a first stage.** Because ENAHO is not linked to MIDIS administrative records, the authors cannot document the take-up discontinuity at the cutoff. They are explicit about this, but without a first-stage estimate the null cannot be translated into a LATE bound, nor can the reader assess whether the design has any power to detect a plausible treatment effect. The claim of a "well-powered null" in the abstract is asserted, not demonstrated.

**Covariate-adjusted specification inconsistency.** The local-linear baseline yields $\hat{\tau} = -0.006$ (SE $= 0.016$); the covariate-adjusted specification yields $-0.027$ (SE $= 0.005$). The paper discloses that these differ because the covariate-adjusted model uses a **wider** bandwidth, attributing the discrepancy to the "broader age-adoption profile." This is methodologically inconsistent: the RDD estimator identifies local variation at the cutoff, not the global age gradient. Widening the bandwidth until the estimate is driven by secular trends and then reporting it as a covariate-adjusted treatment effect is misleading, regardless of the sign. The covariate-adjusted specification should use the MSE-optimal bandwidth from `rdrobust`'s built-in covariate-adjustment routine — not an ad-hoc wider window.

---

### Part 3 — Required and Suggested Analyses

#### Required — absence blocks publication

**None rise to the level of making results uninterpretable.** The core null finding is clearly stated and robustly checked across bandwidth, polynomial order, donut hole, placebo cutoffs, and permutation inference. The paper has passed the interpretability bar.

That said, the following issues need resolution before the paper is ready to be sent to outside referees:

**[MAJOR-1] Covariate-adjusted bandwidth inconsistency** (discussed above). Re-estimate the covariate-adjusted specification using the MSE-optimal bandwidth from `rdrobust` with the `covs` argument. If the wider bandwidth is retained for any reason, it must be labeled clearly as a descriptive regression of the age-adoption profile, not as an alternative RDD estimate.

**[MAJOR-2] Template boilerplate in output tables.** The code review audit confirms that submitted tables contain language from an electoral-threshold study: "municipality-elections where the party's vote share exceeded the electoral threshold" (Table 1 note), "at the Electoral Threshold" (Table 4 header), and "Vote Margin" (Figure 1 x-axis). These artifacts must be corrected. For a top-field submission, their presence signals a quality-control failure that will concern editors independently of the economics.

**[MAJOR-3] Minimum detectable effect and power calibration.** The paper asserts a "precisely estimated null" and refers to the result as "well-powered." Demonstrate this. Given the first-stage take-up rate (~75% among eligible extreme-poor, according to the institutional description) and the pre-treatment baseline wallet rate within the bandwidth (12.9% for control-side observations), report the minimum detectable effect (MDE) at 80% power for the baseline bandwidth. If the MDE is, say, 3 percentage points and actual wallet rates in the treated subpopulation are below 10%, the null is informative. If the MDE is 6–8 points, the null is less decisive than claimed.

#### Suggested — would strengthen, not blockers

**[SUGGESTED-1] SISFOH-stratified subsample.** The relevant first-stage variation is concentrated among extreme-poor individuals who are SISFOH-classified. ENAHO contains poverty classification from the Sumaria module (`POBREZA`). Restricting the RDD to the extreme-poor subsample (POBREZA = 1) would sharpen the design and provide a subsample where program take-up is plausibly higher, allowing a more credible bound on the LATE.

**[SUGGESTED-2] Age-heaping robustness check.** Report the raw histogram of observations per single-year age bin within $[55, 75]$. If mass at age 65 is visually inconsistent with neighbors, implement a donut-hole (already partially done, good) and also consider a quadratic-in-age control for the full density. The McCrary test is necessary but not sufficient for heaping in integer-coded ages.

**[SUGGESTED-3] Urban/rural heterogeneity.** Wallet adoption in Peru is heavily urban-concentrated. The null could mask a positive urban effect offset by a negative or zero rural effect. An interaction with the urban dummy (available in ENAHO) would address whether institutional digitization has differential effects along the urban-rural divide, directly informing policy.

**[SUGGESTED-4] Survey-weighted descriptives.** The paper correctly disclaims population-level inference and explains the non-weighting convention for RDD. However, the abstract's statement that "roughly one in five adult transactions outside cash involved a digital wallet" is a population claim, while the sample wallet ownership mean is 7.4%. This gap is jarring. Report population-weighted descriptive statistics separately from the (unweighted) RDD estimates, and make the disconnect explicit in the paper body, not just in a methodological footnote.

**[SUGGESTED-5] Program receipt proxy via Banco de la Nación account ownership.** ENAHO likely captures bank account ownership (P558E1, response codes for BdN). If so, this could serve as a noisy first-stage proxy. An RDD on BdN account ownership at the cutoff would (a) quantify the take-up discontinuity indirectly and (b) enable a Wald-type IV bound on the LATE, even if imperfect.

---

### Part 4 — Literature Positioning

The citations are largely appropriate. Jack and Suri (2014), Suri (2017), Bachas et al. (2018), Muralidharan et al. (2016), and Banerjee et al. (2020) are the right anchors for the government-transfer–financial-inclusion question. The RDD methodology stack (Calonico et al. 2014, 2019; Cattaneo et al. 2018) is current.

**Gap 1:** The recent Pix literature from Brazil (e.g., Duarte, Rodrigues, and Vaz 2022 on the distributional take-up of instant payments) is directly relevant and would sharpen the comparative frame for why Peru's null differs from Brazil's rapid adoption trajectory.

**Gap 2:** The Aizenman et al. (2022) citation is the stated "closest application," but the paper does not report what that study found, only that it "document[s] weak first-stage effects on digital savings." A one-sentence direct comparison — same null or different magnitude — would anchor the reader.

**Gap 3:** There is a growing literature on the dormancy of government-mandated bank accounts (in addition to Bachas et al.): Kast and Pomeranz (2018, JPubE) on Chile and Brune et al. (2016) on Malawi provide additional comparators for the forced-account dormancy mechanism invoked as a theoretical explanation.

---

### Part 5 — Journal Fit and Recommendation

**For a top-five field journal (JPE, QJE, REStud, AER):** The contribution is too narrow and the design too limited (single cross-section, no administrative linkage, no first stage, no population-weighted estimates) to be competitive with papers the typical top-five editor would compare it against.

**For a top-field development/applied-micro journal (JDE, JEBO, World Bank Economic Review, American Economic Journal: Applied):** The paper is a credible candidate after revision. The 2024 ENAHO data are genuinely novel, the RDD robustness battery is thorough, and a well-powered null on an institutional digitization program has policy relevance.

**Recommendation: Revise before sending.** The template boilerplate in tables (Major-2) must be corrected unconditionally. The covariate-adjusted bandwidth inconsistency (Major-1) and the absence of MDE calibration (Major-3) are substantive gaps that will draw referee comments even at a second-tier journal. Resolving these three issues before submission is strongly advisable.

---

### Part 6 — Questions to the Authors

1. **First stage.** You estimate an ITT of $-0.006$ but cannot observe take-up. Table~\ref{tab:summary} implies wallet adoption is 5.35% above the cutoff versus 8.00% below in the full sample, but this is the raw gap across all ages above and below 65 — not a first-stage discontinuity. Do you have any evidence that the Pensión 65 take-up rate itself exhibits a discontinuity at age 65 within the ENAHO sample, even proxied through Banco de la Nación account ownership? Without any first-stage evidence, the null result is consistent with either (a) no effect conditional on take-up or (b) near-zero take-up at the margin.

2. **Covariate-adjusted bandwidth.** Why does the covariate-adjusted specification use a wider bandwidth than the MSE-optimal bandwidth from the baseline? Specifically: (a) what bandwidth does it use, and how was it selected? (b) Is the $-0.027$ estimate stable if you apply the MSE-optimal bandwidth with the `covs` argument in `rdrobust`? If it collapses toward zero, the current presentation is materially misleading.

3. **Compound discontinuity.** Several other institutional changes cluster at age 65 in Peru beyond Pensión 65 (SIS coverage adjustments, informal retirement norms). What evidence do you have that the age-65 cutoff is informative specifically about Pensión 65 rather than this combination? Could you instrument for Pensión 65 receipt using the SISFOH classification interacted with the age-65 cutoff, or restrict to the extreme-poor subsample where the Pensión 65 channel dominates?

4. **Age heaping.** Integer age coding in ENAHO means all individuals are classified at exact year bins. Can you show the raw histogram of observations per single-year age bin within $[55, 75]$? If age 65 is over-represented relative to 63, 64, 66, and 67, what does this imply for the continuity assumption?

5. **Outcome divergence.** The population mean for `TIENE_BILLETERA` is 7.4% but for `USA_BILLETERA` it is 15.6% — indicating that a large fraction of active wallet users do not self-report owning a wallet. This could reflect measurement error (informal use without formal account registration, or question misunderstanding) or a genuine product-bundling pattern. Can you characterize this discordance and explain why the two outcomes should be expected to respond differently to the Pensión 65 threshold?

6. **Power.** You assert a "precisely estimated null." Please report the minimum detectable effect at 80% power for the primary outcome using the baseline bandwidth and sample size. Given a pre-treatment wallet adoption rate of approximately 13% in the control side of the bandwidth, is a 3-percentage-point effect detectable? A 5-point effect?

7. **Template artifacts.** Table 1 notes and Figure 1 axis labels contain language from an electoral-RDD study unrelated to this paper. Are the underlying table construction scripts fully specific to this study, or are there other inherited artifacts (e.g., miscoded variable labels, wrong outcome descriptions) that may have survived into the tables?

---

### Scoring

```json
{
  "score": 69,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 68,
    "identification_credibility": 74,
    "empirical_execution": 69,
    "writing_presentation": 63,
    "literature_positioning": 72
  },
  "required_analyses": [
    "Covariate-adjusted specification must use MSE-optimal bandwidth (not an ad-hoc wider window); current -0.027 estimate conflates the secular age gradient with the local treatment effect at the cutoff",
    "Template boilerplate must be purged from all tables and figures before any submission (electoral-threshold language in Table 1 notes and Figure 1 axis label)",
    "Minimum detectable effect calculation needed to substantiate the 'well-powered null' claim in the abstract"
  ],
  "suggested_analyses": [
    "SISFOH-stratified RDD subsample (extreme-poor only) to sharpen the first-stage relevance and provide a bound on the LATE",
    "Raw age histogram within [55, 75] to diagnose integer-age heaping and assess continuity assumption robustness",
    "Urban/rural heterogeneity analysis — wallet adoption in Peru is heavily urban, and the null may mask offsetting effects",
    "Banco de la Nación account ownership as a noisy first-stage proxy to bound the take-up discontinuity at the cutoff",
    "Population-weighted descriptive statistics reported separately from unweighted RDD estimates, with explicit reconciliation of the 7.4% sample mean vs. BCRP aggregate figures cited in the introduction"
  ],
  "questions_to_authors": [
    "Do you have any evidence — even proxied through Banco de la Nación account ownership in ENAHO — that Pensión 65 take-up itself exhibits a discontinuity at age 65? Without a first-stage estimate, the null is consistent with near-zero take-up at the margin rather than zero effect conditional on take-up.",
    "Why does the covariate-adjusted specification use a wider bandwidth than the MSE-optimal baseline? Is the -0.027 estimate stable when rdrobust is run with the covs argument at the optimal bandwidth, or does it collapse toward zero?",
    "Several other institutional changes cluster at age 65 in Peru beyond Pensión 65. What evidence distinguishes the Pensión 65 channel from this compound discontinuity, and could restricting to extreme-poor individuals sharpen the identification?",
    "The raw histogram of observations per single-year age bin within [55, 75] — is age 65 over-represented relative to neighbors? What are the implications for the continuity assumption if heaping is present?",
    "The population mean for USA_BILLETERA (15.6%) substantially exceeds TIENE_BILLETERA (7.4%), implying many active wallet users do not self-report owning one. Does this discordance reflect measurement error in ownership coding or a genuine behavioral pattern, and how does it affect the interpretation of two separate null effects?",
    "What is the minimum detectable effect at 80% power given the baseline bandwidth and the ~13% control-side adoption rate? Is the null informative at, say, a 3-percentage-point treatment effect?",
    "Are the surviving template artifacts (electoral-threshold language in Table 1 notes, Vote Margin label in Figure 1) isolated to labeling, or do they indicate that any underlying estimation code may have been misconfigured for this study's outcomes and sample?"
  ],
  "n_critical": 0,
  "n_major": 3
}
```