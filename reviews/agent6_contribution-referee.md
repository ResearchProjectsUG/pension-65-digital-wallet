## Referee Report

**Journal:** Top-Field Economics
**Paper:** "Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption? A Regression Discontinuity Analysis with ENAHO 2024"

---

### Part 1 — Central Contribution

The paper estimates a sharp RDD at Peru's age-65 Pensión 65 eligibility threshold using the first nationally representative microdata (ENAHO 2024) to separately identify digital wallet ownership and use, finding a precisely estimated null ITT effect and contributing credible evidence that institutional digitization of transfers does not, on its own, overcome the age gradient in digital financial adoption.

**Rating: Incremental** — the Peru-specific application is novel and the use of ENAHO 2024 is timely, but the contribution is primarily an addition to an existing null-results literature rather than a new theoretical or empirical advance.

---

### Part 2 — Identification and Credibility

**Variation used:** Discontinuity in Pensión 65 eligibility at age 65. The running variable (completed years of age) is straightforward, and the administrative cutoff is sharp in the sense that no one below 65 can qualify on age grounds.

**Plausible exogeneity:** Broadly credible. Age is not manipulable with precision, the McCrary test shows no bunching at 65, and the paper tests covariate continuity. The identification strategy is standard and well-applied.

**Main threats:**

1. **Eligibility is jointly determined by age AND SISFOH extreme-poor status.** This is the design's most serious unaddressed weakness. The RDD is estimated on the full population of 113,755 individuals, but the program only affects those who are *both* aged 65+ and SISFOH-classified extreme-poor. For the roughly 70% of 65+ individuals who are *not* extreme-poor, crossing the age threshold generates zero first-stage variation. The ITT estimate on the full sample is therefore a diluted mixture of a real program effect (for the eligible poor) and a zero effect (for everyone else). The paper acknowledges incomplete take-up but never quantifies the dilution or presents the analysis restricted to the relevant subpopulation. This is not a fatal flaw — the ITT on the full population is a defensible estimand — but the paper needs to directly address what we learn from it, and whether a subsample estimate for extreme-poor households is feasible with available SISFOH proxies (the POBREZA variable is available in the data).

2. **Missing first-stage evidence.** The paper reports that ~30% of those aged 65+ participate in Pensión 65 and ~25% of eligibles do not take up. There is no table or figure showing the first-stage discontinuity: does crossing age 65 actually increase Pensión 65 benefit receipt in the ENAHO data? Without this, the reader cannot distinguish between two very different stories: (a) the program reaches people but has no effect on digital adoption, or (b) the program barely reaches anyone near the cutoff and the null simply reflects a weak instrument. The first-stage is essential framing even in an ITT design.

3. **Other age-65 discontinuities.** Peru has additional programs and age-based changes that activate at or near 65 (labor market exit, social security rules, EsSalud age thresholds). The paper briefly acknowledges this in the ITT framing but does not attempt to enumerate or bound the contaminating effects.

**Design verdict:** The core identification is credible, but the dilution problem and absent first-stage prevent the paper from claiming it has estimated the effect of Pensión 65's digital onboarding mechanism specifically.

---

### Part 3 — Required and Suggested Analyses

#### Required [CRITICAL]

**[CRITICAL-1] First-stage table.** Show the discontinuity in Pensión 65 receipt (or any Banco de la Nación/Cuenta DNI account ownership) at age 65. This does not need to be formal LATE scaling — even a descriptive figure showing uptake by single-year age bin with a vertical line at 65 would establish that the institutional mechanism the paper hypothesizes actually turns on at the cutoff. Without this, the null is uninterpretable.

**[CRITICAL-2] Subsample analysis for the extreme-poor.** Restrict the sample to individuals in POBREZA = 1 (extreme poor) or use an interaction specification that isolates the effect for the SISFOH-eligible subgroup. The full-population ITT is a valid estimand, but a referee at a top-field journal will ask: "among those for whom crossing age 65 actually matters, what happens?" If the subsample is too small for the rdrobust procedure, acknowledge this explicitly and report whatever precision is available; power limitations are a legitimate finding.

**[CRITICAL-3] Clarify the ITT vs. LATE labeling.** Equation (1) and the surrounding text call τ the "local average treatment effect (LATE)," but Section 3.4 correctly characterizes the design as ITT. These are different estimands. The LATE in an RDD with incomplete take-up is τ divided by the first-stage jump. Use consistent terminology throughout, and explain in the text what the ITT estimate represents quantitatively relative to the potential LATE.

#### Suggested [MAJOR]

**[MAJOR-1] Explain the covariate-adjusted point-estimate shift.** The baseline estimate for ownership is −0.006 (SE = 0.016); the covariate-adjusted estimate is −0.027 (SE = 0.005). In a valid sharp RDD, adding balanced covariates should reduce variance without substantially changing the point estimate. A shift from −0.006 to −0.027 — roughly 4× the standard error of the adjusted estimate — is not a minor refinement; it signals either (a) covariates are not balanced locally despite the global balance test, (b) the bandwidth changes between specifications, or (c) the model is absorbing variation that is correlated with treatment status in a way that affects identification. The paper attributes this to the "secular age gradient," but this logic is circular: if the age gradient is continuous at the cutoff (as assumed), it should not shift the discontinuity estimate. The authors should report whether the bandwidth is identical across both specifications, and provide an F-test or joint significance test for covariate balance *within the bandwidth window*.

**[MAJOR-2] Explain the t-statistic vs. randomization p discrepancy.** The paper reports a conventional t-statistic of −5.999 alongside a randomization p-value of 0.434, and attributes the discrepancy to the discrete running variable. A t-statistic of −6 is extraordinary; even under discrete-age mass-points, this magnitude demands explanation. Is the t-statistic computed from the cluster-robust SEs, the nearest-neighbor SEs, or something else? What is the size of the permutation distribution — does it look symmetric? A figure of the permutation distribution with the observed statistic marked would immediately resolve the concern.

**[MAJOR-3] Use survey weights.** The data audit flags that population-level inference is conducted without survey weights despite the official ENAHO expansion factor (FACPOB07) being available in the cleaned data. For descriptive statistics (Table 1), this matters: the paper reports a 7.4% population mean for wallet ownership, but without weights this is the unweighted sample mean, which overstates rural and small-department representation. For the RDD estimates, the impact is smaller near the cutoff (where sampling variation should not correlate sharply with the design), but the paper's claims about "nationally representative" inference are weakened. At minimum, show weighted and unweighted descriptive means side by side.

**[MAJOR-4] Remove template artifacts.** The code review confirms that three output items still contain electoral RDD boilerplate: Table 1 note references "municipality-elections where the party's vote share exceeded the electoral threshold," Table 4 header reads "at the Electoral Threshold," and Figure 1 x-axis is labeled "Vote Margin." These must be corrected before any submission. A paper this careful about statistical methodology should not reach a referee with these artifacts.

**[MAJOR-5] Fill the missing citation.** Section 2.3 contains a plainly visible "[CITATION MISSING — insert \citet{} key]." This should not appear in a submitted manuscript.

---

### Part 4 — Literature Positioning

The paper cites the right papers (Bachas et al. 2018, Muralidharan & Niehaus 2016, Banerjee et al. 2020 on transfer digitization; Card et al. 2008, Battistin et al. 2009 on age-threshold RDDs; Cattaneo et al. 2018, Calonico et al. 2014/2019 on RDD methodology). The framing of the null as consistent with dormant-account literature is appropriate and the paper correctly identifies its contribution relative to M-Pesa/mobile money literature.

Two gaps: First, the Peru-specific literature is thin. The BCRP 2024 report is cited descriptively, but there is essentially no engagement with prior work on Yape/Plin adoption, Cuenta DNI rollout, or the broader Peruvian fintech ecosystem beyond that single citation. Second, the literature on *heterogeneous effects of digital transfer programs by age* is undercited — the paper's main finding is that the age gradient dominates any program effect, and this deserves richer grounding in the behavioral literature on technology adoption by older adults (e.g., Czaja et al., Liang et al.) rather than the single \citet{deming2023} citation.

The [CITATION MISSING] placeholder in Section 2.3 is the only truly disqualifying presentation error: it signals the paper was not ready for external review.

---

### Part 5 — Journal Fit and Recommendation

The paper addresses a relevant policy question, uses a credible design on a large nationally representative dataset, and applies a thorough robustness battery. The null result is honestly framed and the confidence intervals are reasonably tight. For a top-field journal, however, the absent first-stage is a genuine obstacle — referees will ask for it and its absence means the paper's core interpretive claim (that the program's institutional channel fails to change digital behavior) cannot be distinguished from the claim that the program simply isn't reaching anyone near the threshold. The subsample analysis and ITT/LATE clarification are similarly necessary before this paper can be evaluated on its merits.

**Recommendation: Revise before sending**

The paper is not a desk reject — the design is credible, the data contribution is real, and the robustness work is thorough. But the three required analyses above need to be in the paper before sending to referees. With those in place, this is a solid submission to a field journal (EDCC, JDE, JHE, World Bank Economic Review) and a competitive — though not certain — submission to a top general field journal.

---

### Part 6 — Questions to the Authors

1. **First stage:** Can you show the RDD estimate for Pensión 65 benefit receipt (or any Banco de la Nación account) at age 65 in the ENAHO data? If the program measure is not in ENAHO, what administrative data could be used to validate that the institutional mechanism activates at the cutoff?

2. **SISFOH dilution:** Among individuals in the POBREZA = 1 (extreme poor) cell — the group for whom crossing age 65 actually confers eligibility — what are the RDD estimates for wallet ownership and use? If the sample is underpowered, what is the minimum detectable effect for that subsample?

3. **Covariate-adjusted shift:** Is the bandwidth identical in the unadjusted (−0.006) and covariate-adjusted (−0.027) specifications? If so, can you show a joint F-test for covariate balance within the bandwidth window and explain the mechanism by which balanced covariates shift the point estimate by this magnitude?

4. **t-statistic discrepancy:** Please show the permutation distribution for the primary outcome and clarify which standard error (cluster-robust, nearest-neighbor, or other) yields the t-statistic of −5.999. The conventional and randomization-based inference should be reconciled rather than treated as parallel evidence.

5. **Other age-65 discontinuities:** What other programs or policy changes activate at age 65 in Peru? Have you tested for discontinuities in labor market participation, EsSalud enrollment, or other outcomes at age 65 that could confound the wallet adoption estimate?

6. **Survey weights:** Why were ENAHO expansion factors excluded from the RDD estimates and descriptive statistics? Please show both weighted and unweighted means for the main outcomes and discuss whether the optimal bandwidth changes under weighted estimation.

7. **Mechanism:** Given the null result, can you use ENAHO data to characterize the intensive margin — for those who *do* receive Pensión 65, is there any evidence that wallet ownership or use is higher than for non-recipients of the same age and poverty status? An OLS comparison (with obvious caveats about selection) would sharpen the policy interpretation.

---

```json
{
  "score": 67,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 68,
    "identification_credibility": 63,
    "empirical_execution": 70,
    "writing_presentation": 64,
    "literature_positioning": 67
  },
  "required_analyses": [
    "First-stage discontinuity in Pensión 65 receipt at age 65",
    "Subsample RDD restricted to extreme-poor (POBREZA=1) individuals",
    "Consistent ITT vs. LATE labeling and quantitative reconciliation across specifications"
  ],
  "suggested_analyses": [
    "Explain and decompose the covariate-adjusted point-estimate shift from -0.006 to -0.027",
    "Provide permutation distribution figure and reconcile t=-5.999 with randomization p=0.434",
    "Re-run descriptive statistics and robustness checks with official survey weights (FACPOB07)",
    "Remove all electoral RDD template artifacts from tables and figures",
    "Fill [CITATION MISSING] placeholder in Section 2.3"
  ],
  "questions_to_authors": [
    "Can you show the first-stage RDD for Pensión 65 receipt (or Banco de la Nación account ownership) at age 65, either from ENAHO or administrative records?",
    "Among the POBREZA=1 extreme-poor subsample — the only group for whom age 65 confers eligibility — what are the RDD estimates, and what is the MDE if the subsample is underpowered?",
    "Is the bandwidth identical across the unadjusted and covariate-adjusted specifications? If so, what is the F-test for covariate balance within the bandwidth, and what is the theoretical mechanism for the point estimate shift?",
    "Which standard error yields t=-5.999 for the primary outcome, and can you show the full permutation distribution with the observed statistic marked?",
    "What other programs or institutional changes activate at age 65 in Peru, and have you tested for discontinuities in labor market participation or other potential confounders?",
    "Why were ENAHO expansion factors excluded from the main estimates? Please show weighted and unweighted descriptive means and discuss sensitivity of the bandwidth to weighting."
  ],
  "n_critical": 3,
  "n_major": 5
}
```