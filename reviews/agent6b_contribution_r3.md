## Pre-Submission Referee Report (Round 3)

**Date**: 2026-05-02
**Target**: Top-field economics journal
**Paper**: Pensión 65 / ENAHO 2024 RDD — Digital Financial Inclusion

---

## Preliminary Note on the Submitted Manuscript

The `main.tex` file submitted for this round is **structurally broken**: bibliography `\bibitem` entries appear directly in the document preamble (before `\begin{document}`), and no body content — introduction, data section, results, or tables — is visible in the submitted file. This is either a truncation artifact in transmission or a genuine LaTeX compilation failure. The referee cannot assess the full paper text and must therefore evaluate this round primarily from the evidence packet (data audit, code review, summary table) and the Round 2 concerns. **If the manuscript compiles correctly on the authors' machine, a clean `.pdf` must accompany any future submission.**

---

## Part 1 — Central Contribution

**Statement**: The paper provides quasi-experimental evidence on the effect of Pensión 65 — Peru's social pension for elderly poor — on digital wallet ownership and active use among program-eligible households, exploiting the program's age/poverty-score eligibility cutoff in an RDD framework using ENAHO 2024 data.

**Rating**: **Incremental**

This is the right rating, not a criticism. The question is policy-relevant: as Latin American governments digitize transfer delivery, whether a legacy cash transfer program induces complementary digital financial adoption is genuinely important. The contribution is meaningful but not transformative — it extends a now-standard "mobile money + social protection" literature to Peru with a clean administrative cutoff.

---

## Part 2 — Identification and Credibility

**Variation used**: Age/poverty-score eligibility cutoff for Pensión 65, implemented as an RDD. The identifying assumption is that potential outcomes (digital wallet ownership, use) are continuous at the cutoff — i.e., households just above and just below the eligibility threshold are comparable in all unobserved respects.

**Plausible exogeneity**: Age-based cutoffs are generally clean, as individuals cannot precisely manipulate their birthdate. If the running variable is a composite poverty/wealth index (SISFOH score), the story is more complicated — households near the cutoff have strong incentives to misreport assets, which would violate continuity. The McCrary density test reported in the robustness pipeline addresses this, which is appropriate.

**Main identification threats**:

1. **Running variable ambiguity (unresolved)**: From the evidence available, the identification design is not unambiguously clear. Table 1 labels "Above Threshold (Treated)" with N = 14,088 and "Below Threshold (Control)" with N = 99,667 — a 7:1 imbalance that is unusual for a symmetric RDD window. The treated group shows *lower* wallet ownership (5.35% vs. 8.00%) and dramatically lower wallet *use* (3.19% vs. 17.94%), yet *higher* per-capita income (13,454 vs. 11,417 soles). This pattern is consistent with an **age-based** cutoff where "treated" = elderly (≥ 65), who have structurally lower baseline digital literacy and income volatility — but the income numbers then need explanation since Pensión 65 transfers would add to income for the treated. The paper must clearly state the running variable, centering, and why the sample is so asymmetrically distributed around the cutoff.

2. **Compound treatment**: Pensión 65 delivers both income and an institutional relationship with the state (bank account, biometric registration). The ITT estimate conflates these channels. The paper presumably does not attempt to decompose them — acceptable if acknowledged — but the interpretation of results must be precise about what "access" means.

3. **Survey weights omitted**: The data audit flags no survey weight column. ENAHO is a complex stratified sample; using unweighted regressions may yield estimates that are not population-representative and could introduce bias if survey design correlates with the outcome. This is a substantive methodological concern, not a minor formatting note.

---

## Part 3 — Required and Suggested Analyses

### Required [CRITICAL]

**[CRITICAL-1] Template boilerplate in output tables and figures — results cannot be verified**

The code review (current round) reports that `03_output.py` still contains electoral-RDD boilerplate: Table 1 note references "municipality-elections where the party's vote share exceeded the electoral threshold"; Table 4 header reads "at the Electoral Threshold"; Figure 1 x-axis reads "Vote Margin." These are not cosmetic issues. If the table notes and axis labels describe a different study, a reader cannot verify that the tables and figures shown actually correspond to the described Pensión 65 / digital-wallet analysis. This is a reproducibility and integrity concern that makes the empirical outputs uninterpretable without the source code audit. **This must be corrected before submission.** It was flagged in the code review and remains unresolved.

**[CRITICAL-2] Survey weights — population representativeness**

ENAHO is a probability sample designed to be nationally representative only when weights are applied. Using unweighted regressions in an RDD near the Pensión 65 cutoff risks overrepresenting certain strata (rural, multi-stage clusters). The data audit explicitly flags no weight column. At minimum, the authors must (a) demonstrate that the RDD estimates are robust to applying survey weights, or (b) explicitly argue why the unweighted local-linear estimate identifies the relevant parameter. In a top-field journal, omitting design weights from a nationally representative household survey without justification is a material flaw.

### Suggested [MAJOR]

**[MAJOR-1] Asymmetric bandwidth explanation**

The 7:1 sample imbalance (14K treated, 99K control) must be explained. If the optimal bandwidth is asymmetric — wider on the control side — the paper should report the data-driven bandwidth selector and show estimates are stable to symmetric alternatives. If this reflects the demographic distribution of ENAHO (far more people below 65 than above in the relevant sample), that itself warrants a note.

**[MAJOR-2] Income effects vs. institutional access channel**

The paper's framing is "institutional access on digital adoption," but Pensión 65 also provides income. A rough check: does controlling for income changes near the cutoff attenuate the digital adoption effect? This is standard in the P65 literature (e.g., Agüero et al.) and reviewers at top fields will ask.

**[MAJOR-3] Hardcoded absolute path — reproducibility blocker**

`00_clean.py:16` contains `DATA_FILE = "C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv"`. Combined with a fragile `import_module("01_main")` that may fail depending on Python version and sys.path, the replication package cannot be run by a second machine. A `requirements.txt`, relative paths, and a master `run_all.py` are non-negotiable for any journal with a replication policy — which includes all top-field outlets.

**[MAJOR-4] Poverty variable as outcome or control**

POBREZA appears in Table 1 as a covariate with mean 2.74 (treated) vs. 2.68 (control). It is unclear whether this is a categorical poverty classification or a continuous score, and whether it is used as a control or a placebo outcome. If it is the running variable itself, reporting it as a covariate in the balance table is misleading.

**[MAJOR-5] Missing explicit first-stage**

For an ITT design, the paper should report the first-stage takeup rate — what fraction of eligible households (above cutoff) actually enrolled in Pensión 65 and received transfers? Without this, the reader cannot judge whether the ITT estimates are attenuated by partial compliance and cannot compute a rough LATE for policy benchmarking.

---

## Part 4 — Literature Positioning

The bibliography includes Jack & Suri (2014), Muralidharan et al. (2016), and Suri (2017) — the canonical mobile money and state capacity references. These are appropriate anchors. However, based on the evidence available:

- The Peru-specific literature on Pensión 65 (Agüero, García, Hübler; Behrman et al.) should be more explicitly engaged with, as this program has a substantial evaluation literature the paper must position against.
- The digital financial inclusion literature specific to Latin America (e.g., Bachas et al. 2021 on debit cards and savings in Mexico) is a close neighbor and should be cited.
- The Round 2 concern about a phantom Deming & Noray (2023) citation cannot be verified from the current truncated submission, but if it persists it must be removed.

---

## Part 5 — Journal Fit and Recommendation

**Recommendation**: **Revise before sending**

The question is timely, the RDD design is credible in principle, and the robustness suite is notably comprehensive (McCrary test, placebo outcomes, bandwidth sensitivity, donut holes, covariate balance, polynomial sensitivity, placebo cutoffs, permutation inference). A paper with this apparatus, on this question, with this data, is publishable.

However, the paper cannot go to referees in its current state:
- The manuscript file is broken or was transmitted incorrectly
- Template boilerplate in the outputs is unresolved from the prior code review
- Survey weights are absent without justification
- The running variable and sample asymmetry need clarification

These are all fixable in one revision cycle. The underlying economics and design are sound enough to warrant the effort.

---

## Part 6 — Questions to the Authors

1. **Running variable**: What is the exact running variable — age in months relative to the Pensión 65 eligibility cutoff, a SISFOH poverty score, or a composite? Why is the treated sample (N = 14,088) so much smaller than the control (N = 99,667)? Is the bandwidth asymmetric, and if so, what data-driven criterion determines it?

2. **Income vs. access**: Pensión 65 provides both a cash transfer and an institutional link to the financial system. What is the theoretical mechanism by which program participation increases *digital wallet adoption* specifically? Is there a channel through which the pension delivery method (cash at a bank branch, mobile disbursement) directly induces wallet registration?

3. **Survey weights**: ENAHO is a stratified probability sample. Why are no survey design weights applied in the main specification? Do estimates change materially when weights are used?

4. **Takeup rate / first stage**: What fraction of households above the eligibility threshold actually received Pensión 65 transfers in 2024? Is the ITT substantially attenuated by partial compliance?

5. **Template boilerplate**: Tables 1 and 4 and Figure 1 in the output scripts retain labels from an electoral RDD study ("vote margin," "electoral threshold"). Have the final submitted tables and figures been manually verified to correspond to the Pensión 65 / digital wallet analysis? Can the authors confirm the replication package produces the exact tables in the paper?

6. **POBREZA variable**: Is POBREZA the running variable, a control covariate, or a placebo outcome? Reporting it in the balance table alongside other covariates is ambiguous.

7. **Income direction**: Treated households show higher INGRESO\_PC (13,454 vs. 11,417 soles) despite being the program-eligible group. Does this include pension transfer income? If so, how does the paper interpret digital wallet adoption effects that are partly income-mediated?

---

## Scoring

```json
{
  "score": 65,
  "contribution_rating": "Incremental",
  "recommendation": "Revise before sending",
  "dimension_scores": {
    "contribution_novelty": 68,
    "identification_credibility": 67,
    "empirical_execution": 58,
    "writing_presentation": 52,
    "literature_positioning": 65
  },
  "required_analyses": [
    "Remove electoral-RDD template boilerplate from all output tables and figures and verify outputs match the Pensión 65 analysis",
    "Apply ENAHO survey design weights or provide explicit justification for unweighted estimates"
  ],
  "suggested_analyses": [
    "Clarify running variable, bandwidth choice, and the 7:1 sample asymmetry",
    "Report first-stage takeup rate to allow LATE calculation",
    "Test income channel by controlling for or instrumenting income change near cutoff",
    "Fix hardcoded paths and fragile imports in replication package; add requirements.txt and master run script",
    "Clarify role of POBREZA variable: running variable, covariate, or placebo"
  ],
  "questions_to_authors": [
    "What is the exact running variable and why is the treated sample (N=14,088) so much smaller than control (N=99,667)?",
    "What is the theoretical mechanism linking Pensión 65 eligibility to digital wallet adoption specifically?",
    "Why are ENAHO survey design weights not applied? Are estimates robust to weighting?",
    "What is the program takeup rate for eligible households in the 2024 sample?",
    "Have the final submitted tables and figures been manually verified to match the Pensión 65 analysis (not electoral RDD boilerplate)?",
    "Is POBREZA the running variable, a control covariate, or a placebo outcome in the RDD design?",
    "Why do treated households show higher INGRESO_PC than controls — does this include pension transfer income, and how does this affect interpretation?"
  ],
  "n_critical": 2,
  "n_major": 5
}
```

---

**Scoring rationale**: The baseline of 72 is adjusted downward primarily by two factors: (1) the empirical execution score (58) reflects genuinely unresolved critical issues from prior rounds — template boilerplate in outputs is not cosmetic, it prevents verification of results; (2) the writing/presentation score (52) reflects a manuscript file that does not compile or was submitted in broken form, which is a functional blocker regardless of the underlying quality. The identification design and robustness suite are genuine strengths that keep contribution and credibility near 68. If the authors resolve the output boilerplate, submit a compilable manuscript, and address the survey weights question, the paper is likely in the 72–76 range.