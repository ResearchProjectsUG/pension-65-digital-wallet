## Referee Report: "Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption?"

---

### Part 1 — Central Contribution

The paper uses a sharp RDD at the age-65 eligibility cutoff for Peru's Pensión 65 program to estimate the effect of institutional digitization of government transfers on digital wallet ownership and active use, finding a precisely estimated null across a comprehensive battery of robustness checks using the first ENAHO wave to include wallet-specific microdata.

**Rating: Incremental.** The data contribution (ENAHO 2024) is genuine, and a well-powered null from a credible design has publication merit. However, the contribution is narrowly scoped and primarily of interest to development economists working on Peru or non-contributory pensions in Latin America.

---

### Part 2 — Identification and Credibility

**Variation used:** Administrative age-65 eligibility threshold for Pensión 65, with age in years as the running variable.

**Plausible exogeneity:** The design is conceptually sound. Individuals cannot precisely manipulate their birth year to cross the threshold, and McCrary density tests produce no evidence of manipulation. The bank of robustness checks — bandwidth sensitivity, polynomial order, donut-hole exclusions, placebo cutoffs, permutation inference — is thorough.

**Main identification threats:**

1. **The sharp-versus-fuzzy distinction is systematically elided.** Pensión 65 eligibility requires *joint* satisfaction of two criteria: age ≥ 65 AND SISFOH classification as extreme-poor. The age cutoff is administratively sharp, but the fraction of people at the cutoff who actually become program-eligible is approximately 25–30% (the coverage share among 65+). The paper explicitly labels its estimand a "LATE" in Equation (1) and throughout, but what is actually identified is an ITT: the reduced-form effect of crossing the age threshold on the joint population, most of whom never receive the digital transfer. The ITT and the LATE (program effect on compliers) are conceptually distinct. No first-stage discontinuity in Pensión 65 *receipt* at the cutoff is shown, so the reader cannot distinguish between (a) the program having no effect on wallets among takers, and (b) dilution of a real effect across a predominantly ineligible population.

2. **Discrete running variable.** Age in years creates mass points at every integer. Within the optimal bandwidth of ±14.2 years, there are at most ~28 distinct values of the running variable. The McCrary test itself flags this. With such coarse discretization, the "local" in local-linear is doing less work than in canonical RDD applications, and the triangular kernel's continuity argument is weaker. The paper acknowledges mass points but does not quantify the potential distortion.

3. **Large raw gap unexplained.** Table 1 shows USA_BILLETERA means of 3.19% (above threshold) vs. 17.94% (below threshold) — a raw gap of nearly 15 percentage points. The RDD estimates near zero imply that this gap is smooth through the cutoff, driven entirely by the age gradient. An RD plot showing this is essential to make the null credible; without it, the near-zero local estimate against a 15pp raw gap looks counterintuitive.

---

### Part 3 — Required and Suggested Analyses

**Required (blockers for submission):**

1. **[CRITICAL] Template artifacts in tables and figures.** The code review evidence confirms that table notes in the output scripts contain electoral RDD boilerplate verbatim: references to "municipality-elections," "vote share," and "electoral threshold." These are machine-generated artifacts that survive into the submitted tables. A referee or editor encountering table notes that describe an electoral study inside a paper about digital wallets will reject without reading further. All tables and figures must be audited and cleaned before any submission.

2. **[CRITICAL] Missing citation in text.** Section 2.3 contains the literal string "[CITATION MISSING — insert \\citet{} key]" in the submitted manuscript. This cannot appear in any submission to any journal. Resolve or remove before sending.

3. **[CRITICAL] First-stage discontinuity for the fuzzy design.** Without evidence of a discontinuity in actual Pensión 65 receipt at age 65, the paper cannot distinguish a true null program effect from complete dilution of an effect across mostly-ineligible population members. Report the first-stage: the discontinuity in the probability of being a Pensión 65 beneficiary at age 65, using either MIDIS administrative data linked to ENAHO or the ENAHO income/transfer module. Then compute the IV/fuzzy-RDD LATE and contrast it with the ITT to clarify what the null means.

**Suggested (strengthen but not blockers):**

4. **[MAJOR] Reconcile the -5.999 t-statistic with permutation p = 0.434.** The paper presents this contrast as evidence in favor of the null, but the logic is opaque. A |t| of 6 would ordinarily be decisive evidence against the null; a permutation p of 0.434 argues the opposite. The paper attributes this to the discrete age distribution, but does not demonstrate it. Provide the permutation null distribution, explain exactly what is being permuted (treatment assignment? running variable values?), and clarify why the parametric and non-parametric tests give such wildly different answers.

5. **[MAJOR] Address the smartphone ownership paradox.** Among the above-threshold group, smartphone ownership is 83.1% (Table 1), yet active digital wallet use is 3.19%. This gap is striking: if elderly Peruvians own smartphones at near-universal rates, the null effect cannot be primarily explained by hardware access. The paper should characterize what barriers remain — digital literacy, trust, connectivity quality, account registration friction — using available ENAHO variables. This directly sharpens the policy interpretation beyond "institutional channels alone are insufficient."

6. **[MAJOR] Show the RD plots.** The paper references Figure 1 (Pensión 65 raw gap density) but no binscatter or local polynomial plot of outcomes against centered age is described in the results section. RD plots are required for credibility: they are the most transparent way to show the reader that the near-zero estimate reflects a smooth trend through the cutoff rather than a noisy flat region.

7. **[MAJOR] Fix the placebo cutoff text error.** Section 4.2 lists both placebo cutoffs as "age 53" — one should clearly be age 77 (65 + 12). This may be a transcription error but suggests the robustness section was not carefully proofread.

---

### Part 4 — Literature Positioning

The core citations — Bachas et al. (2018), Muralidharan & Niehaus (2016), Banerjee et al. (2020), Jack & Suri (2014), Card et al. (2008 Medicare RDD), Calonico et al. (2014), Cattaneo et al. (2018) — are appropriate and correctly applied. The framing of the result against the "dormant account" literature is apt.

**Gaps:**
- The Peru-specific payment literature is underused. The Banco Central de Reserva del Perú statistical reports are cited but primary empirical work on Yape/Plin/Cuenta DNI adoption determinants (if any exists) is not.
- The missing citation in Section 2.3 identifies a gap in the literature positioning of "age-65 cutoff and digital savings in Latin America." This must be filled.
- The aging-and-technology-adoption literature (cited via Deming 2023 as a single reference) is thin. The digital exclusion literature on older adults is more developed than represented here.

---

### Part 5 — Journal Fit and Recommendation

A top-five general-interest journal (AER, QJE) would require sharper identification and a more transformative contribution. For a top field journal — *Journal of Development Economics*, *Journal of Public Economics*, or *American Economic Journal: Applied Economics* — the paper is a reasonable candidate **after revision**.

**Recommendation: Revise before sending.**

The three critical issues identified above (template artifacts, missing citation, missing first-stage) are all fixable and do not reflect fundamental flaws in the empirical design. The RDD is credible, the data are genuinely new, and the null result is honestly and rigorously reported. However, in its current state the manuscript is not submission-ready: a referee encountering electoral boilerplate in a digital-wallet paper and a "[CITATION MISSING]" placeholder will conclude the paper was not carefully reviewed before submission, regardless of empirical quality.

---

### Part 6 — Questions to the Authors

1. **First stage and LATE.** The paper labels the estimand "LATE" throughout but explicitly acknowledges an ITT design due to incomplete take-up and the joint age-and-poverty eligibility condition. Can you report the first-stage discontinuity in the probability of Pensión 65 *receipt* at age 65 and compute the corresponding fuzzy-RDD IV estimate? What does the LATE (effect on compliers — those induced into the program by crossing age 65) look like relative to the ITT?

2. **The raw gap.** Table 1 shows a 15-percentage-point raw gap in USA_BILLETERA (17.94% below vs. 3.19% above threshold). The local-linear estimate near the cutoff is essentially zero. Please provide the binscatter or RD plot of this outcome against centered age so the reader can verify that the gradient is indeed smooth through the cutoff and the near-zero estimate is not an artifact of bandwidth or kernel choice.

3. **Permutation inference inconsistency.** The covariate-adjusted specification produces a t-statistic of −5.999 but a permutation p-value of 0.434. These appear to be testing the same null hypothesis. Can you describe exactly what is permuted in the randomization inference procedure, provide the histogram of permuted t-statistics, and explain why the parametric and non-parametric tests diverge so sharply? Is the permutation test appropriately conditioning on the age polynomial?

4. **Smartphone paradox.** With 83% smartphone ownership among the above-threshold group, why is active digital wallet use only 3.19%? Do ENAHO data permit you to estimate whether the barrier is digital literacy (education, internet use, prior banking experience) or program-specific frictions (awareness, account registration, connectivity)? This is the most actionable policy takeaway, and the current discussion is underspecified.

5. **Template artifacts.** The code review audit identifies table notes containing electoral RDD text ("municipality-elections where the party's vote share exceeded the electoral threshold"). Can you confirm that all tables, figures, and appendix materials have been fully reviewed and that no pipeline template artifacts remain in the submitted manuscript?

6. **Discrete running variable.** The bandwidth of ±14.2 years implies approximately 28 distinct age values in the estimation sample. How does the analysis account for the mass-point structure of the running variable? Have you considered an alternative specification using months or quarters of birth (if available in ENAHO), or a discrete-support RDD estimator that does not assume a continuous density?

7. **Covariate-adjusted sign change.** The baseline estimate for ownership is −0.006 (SE = 0.016, not significant), but the covariate-adjusted estimate is −0.027 (SE = 0.005, significant and negative). The paper interprets this as capturing the age gradient absorbed by the nonparametric estimator. But a statistically significant negative effect on ownership — even small in magnitude — is a finding: crossing the Pensión 65 threshold is associated with *lower* wallet ownership conditional on predetermined covariates. Is this consistent with any mechanism, or is it entirely attributable to residual age effects? The current treatment of this result is too dismissive.

---

### Scores

```json
{
  "score": 67,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 65,
    "identification_credibility": 70,
    "empirical_execution": 62,
    "writing_presentation": 60,
    "literature_positioning": 68
  },
  "required_analyses": [
    "Remove all template artifacts (electoral boilerplate) from tables and figures before submission",
    "Resolve the '[CITATION MISSING]' placeholder in Section 2.3",
    "Report first-stage discontinuity in Pensión 65 receipt and compute fuzzy-RDD LATE to distinguish program ITT from dilution artifact"
  ],
  "suggested_analyses": [
    "Reconcile the t=-5.999 parametric result with the permutation p=0.434 by showing the permutation null distribution",
    "Address the smartphone ownership paradox: 83% smartphone ownership vs. 3% wallet use among 65+",
    "Show RD plots (binscatter of outcomes vs. centered age) to visually validate the near-zero estimate against the 15pp raw gap",
    "Fix the placebo cutoff text error: both placebo ages listed as 53; one should be 77"
  ],
  "questions_to_authors": [
    "Can you report the first-stage discontinuity in Pensión 65 receipt and the fuzzy-RDD IV (LATE on compliers), distinguishing it from the ITT reported throughout?",
    "Please provide RD plots showing USA_BILLETERA and TIENE_BILLETERA against centered age — how does the near-zero local estimate arise from a 15pp raw gap?",
    "Explain the permutation inference discrepancy: t=-5.999 vs. permutation p=0.434 — what exactly is permuted and why do parametric and non-parametric inference diverge this sharply?",
    "With 83% smartphone ownership among the above-threshold group, what do ENAHO data suggest about the barriers preventing conversion from hardware access to wallet use?",
    "Can you confirm all tables and figures have been audited for pipeline template artifacts before submission?",
    "How does the analysis account for the discrete (integer) support of the running variable within the ±14-year bandwidth?",
    "The covariate-adjusted estimate is −0.027 (SE=0.005), statistically significant and negative. Is this finding being dismissed too quickly — does any mechanism predict lower wallet ownership among newly age-eligible Pensión 65 candidates conditional on their observable characteristics?"
  ],
  "n_critical": 3,
  "n_major": 4
}
```