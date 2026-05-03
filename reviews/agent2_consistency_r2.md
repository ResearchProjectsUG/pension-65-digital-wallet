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