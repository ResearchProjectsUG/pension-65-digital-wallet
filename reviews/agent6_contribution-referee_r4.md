## Referee Report

**Paper:** "Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption? A Regression Discontinuity Analysis with ENAHO 2024"

---

### Part 1 — Central Contribution

The paper provides the first regression-discontinuity estimate of the association between Pensión 65 eligibility and digital wallet adoption in Peru, using the 2024 ENAHO wave—the first to separately identify wallet ownership and use—and documents a precisely estimated null intent-to-treat effect across multiple robustness checks.

**Rating: Incremental.** The contribution is real: the data moment is genuinely new (2024 ENAHO is the first survey wave with wallet-level granularity), the null is policy-informative, and the identification is more credible than typical OLS comparisons. However, the finding—that a pension program's digital disbursement channel alone does not shift broader wallet adoption among the elderly poor—is largely anticipated by the existing literature on dormant forced accounts (Bachas et al., 2018; Muralidharan & Niehaus, 2016). The incremental rating reflects methodological rigor on a question the literature had partly pre-answered theoretically.

---

### Part 2 — Identification and Credibility

**Variation used:** A sharp RDD exploiting the age-65 administrative eligibility cutoff for Pensión 65. The paper correctly characterizes this as an ITT design: the threshold is sharp on age, but actual program receipt requires additionally meeting the SISFOH extreme-poverty criterion, which the authors cannot observe in ENAHO.

**Plausible exogeneity:** The age cutoff is institutionally hard and predetermined. The McCrary density test and placebo covariate checks appear to confirm design integrity, and the randomization inference p-value of 0.434 is comfortably null. The running variable is large ($N = 113{,}755$; $N = 27{,}809$ within the MSE-optimal bandwidth), and the CI bounds are tight ($[-0.034, 0.031]$), so the null is precisely estimated, not powered-down.

**Primary threat not fully addressed — Discrete running variable.** Age is reported in completed years, meaning the running variable is discrete with mass points at each integer. Standard `rdrobust` estimators assume continuity of the density of the running variable; with integer ages, this assumption is violated. The Kolesar & Rothe (2018, *Review of Economics and Statistics*) honest confidence intervals for discrete running variables are the methodological standard when the number of support points is finite. The authors use the Cattaneo et al. (2018) density test designed for continuous running variables and do not acknowledge or correct for the discreteness. This is the most credible identification concern not addressed in the text.

**Secondary threat — No first stage.** The paper cannot observe SISFOH classification status for ENAHO respondents. It therefore cannot compute a first-stage estimate (share of age-65-crossers who are actually SISFOH-eligible and receive the pension) or scale the ITT to a LATE. While the ITT framing is explicitly and correctly adopted, the authors cannot rule out that the ITT is null because take-up among SISFOH-eligible individuals near the cutoff is too low for a signal to appear, rather than because the program channel itself is ineffective. A back-of-envelope calculation using administrative coverage figures (750,000 beneficiaries ≈ 30% of age 65+) would help bound this.

**Contamination of the age-65 cutoff.** Peru has at least one other age-based institutional change at 65—mandatory retirement under the private pension (AFP) system for workers who elect programmatic or early retirement. If AFP-related income shocks or banking interactions co-occur at exactly age 65 in a subpopulation, the ITT captures a compound effect. The paper does not address this alternative pathway.

---

### Part 3 — Required and Suggested Analyses

**Required [CRITICAL]:**

None that would cause an outright desk reject. The design is credible, the null is precisely estimated, and the robustness battery is extensive. However, the following issues require substantive revision before submission to a top-field journal.

**Major [MAJOR]:**

1. **[MAJOR] Discrete running variable correction.** The authors must either (a) implement Kolesar-Rothe (2018) honest CIs for discrete running variables, or (b) demonstrate that the results are unchanged under a "donut of one year" around each integer mass point, or (c) provide a formal argument for why the standard `rdrobust` inference is valid in this setting. Failing to address discreteness in a top-field submission will be caught by every technically competent referee.

2. **[MAJOR] Covariate-adjusted estimate vs. local-linear baseline discrepancy.** The baseline ITT is $-0.006$ (SE $= 0.016$); the covariate-adjusted estimate is $-0.027$ (SE $= 0.005$). The authors attribute this gap to a wider bandwidth in the adjusted specification. If so, the robustness curve across bandwidths should show the baseline estimate drifting to $-0.027$ as bandwidth widens — this should be plotted explicitly. The current text briefly flags the issue but does not resolve it. A reader cannot judge whether the covariate-adjusted result reflects genuine heterogeneity in the age-adoption profile or a bandwidth-driven artifact.

3. **[MAJOR] Template boilerplate in output tables.** The code review reports that Table 1's footnote references "municipality-elections where the party's vote share exceeded the electoral threshold" and Figure 1's x-axis is labeled "Vote Margin." These are not typographic errors — they are unrevised artifacts from an electoral RDD template. A paper reaching a top-field journal with these passages visible will receive an immediate desk reject on presentation grounds alone. This must be corrected unconditionally.

4. **[MAJOR] No minimum detectable effect (MDE) or power analysis.** A null result is more persuasive when the authors demonstrate that their design was powered to detect economically meaningful effects. Given the within-bandwidth means (ownership: 12.9% control / 6.4% treated), the authors should report the MDE at 80% power for the primary outcome and argue that the effect the program could plausibly produce is smaller. The current text asserts "precisely estimated null" but does not benchmark precision against a substantive effect size.

**Suggested:**

5. **[Suggested]** Quantify the first-stage using administrative coverage statistics. Even an external estimate of the share of ENAHO respondents aged 65–75 who are SISFOH-classified extreme poor would allow a rough scaling of the ITT to bound the LATE. This would substantially enrich the policy discussion.

6. **[Suggested]** Heterogeneity by urban/rural and by department-level digital infrastructure. The null might conceal positive effects in areas with better smartphone penetration or Yape/Plin coverage. The bandwidth sample spans all 25 departments; a split by \texttt{AREA} (urban vs. rural) or by BCRP financial-density quintile would be informative and is standard in the financial-inclusion literature.

7. **[Suggested]** Falsification on a placebo outcome where Pensión 65 has no channel: e.g., ownership of a traditional savings account at a commercial bank (P558E1 codes other than 9). If the RDD also shows no discontinuity on that outcome, the design is confirmed; if it shows a positive effect, it would suggest broader financial-access effects from crossing age 65 that contaminate the wallet interpretation.

---

### Part 4 — Literature Positioning

The citations are appropriate and the framing is honest. The connection to Bachas et al. (2018), Muralidharan & Niehaus (2016), and Jack & Suri (2014)/Suri (2017) is well-motivated and the theoretical null is correctly anticipated. The claim that \citet{aizenman2022} is the "closest application" is asserted without enough detail for a referee to verify the comparison; the authors should be more specific about how the sample, design, and outcomes differ.

One gap: the paper does not cite the literature on age gradients in digital adoption (e.g., Lusardi & Mitchell 2014 on financial literacy among older adults; Czaja et al. on technology adoption among seniors). Given that the paper's null is attributed partly to an "age gradient in digital financial behavior," anchoring that interpretation in a specific literature would strengthen the discussion section.

---

### Part 5 — Journal Fit and Recommendation

For a **top-field journal** (AER, QJE, JPE, AEJ:Applied, AEJ:Policy), the bar is high. The paper is methodologically disciplined and the null is precisely documented, but the contribution is incremental (Peru-specific, single program, anticipated null), the discrete running variable issue is unaddressed, and the output tables contain template artifacts. At a specialist journal (Journal of Development Economics, World Development, Journal of Policy Analysis and Management), this paper would be competitive after revision.

**Recommendation: Revise before sending.**

The required analyses (items 1–4 above) are all addressable in a standard revision cycle and none requires new data collection. If the authors respond adequately, particularly on the discrete running variable and the covariate-adjustment discrepancy, the paper would be suitable for a second round at a field journal.

---

### Part 6 — Questions to the Authors

1. **Discrete running variable:** Age in ENAHO is recorded as completed years — an integer-valued variable. Standard `rdrobust` inference assumes a continuous density of the running variable. Why did you not apply the Kolesar-Rothe (2018) honest confidence interval procedure, or at minimum report sensitivity to this concern? How do your CIs change under that correction?

2. **Covariate-adjusted vs. local-linear discrepancy:** The baseline ITT on ownership is $-0.006$ (SE $= 0.016$) while the covariate-adjusted estimate is $-0.027$ (SE $= 0.005$) — a difference of 21 percentage points in point estimates and a threefold difference in precision. You attribute this to a wider bandwidth in the adjusted specification. Can you plot the bandwidth-sensitivity curve for the baseline (no covariates) and show that the point estimate drifts to $-0.027$ at the wider bandwidth? If it does not, what explains the difference?

3. **First stage and LATE interpretation:** You estimate an ITT but cannot observe SISFOH classification. Using your figure of 750,000 beneficiaries representing approximately 30% of Peruvians aged 65+, what is your best estimate of the first-stage compliance rate among observations in the bandwidth window? Does scaling the ITT by this compliance rate produce an effect that is still economically negligible, or does it become non-trivial?

4. **AFP retirement at age 65:** Peru's private pension system (AFP Ley 26790 / DL 25897) contains provisions that interact with age 65 — including the right to elect early retirement and the standard programmatic retirement age. Is there evidence from your data (e.g., labor market exit, AFP-related income variables in ENAHO module 5) that AFP-related transitions co-occur at exactly age 65 in your sample? If so, how do you separate the Pensión 65 ITT from AFP-driven effects on the financial behavior of this subpopulation?

5. **Table notes and figure labels:** Table 1's footnote mentions "municipality-elections where the party's vote share exceeded the electoral threshold" and Figure 1 is labeled "Vote Margin." Can you confirm these are typographic artifacts and provide the corrected versions of all affected tables and figures?

6. **MDE and power:** What is the minimum detectable effect size (at 80% power, two-sided 5% level) for your primary outcome within the MSE-optimal bandwidth? Is this MDE smaller than the effect size a policy analyst would consider economically meaningful for a program reaching 750,000 beneficiaries?

7. **Urban/rural heterogeneity:** Digital wallet adoption is highly concentrated in urban areas (the BCRP 2024 figures you cite refer overwhelmingly to metropolitan areas). Given that Pensión 65 disproportionately reaches rural extreme-poor elderly, is the null driven by a rural subpopulation with structurally zero wallet adoption regardless of the program? A simple split by \texttt{AREA} within your bandwidth sample would clarify whether the null is uniform or concentrated.

---

```json
{
  "score": 73,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 69,
    "identification_credibility": 71,
    "empirical_execution": 70,
    "writing_presentation": 79,
    "literature_positioning": 73
  },
  "required_analyses": [
    "Discrete running variable correction (Kolesar-Rothe 2018 or equivalent) — standard rdrobust assumes continuous density, violated by integer ages",
    "Covariate-adjusted vs. local-linear bandwidth-sensitivity curve to explain the -0.006 vs -0.027 discrepancy",
    "Remove template boilerplate from Table 1 footnotes and Figure 1 axis labels before any submission"
  ],
  "suggested_analyses": [
    "First-stage approximation using administrative coverage to bound the LATE and rule out a low-compliance explanation for the null",
    "Minimum detectable effect calculation to formally benchmark the precision of the null",
    "Urban/rural heterogeneity split within the MSE-optimal bandwidth",
    "Placebo outcome on non-wallet financial products to test for general age-65 financial-access effects",
    "AFP retirement co-occurrence check at age 65 to address running-variable contamination"
  ],
  "questions_to_authors": [
    "Why was the Kolesar-Rothe (2018) honest CI procedure not applied given that age is a discrete integer-valued running variable? How do the CIs change under that correction?",
    "The covariate-adjusted estimate (-0.027) differs from the local-linear baseline (-0.006) by 21 percentage points — can you plot the bandwidth-sensitivity curve for the unadjusted estimator and show that this gap is entirely attributable to the wider bandwidth?",
    "Using the 30% administrative coverage figure, what is the implied LATE under a 2SLS scaling, and is it still economically negligible?",
    "Do AFP-related retirement transitions co-occur at age 65 in your ENAHO sample, and if so, how do you separate that effect from the Pensión 65 ITT?",
    "Can you confirm and correct the template boilerplate in Table 1 footnotes and Figure 1 axis labels?",
    "What is the minimum detectable effect at 80% power within your MSE-optimal bandwidth, and how does it compare to the effect size a policymaker would consider meaningful?",
    "Does the null hold uniformly across urban and rural subsamples, or is it driven by a rural subpopulation with structurally near-zero wallet adoption?"
  ],
  "n_critical": 0,
  "n_major": 4
}
```