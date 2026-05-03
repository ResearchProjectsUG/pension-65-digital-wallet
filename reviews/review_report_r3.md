# Pre-Submission Referee Report (Round 3)

**Date**: 2026-05-02

**Target**: top-field

---


## 1. Spelling, Grammar & Style

The `main.tex` file provided is missing essentially all of its content. What was supplied contains only the LaTeX preamble (package declarations) and three bibliography entries — there is no `\begin{document}`, no title, no abstract, no body sections, no results, no conclusion. The file appears to have been severely truncated before being passed in.

**What IS visible (the three bibliography entries):**

- `Jack & Suri (2014)` — correctly formatted, consistent with the style used in Round 2 feedback.
- `Muralidharan et al. (2016)` — correctly formatted.
- `Suri (2017)` — correctly formatted.

These three entries do not exhibit the issues flagged in Round 2 (the problematic entries were `banerjee2020`, `deming2023`, etc., which are not present here).

**What I cannot review:**

- The Introduction, body sections (§1–§6), and conclusion — absent.
- Whether CRITICAL-1 (Figure 1 age-direction contradiction) was fixed.
- Whether MAJOR-1 through MAJOR-6 corrections were applied.
- Whether `deming2023` was removed or the phantom citation resolved.
- Whether spelling inconsistencies ("centred" vs. "centered") were standardized.

**Action required:** Please re-paste the full paper content — at minimum the text body. The file as submitted cannot be meaningfully reviewed.

```json
{
  "n_critical": 0,
  "n_major": 0,
  "n_minor": 0,
  "top_issues": [
    "Paper body is entirely absent from the provided file — review impossible",
    "No \\begin{document} tag present; preamble runs directly into bibliography",
    "Cannot verify resolution of any Round 2 issues without body text"
  ]
}
```

---


## 2. Internal Consistency & Cross-References

## Technical Coherence Review — Round 3

> **Note on scope**: The provided `main.tex` contains only three bibliography entries — the full paper body is absent. Section-level text claims cannot be verified against tables, and all Round 2 body-text issues remain unverifiable. The review below is based entirely on the evidence packet and the four LaTeX tables.

---

### What Round 2 Issues Can Be Confirmed as Resolved

**None can be confirmed.** CRITICAL-1 (Figure 1 direction contradiction), CRITICAL-2 (Deming & Noray phantom reference), and MAJOR-1 through MAJOR-6 all concern body text that was not submitted. These issues are neither cleared nor re-raised here — they are in limbo pending a full manuscript.

---

## Numerical Consistency Issues Found in Tables

---

**[CRITICAL-1] Duplicated covariates across Table 3 Panel D and Table 4 with irreconcilable numbers**

Both `INTERNET_HOGAR` and `SMARTPHONE` appear as RDD outcomes in Table 3 Panel D ("Placebo") and Table 4 ("Covariate Balance"). The numbers do not agree:

| Variable | Table | Estimate | SE | CI | BW | N |
|---|---|---|---|---|---|---|
| INTERNET_HOGAR | Table 3 Panel D | 0.0139 | 0.0487 | [−0.0615, 0.1296] | **15.23** | **29,668** |
| INTERNET_HOGAR | Table 4 | 0.0147 | 0.0489 | [−0.0607, 0.1308] | **14.24** | **27,809** |
| SMARTPHONE | Table 3 Panel D | 0.0138 | 0.0246 | [−0.0218, 0.0748] | **14.29** | 27,809 |
| SMARTPHONE | Table 4 | 0.0139 | 0.0256 | [−0.0146, 0.0857] | **14.24** | 27,809 |

For `INTERNET_HOGAR`, sample size differs by **1,859 observations**. For `SMARTPHONE`, N is identical but the CI width diverges by ~4% (0.0966 vs. 0.1003) and the intervals themselves shift materially (lower bound: −0.0218 vs. −0.0146). Neither table contains a note explaining why the same test is reported twice under different specifications. Table 4 states it uses "the MSE-optimal bandwidth (h\* = 14.24)" but Table 3 uses outcome-specific optimal bandwidths (15.23, 14.29). A referee comparing these two tables will halt.

---

**[MAJOR-1] Table 2 switches estimation method without disclosure — rdrobust → statsmodels\_WLS with a 2.4× wider bandwidth**

| Specification | Method | BW | N |
|---|---|---|---|
| baseline (TIENE\_BILLETERA) | rdrobust | 14.24 | 27,809 |
| baseline (USA\_BILLETERA) | rdrobust | 17.29 | 33,267 |
| with\_covariates | **statsmodels\_WLS** | **34.22** | **59,649** |
| extended\_covariates | **statsmodels\_WLS** | **33.46** | **57,039** |

No table note discloses the method switch or the bandwidth jump. The WLS CIs are fully symmetric and tight (e.g., [−0.0373, −0.0167] for `with_covariates` TIENE\_BILLETERA), structurally incomparable to the rdrobust robust CIs. A bandwidth of 34.22 years when the age cutoff is 65 stretches the local-randomization window across nearly the full sample, undermining the RDD identification logic for those rows. This must be noted explicitly in the table.

---

**[MAJOR-2] Paper body absent — Round 2 CRITICAL and MAJOR issues unverifiable**

The `main.tex` submitted for this round contains only three bibliography items (`jack2014`, `muralidharan2016`, `suri2017`). The following Round 2 findings remain in open status and **must be cleared in a future submission**:

- CRITICAL-1: Figure 1 age-direction contradiction
- CRITICAL-2: Deming & Noray (2023) phantom reference
- MAJOR-1: "Importantly" in §5.1
- MAJOR-2: "centred" / "centered" inconsistency
- MAJOR-3: "literature is insufficient"
- MAJOR-4: Missing "the effect of"
- MAJOR-5: Banerjee et al. year label mismatch
- MAJOR-6: Limitations structural breakdown

---

**[MINOR-1] NIVEL\_EDUCATIVO missing observations unacknowledged in Table 1**

Table 1 total N: 14,088 + 99,667 = **113,755** (matches data audit ✓).
But `NIVEL_EDUCATIVO` N: 13,793 + 92,826 = **106,619** — a shortfall of **7,136 observations (6.3%)** with no footnote. Readers will notice the denominator change with no explanation.

---

**[MINOR-2] Template boilerplate in table notes — unverified**

The Stage 4.7 code review flagged `03_output.py` for electoral RDD artifacts ("at the Electoral Threshold," "Vote Margin") surviving into table notes and figure labels. `table_4_covariate_balance.tex` appears clean, but `table_1_summary.tex` notes are truncated in the packet and figures are not inspectable. If this language persists anywhere in the submission, it is fatal at desk review.

---

**[MINOR-3] Table 3 Panel A, H Double: extreme bias-correction asymmetry**

- Conventional estimate: −0.0204; SE: 0.0137; CI: [−0.0272, 0.0264]
- Distance from estimate to lower bound: **0.0068**
- Distance from estimate to upper bound: **0.0468** (6.9× larger)

This implies the bias-corrected rdrobust estimate is near 0, meaning the bias correction shifts the effective estimate by ~0.020 — nearly equal in magnitude to the point estimate itself. This should be acknowledged in text, as it means doubling the bandwidth produces an estimate where bias concerns dominate inference.

---

```json
{
  "n_critical": 1,
  "n_major": 2,
  "n_minor": 3,
  "top_issues": [
    "[CRITICAL-1] INTERNET_HOGAR and SMARTPHONE appear in both Table 3 Panel D and Table 4 with different estimates, SEs, CIs, and N (INTERNET_HOGAR differs by 1,859 obs) — no note explains the discrepancy between outcome-specific vs. fixed bandwidths",
    "[MAJOR-1] Table 2 switches from rdrobust (BW ≈ 14–17) to statsmodels_WLS (BW ≈ 34) for covariate-adjusted rows without any disclosure — incomparable methods and a 2.4× wider window are presented side-by-side as though equivalent",
    "[MAJOR-2] Paper body is absent from the submitted main.tex — 8 Round 2 issues (Figure 1 direction, phantom reference, spelling, word choice, missing words, Banerjee year, Limitations) cannot be confirmed as resolved"
  ]
}
```

---


## 3. Unsupported Claims & Identification Integrity

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

---


## 4. Mathematics, Equations & Notation

## Mathematical & Formal Content Review — Round 3

### Preliminary Note: Critically Truncated Manuscript

The `main.tex` provided contains **only the LaTeX preamble and three bibliography entries.** The entire document body — title, abstract, all numbered sections, all equations, all tables, all figures — is absent. This makes it impossible to evaluate mathematical correctness, notation consistency, equation numbering, regression specification alignment, or statistical notation. The seven checklist items cannot be assessed on content that was not transmitted.

What is present: package declarations + 3 `\bibitem` entries + `\end{document}`
What is absent: `\begin{document}`, document body, most bibliography entries

The issues below are therefore structural LaTeX problems visible in the provided fragment.

---

### CRITICAL Issues

**[CRITICAL-1] Missing `\begin{document}` — document will not compile**

No `\begin{document}` command appears anywhere in the file. Every line after the preamble is effectively in the preamble. This is a fatal compilation error regardless of content.

---

**[CRITICAL-2] Missing `\begin{thebibliography}` — unmatched environment**

The file ends with `\end{thebibliography}` but contains no corresponding `\begin{thebibliography}{...}`. LaTeX will throw an unmatched `\end` error and halt.

---

**[CRITICAL-3] Jack & Suri (2014) `\bibitem` command accidentally commented out**

The comment block reads:

```latex
% natbib in authoryear mode requires a .bbl file. Since we use a manual
% thebibliography environment with \bibitem[Jack and Suri(2014)]{jack2014}
Jack, W. and Suri, T. (2014).
Risk Sharing and Transactions Costs: Evidence from Kenya's Mobile Money Revolution.
\textit{American Economic Review}, 104(1):183--223.
```

The `\bibitem[Jack and Suri(2014)]{jack2014}` invocation was placed on the second comment line and is therefore a comment, not a command. The entry body ("Jack, W. and Suri, T...") appears as raw floating text with no `\bibitem` anchor. Any `\cite{jack2014}` call in the text will resolve to `??`. The correct structure:

```latex
\begin{thebibliography}{99}

\bibitem[Jack and Suri(2014)]{jack2014}
Jack, W. and Suri, T. (2014).
Risk Sharing and Transactions Costs: Evidence from Kenya's Mobile Money Revolution.
\textit{American Economic Review}, 104(1):183--223.
```

---

### MAJOR Issues

**[MAJOR-1] Mathematical review is blocked — paper body not provided**

None of the seven checklist items (mathematical correctness, notation consistency, undefined notation, equation numbering, regression–text–table alignment, statistical notation, LaTeX math formatting) can be evaluated. The fragment provides nothing to check.

---

### Status of Round 2 Issues

| Issue | Status | Basis |
|---|---|---|
| CRITICAL-2: Deming & Noray phantom reference | **Apparently resolved** — entry absent from the three provided `\bibitem`s | Visible in fragment |
| MAJOR-5: Banerjee et al. year inconsistency | **Cannot verify** — entry not present in fragment | Truncation |
| CRITICAL-1: Figure 1 age-direction contradiction | **Cannot verify** — §5.5 body absent | Truncation |
| MAJOR-1 through MAJOR-6: prose issues | **Cannot verify** — body absent | Truncation |

---

### Recommendation

The file as transmitted is non-compilable and lacks the document body. Before any substantive mathematical review can proceed, the authors must supply the complete `main.tex` with:

1. A proper `\begin{document}` ... `\end{document}` wrapper
2. A properly opened `\begin{thebibliography}{99}` environment
3. The `\bibitem` command for Jack & Suri (2014) removed from the comment

Once the full document body is available, the mathematical checklist — derivations, regression specifications, notation, equation numbering — can be evaluated properly.

---

```json
{
  "n_critical": 3,
  "n_major": 1,
  "n_minor": 0,
  "top_issues": [
    "Missing \\begin{document} — document is entirely non-compilable",
    "Missing \\begin{thebibliography} — unmatched \\end{thebibliography} will halt compilation",
    "Jack & Suri (2014) \\bibitem command accidentally placed inside a LaTeX comment — citation key jack2014 is undefined",
    "Document body absent — mathematical content (equations, specifications, notation) could not be reviewed"
  ]
}
```

---


## 5. Tables, Figures & Documentation

The figure files are binary PNGs — I'll base the figure review on structural checks (captions, cross-references, axis labels) derivable from context, flagging what requires visual verification. Here is the full production-editor report.

---

# Production Editor Review — Round 3
**Paper**: Determinantes de adopción de billetera digital en Perú (RDD / Pensión 65)
**Review scope**: Tables 1–4 (LaTeX source) + Figures 1–2 + McCrary density figure
**Note**: Issues already resolved in Round 2 are not re-raised.

---

## TABLES

### Table 1 — Summary Statistics

**[CRITICAL-T1-1] Phantom "---" columns render the table malformed**

The column spec is `l cccc cccc` — eight data columns per group — but the 4th and 8th columns are headed `---` and every data cell in those positions also reads `---`. No note explains what these columns represent. A table submitted to a journal with literal `---` headers will fail copyediting unconditionally. Either:

- Populate them with real data (e.g., p-value of the cross-group difference, Min, or Max), or
- Remove them entirely and trim the spec to `l ccc ccc`.

---

**[MAJOR-T1-1] All row labels are raw database-variable names**

Every row uses an all-caps code identifier (`TIENE_BILLETERA`, `USA_BILLETERA`, `INTERNET_HOGAR`, `SMARTPHONE`, `POBREZA`, `INGRESO_PC`, `NIVEL_EDUCATIVO`). Journal style requires human-readable labels, e.g.:

| Code | Suggested label |
|---|---|
| `TIENE_BILLETERA` | Owns digital wallet |
| `USA_BILLETERA` | Uses digital wallet |
| `INTERNET_HOGAR` | Internet access at home |
| `SMARTPHONE` | Smartphone ownership |
| `POBREZA` | Poverty classification (SISFOH) |
| `INGRESO_PC` | Per capita income |
| `NIVEL_EDUCATIVO` | Education level |

---

**[MAJOR-T1-2] NIVEL_EDUCATIVO missing-observation gap not explained**

`NIVEL_EDUCATIVO` reports N = 13,793 (treated) and 92,826 (control) against group totals of 14,088 and 99,667. The ~295 treated and ~6,841 control missing observations are mentioned nowhere in the note or paper body. The table note must state the reason (e.g., "NIVEL_EDUCATIVO is missing for respondents who did not complete the education module; listwise deletion applied").

---

**[MAJOR-T1-3] INGRESO_PC values reported without units**

Mean values of 13,454 and 11,417 carry no currency, price-year, or frequency label. Specify in the row label or note: e.g., "Per capita income (monthly, 2024 PEN)" or "annual real soles."

---

**[MINOR-T1-1] Full-sample vs. estimation-sample comparison risks misreading**

Treated N = 14,088 and control N = 99,667 span the full dataset, while all causal estimates use the bandwidth-restricted sample (N = 27,809). The note does flag this, but consider adding a bracketed subtitle under the table title — e.g., "*Full sample (not bandwidth-restricted; estimation sample: N = 27,809 within h\* = 14.24)*" — so the distinction is visible before a reader reaches the note.

---

### Table 2 — Main Results

**[MAJOR-T2-1] Software package names used as method descriptors**

The `Method` row displays `rdrobust` and `statsmodels_WLS`. These are implementation names, not econometric descriptions. Replace with:
- `rdrobust` → "Local linear RD (rdrobust)"
- `statsmodels_WLS` → "Parametric WLS regression"

---

**[MAJOR-T2-2] Section-group headers contain underscores**

Row-group headings `baseline`, `with_covariates`, and `extended_covariates` are rendered verbatim with underscores. Typeset as: *Baseline*, *With covariates*, *Extended covariates* (italic or small-caps, matching journal house style). Underscores suggest the code label was inserted without editing.

---

**[MAJOR-T2-3] Unexplained "---" in the SISFOH heterogeneity panel, USA\_BILLETERA column**

All three SISFOH subgroup rows (extreme-poor, non-extreme-poor, non-poor) show `---` under `USA_BILLETERA`. It is unclear whether the analysis was not run, failed to converge, or is simply omitted for space. The table note must state: "Heterogeneity by SISFOH poverty classification was estimated for TIENE\_BILLETERA only; the subgroup samples are too small for a precise estimate of USA\_BILLETERA."  (Or supply the estimates if they exist.)

---

**[MINOR-T2-1] Absence of significance stars not declared**

Neither Table 2 nor any other table uses significance stars. This is a valid reporting choice, but it must be stated once — typically in the first results table note: "Significance thresholds are not starred; 95% confidence intervals are reported throughout." Without the declaration, production editors will query every results table.

---

### Table 3 — Robustness

**[CRITICAL-T3-1] Identical point estimates for H Half and H Optimal — suspected copy-paste error**

Panel A reports:

| Row | BW | N | Estimate |
|---|---|---|---|
| H Half | 7.12 | 14,803 | **−0.0056** |
| H Optimal | 14.24 | 27,809 | **−0.0056** |
| H Double | 28.48 | 50,989 | −0.0204 |

The bias-corrected point estimate from `rdrobust` at half-bandwidth (N = 14,803) being bit-for-bit identical to the estimate at full-bandwidth (N = 27,809) is nearly impossible in practice — local linear RD estimates change with sample composition. This overwhelmingly suggests the H Half row was copied from the H Optimal row. The SE and CI do differ (0.0221 vs. 0.0179; wider at smaller BW, which is directionally correct), but the estimate itself must be verified and corrected. **If Figure 2 (bandwidth sensitivity) displays these values, it must be regenerated after correction.**

---

**[MAJOR-T3-1] Bandwidth labels "H Half / H Optimal / H Double" are undefined**

"H" appears nowhere in the note or table header. Replace with notation that is self-defining: "0.5 × h\*", "h\* (baseline)", "2 × h\*" — or add to the note: "*H denotes the MSE-optimal bandwidth h\* = 14.24; Half and Double refer to 0.5h\* and 2h\*, respectively.*"

---

**[MAJOR-T3-2] Table 3 Panel D and Table 4 report the same covariate-balance test with different numbers — no explanation**

Both tables use pre-determined covariates as RD outcomes, but the specifications differ silently:

| | INTERNET\_HOGAR | SMARTPHONE |
|---|---|---|
| **Table 3 Panel D** | BW = 15.23, N = 29,668, SE = 0.0487, CI = [−0.0615, 0.1296] | BW = 14.29, N = 27,809, SE = 0.0246, CI = [−0.0218, 0.0748] |
| **Table 4** | BW = 14.24, N = 27,809, SE = 0.0489, CI = [−0.0607, 0.1308] | BW = 14.24, N = 27,809, SE = 0.0256, CI = [−0.0146, 0.0857] |

A referee encountering both tables will flag this as contradictory data unless it is explained. The most likely interpretation is that Table 3 Panel D uses each covariate's own MSE-optimal bandwidth, while Table 4 fixes the bandwidth at h\* = 14.24. Add to the Table 3 note: "*Panel D uses the covariate-specific MSE-optimal bandwidth; Table 4 reports the same test at the fixed baseline bandwidth h\* = 14.24.*" Add the mirror statement to Table 4.

---

**[MINOR-T3-1] Table note misleadingly says Donut ±0.5 "effectively coincides with the baseline"**

The note states: "*Donut ±0.5 effectively coincides with the baseline because EDAD is integer-valued.*" But the estimate shifts from −0.0056 (baseline) to −0.0001 (±0.5 donut) and N drops from 27,809 to 25,431 (a loss of 2,378 observations). This is not a coincidence; it removes everyone recorded at exactly age 65. Revise to: "*Because EDAD is recorded in integer years, the ±0.5-year donut is the smallest feasible exclusion window; it drops the 2,378 observations reported at exactly age 65.*"

---

### Table 4 — Covariate Balance

**[MINOR-T4-1] NIVEL\_EDUCATIVO N = 27,325 gap not noted**

All other covariates report N = 27,809. NIVEL\_EDUCATIVO reports N = 27,325 — 484 observations fewer. The note is silent on this. Add: "*NIVEL\_EDUCATIVO is missing for 484 observations within the estimation bandwidth.*"

---

**[MINOR-T4-2] Bandwidth distinction from Table 3 Panel D not stated**

As described in [MAJOR-T3-2] above, Table 4 should note explicitly that it uses the fixed h\* = 14.24 (not the covariate-specific optimal bandwidth used in Table 3 Panel D). One sentence in the note suffices.

---

## FIGURES

The figure files are binary (PNG/PDF) and could not be read programmatically. The following issues are flagged based on structural context and cross-referencing.

---

**[MAJOR-F1-1] Figure captions cannot be confirmed — main.tex body is absent from the submitted excerpt**

The `main.tex` provided is truncated: it ends at `\usepackage{threeparttable}` and then jumps directly into bibliography entries, with no `\begin{document}`, no `\begin{figure}` environments, and no `\caption{}` commands visible. It is therefore impossible to confirm that any figure has a caption. Production must verify that each figure environment includes:
- A complete, self-contained caption
- Identification of what is plotted (outcome, sample, bandwidth)
- The CI method (bias-corrected, robust)
- The data source

---

**[MAJOR-F1-2] Figure 1 (RD plot) — Round 2 logical-error correction not verifiable from submitted materials**

Round 2 flagged a direction inversion in the Figure 1 caption ("rates rise from approximately 4% at age 50 to a maximum of 11% near age 35"). The authors reportedly revised this, but the revised caption is not included in the materials submitted for Round 3. Confirm the corrected text reads consistently with the plotted data before accepting.

---

**[MAJOR-F1-3] figure\_mccrary\_density.png — in-text citation not confirmable**

A McCrary density-test figure exists but no `\begin{figure}` block referencing it appears in the truncated main.tex. Confirm: (a) it is assigned a figure number, (b) it is cited in the robustness section with a sentence reporting the test statistic and p-value, and (c) its caption states the null hypothesis being tested and whether it is rejected.

---

**[MINOR-F2-1] Figure 2 (bandwidth sensitivity) may need regeneration**

If [CRITICAL-T3-1] above confirms that the H Half estimate (−0.0056) is a copy-paste of the H Optimal estimate, any sensitivity plot that displays that value will also be wrong. Regenerate Figure 2 after the Table 3 Panel A correction.

---

## CROSS-TABLE CONSISTENCY

**[MINOR-X1] NIVEL\_EDUCATIVO missing-N pattern is internally consistent but undocumented across tables**

Table 1: 13,793 / 14,088 treated (missing 295); Table 4: 27,325 / 27,809 (missing 484). Both shortfalls are attributable to the same systemic missingness. Use identical phrasing in both table notes so the pattern reads as intentional and documented.

---

## SUMMARY COUNT

| Severity | Count | Location |
|---|---|---|
| CRITICAL | 2 | Table 1 (phantom columns), Table 3 (identical estimates) |
| MAJOR | 9 | Tables 1–3 × 3 each; Figure captions + in-text citations |
| MINOR | 6 | Tables 1–4; Figure 2 regeneration |

---

```json
{
  "n_critical": 2,
  "n_major": 9,
  "n_minor": 6,
  "tables_reviewed": 4,
  "figures_reviewed": 3,
  "top_issues": [
    "Table 3 Panel A: H Half and H Optimal point estimates are bit-for-bit identical (-0.0056) — near-certain copy-paste error requiring data verification and Figure 2 regeneration",
    "Table 1: Columns 4 and 8 are headed '---' with all cells reading '---' — phantom placeholder columns that will fail copyediting",
    "Table 3 Panel D and Table 4 both test covariate balance but report different estimates/bandwidths with no explanation — will be flagged as contradictory data by referees",
    "Table 1: All row labels are raw code names (TIENE_BILLETERA etc.) — must be replaced with human-readable descriptions before submission",
    "Table 2: Method labels 'rdrobust' and 'statsmodels_WLS' are software package names — replace with econometric descriptions",
    "main.tex body absent from submitted excerpt — figure captions cannot be verified; Round 2 Figure 1 correction unconfirmable"
  ]
}
```

---


## 6. Contribution Evaluation

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

---
