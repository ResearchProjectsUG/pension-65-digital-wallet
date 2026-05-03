## Pre-Submission Referee Report — Round 2

**Date**: 2026-05-02
**Target**: Top-field economics journal

---

### Preliminary Note on the Submitted Revision

The `main.tex` file provided contains only document-class declarations and a three-entry bibliography; the paper body is absent from the submitted materials. This prevents me from confirming whether the Round 2 textual corrections (CRITICAL-1, CRITICAL-2, MAJOR-1 through MAJOR-6) were implemented. I therefore cannot mark those issues as resolved, and they remain open until a complete draft is submitted. I evaluate below only what the evidence packet allows me to assess directly.

---

### Part 1 — Central Contribution

The paper estimates the effect of Pensión 65 eligibility on digital financial adoption (wallet ownership, wallet usage, smartphone ownership, internet access) among elderly poor Peruvians, exploiting a discrete program eligibility cutoff in ENAHO 2024 via regression discontinuity. **Rating: Incremental.** The question is policy-relevant — Peru's digital payment infrastructure is actively expanding — and the setting is understudied. The contribution sits squarely within the mobile money and government transfer literature. Incremental is not a criticism; most publishable empirical papers are incremental.

---

### Part 2 — Identification and Credibility

The RDD exploits a discrete Pensión 65 eligibility cutoff. The identifying assumption — continuity of potential outcomes at the cutoff — is standard for age- or welfare-score-based program eligibility designs. The code review confirms a thorough robustness battery: McCrary density test, placebo outcomes, bandwidth sensitivity, donut holes, covariate balance, polynomial sensitivity, placebo cutoffs, and permutation inference. This is methodologically serious work.

**Main identification threats not fully resolved:**

1. **Compound discontinuities**: Peru operates multiple age-indexed social programs (SIS modifications, ONP, others). If any other program changes eligibility at the same cutoff that identifies Pensión 65, the estimated discontinuity is not attributable to Pensión 65 alone. The materials do not address this.

2. **ITT vs. LATE**: The design is explicitly ITT. Without information on compliance (take-up rates near the cutoff), readers cannot scale the ITT estimate to recover the program effect, limiting interpretability.

3. **Sample scope of the RDD**: See Part 3, CRITICAL-1 below.

---

### Part 3 — Required and Suggested Analyses

#### Required [CRITICAL]

**[CRITICAL-1] — Sample composition anomaly in Table 1**

Table 1 reports 14,088 observations above the threshold (treated) and 99,667 below (control) — a ratio of roughly 1:7. In a bandwidth-restricted RDD sample, we expect approximately equal counts on both sides of the cutoff within the selected window. The full sample is 113,755 observations (14,088 + 99,667 = 113,755 exactly), strongly suggesting Table 1 is constructed from the full, unrestricted dataset rather than from a local bandwidth window.

This has two implications. First, if the main RDD estimates also use the full sample without local restriction, this is a methodological error — RDD validity requires local estimation near the cutoff, not global comparison. Second, if the main estimates do use a bandwidth (as rdrobust would impose), then Table 1 is misleading because the means displayed do not correspond to the estimation sample. Authors must (a) clarify what sample Table 1 describes, (b) provide a bandwidth-restricted summary table showing counts on each side within the optimal bandwidth, and (c) confirm the main regressions use local estimation.

**[CRITICAL-2] — Survey weights absent from ENAHO analysis**

The data audit explicitly flags: *"No survey weight column found. Results may not be population-representative."* ENAHO is a stratified, multi-stage probability sample with stratum-level expansion weights that are required for representative inference. Unweighted means in Table 1 and unweighted RDD regressions estimate quantities for the realized sample, not the population. For a paper making policy claims about the elderly poor in Peru, this is not a minor issue. Authors must either apply survey weights throughout or provide weighted estimates as a robustness check and explicitly limit population claims to the in-sample population.

#### Suggested [MAJOR]

**[MAJOR-1] — Electoral RDD template boilerplate persists in output scripts**

The code review (Stage 4.7) finds that `03_output.py` retains template artifacts from an electoral RDD: Table 1 notes reference "municipality-elections where the party's vote share exceeded the electoral threshold"; Table 4 header reads "at the Electoral Threshold"; Figure 1 x-axis label reads "Vote Margin." None of these match a digital wallet / ENAHO study. These must be corrected before any submission or workshop presentation.

**[MAJOR-2] — Direction of pre-treatment digital adoption requires explanation**

Table 1 shows the treated group has substantially lower wallet ownership (5.35% vs. 8.00%) and dramatically lower wallet usage (3.19% vs. 17.94%) than controls. This is plausibly explained by an age gradient in technology adoption — older individuals are less digitally active — but the paper must make this explicit. A reader unfamiliar with ENAHO's age structure will find the negative treated-control comparison for the program's primary outcome variable puzzling, and could misread it as evidence of a negative treatment effect.

**[MAJOR-3] — Differential missing data in education variable**

NIVEL_EDUCATIVO has 295 missing observations in the treated group (2.1% of 14,088) but 6,841 missing in the control group (6.9% of 99,667). This differential missingness rate could reflect item non-response correlated with unobservables. Authors should confirm whether missing rates are smooth through the cutoff, and test whether excluding education from covariate adjustment affects the main estimates.

**[MAJOR-4] — Hardcoded absolute path blocks reproducibility**

`00_clean.py:16` contains `DATA_FILE = "C:/Users/jesus/Desktop/papers-HQ- AI/..."`. This path is machine-specific and will fail on any other system. Replace with a relative path from project root or an environment variable (`DATA_DIR` / `PROJECT_ROOT`). This is a blocking issue for any replication attempt.

**[MAJOR-5] — Reproducibility infrastructure**

No master run script, no `requirements.txt`, no documented execution order are present. Journals increasingly require a documented, end-to-end replication package. Add a `README.md` specifying sequential execution and a `requirements.txt` or `environment.yml` pinning package versions (particularly `rddensity`, `rdrobust`, and `numpy`).

---

### Part 4 — Literature Positioning

The three visible bibliography entries — Jack and Suri (2014) on mobile money and risk sharing, Muralidharan et al. (2016) on biometric smartcards and state capacity, Suri (2017) on mobile money — are appropriate anchors. However, three entries is far too sparse for a top-field submission. Conspicuously absent:

- **Bachas, Gertler, Higgins, and Seira (2021)** (*AER*): debit cards and savings behavior among the poor — directly relevant to the wallet adoption question
- **Muralidharan, Niehaus, and Sukhtankar (2023)**: government digital payment adoption in developing countries
- **Peru-specific evaluation literature** on Pensión 65 (Bando et al., IDB working papers on the program's consumption and labor effects)
- **Financial inclusion measurement literature** (Demirgüç-Kunt, Klapper, Singer)

The thin bibliography weakens the framing and will draw immediate attention from referees familiar with the field.

---

### Part 5 — Journal Fit and Recommendation

**Recommendation: Revise before sending.**

The paper has a relevant question, a credible identification strategy, and a thorough robustness suite. However, it cannot be sent to external referees in its current state for two reasons: (1) the bandwidth/sample composition anomaly in Table 1 calls into question what the main estimates actually identify, and (2) the missing survey weights undermine the representativeness of every descriptive and causal claim. These are not stylistic issues — they require author verification and revision. Additionally, the incomplete `main.tex` submission prevents assessment of Round 2 textual corrections.

Once the sample composition is clarified, weights are applied (or rigorously justified as unnecessary), and the template boilerplate is purged, this paper is a reasonable candidate for external review at a field journal, if not necessarily the very top venue.

---

### Part 6 — Questions to the Authors

1. **Bandwidth and sample**: Table 1 sums to exactly 113,755 total observations, suggesting no bandwidth restriction was applied. Was the table constructed from the full dataset or from the bandwidth-restricted sample? Please provide a table showing treated/control counts within the optimal bandwidth, alongside the global table.

2. **Survey weights**: ENAHO requires expansion weights for representative inference. Why are no weights applied in the analysis? Please provide survey-weighted descriptive statistics and RDD estimates as a robustness check, or explicitly restrict all population claims to the in-sample population.

3. **Compound discontinuities**: Do any other social programs in Peru (SIS age transitions, ONP, Contigo, or similar) change eligibility at the same age or welfare-score threshold that identifies Pensión 65 eligibility? How do you rule out that the estimated RD discontinuity reflects those programs?

4. **Take-up and compliance**: What is the Pensión 65 take-up rate among eligibles near the cutoff? Please provide the first-stage discontinuity and clarify how readers should scale the ITT estimate to recover the treatment-on-the-treated effect.

5. **Direction of effects in Table 1**: The treated group shows lower digital wallet usage (3.19%) than controls (17.94%). Please clarify whether this reflects a pre-program age gradient in technology adoption or a contemporaneous post-treatment cross-section, and explain how the RDD design recovers a causal estimate given this unconditional pattern.

6. **Differential education missingness**: NIVEL_EDUCATIVO has 2.1% missing in treated vs. 6.9% in control. Is this differential rate smooth through the cutoff? Does including or excluding education from covariate adjustment materially change the main estimates?

7. **Round 2 textual revisions**: The submitted `main.tex` contains only bibliography entries and no paper body. Please confirm that CRITICAL-1 (Figure 1 description), CRITICAL-2 (Deming & Noray phantom citation), and MAJOR-1 through MAJOR-6 from the prior round have been addressed, and resubmit the complete draft.

---

```json
{
  "score": 67,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 71,
    "identification_credibility": 67,
    "empirical_execution": 64,
    "writing_presentation": 65,
    "literature_positioning": 62
  },
  "required_analyses": [
    "Clarify whether Table 1 uses the full sample or the bandwidth-restricted sample; provide RDD estimates restricted to the optimal bandwidth with balanced treated/control counts",
    "Apply ENAHO survey weights throughout or provide weighted robustness checks and restrict population claims accordingly"
  ],
  "suggested_analyses": [
    "Remove all electoral-RDD template boilerplate from table notes and figure labels in 03_output.py before any submission",
    "Explicitly explain the negative unconditional correlation between treatment status and digital adoption (age gradient vs. selection) in the descriptive section",
    "Investigate and report the differential missingness rate in NIVEL_EDUCATIVO across treated and control groups near the cutoff",
    "Replace hardcoded absolute path in 00_clean.py:16 with a relative path or PROJECT_ROOT environment variable",
    "Add README.md with sequential execution order and requirements.txt/environment.yml for end-to-end reproducibility"
  ],
  "questions_to_authors": [
    "Table 1 sums to exactly 113,755 observations — the full sample. Was any bandwidth restriction applied before constructing this table? Please provide treated/control counts within the optimal bandwidth alongside the full-sample table.",
    "ENAHO is a stratified probability sample requiring expansion weights for representative inference. Why are no survey weights applied? Please provide weighted estimates or restrict all population claims to the in-sample population.",
    "Do any other Peruvian social programs change eligibility at the same threshold that identifies Pensión 65? How do you rule out compound discontinuities driving the estimated effect?",
    "What is the Pensión 65 take-up rate among eligibles near the cutoff? Please provide the first-stage discontinuity so readers can scale the ITT estimate to a treatment-on-the-treated effect.",
    "Table 1 shows treated individuals have lower wallet usage (3.19%) than controls (17.94%). Is this a pre-program age gradient in technology adoption? Please clarify the counterfactual logic and how the RDD recovers a causal estimate given this unconditional pattern.",
    "NIVEL_EDUCATIVO has 2.1% missing in treated vs. 6.9% in control. Is this differential rate smooth through the cutoff? Does it affect covariate balance tests?",
    "The submitted main.tex contains no paper body. Please confirm Round 2 textual corrections were implemented and resubmit the complete draft."
  ],
  "n_critical": 2,
  "n_major": 5
}
```