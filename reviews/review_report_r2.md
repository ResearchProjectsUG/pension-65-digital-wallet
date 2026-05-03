# Pre-Submission Referee Report (Round 2)

**Date**: 2026-05-02

**Target**: top-field

---


## 1. Spelling, Grammar & Style

## Copy-Editorial Review — Pensi\'on 65 / ENAHO 2024 RDD Paper

---

### CRITICAL Issues

**[CRITICAL-1] Logical contradiction in Figure 1 description (§5.5, Visual Evidence)**

> "rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."

Age 35 is *younger* than age 50. Rates cannot simultaneously *rise* from age 50 to age 35 **and** *decline monotonically with age.* The sentence appears to describe a downward-sloping age profile but has the direction inverted. Suggested replacement:

> "rates peak at approximately 11% near age 35 and decline monotonically with age, falling to approximately 4% near age 50 and continuing downward through the cutoff."

---

**[CRITICAL-2] Uncited bibliography entry**

The reference `\bibitem[Deming and Noray(2023)]{deming2023}` (Earnings Dynamics, Changing Job Skills, and STEM Careers, *QJE*) appears in the bibliography but is **never cited in the text**. Remove it or insert a citation. Publishing a paper with a phantom reference will prompt referee and production queries.

---

### MAJOR Issues

**[MAJOR-1] Style violation: "Importantly" (§5.1, Main Results, ¶2)**

> "**Importantly**, this covariate-adjusted specification uses a wider bandwidth..."

Per journal style guidelines, "importantly" must be deleted. Rephrase:

> "Note that this covariate-adjusted specification uses a wider bandwidth..."

---

**[MAJOR-2] British/American spelling inconsistency: "centred" vs. "centered"**

"Centred" appears twice (Introduction: "centred on zero"; §5.4: "centred near zero") while "centered" is used everywhere else (§5.1: "centered very close to zero"; equations: "centered running variable"). Standardize to **"centered"** throughout.

---

**[MAJOR-3] Wrong word choice: "Existing literature is insufficient" (§1, ¶5)**

> "Existing literature is insufficient on two fronts."

Literature is not "insufficient"; it is *limited* or *sparse*. Either replace with "Existing evidence is limited on two fronts" or "The literature falls short on two fronts." As written, the sentence implies the papers that do exist are not good enough, which is not the intended meaning.

---

**[MAJOR-4] Missing words: "estimate of institutional access on digital adoption" (§1, ¶2)**

> "…provides quasi-experimental variation suitable for an intent-to-treat (ITT) estimate of institutional access on digital adoption among the elderly poor."

Missing "the effect of." Should read:

> "…suitable for an intent-to-treat (ITT) estimate of **the effect of** institutional access on digital adoption among the elderly poor."

---

**[MAJOR-5] Bibliography year inconsistency — Banerjee et al.**

```
\bibitem[Banerjee et~al.2019]{banerjee2020}
Banerjee, A., Niehaus, P., and Suri, T. (2020).
Universal Basic Income in the Developing World.
Annual Review of Economics, 11:959--983.
```

The bibitem *label* says 2019; the inline citation reads "(2020)"; the citation key is `banerjee2020`. *Annual Review of Economics* Volume 11 was published in 2019. Resolve: if the year of publication is 2019, correct the inline date to `(2019)`, rename the key to `banerjee2019`, and update all `\citep{banerjee2020}` calls. Also add parentheses around the year: `\bibitem[Banerjee et~al.(2019)]{banerjee2019}`.

---

**[MAJOR-6] Structural breakdown in Limitations (§6.2)**

The section opens with "Five limitations bear emphasis" and provides bold headers for only two (Integer running variable; Dual eligibility). The remaining three limitations are introduced mid-paragraph with "First, our estimates capture…", "Second, our cross-sectional design…", "Third, the population-level null…" — but there is no bold header introducing them as a group, and the numbering is embedded inside the Dual Eligibility paragraph. This makes it appear that the numbered items are sub-points of Dual Eligibility, not standalone limitations. Either add a third bold header (e.g., **Additional limitations**) before "First, our estimates capture…", or restructure all five into a numbered list with consistent formatting.

---

**[MAJOR-7] Ambiguous/awkward abstract sentence**

> "We interpret these intent-to-treat estimates as the combined effect of crossing the institutional threshold associated with Pensi\'on 65 and other age-65-specific changes **on the running variable**."

"Changes on the running variable" is opaque — the running variable is age, not something that can have changes on it. Likely intended:

> "…and other institutional or behavioral changes associated with crossing age 65."

---

### MINOR Issues

**[MINOR-1] "move the dial" — mixed idiom (§5.4)**

> "institutional eligibility does not move the dial on digital adoption"

The standard idiom is "move the **needle**." Replace accordingly.

**[MINOR-2] Missing comma before "while" (§3.3, Outcomes)**

> "(the respondent has installed and registered for a wallet) while active use reflects behavioral integration"

Add comma: "…registered for a wallet)**,** while active use reflects…"

**[MINOR-3] Missing comma after "receipt" (§5.4)**

> "without administrative data on Pensi\'on 65 receipt we cannot bound take-up directly"

Insert comma: "…on Pensi\'on 65 receipt**,** we cannot bound take-up directly."

**[MINOR-4] Redundant phrase: "on the age dimension" (§1, ¶2)**

> "The age-65 eligibility threshold is administratively sharp on the age dimension."

An age threshold is by definition on the age dimension. Delete "on the age dimension."

**[MINOR-5] Double "first" (§1, contributions paragraph)**

> "This paper makes three contributions. **First**, it provides the **first** regression-discontinuity evaluation…"

Rephrase one instance: "This paper makes three contributions. First, it provides the **only** regression-discontinuity evaluation…" or invert the sentence structure.

**[MINOR-6] Non-parallel list in Conclusion future directions**

> "(i) merging Pensi\'on 65 administrative data… (ii) panel data tracking the same individuals… (iii) evaluation of complementary policies…"

Items (i) uses a gerund phrase; (ii) and (iii) use noun phrases. Standardize to gerunds:

> "(i) merging… (ii) tracking the same individuals over time… (iii) evaluating complementary policies…"

**[MINOR-7] Bibliography: missing parentheses around year, Ardington et al.**

`\bibitem[Ardington et~al.2016]{ardington2016}` → `\bibitem[Ardington et~al.(2016)]{ardington2016}`

**[MINOR-8] "restricting to extreme-poor" missing article (§6.2)**

> "Section~\ref{sec:extreme_poor} addresses this by restricting to extreme-poor"

Add article or noun: "restricting to **the** extreme-poor" or "restricting to extreme-poor **individuals**."

**[MINOR-9] "policy attention on the elderly poor population" (§6.3)**

> "policy attention on the elderly poor population should focus on…"

Rephrase: "policy attention **for** the elderly poor" or "policy **aimed at** the elderly poor."

**[MINOR-10] Awkward abstract phrasing: "institutional channels for transfer digitization"**

> "institutional channels for transfer digitization being insufficient, on their own, to overcome the age gradient"

Consider: "**the** institutional **channel** for transfer digitization **is** insufficient, on its own, to overcome…" (singular is more precise — the specific channel here is Pensi\'on 65's Cuenta DNI pathway).

---

### Summary Table

| Section | Issue | Tag |
|---|---|---|
| §5.5 Visual Evidence | Age direction logically inverted in Fig. 1 description | [CRITICAL] |
| Bibliography | Deming & Noray (2023) cited in references but never in text | [CRITICAL] |
| §5.1 Main Results | "Importantly" — forbidden hedge word | [MAJOR] |
| Throughout | "centred" (British) vs. "centered" (American) inconsistency | [MAJOR] |
| §1 Introduction | "Existing literature is insufficient" — wrong word | [MAJOR] |
| §1 Introduction | "estimate of institutional access on digital adoption" — missing "the effect of" | [MAJOR] |
| Bibliography | Banerjee et al.: year 2019 vs. 2020 conflict; missing parentheses | [MAJOR] |
| §6.2 Limitations | Five limitations announced; only two have bold headers; three embedded mid-paragraph | [MAJOR] |
| Abstract | "other age-65-specific changes on the running variable" — ambiguous | [MAJOR] |
| §5.4 Heterogeneous Effects | "move the dial" → "move the needle" | [MINOR] |
| §3.3 Outcomes | Missing comma before "while" | [MINOR] |
| §5.4 Extreme-Poor | Missing comma after "receipt" | [MINOR] |
| §1 Introduction | "on the age dimension" — redundant | [MINOR] |
| §1 Introduction | Double "first" in contributions paragraph | [MINOR] |
| §7 Conclusion | Non-parallel future-directions list | [MINOR] |
| Bibliography | Ardington et al. bibitem missing parentheses around year | [MINOR] |
| §6.2 Limitations | "restricting to extreme-poor" — missing article/noun | [MINOR] |
| §6.3 Policy | "policy attention on" — wrong preposition | [MINOR] |
| Abstract | "institutional channels for transfer digitization" — awkward plural | [MINOR] |

---

```json
{
  "n_critical": 2,
  "n_major": 7,
  "n_minor": 10,
  "top_issues": [
    "CRITICAL: Fig. 1 description states rates 'rise from age 50 to age 35' — logically inverted; age 35 is younger than 50, contradicting the stated monotone decline.",
    "CRITICAL: Deming & Noray (2023) appears in the bibliography but is never cited in the text — phantom reference must be removed.",
    "MAJOR: 'Importantly' in §5.1 (Main Results, ¶2) violates journal style — delete or rephrase.",
    "MAJOR: 'centred' (British) vs. 'centered' (American) used inconsistently — standardize to 'centered' throughout.",
    "MAJOR: Banerjee et al. bibliography entry carries year label '2019' but citation key and inline date say '2020' — resolve year before submission.",
    "MAJOR: §6.2 Limitations announces five limitations but only two have bold headers; the remaining three are embedded mid-paragraph under 'Dual eligibility' with confusing 'First/Second/Third' numbering.",
    "MAJOR: 'Existing literature is insufficient on two fronts' (§1) — literature is not 'insufficient'; use 'limited' or 'sparse.'"
  ]
}
```

---


## 2. Internal Consistency & Cross-References

## Internal Coherence Review

Working through each layer systematically — abstract → body, text → tables, table-to-table, and bibliography.

---

### [CRITICAL] #1 — SE/CI contradiction between Table 2 and Table 3 Panel A for the identical specification

The local-linear baseline for `TIENE_BILLETERA` (rdrobust, BW = 14.24) appears in **two tables with different standard errors and confidence intervals**:

| Source | Estimate | SE | 95% CI |
|---|---|---|---|
| Table 2, *baseline* | −0.0056 | 0.0165 | [−0.0336, 0.0310] |
| Table 3, Panel A *H Optimal* | −0.0056 | **0.0179** | **[−0.0397, 0.0306]** |

Same point estimate, same bandwidth, same N (27,809) — but the SE differs by ~8% and the CI is materially wider in the robustness table. A reader comparing the two tables will notice the inconsistency immediately. The likely cause is that Table 2 reports the conventional SE while Table 3 reports the robust-bias-corrected SE (or vice versa), but the paper never documents this distinction. The text narrates only one set of numbers (SE = 0.016, CI [−0.034, 0.031]) and treats them as unambiguous.

---

### [CRITICAL] #2 — Donut-hole specs produce identical output (coding error)

Table 3, Panel B:

| Spec | Estimate | SE | 95% CI | BW | N |
|---|---|---|---|---|---|
| Donut ±0.5 | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |
| Donut ±1.0 | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |

Every reported number is **identical**. By construction, excluding ±1 year removes more observations than excluding ±0.5, so N, BW, and the estimate cannot all be the same. This is a clear copy-paste or output-overwrite bug in the analysis code. The text (Sec. 4.2) treats these as two distinct results: *"Donut-hole specifications excluding observations within ±0.5 and ±1.0 years of the cutoff yield estimates of −0.001, removing the small negative point estimate entirely"* — but a reader cannot distinguish the two.

---

### [MAJOR] #1 — Banerjee et al. bibliography: year mismatch within the same entry

```latex
\bibitem[Banerjee et~al.2019]{banerjee2020}
Banerjee, A., Niehaus, P., and Suri, T. (2020).
```

The natbib label (`2019`) and the reference body text (`2020`) conflict. The Annual Review of Economics paper by Banerjee, Niehaus, and Suri (*Universal Basic Income in the Developing World*) was published in AER Vol. 11, **2019** — so the label year is correct and the body text is wrong. In-text citations (`\citet{banerjee2020}`) will render as "Banerjee et al. 2019" while the reference list says "(2020)" — a contradiction visible to any referee who checks the bibliography.

---

### [MAJOR] #2 — Ardington et al. bibliography: year and volume are wrong

```latex
\bibitem[Ardington et~al.2016]{ardington2016}
Ardington, C., Case, A., and Hosegood, V. (2016).
Labor Supply Responses to Large Social Transfers...
American Economic Journal: Applied Economics, 8(1):22--48.
```

The Ardington–Case–Hosegood paper on South African social transfers and labor supply was published in *AEJ: Applied Economics* **Vol. 1(1), 2009**, not Vol. 8(1), 2016. The volume number 8(1) corresponds to January **2016**, which is ~7 years off. The citation key (`ardington2016`), the label year, the body year, and the volume are all wrong relative to the actual publication.

---

### [MAJOR] #3 — Galiani et al. (2020) described contradictorily in two sections

- **Sec. 2.1:** *"\citet{galiani2020} find positive but heterogeneous effects of conditional cash transfer digitization on financial behavior in Argentina."*
- **Sec. 2.3:** *"A closely related application is \citet{galiani2020}, who use a digitization-of-transfers context in Argentina and document **weak downstream behavioral effects** of forced account openings on saving and active financial behavior."*

"Positive but heterogeneous effects" and "weak downstream behavioral effects" are not the same characterization. A reader will see the same paper described in opposite terms within three pages. One of these is either inaccurate or needs to be scoped (e.g., positive effects on transaction frequency but weak effects on saving).

---

### [MAJOR] #4 — Population means (7.4%, 15.6%) appear inconsistent with Table 1 and the data audit flags no weights

Sec. 3.3 states:

> `TIENE_BILLETERA` population mean: **7.4%**
> `USA_BILLETERA` population mean: **15.6%**

Cross-checking against Table 1 (unweighted):
- `TIENE_BILLETERA`: (14,088 × 0.0535 + 99,667 × 0.0800) / 113,755 ≈ **7.7%**
- `USA_BILLETERA`: (14,088 × 0.0319 + 99,667 × 0.1794) / 113,755 ≈ **16.1%**

The paper labels these as "population means," implying survey-weighted estimates. But the **data audit explicitly flags**: *"No survey weight column found. Results may not be population-representative."* If the weight column (`FACTOR_EXPANSION`) was not used, the "population means" cited in the text are just unweighted sample means — and even those don't match (7.7% ≠ 7.4%, 16.1% ≠ 15.6%). The discrepancy is not large enough to alter conclusions, but the labeling is inconsistent with the audit finding.

---

### [MINOR] #1 — "Baseline mean" of S/11,700 for per-capita income doesn't match Table 1

Sec. 4.3: *"the jump in per-capita income is −S/47 on a baseline mean of S/11,700"*

Table 1 shows:
- Below-threshold (control group) mean: **S/11,416**
- Above-threshold mean: S/13,454
- Sample overall: ≈ S/11,667

In RDD convention, "baseline mean" refers to the control group (below cutoff). S/11,700 ≠ S/11,416. The value S/11,667 (overall sample mean) is closer, but that's not what "baseline" means in this context. A referee checking Table 1 will notice the mismatch.

---

### [MINOR] #2 — Orphan bibliography entry: Deming and Noray (2023) never cited in text

```latex
\bibitem[Deming and Noray(2023)]{deming2023}
Deming, D.~J. and Noray, K. (2023).
Earnings Dynamics, Changing Job Skills, and STEM Careers.
```

This reference appears nowhere in the main text. It is boilerplate from a prior template (consistent with the code review's finding that "template artifacts from an electoral RDD study survived into the output scripts").

---

### [MINOR] #3 — CI described as symmetric ±3.4 pp when it is not

Sec. 4.1: *"the confidence interval is narrow enough to rule out moderately sized effects (the interval excludes effects larger than ±3.4 percentage points)"*

The CI is [−0.034, **0.031**] — the upper bound is **3.1 pp**, not 3.4. The interval is asymmetric; describing it as ±3.4 overstates the upper bound by 0.3 pp. Minor but imprecise.

---

### [MINOR] #4 — Figure 1 description is confusingly phrased

Sec. 4.6: *"rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age"*

This describes rates *increasing* as age *decreases* (from 50 to 35), using the word "rise." The direction of movement (older→younger) is the opposite of the usual age-gradient description. The sentence is not wrong, but it reads as if rates rise as people age from 35 to 50, which is the opposite of what is meant. It should read something like: *"rates peak at approximately 11% near age 35 and decline monotonically with age, reaching approximately 4% by age 50."*

---

### [MINOR] #5 — Duplicate LaTeX labels between outer table environments and included files

`main.tex` defines `\label{tab:main}` in the outer `table` float, then `\input{tables/table_2_main_results.tex}` which internally defines `\label{tab:main_results}`. Same conflict for `tab:balance` vs. `tab:cov_balance` in Table 4. LaTeX will emit multiply-defined label warnings; the outer label wins, so cross-references resolve correctly — but the internal labels in the included files are dead. A clean compile will produce warnings that may alarm co-authors or journal production staff.

---

### Summary

| Severity | Count | Key issues |
|---|---|---|
| CRITICAL | 2 | SE/CI contradiction between Tables 2 and 3 for the identical specification; donut-hole results are identical for ±0.5 and ±1.0 (coding error) |
| MAJOR | 4 | Banerjee bib year mismatch (2019 label vs. 2020 text); Ardington bib year and volume wrong (~7 years off); Galiani (2020) described as "positive" in one section and "weak" in another; population means inconsistent with Table 1 and data audit flags no weights |
| MINOR | 5 | S/11,700 baseline income ≠ S/11,416 control mean; orphan Deming & Noray reference; CI described as ±3.4 pp when upper bound is 3.1 pp; Figure 1 description reads backwards; duplicate LaTeX labels |

```json
{
  "n_critical": 2,
  "n_major": 4,
  "n_minor": 5,
  "top_issues": [
    "Donut-hole ±0.5 and ±1.0 produce byte-for-byte identical rows in Table 3 — coding error, one spec was not actually run",
    "Local-linear baseline SE and CI differ between Table 2 (SE=0.0165, CI=[−0.034, 0.031]) and Table 3 H-Optimal row (SE=0.0179, CI=[−0.040, 0.031]) for the same specification and bandwidth",
    "Banerjee et al. bibitem label says '2019', body text says '2020', citation key is banerjee2020 — year is inconsistent within the entry and the paper is cited as 2020 in-text throughout"
  ]
}
```

---


## 3. Unsupported Claims & Identification Integrity

# Claim Discipline Audit: Digital Wallet Adoption RDD Paper

---

## [CRITICAL] Issues

---

### CRITICAL-1: Survey weights absent despite population-representative inference claims

The paper states: *"Population-level inference is carried out with the official expansion factor (FACPOB07, renamed FACTOR\_EXPANSION in our cleaned file)"* (§3.1), and reports "population mean: 7.4%" for `TIENE_BILLETERA`.

The data audit explicitly flags: **"No survey weight column found. Results may not be population-representative."**

These are irreconcilable. If `FACTOR_EXPANSION` was dropped during cleaning, every standard error, mean, and population-level claim in the paper rests on unweighted counts from a complex stratified design. The paper never acknowledges this discrepancy, and all references to "population" estimates should be qualified as "sample" estimates until resolved.

---

### CRITICAL-2: Statistically significant placebo result dismissed without valid justification

The paper states: *"Both placebos are economically negligible and consistent with the absence of a discontinuity specific to age 65"* (§4.2).

Table 3 (Panel D) shows the first placebo cutoff (TIENE\_BILLETERA, BW=7.41, N=99,667) has **CI [−0.0083, −0.0062]**, which excludes zero. This is a **statistically significant discontinuity at the placebo cutoff** — the opposite of what the paper claims.

The paper's explanation — *"The left placebo's tight confidence interval reflects an artificially small standard error driven by the placebo using a far-from-cutoff window where there is little local variation"* — is **logically inverted**: scarcity of local variation produces wider, not narrower, standard errors. A valid justification for dismissing this result is never provided. A significant placebo is a direct threat to the RDD validity assumption, and the paper's dismissal is unsubstantiated.

---

### CRITICAL-3: Invalid WLS confidence intervals reported as primary evidence

The paper acknowledges: *"the t-statistic computed in the asymptotic covariate-adjusted WLS specification (t≈−5.1, computed as −0.027/0.005) would suggest rejection at any conventional level, but the randomization p-value reflects the actual permutation distribution"* (§4.1) and identifies the asymptotic SE as wrong due to discrete mass-points.

Despite this, the CI [−0.037, −0.017] derived from that SE appears in **Table 2**, the **abstract**, and the **discussion**. An SE the paper itself characterizes as incorrect has no business anchoring confidence intervals that are then presented to readers. The paper should either report the randomization-inference-compatible interval or explicitly mark the WLS CI as unreliable — not present it as primary output.

---

### CRITICAL-4: Duplicate donut-hole estimates presented as independent robustness checks

Table 3, Panel B:

| Donut | Estimate | SE | CI | BW | N |
|---|---|---|---|---|---|
| 0.5 yr | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |
| 1.0 yr | −0.0014 | 0.0213 | [−0.0388, 0.0449] | 10.65 | 19,434 |

**Six significant figures identical across two nominally different specifications.** Two distinct exclusion windows cannot produce identical bandwidths, sample sizes, SEs, and point estimates unless the code executed the same specification twice. The paper treats these as two independent robustness data points; they are almost certainly a single result counted twice, inflating the apparent robustness evidence.

---

### CRITICAL-5: McCrary density test result potentially never computed (API extraction bug)

The code review flags that p-value extraction uses `rd_den.p`, but the `rddensity` Python package stores test results in `.test` (a dict), not a `.p` attribute. If `.p` does not exist, the result silently becomes `NaN`.

The paper reports a test statistic of 2.0 and concludes no manipulation. If the statistic was read from a NaN-valued attribute — or if 2.0 is the *statistic* rather than the *p-value*, as a z-statistic of 2.0 would imply marginal rejection at α=0.05 — the no-manipulation assumption is unvalidated. The paper provides no p-value for this test, only the statistic.

---

## [MAJOR] Issues

---

### MAJOR-1: "LATE" label applied to an ITT reduced-form estimand

Section 4.1 states: *"The estimand is the local average treatment effect (LATE) of crossing the eligibility threshold"* and labels equation (1) accordingly.

This is an ITT (reduced-form) RDD estimate, not a LATE in the IV/Wald sense. The paper acknowledges this explicitly elsewhere — *"We do not claim to identify a sharp local average treatment effect on actual program compliers"* — but then uses "LATE" in the formal identification section. LATE has a precise meaning (Wald estimand on compliers) that this paper does not deliver. The methods section should consistently use "ITT" or "intent-to-treat effect at the cutoff."

---

### MAJOR-2: "Sharp RDD" throughout despite acknowledged fuzzy treatment

The abstract, title, and Section 4 heading all call this a **"sharp regression discontinuity."** The paper simultaneously acknowledges: (a) only ~22.5% of age-65 individuals satisfy both eligibility criteria (age + SISFOH); (b) take-up among the jointly eligible is ~75%; (c) *"the design we exploit is best characterized as an intent-to-treat (ITT) RDD."*

The running variable has a sharp cutoff; the treatment probability does not jump from 0 to 1. This is a **fuzzy design** estimated as a reduced form. Calling it "sharp" throughout obscures the core identification limitation. The appropriate label is "fuzzy RDD, estimated as ITT."

---

### MAJOR-3: Extreme-poor subsample effect described as "moderate" when it implies ~114% relative increase

Section 4.4: *"the confidence interval covers zero and the magnitude is moderate (+2.5 percentage points on a baseline rate of approximately 2.2%)."*

A 2.5 pp effect on a 2.2% baseline is a **~114% relative increase** — roughly a doubling of the outcome in the target population. Describing this as "moderate" suppresses information about economic significance. The paper correctly notes the CI covers zero, but mischaracterizes the point estimate's economic scale. The relative-effect framing matters here precisely because this is the relevant population for the policy question.

---

### MAJOR-4: Randomization inference procedure is non-standard for RDD and target specification is ambiguous

The paper describes permuting *treatment assignment* within the age window [55, 75]. Standard Fisher randomization inference for RDD either (a) shifts the cutoff to placebo locations or (b) randomly assigns treatment to individuals within the local bandwidth, preserving local density. Permuting treatment within a 20-year window destroys the local identification structure of the estimand and is not a standard test of the RDD null.

Additionally, the paper conflates two non-equivalent uses of p=0.434: if the permutation test was run on the rdrobust specification (where t≈−0.37), the p-value is unremarkable and there is no "apparent inconsistency." If run on the WLS specification (where t≈−5.1), the contradiction implies the WLS SE is off by nearly an order of magnitude. The paper presents this as one number without specifying which specification it tests.

---

### MAJOR-5: Abstract presents covariate-adjusted estimate alongside baseline without disclosing different bandwidth

The abstract reports: *"Estimates with predetermined covariates yield a small negative effect on ownership (−0.027, SE=0.005)"* immediately after the baseline estimate of −0.006. The abstract does not mention that the covariate-adjusted specification uses bandwidth h=34.2 versus the optimal h*=14.2 — a 2.4× difference. The paper acknowledges in Section 4.1 that these "reflect a different identification window" and "should not be interpreted as variance reduction holding bandwidth constant." Readers of the abstract receive no such warning and will naturally compare the two estimates as if they estimate the same local quantity.

---

### MAJOR-6: Causal policy prescription from null ITT cross-section

The conclusion states: *"institutional digitization of government transfers, on its own, is an insufficient lever for moving vulnerable populations into active digital wallet use"* and *"policy attention on the elderly poor population should focus on the underlying determinants of digital adoption."*

A null ITT result in a cross-sectional survey is consistent with at minimum four mechanisms: (a) truly no effect, (b) effect diluted by low take-up (~22.5% × 75% ≈ 17% compliance rate), (c) effect present only for long-run enrollees undetectable in one cross-section, (d) cohort confounding at the cutoff. The paper acknowledges all four in Section 5.2 but abandons them in the conclusion and reaches actionable causal policy prescriptions (*"pair the institutional channel with behavioral-change components"*) that go beyond what an ITT null on one cross-section can support.

---

## [MINOR] Issues

---

### MINOR-1: "First" contribution claims unverified

Three claims of priority — *"first regression-discontinuity evaluation,"* *"first sharply-identified evidence,"* *"first wave to include digital wallets"* — are asserted without supporting citations. The paper discloses in the acknowledgment footnote that it was autonomously generated, which further reduces confidence in literature priority screening.

---

### MINOR-2: RD plot description internally inconsistent

Section 4.5: *"rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."* A profile with a peak at age 35 cannot decline **monotonically** with age (it must rise from younger ages to reach that peak). The description is contradictory and the age-profile narration (reading from age 50 to 35) is nonstandard.

---

### MINOR-3: WLS fallback due to memory failure presented as methodological parity

Section 4.1 acknowledges the WLS specification was used because *"the local-polynomial rdrobust routine encountered memory limitations."* A computational fallback is not a methodological choice. Presenting WLS alongside rdrobust as two primary specifications implies they are comparably designed; one is the appropriate estimator and the other is a workaround with a different bandwidth and demonstrably wrong asymptotic SEs.

---

### MINOR-4: 25 clusters insufficient for asymptotic cluster-robust SEs, not flagged

The WLS specifications cluster at the department level (25 clusters). The econometrics literature is clear that simple cluster-robust SEs are downward-biased with fewer than ~30 clusters; CR2 or wild-bootstrap corrections are recommended. This limitation is not mentioned.

---

### MINOR-5: "Precisely estimated null" framing relative to base rate

The paper calls results *"tightly bounded"* and *"precisely estimated."* The 95% CI for ownership is [−0.034, 0.031], a width of 6.5 pp around a 7.4% baseline. This rules out effects larger than ±3.4 pp — i.e., a true positive effect of 46% relative size would still lie within the CI. Whether this constitutes precision depends on the policy-relevant minimum detectable effect size, which the paper never motivates.

---

### MINOR-6: Active-use outcome is degenerate zeros in the policy-relevant subpopulation — finding underreported

Section 4.4 notes *"no extreme-poor individual aged 65–75 in our sample reports active wallet use"* in passing, as a technical issue with inference. This is itself a substantive finding: the primary policy-relevant population (elderly extreme-poor) does not use digital wallets actively in the data at all. This should be elevated as a standalone result, not buried as a caveat to degenerate inference.

---

## Summary

```json
{
  "n_critical": 5,
  "n_major": 6,
  "n_minor": 6,
  "causal_overclaiming": [
    "These findings imply that institutional digitization of government transfers, on its own, is an insufficient lever for moving vulnerable populations into active digital wallet use.",
    "The well-documented age gradient in technology adoption appears to dominate any program-specific effect; if Pensión 65 has a positive impact on digital behavior, it is overwhelmed at the population level by underlying cohort differences in digital literacy and smartphone access.",
    "institutional digitization works best when paired with explicit digital-literacy support, smartphone-access subsidies, or in-person enrollment assistance, rather than as a stand-alone lever.",
    "policy attention on the elderly poor population should focus on the underlying determinants of digital adoption---smartphone ownership, internet access, digital literacy training---rather than on institutional accounts alone.",
    "Both placebos are economically negligible and consistent with the absence of a discontinuity specific to age 65."
  ],
  "missing_caveats": [
    "Survey expansion weights are absent from the cleaned data despite claims of population-representative inference; all population-level descriptive statistics are unvalidated.",
    "The first placebo cutoff (age 15) produces a CI that excludes zero; the paper dismisses this with a logically inverted explanation and never addresses the threat to RDD validity.",
    "The WLS confidence intervals [-0.037, -0.017] rest on an SE the paper identifies as incorrect; these intervals should not be reported as valid.",
    "The donut-hole robustness checks at 0.5 and 1.0 years produce identical estimates, SEs, and sample sizes, suggesting a coding error rather than two independent checks.",
    "With ~22.5% joint eligibility and ~75% take-up, the ITT dilutes the effect on compliers by a factor of approximately 0.17; no Lee-Bound or first-stage scaling is provided to bracket the complier effect.",
    "No extreme-poor individual aged 65-75 in the sample actively uses a digital wallet; the active-use outcome is uninformative for the target population and should be reported as a substantive finding, not a technical footnote.",
    "The McCrary density test p-value is potentially NaN due to a confirmed API extraction bug in the code; the no-manipulation assumption may be empirically untested.",
    "The cohort-versus-age confound is acknowledged only in the limitations section; the local-linear estimator attenuates but cannot eliminate this threat and it should be central to the identification discussion."
  ]
}
```

---


## 4. Mathematics, Equations & Notation

## Formal Review: Mathematical and Notation Analysis

---

### 1. Mathematical Correctness

**Equation (1) — LATE estimand**

$$\tau = \lim_{a \downarrow 65} E[Y \mid A = a] - \lim_{a \uparrow 65} E[Y \mid A = a]$$

Direction is correct: right limit minus left limit. Standard sharp-RDD estimand. ✓

**Equation (2) — Local-linear baseline**

$$Y_i = \alpha + \tau D_i + \beta_1 (A_i - 65) + \beta_2 D_i (A_i - 65) + \varepsilon_i$$

Correct: the $\beta_2 D_i(A_i - 65)$ term allows separate slopes on each side. ✓

---

### 2. Equation (3) — Missing slope interaction [MAJOR]

The covariate-adjusted specification is written:

$$Y_i = \alpha + \tau D_i + g(A_i - 65) + \mathbf{X}_i' \boldsymbol{\gamma} + \varepsilon_i$$

The polynomial $g(A_i - 65)$ is a **single function** of the running variable, forcing the same slope on both sides of the cutoff. Equation (2) explicitly allows separate slopes via the $D_i(A_i-65)$ interaction. Standard RDD practice — and specifically the Calonico et al. (2014) method cited — fits separate polynomials on each side. The correct specification should be $g(A_i - 65, D_i)$ or equivalently include $D_i \cdot p(A_i - 65)$ terms. As written, Equation (3) is inconsistent with Equation (2) and with the cited methodology.

---

### 3. Arithmetic Error in Explicit Computation [MAJOR]

Section 5.1 states:

> "the $t$-statistic computed in the asymptotic covariate-adjusted WLS specification ($t \approx -5.1$, computed as $-0.027/0.005$)"

$$\frac{-0.027}{0.005} = -5.4 \neq -5.1$$

The paper explicitly derives the value inline, making this a verifiable arithmetic error, not a rounding issue. The correct value is $-5.4$.

---

### 4. Inconsistent Characterization of Galiani et al. (2020) [MAJOR]

The same paper is described differently in two places:

- **Introduction**: "find positive but heterogeneous effects of conditional cash transfer digitization on financial behavior in Argentina"
- **Section 2.3**: "document weak downstream behavioral effects of forced account openings on saving and active financial behavior"

"Positive" and "weak downstream" are contradictory characterizations. A reader using either passage to set priors about the literature will receive conflicting signals. One of these must be corrected or reconciled.

---

### 5. Orphan Bibliography Entry [MAJOR]

The bibliography contains:

```latex
\bibitem[Deming and Noray(2023)]{deming2023}
Deming, D.~J. and Noray, K. (2023). Earnings Dynamics...
```

The key `deming2023` is never cited anywhere in the text. This is an uncleaned entry from a prior draft. Beyond aesthetics, it inflates the apparent literature engagement and may trigger questions from referees.

---

### 6. Banerjee bibitem Label–Year Mismatch [MAJOR]

```latex
\bibitem[Banerjee et~al.2019]{banerjee2020}
Banerjee, A., Niehaus, P., and Suri, T. (2020). ...
```

The natbib label in brackets reads `2019`; the bibliography text says `(2020)`; the key is `banerjee2020`. When rendered, `\citet{banerjee2020}` will display "Banerjee et al.2019" while the bibliography entry says 2020. The in-text citation and bibliography will visibly disagree. Compare with the correctly formatted `\bibitem[Bachas et~al.(2018)]{bachas2018}`.

---

### 7. Undefined Notation: Potential Outcomes [MINOR]

The identifying assumptions (Section 4.1) introduce $Y(0)$ and $Y(1)$:

> "$E[Y(0) \mid A = a]$ and $E[Y(1) \mid A = a]$ are continuous..."

These potential outcome random variables are never defined. Given that the estimand in Equation (1) uses $Y$ (not $Y(0), Y(1)$), a brief definition — e.g., "where $Y(d)$ denotes the potential outcome under treatment status $d \in \{0,1\}$" — is needed before first use.

---

### 8. Bandwidth Arithmetic Discrepancy [MINOR]

Section 5.2 states: "$h^*/2 = 7.1$, $h^* = 14.2$, and $2h^* = 28.5$"

$$2 \times 14.2 = 28.4 \neq 28.5$$

Consistent with $h^* = 14.25$ (unrounded), but since the paper reports $h^* = 14.2$, the double-bandwidth should be stated as 28.4.

---

### 9. bibitem Format Inconsistency [MINOR]

The natbib manual specifies `\bibitem[short(year)]{key}` for author-year mode. Several entries are missing parentheses around the year:

- `\bibitem[Ardington et~al.2016]{ardington2016}` — should be `[Ardington et~al.(2016)]`
- `\bibitem[Banerjee et~al.2019]{banerjee2020}` — see issue #6 above

Compare correctly formatted entries: `[Bachas et~al.(2018)]`, `[Battistin et~al.(2009)]`. Inconsistent formatting may cause natbib to render citations differently across entries.

---

### 10. Cohen's *d* Slight Discrepancy [MINOR]

The paper reports Cohen's $d = -0.021$. For a binary outcome with population mean $\bar{p} = 0.074$:

$$\text{SD} = \sqrt{0.074 \times 0.926} \approx 0.262, \quad d = \frac{-0.006}{0.262} \approx -0.023$$

The reported value of $-0.021$ could use a slightly different SD (e.g., the within-bandwidth SD rather than the population SD), but the computation basis is not stated.

---

### 11. Figure 1 Caption — Directional Confusion [MINOR]

Section 5.5 writes: "rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."

The phrase "rise from age 50 to age 35" describes movement in the direction of *decreasing* age, which is non-standard in time-series or cross-sectional description. A clearer formulation: "ownership rates peak at approximately 11% near age 35 and decline monotonically with age, reaching approximately 4% by age 50." The current wording also places the global maximum at age 35 — unusual for a figure nominally centered on the age-65 cutoff; clarify whether the RD plot spans ages 35–75 or a narrower window.

---

## Summary Table

| # | Issue | Location | Severity |
|---|-------|----------|----------|
| 1 | Equation (3) missing $D_i$ interaction in polynomial | §4.2, Eq. (3) | **MAJOR** |
| 2 | Arithmetic: $-0.027/0.005 = -5.4$, not $-5.1$ | §5.1 | **MAJOR** |
| 3 | Contradictory descriptions of Galiani et al. (2020) | Intro vs. §2.3 | **MAJOR** |
| 4 | Orphan bibitem `deming2023` never cited | Bibliography | **MAJOR** |
| 5 | Banerjee bibitem label `2019` conflicts with text `2020` | Bibliography | **MAJOR** |
| 6 | $Y(0), Y(1)$ undefined before first use | §4.1 | MINOR |
| 7 | $2h^* = 28.4$, reported as $28.5$ | §5.2 | MINOR |
| 8 | Inconsistent `\bibitem` year formatting (missing parentheses) | Bibliography | MINOR |
| 9 | Cohen's $d$ basis unstated; computed value slightly off | §5.1 | MINOR |
| 10 | Figure 1 directional description confusing | §5.5 | MINOR |

---

```json
{
  "n_critical": 0,
  "n_major": 5,
  "n_minor": 5,
  "top_issues": [
    "Arithmetic error: paper explicitly states 't ≈ -5.1, computed as -0.027/0.005' but -0.027/0.005 = -5.4",
    "Equation (3) omits D_i interaction with the polynomial g(·), forcing equal slopes on both sides — inconsistent with Eq. (2) and with rdrobust methodology",
    "Galiani et al. (2020) characterized as 'positive but heterogeneous effects' in the Introduction and 'weak downstream behavioral effects' in Section 2.3 — directly contradictory",
    "Orphan bibitem 'deming2023' (Deming and Noray 2023) appears in the bibliography but is never cited in the text",
    "Banerjee et al. bibitem label reads '2019' while the bibliography entry and citation key say '2020', causing natbib to render conflicting years"
  ]
}
```

---


## 5. Tables, Figures & Documentation

The full table source was already provided in the prompt. I have everything needed for a complete review. Here it is.

---

## Production Editor Review: Tables & Figures

### TABLE 1 — `table_1_summary.tex`
*(Main.tex caption: "Summary Statistics by Age-65 Cutoff")*

**[CRITICAL] Nested float environment.** `table_1_summary.tex` wraps its content in a full `\begin{table}...\end{table}` environment. Main.tex `\input{}`s it inside *another* `\begin{table}`. LaTeX does not allow nested floats — this will either throw a compilation error or produce a double caption. The file should contain only the `tabular` and `threeparttable` contents, with no outer `\begin{table}` wrapper.

**[CRITICAL] Duplicate label `tab:summary`.** The label is defined both in main.tex's outer `\begin{table}` block and again inside the imported file. LaTeX will emit a multiply-defined label warning and references may resolve incorrectly.

**[MAJOR] Four "---" phantom columns.** Each side of the table has a fourth column whose header and every cell contain nothing but "---". The note says this indicates "unavailable data," but there is no data intended for that column — the columns serve no purpose and waste space. Delete them; a three-column layout (Mean, SD, N) per group is standard.

**[MAJOR] INGRESO\_PC has no unit in the table.** The mean is 13,454 — is this Peruvian soles (S/)? The variable name alone does not tell the reader. Add "(S/)" to the row label or a column-header note.

**[MAJOR] Missing-observation discrepancy unexplained.** NIVEL\_EDUCATIVO reports N = 13,793 (treated) and 92,826 (control) versus the group totals of 14,088 and 99,667. The ~3.5% attrition is not explained in the notes. Add: "NIVEL\_EDUCATIVO has X missing values; remaining statistics exclude them."

**[MINOR] Variable names are raw code strings.** TIENE\_BILLETERA, USA\_BILLETERA, INTERNET\_HOGAR, etc. should be replaced with descriptive English or Spanish labels (e.g., "Digital Wallet Ownership," "Active Wallet Use," "Household Internet Access"). Code names belong in the data appendix, not the publication table.

**[MINOR] Caption mismatch.** Main.tex caption says "Summary Statistics by Age-65 Cutoff"; the file's own caption says "Summary Statistics by Treatment Status." Once the nested-table issue is fixed (one caption remains), decide on a single consistent caption.

**[MINOR] `\begin{tablenotes}` without `threeparttable` wrapper.** The notes are inside `\begin{tablenotes}` but the `tabular` is not wrapped in `\begin{threeparttable}...\end{threeparttable}`. The notes will not render in the correct position. Although `threeparttable` is loaded in main.tex, the wrapper must surround the specific table body.

---

### TABLE 2 — `table_2_main_results.tex`
*(Main.tex caption: "Main RDD Results: Effect of Crossing Age 65 on Digital Wallet Outcomes")*

**[CRITICAL] Nested float environment.** Same structural defect as Table 1 — the file contains its own `\begin{table}` wrapper. Will not compile cleanly when `\input{}`'d into main.tex.

**[CRITICAL] Label mismatch breaks cross-reference.** Main.tex defines `\label{tab:main}` and the text references `Table~\ref{tab:main}`. The file defines `\label{tab:main_results}`. These are different keys; `\ref{tab:main}` will resolve to "??" in the PDF.

**[CRITICAL] het\_POBREZA\_low repeats the full-sample baseline estimates verbatim.** The block for `het_POBREZA_low` shows Estimate = −0.0056, SE = 0.0165, CI = [−0.0336, 0.0310], N/BW = 27,809 / 14.24 — identical to the baseline. The same duplication appears for `het_SMARTPHONE_low`. These look like copy-paste errors; the subsample RDD should produce different point estimates, bandwidths, and N. Verify and correct.

**[MAJOR] Column headers use raw variable names.** "TIENE\_BILLETERA" and "USA\_BILLETERA" are not self-explanatory to a reader unfamiliar with ENAHO codebooks. Replace with "Digital Wallet Ownership" and "Active Wallet Use" (with the variable name relegated to a note or parenthetical).

**[MAJOR] Method names are implementation artefacts.** "rdrobust" and "statsmodels\_WLS" in the "Method" row expose the software stack, not the econometric method. Replace with "Local-linear RD" and "WLS (linear, triangular kernel)" or similar journal-ready descriptions.

**[MAJOR] Permutation p-value (p = 0.434) appears only in prose, never in a table.** The primary inference result for the main outcome should be reported in a table row (e.g., "Randomization p-value" panel). Readers should not have to hunt prose for the headline test statistic.

**[MAJOR] Heterogeneity subgroup labels are opaque.** "het\_POBREZA\_low", "het\_INTERNET\_HOGAR\_low", "het\_SMARTPHONE\_high" are not human-readable panel headers. Use "By poverty status: poor/extreme-poor", "By internet access: no access", etc.

**[MINOR] "N / BW" row conflates two distinct statistics.** Use separate rows or columns: "Observations" and "Optimal Bandwidth (years)."

---

### TABLE 3 — `table_3_robustness.tex`
*(Main.tex caption: "Robustness Checks")*

**[CRITICAL] Nested float environment.** Same defect — file contains its own `\begin{table}` wrapper.

**[CRITICAL] Panel B (donut-hole) shows identical estimates for 0.5 and 1.0 year exclusions.** Both rows show Estimate = −0.0014, SE = 0.0213, CI = [−0.0388, 0.0449], BW = 10.65, N = 19,434. Excluding a different donut window must change the effective sample and the optimal bandwidth; these cannot legitimately be equal. This is almost certainly a data error — the 1.0-year donut result was not computed and the 0.5-year result was pasted twice.

**[MAJOR] Dependent variable not stated anywhere in the table.** The table contains six different tests but never states which outcome variable is being estimated. The header or a table note must specify: "Outcome: TIENE\_BILLETERA (digital wallet ownership)."

**[MAJOR] Two "TIENE\_BILLETERA" rows in Panel D are indistinguishable.** The table lists:

```
TIENE_BILLETERA | -0.0067 | 0.0006 | [-0.0083, -0.0062] | 7.41 | 99,667
TIENE_BILLETERA | 0.0080  | 0.0148 | [-0.0176, 0.0403]  | 7.21 | 99,667
```

The text identifies these as placebo cutoffs at age 15 and age 53, but the table provides no such label. The first row also has N = 99,667 (the full below-threshold sample) which is atypical for a placebo cutoff. These rows need distinct, descriptive labels ("Placebo: age 15", "Placebo: age 53") and the sample scope must be explained.

**[MAJOR] McCrary density test statistic absent from table.** The text reports a test statistic of 2.0 for the running-variable manipulation test (\citealt{cattaneo2018}) but this result does not appear in Table 3 or any table. Add a "Panel E: Density test" row with the test statistic and p-value.

**[MINOR] Panel D mixes two conceptually different placebo types** (covariate placebos in the first two rows, cutoff placebos in the last two) without separating them. Split into Panel D (covariate placebos) and Panel E (placebo cutoffs).

---

### TABLE 4 — `table_4_covariate_balance.tex`
*(Main.tex caption: "Covariate Balance at Age-65 Cutoff (RDD Estimates)")*

**[CRITICAL] Nested float environment.** Same defect as the other three tables.

**[CRITICAL] Label mismatch breaks cross-reference.** Main.tex defines `\label{tab:balance}`; the text references `Table~\ref{tab:balance}`. The file defines `\label{tab:cov_balance}`. The reference will produce "??" in the PDF.

**[MINOR] Asterisk footnote defined but never used.** The note says "$^{*}$ 95% CI excludes zero" but no row in the table carries a superscript asterisk. Either remove the footnote definition or apply the asterisk to rows where the CI excludes zero (none in this table, which is the expected/reassuring result — but the dangling footnote is confusing).

**[MINOR] NIVEL\_EDUCATIVO N discrepancy.** N = 27,325 versus 27,809 for all other covariates. The ~1.7% difference is not explained in the notes.

**[MINOR] Caption mismatch between main.tex and file.** "Covariate Balance at Age-65 Cutoff (RDD Estimates)" vs "Covariate Balance at the Age-65 Eligibility Threshold (Within Bandwidth)." Fix to a single caption after resolving the nested-float issue.

---

### FIGURE 1 — RDD Plot (`figure_1_rdplot`)

**[MAJOR] Internal inconsistency in prose description.** Section 4.5 states: "rates rise from approximately 4% at age 50 to a maximum of 11% *near age 35 (younger adults)*." Age 35 is far outside the bandwidth (h* = 14.2 years around 65) and inconsistent with "the binned scatter shows a smooth age profile." This is either a typo (should be "age 55" or "age 40") or a misdescription of the figure. Verify against the actual plot and correct.

**[MAJOR] Caption is not self-contained on sample scope.** It does not state whether the plot shows the full sample or only observations within the optimal bandwidth. Add: "Observations within [age range]. Bandwidth h* = 14.2 years."

**[MINOR] No axis label units specified.** The caption should state x-axis = "Age (years)" and y-axis = "Share with digital wallet (proportion)." These may be on the figure itself, but the caption should be self-sufficient for a reader who sees only the caption in a proof.

**[MINOR] No data source or bin-width noted.** Add: "Source: ENAHO 2024. Each bin represents [X] age-year observations."

---

### FIGURE 2 — Bandwidth Sensitivity (`figure_2_bandwidth_sensitivity`)

**[MINOR] Column header uses code variable name.** Caption says "primary outcome (\texttt{TIENE\_BILLETERA})" — acceptable in a caption, but should be followed by the plain-language label: "digital wallet ownership."

**[MINOR] Caption does not specify axis units.** x-axis = "Bandwidth (years)"; y-axis = "RD point estimate (proportion)."

**[MINOR] Caption does not specify number of bandwidths shown.** "across bandwidth choices ranging from h*/2 to 2h*" — add the actual range in years: "from 7.1 to 28.5 years."

---

### FIGURE 3 — McCrary Density Plot (`figure_mccrary_density`)

**[MAJOR] Test statistic and p-value absent from caption.** The McCrary/Cattaneo density test produces a test statistic and p-value that should appear here (or in a table). The text says "test statistic of 2.0" but gives no p-value and the figure caption is silent on both. Add: "Cattaneo–Jansson–Ma density test statistic = 2.0 (p = [value]). Null: no manipulation at the cutoff."

**[MINOR] Histogram range not specified.** "Around the Age-65 Cutoff" is vague. State the age range displayed.

**[MINOR] No y-axis unit described.** Specify whether the y-axis is raw counts, relative frequency, or kernel-density estimate.

---

### BIBLIOGRAPHY

**[MAJOR] Orphan bibliography entry.** `\bibitem[Deming and Noray(2023)]{deming2023}` (Deming & Noray, *QJE*, 2023) is defined but never cited anywhere in the text. Remove it or add the citation.

**[MINOR] Malformed natbib author-year key.** `\bibitem[Ardington et~al.2016]{ardington2016}` is missing the parentheses around the year required for the natbib author-year style: should be `[Ardington et~al.(2016)]`. This will produce malformed in-text citations.

---

## Summary

| Severity | Count | Top issues |
|---|---|---|
| CRITICAL | **5** | Nested float environments in all 4 table files; broken `\ref{}` for Tables 2 & 4; donut-hole identical estimates in Table 3 |
| MAJOR | **11** | Copy-pasted het. estimates in Table 2; permutation p-value missing from tables; two unlabeled TIENE\_BILLETERA placebo rows; McCrary statistic absent; "---" columns; method names as software identifiers; internal inconsistency in Fig. 1 prose; orphan bibliography entry |
| MINOR | **10** | Axis labels; asterisk footnote unused in Table 4; NIVEL\_EDUCATIVO N unexplained; code variable names throughout; bibitem format error |

```json
{
  "n_critical": 5,
  "n_major": 11,
  "n_minor": 10,
  "tables_reviewed": 4,
  "figures_reviewed": 3,
  "top_issues": [
    "All four table .tex files contain a \begin{table} wrapper, creating illegal nested floats when \\input{}'d into main.tex — will cause LaTeX compilation failure or double captions in all tables",
    "Label mismatch tab:main vs tab:main_results (Table 2) and tab:balance vs tab:cov_balance (Table 4) produce broken \\ref{} cross-references (?? in PDF)",
    "Table 3 Panel B: donut-hole estimates for 0.5-year and 1.0-year exclusions are byte-for-byte identical — likely a copy-paste error, not computed independently",
    "Table 2: het_POBREZA_low and het_SMARTPHONE_low subgroup rows repeat the full-sample baseline estimates verbatim — suspected copy-paste error corrupting the heterogeneity analysis",
    "Permutation randomization p-value (p=0.434) — the primary inference result — appears only in prose; never tabulated",
    "Table 3 Panel D: two TIENE_BILLETERA placebo-cutoff rows are indistinguishable (no labels for age-15 vs age-53 placebo)",
    "McCrary density test statistic (T=2.0) reported in text but absent from all tables and figures",
    "Figure 1 prose states wallet ownership peaks 'near age 35 (younger adults)' — internally inconsistent with an RDD at age 65 and likely a typo",
    "Orphan bibliography entry: Deming & Noray (2023) defined but never cited in text",
    "Bibitem key for Ardington et al. (2016) missing parentheses around year — malformed natbib author-year format"
  ]
}
```

---


## 6. Contribution Evaluation

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

---
