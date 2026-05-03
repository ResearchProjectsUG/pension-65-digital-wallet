## Referee Report — *Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption?*

---

### Part 1 — Central Contribution

The paper estimates the intent-to-treat effect of crossing Peru's Pensión 65 age-65 eligibility threshold on digital wallet ownership and active use, using the first ENAHO wave (2024) to include wallet adoption as a distinct survey category, and documents a precisely estimated null result across multiple specifications and robustness procedures.

**Rating: Incremental.** The design is not novel (age-RDD at a pension threshold is standard), but the outcome domain (digital wallet adoption), the data vintage, and the policy question are genuinely new for this setting. A well-powered null from a credible design in a middle-income country with an explicit institutional digitization push has real informational value.

---

### Part 2 — Identification and Credibility

**Variation used.** A sharp discontinuity in Pensión 65 eligibility at completed age 65. The running variable is age in integer years; the cutoff is administratively fixed and publicly known.

**Plausible exogeneity.** Age is not manipulable in the usual strategic sense, and the McCrary density test and balance checks reportedly confirm continuity at the cutoff. This is the paper's main strength.

**Threat 1 — The full-population vs. eligible-population mismatch.** Pensión 65 requires *both* age ≥ 65 *and* SISFOH extreme-poor classification. The paper estimates the RDD on the full ENAHO sample (N = 113,755), in which SISFOH-eligible extreme-poor individuals represent roughly 30% of the age-65-and-above group. The ITT on the full population is legitimate, but the effective "dose" at the cutoff is heavily diluted. The paper acknowledges the ITT framing but does not report a subgroup estimate restricted to SISFOH-classified individuals — the one sample where the institutional channel is actually switched on. This is not a fatal flaw, but it means the null could reflect dilution rather than absence of effect on compliers.

**Threat 2 — Age-65 as a multi-program threshold.** Age 65 in Peru is not only Pensión 65 eligibility; it also coincides with changes in Essalud benefit rules, formal labor-market exit norms, and other institutional shifts. The paper acknowledges this but does not attempt to decompose the running-variable confound.

**Threat 3 — Cross-sectional measurement of a flow program.** The wallet ownership variable is a cross-sectional stock measure at survey date. Program beneficiaries may have received disbursements over multiple years, yet the survey captures only a snapshot. The paper does not discuss whether any dynamics in the take-up rate between cohorts could produce measurement noise at the cutoff.

---

### Part 3 — Required and Suggested Analyses

**Required (blockers):**

**[CRITICAL-1] — Bandwidth inconsistency in the covariate-adjusted specification.** The paper reports a covariate-adjusted estimate of −0.027 (SE = 0.005, CI [−0.037, −0.017]) but explicitly states this uses a bandwidth of *h* = 34.2 years — more than double the optimal *h\** = 14.2 from the local-linear baseline — because rdrobust "encountered memory limitations." Using a 34-year bandwidth for a design centered on a threshold at age 65 is not a RDD estimate: it is a global age regression. The paper acknowledges this in prose but then presents the estimate in Table 2 alongside the local-linear baseline without clearly signaling to a reader scanning the table that the two rows are identifying different quantities. The covariate-adjusted column must either (a) be re-estimated at *h\** = 14.2, or (b) be removed from the main results table and relegated to a clearly labeled appendix as a descriptive exercise. As currently presented, the table invites misreading.

**[CRITICAL-2] — The t-statistic / permutation p-value inconsistency is unexplained.** The paper reports a t-statistic of approximately −5.1 in the covariate-adjusted WLS specification yet a permutation randomization p-value of 0.434 on the "primary outcome." The paper attributes the gap to the discrete running variable causing asymptotic SEs to understate uncertainty — a plausible mechanism — but then adopts p = 0.434 as "the primary inference result" without demonstrating that the permutation procedure is correctly specified. If the permutation randomizes treatment assignment within the age window [55, 75] without respecting the actual local-polynomial estimator (i.e., if it re-randomizes on the WLS coefficient from a wide-bandwidth regression rather than the local-linear coefficient at *h\** = 14.2), the permutation test and the asymptotic test are not testing the same estimand. The paper must clarify: (a) which estimator the permutation p-value corresponds to — local-linear at *h\** or WLS at *h* = 34.2; (b) why a p-value of 0.434 and a t-stat of −5.1 can both be valid for the same estimand; and (c) provide a permutation null distribution plot so that the reader can assess whether the test statistic falls inside the null mass.

**Suggested (would strengthen):**

**[MAJOR-1] — SISFOH-stratified subgroup estimate.** The most direct test of the institutional channel hypothesis is an RDD estimated on the subsample of SISFOH-classified extreme-poor individuals around age 65. ENAHO includes the POBREZA variable, which can proxy this restriction. Without this, the null result is uninformative about whether the program effect is zero for eligible individuals or merely diluted by the full-population denominator. The paper cites dilution as a concern in passing but takes no analytic step to address it.

**[MAJOR-2] — Survey-weight adjustment.** The data audit flags the absence of ENAHO's official expansion factor (FACPOB07) in the estimation. ENAHO is a stratified cluster design with documented urban-rural and regional oversampling. Unweighted RDD estimates can be consistent if the density test confirms no manipulation — and the paper performs that test — but the population-level interpretation of wallet adoption rates (e.g., "7.4% mean") rests on weighted estimates. The paper should either use survey-weighted outcomes or explicitly defend why unweighted local estimates are the correct estimand.

**[MAJOR-3] — Heterogeneity by area type (rural/urban) and gender.** The secular age-adoption gradient is substantially steeper for rural and female respondents in most digital financial inclusion studies. Pooled null effects at the cutoff could mask positive effects in urban subsamples. Subgroup RDDs by area or gender would sharpen the policy interpretation.

**[MAJOR-4] — Correct boilerplate in output scripts before submission.** The code review confirms that table notes and figure axis labels surviving from an electoral RDD template (references to "municipality-elections," "vote share," "Vote Margin," "Electoral Threshold") appear in the output scripts. These are apparently not in the version submitted — I note them here because the reproducibility package, if released, would be misleading.

**[MAJOR-5] — Effect on intermediate outcomes (Banco de la Nación account ownership).** If crossing the eligibility threshold does not affect wallet adoption, it is worth confirming whether it affects Banco de la Nación account ownership — a closer-to-treatment outcome. If ENAHO 2024 includes this (the bank-account ownership question P558E1 covers multiple institutions), an RDD on account ownership would bound the compliance margin and distinguish between zero-program-uptake and program-uptake-with-no-downstream-effect.

---

### Part 4 — Literature Positioning

The citations to Calonico et al. (2014, 2019) and Cattaneo et al. (2018) are correct and the methodological framing is accurate. The financial inclusion citations (Jack & Suri 2014, Bachas et al. 2018, Muralidharan et al. 2016) are appropriate and well integrated.

Two concerns:

**Galiani (2020).** The paper cites "Galiani (2020)" three times as evidence on transfer digitization effects in Argentina. No working paper or publication with this exact profile appears in standard databases as of knowledge cutoff. If this citation is fabricated — a non-trivial risk for an autonomously generated paper — it must be removed or replaced with the actual source. The editors will verify every citation.

**Missing Peru-specific digital finance evidence.** The BCRP (2024) report cited exists, but the literature review omits any reference to INEI or MIDIS administrative evaluations of Pensión 65 that have been published since 2018. The paper positions itself as "the first sharply-identified evidence" on the program's digital effects, which may be accurate — but this claim should engage with any prior reduced-form or descriptive work on the program more explicitly.

---

### Part 5 — Journal Fit and Recommendation

For a **top-field** economics journal (AER, JPE, QJE, RES), the standard contribution bar is transformative or at minimum a major advance in an important debate. This paper is an incremental but honest and credible contribution to the financial inclusion literature. The institutional setting is specific to Peru, the null result is well-documented, and the 2024 data vintage is timely — but the design is standard, the finding is not surprising given prior literature, and the methodological execution has the two critical gaps described above.

The paper is better positioned for a **field journal** (Journal of Development Economics, World Development, JEBO, American Economic Journal: Applied Economics) where a credible null from a nationally representative RDD in a LMIC context would receive serious consideration.

**Recommendation: Revise before sending.**

The two critical issues — bandwidth inconsistency in the covariate-adjusted column and the unresolved t-stat/permutation-p contradiction — must be resolved before this draft is ready for external referees. Both are correctable in a focused revision and do not require new data collection.

---

### Part 6 — Questions to the Authors

1. The covariate-adjusted estimate uses a bandwidth of 34.2 years, attributed to computational constraints with rdrobust. Can you re-estimate this specification at the optimal local-linear bandwidth *h\** = 14.2 using a lighter estimator (e.g., the `lm`/`statsmodels` local-linear at *h\** rather than the global WLS)? The 34-year window spans ages 31–99 and cannot plausibly satisfy the continuity-of-potential-outcomes assumption that justifies the RDD interpretation.

2. The randomization p-value of 0.434 and the WLS t-statistic of −5.1 coexist in the paper. Which estimator — local-linear at *h\** or WLS at *h* = 34.2 — does the permutation test use? Please provide the permutation null distribution plot and confirm that both the observed statistic and the permuted statistics are computed from the same estimator and bandwidth.

3. SISFOH-classified extreme-poor individuals at age 65 are the direct targets of the institutional channel this paper studies. Does ENAHO 2024 include sufficient SISFOH proxy variables (e.g., extreme-poor classification from POBREZA) to permit a subgroup RDD restricted to the eligible population? If so, why was this not reported?

4. The survey audit flags that ENAHO's official expansion factor (FACPOB07) is absent from the estimation. Was this a deliberate methodological choice — i.e., treating the local-linear estimate at *h\** as a population-agnostic conditional-mean estimator — or an oversight? If the latter, how do the weighted and unweighted estimates compare on the primary outcome?

5. Can you verify the Galiani (2020) citation? A paper by Sebastian Galiani on Argentina transfer digitization matching that year and topic does not appear in accessible databases. If the citation was generated rather than verified, it should be replaced with the correct source or removed.

6. The paper interprets the null as evidence that "institutional channels for transfer digitization [are] insufficient, on their own, to overcome the age gradient." But the RDD identifies an average effect over the full population at age 65 (of whom only ~30% are SISFOH-eligible). Is the null informative about the institutional channel specifically, or is it more accurately interpreted as "among all Peruvians turning 65, digital wallet adoption does not jump"? The policy inference depends critically on this distinction.

7. What fraction of the 14,088 above-threshold observations in Table 1 are estimated to be Pensión 65 beneficiaries? If program coverage is ~750,000 beneficiaries out of approximately 2.5 million Peruvians aged 65+, the implicit compliance share within the above-threshold ENAHO sample would be around 30%. Please report this implied first-stage magnitude so readers can assess the LATE-scaled effect size.

---

```json
{
  "score": 67,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 65,
    "identification_credibility": 72,
    "empirical_execution": 62,
    "writing_presentation": 74,
    "literature_positioning": 63
  },
  "required_analyses": [
    "Re-estimate covariate-adjusted specification at optimal RDD bandwidth h*=14.2, not the 34.2-year WLS fallback",
    "Resolve the t-stat (-5.1) vs permutation p-value (0.434) contradiction: specify which estimator the permutation test uses and provide null distribution plot"
  ],
  "suggested_analyses": [
    "SISFOH-stratified subgroup RDD to test the institutional channel on the actual eligible population",
    "Survey-weighted estimation using ENAHO expansion factor FACPOB07",
    "Heterogeneity by rural/urban and gender",
    "RDD on Banco de la Nación account ownership as an intermediate/compliance outcome",
    "Verify Galiani (2020) Argentina citation — likely fabricated"
  ],
  "questions_to_authors": [
    "Can you re-estimate the covariate-adjusted column at h*=14.2 rather than h=34.2 to preserve the RDD identifying assumption?",
    "Which estimator does the permutation test correspond to — local-linear at h* or WLS at h=34.2 — and why do t=-5.1 and p=0.434 coexist for the same estimand?",
    "Does ENAHO 2024 permit a SISFOH-restricted subgroup RDD on the actual eligible extreme-poor population?",
    "Was the absence of survey weights (FACPOB07) a deliberate choice or an oversight? How do weighted vs. unweighted primary estimates compare?",
    "Can you verify the Galiani (2020) Argentina digitization citation against an accessible database?",
    "Is the null informative about the institutional channel specifically, or about all Peruvians at age 65 (only ~30% of whom are eligible)?",
    "What fraction of above-threshold observations are estimated Pensión 65 beneficiaries, and what is the implied LATE-scaled effect size?"
  ],
  "n_critical": 2,
  "n_major": 5
}
```