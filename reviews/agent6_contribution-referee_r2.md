## Referee Report

**Journal:** Top-field economics journal
**Paper:** "Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption? A Regression Discontinuity Analysis with ENAHO 2024"
**Date:** 2026-05-02

---

## Part 1 — Central Contribution

The paper provides the first quasi-experimental estimate of whether institutional digitization of a non-contributory pension program (Pensión 65) shifts digital wallet adoption among elderly poor Peruvians, using a sharp regression discontinuity at the age-65 eligibility threshold with ENAHO 2024 — the first survey wave to record wallet ownership and use as separate categories.

**Rating: Incremental.** The first use of ENAHO 2024's digital-wallet module is a genuine data contribution. A well-powered null from a credible design also has real value. However, the contribution is primarily one of application: the method is standard, the setting is not uniquely important to the broader literature, and the null result — while honest — does not fundamentally revise our priors given the Bachas (2018) and Muralidharan (2016) findings on dormant forced accounts.

---

## Part 2 — Identification and Credibility

**Variation used.** The running variable is completed age in years; the cutoff is 65. The key identifying assumption is that potential outcomes are continuous in age at 65, so that individuals just below serve as valid counterfactuals for those just above.

**Plausible exogeneity.** Age is not manipulable in a way that would be continuous across the cutoff, and the McCrary density test is reported. The design is conceptually sound.

**Main threat — Sharp versus Fuzzy design (unresolved).**
This is the most important identification issue in the paper and it is never fully resolved. Pensión 65 eligibility requires *two* conditions: (1) age ≥ 65 and (2) SISFOH extreme-poor classification. The paper's estimating equation uses D_i = 1{A_i ≥ 65} as the treatment indicator, but this indicator equals 1 for *all* individuals aged 65 and above, regardless of SISFOH status — the large majority of whom are *not* eligible for Pensión 65. The treatment probability does not jump from 0 to 1 at age 65; it jumps from 0 to some fraction (approximately the share of extreme-poor among 65+, perhaps 30–40%). By definition, that is a fuzzy RDD.

The paper acknowledges this in prose ("the design we exploit is best characterized as an intent-to-treat RDD") but Equation (1) labels the estimand LATE — which it is not. The ITT and the LATE are conceptually distinct: the LATE is the ITT scaled by the first stage (actual take-up discontinuity), and requires presenting that first stage. The paper never shows a first-stage estimate — no discontinuity plot for Pensión 65 receipt, no estimate of the jump in program take-up at age 65. Without a first stage, the reader cannot assess whether there is *any* variation in the treatment to detect.

**Secondary threats.**

1. *Discrete running variable.* Completed age in years creates integer mass points. The standard local-polynomial bias correction (Calonico et al. 2014) is derived under continuity of the running variable. With only ~14 distinct age values on each side at the optimal bandwidth, the triangular kernel assigns substantial weight to a small number of mass points. The paper notes this in passing ("integer running variable creates discrete mass points") to explain the conflict between the WLS t-statistic and the permutation p-value, but does not apply a correction designed for discrete running variables (e.g., Kolesár and Rothe 2018).

2. *Covariate balance at the SISFOH cutoff.* SISFOH poverty classification could itself jump at age 65 if program eligibility changes economic behavior or if administrative reclassification occurs at that age. A jump in poverty status at the cutoff would violate the continuity assumption. The paper tests predetermined covariate balance but does not explicitly test for a discontinuity in SISFOH classification itself at age 65 — the very variable that jointly determines eligibility.

3. *Covariate-adjusted specification bandwidth mismatch.* The covariate-adjusted estimate uses h = 34.2 years rather than the optimal h* = 14.2, attributed to "memory limitations" of the rdrobust routine. This is a computational shortcut with non-trivial econometric consequences: the wider window loads on the secular age-adoption gradient (older = fewer smartphones, less internet) rather than on local variation at the cutoff. The shift from −0.006 to −0.027 across specifications is then explained as reflecting the age gradient rather than variance reduction — which is honest but renders the covariate-adjusted estimate largely uninformative as an RDD robustness check.

---

## Part 3 — Required and Suggested Analyses

### Required [CRITICAL]

**[CRITICAL] C1 — First-stage evidence is absent.**
The paper cannot identify the program's effect on digital wallet adoption without showing that crossing age 65 actually generates a discontinuity in Pensión 65 receipt. Present a first-stage RDD estimate of the jump in program take-up at age 65, ideally using ENAHO 2024 or administrative MIDIS data. If the first stage is weak (i.e., the jump in take-up at the cutoff is small within the optimal bandwidth), that directly informs the interpretation of the null ITT: a small first stage with a near-zero ITT implies the LATE is not well identified in either direction. Without the first stage, the paper is an age-RDD on digital wallets with no demonstrated connection to Pensión 65.

**[CRITICAL] C2 — Sharp versus fuzzy design must be resolved and the terminology corrected.**
Either (a) recharacterize the design explicitly and consistently as a fuzzy RDD with an instrument at age 65 and show both ITT and LATE (scaled by the first stage), or (b) demonstrate empirically that the SISFOH filter does not generate an additional running-variable-like structure (e.g., show that the share of SISFOH-extreme-poor in ENAHO is essentially flat through the 60–70 age range), justifying the sharp ITT interpretation. In either case, remove the LATE label from Equation (1). ITT ≠ LATE, and conflating them in the key identification equation is an error a top-field referee will flag immediately.

**[CRITICAL] C3 — Bandwidth-restricted summary statistics.**
Table 1 reports summary statistics for the *full* ENAHO sample split at age 65 (99,667 below, 14,088 above), not for the bandwidth-restricted sample (ages ≈ 51–79 at h* = 14.2). The identifying variation is entirely local; characterizing the full sample in the main descriptive table misrepresents who the comparison is actually between. Replace Table 1 with within-bandwidth summary statistics, or add a within-bandwidth version alongside the full-sample table. The difference is not trivial: the below-cutoff group in the full sample includes children and young adults with radically different digital behavior from 55–64 year-olds.

### Suggested [MAJOR]

**[MAJOR] M1 — Fix the covariate-adjusted specification.**
The "memory limitations" of rdrobust are a computational artifact, not an econometric constraint. Running rdrobust on a pre-restricted age window (e.g., ages 50–80, approximately 25,000–30,000 observations) would eliminate the memory issue while preserving local identification. The current fallback to WLS with h = 34.2 is not a valid robustness check; it is a different estimand. Fix this or remove the covariate-adjusted estimate from the main table.

**[MAJOR] M2 — Address discrete running variable explicitly.**
Apply the Kolesár-Rothe (2018) confidence intervals for discrete running variables, or at minimum show that results are robust when the randomization inference p-value is treated as the primary inference result throughout (not only as a correction for the WLS t-statistic). The asymptotic SEs from rdrobust with a discrete running variable are known to be anti-conservative; this needs to be the paper's primary inference approach, stated upfront, not introduced as a post-hoc fix for an apparent inconsistency.

**[MAJOR] M3 — Heterogeneity by SISFOH poverty status.**
The core mechanism operates only for extreme-poor individuals who are SISFOH-classified. ENAHO contains the POBREZA variable that proxies this. Splitting the sample by extreme-poor versus non-extreme-poor and estimating the RDD separately would directly test whether the (locally estimated) ITT is larger for the population most likely to be affected by Pensión 65 digitization. A null even among the extreme-poor at the cutoff would be the strongest possible evidence for the paper's interpretation.

**[MAJOR] M4 — Correct code artifacts before submission.**
The code review report flags that table notes and figure axis labels carry electoral-RDD boilerplate (references to "municipality-elections," "vote share," "electoral threshold," "Vote Margin"). These appear to have survived from a template. Any reviewer who checks the replication package will notice immediately, which raises questions about the integrity of the entire pipeline. Fix all labels before submission.

**[MAJOR] M5 — Clarify the population-level means.**
The paper reports population-level means of 7.4% for ownership and 15.6% for active use, but Table 1 shows 8.0% ownership and 17.9% active use for the below-threshold group and 5.4% / 3.2% for the above-threshold group. These figures are unweighted and use the full sample. Given that ENAHO has substantial survey weights and that TIENE\_BILLETERA and USA\_BILLETERA rates are likely heterogeneous across demographic strata, report the expansion-factor-weighted population means and clarify whether the RDD estimates use weights or not.

---

## Part 4 — Literature Positioning

The paper's engagement with the existing literature is competent and mostly appropriate. The citations to Bachas et al. (2018), Muralidharan and Niehaus (2016), and Jack and Suri (2014) are on-point and correctly frame the prior evidence on forced-account dormancy. The Card (2008) citation for age-eligibility RDD methodology is standard.

Two concerns:

First, the Galiani (2020) citation appears twice in slightly different roles (Section 2.1 and Section 2.3) and the specific mechanism documented is conflated between uses. In Section 2.1 it is cited for "positive but heterogeneous effects of conditional cash transfer digitization," while in Section 2.3 it is cited for "weak downstream behavioral effects of forced account openings on saving." These are meaningfully different claims and it is not obvious they come from the same paper. The authors should verify that both characterizations are accurate and disambiguate if citing different papers.

Second, the literature review is missing engagement with two relevant bodies of evidence: (a) direct studies of Yape/Plin/Cuenta DNI adoption patterns in Peru — even if only descriptive, this contextualizes what the paper is measuring; (b) the recent literature on digital public infrastructure in Latin America (IDB working paper series, CGAP reports) that would situate the Cuenta DNI / Banco de la Nación integration as a case within a broader policy trajectory.

---

## Part 5 — Journal Fit and Recommendation

For a *top-field* journal (AER, QJE, JPE, ReStud), the paper as submitted falls short. The primary obstacles are the unresolved sharp-versus-fuzzy identification issue and the absent first stage — these are not presentational problems but go to the core of what the RDD is identifying. The covariate-adjusted specification fallback and the discrete running variable treatment further undermine the empirical execution.

The contribution rating of "incremental" combined with these identification gaps means the paper is not ready to send to referees at a top-field outlet. At a strong field journal (JDE, JHE, World Development, Journal of Development Economics) this paper — with the three required analyses addressed — would be competitive.

**Recommendation: Revise before sending.**

A focused revision addressing C1–C3 (first stage, sharp/fuzzy resolution, bandwidth-restricted summary statistics) would substantially strengthen the paper. M1 (fixing the covariate-adjusted specification) is also important and should be bundled into the same revision cycle.

---

## Part 6 — Questions to the Authors

1. **On the first stage:** Does ENAHO 2024 include a question on Pensión 65 receipt? If so, what does a first-stage RDD at age 65 show for actual program take-up within the optimal bandwidth? If ENAHO does not record program receipt, can you use MIDIS administrative records matched to the survey to validate that there is a meaningful discontinuity in take-up at age 65?

2. **On the sharp versus fuzzy design:** The treatment indicator in Equation (1) assigns D_i = 1 to all individuals aged 65 and above, including those who are not SISFOH-classified as extreme-poor and therefore not eligible for Pensión 65. How do you justify calling this a sharp RDD when only a subset of 65+ individuals is actually treated? If the proportion extreme-poor in the 65+ population is, say, 35–40%, the treatment probability jump at the cutoff is well below 1, which defines a fuzzy design. Have you estimated the size of this jump?

3. **On the covariate-adjusted specification:** The paper attributes the use of a wider bandwidth (h = 34.2) and WLS fallback to "memory limitations" of rdrobust. Could you rerun the local-polynomial covariate-adjusted specification on a pre-restricted sample of, say, ages 50–80? On approximately 25,000 observations, rdrobust with covariates should not encounter memory constraints. The current result conflates the local RDD estimate with the global age gradient, and that conflation significantly complicates interpretation.

4. **On SISFOH continuity at the cutoff:** Is there any evidence that SISFOH poverty classification itself changes discontinuously at age 65 — for example, due to age-related reclassification protocols or differential program outreach that affects self-reported income near the threshold? A jump in POBREZA at age 65 would be a violation of the continuity assumption and would need to be addressed directly.

5. **On the population of inference:** The analysis uses all 113,755 ENAHO respondents of all ages for the summary statistics, while the RDD estimates use only those within h* = 14.2 years of the cutoff (approximately ages 51–79). Who are the local compliers in this design, and is a top-field submission about digital wallet adoption among elderly Peruvians near the extreme-poverty threshold a contribution of sufficient general interest to merit placement at that level, or is the paper better suited to a field journal where the Peru/Latin America policy context carries more weight?

6. **On the permutation inference conflict:** The asymptotic t-statistic for the covariate-adjusted WLS estimate is approximately −5.4 (−0.027/0.005), while the permutation p-value is 0.434. The paper attributes this to the discrete running variable anti-conservatism in asymptotic SEs. Can you show the full permutation distribution of the WLS t-statistic under the null and confirm that the empirical t = −5.4 falls well within the null distribution? A figure of this distribution would make the conflict interpretable to referees who have not encountered this artifact before.

7. **On template artifacts:** The code review report documents that Table 4 carries the header "at the Electoral Threshold" and that Figure 1's x-axis reads "Vote Margin." Were these corrected before submission? If the replication code contains outputs from an electoral RDD template, a referee who attempts to replicate will encounter these immediately. Confirming that the submitted tables and figures have been manually verified against the code output is necessary.

---

## Scoring

```json
{
  "score": 68,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 73,
    "identification_credibility": 62,
    "empirical_execution": 64,
    "writing_presentation": 74,
    "literature_positioning": 70
  },
  "required_analyses": [
    "First-stage discontinuity in Pensión 65 take-up at age 65 must be shown or demonstrated to be infeasible with available data",
    "Sharp vs. fuzzy design must be resolved: either recharacterize as fuzzy RDD with ITT and scaled LATE, or demonstrate SISFOH share is continuous through the cutoff; remove LATE label from Equation (1)",
    "Replace full-sample Table 1 with bandwidth-restricted summary statistics (ages within h*=14.2 of the cutoff); the current table is misleading about who the identifying comparison is between"
  ],
  "suggested_analyses": [
    "Fix covariate-adjusted specification to use h*=14.2 bandwidth by pre-restricting sample to ages 50-80 before calling rdrobust; current WLS fallback with h=34.2 is a different estimand, not a robustness check",
    "Apply Kolesár-Rothe (2018) confidence intervals for discrete running variables or commit to randomization inference as the primary inference procedure throughout, not as a post-hoc correction",
    "Heterogeneity by SISFOH poverty classification: estimate RDD separately for extreme-poor vs. non-extreme-poor subsamples to test the core mechanism",
    "Correct all electoral-RDD boilerplate in table notes and figure labels before resubmission; code review confirms these artifacts survive in the output pipeline",
    "Report expansion-factor-weighted population means for outcomes and clarify whether RDD estimates use survey weights"
  ],
  "questions_to_authors": [
    "Does ENAHO 2024 record Pensión 65 receipt? If so, what is the first-stage RDD estimate of the take-up jump at age 65 within the optimal bandwidth?",
    "How do you justify calling the design sharp when only SISFOH-classified extreme-poor individuals aged 65+ are eligible, meaning the treatment probability jump at the cutoff is substantially below 1?",
    "Can you rerun the covariate-adjusted local-polynomial specification on a pre-restricted sample of ages 50-80 to avoid the memory constraint while preserving local identification?",
    "Is there evidence that SISFOH poverty classification itself is continuous at age 65, or could age-related reclassification introduce a discontinuity in the running variable's joint distribution with poverty status?",
    "Can you show the full permutation distribution of the WLS t-statistic and confirm that the empirical t≈-5.4 falls within the null distribution, making the randomization p=0.434 credible?",
    "Were the electoral-RDD boilerplate labels in Table 4 and Figure 1 corrected in the submitted version, or do those artifacts survive in the actual output files?",
    "Given that the identifying variation is local to ages 51-79 (h*=14.2) and the population of interest is elderly extreme-poor Peruvians, do the authors view this as a top-field submission or a field-journal submission, and how do they frame the contribution accordingly?"
  ],
  "n_critical": 3,
  "n_major": 5
}
```