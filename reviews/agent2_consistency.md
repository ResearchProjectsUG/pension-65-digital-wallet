## Internal Coherence Review — Pensión 65 RDD Paper

---

### 1. Numerical Consistency: Text vs. Evidence Packet

**Abstract / Introduction / Section 5 — Baseline estimates**

| Quantity | Text | Table 2 | Verdict |
|---|---|---|---|
| Baseline TIENE_BILLETERA estimate | −0.006 | −0.0056 | ✓ |
| Baseline TIENE_BILLETERA SE | 0.016 | 0.0165 | ✓ |
| Baseline TIENE_BILLETERA 95% CI | [−0.034, 0.031] | [−0.0336, 0.0310] | ✓ |
| Baseline USA_BILLETERA estimate | +0.007 | 0.0066 | ✓ |
| Baseline USA_BILLETERA SE | 0.018 | 0.0180 | ✓ |
| Baseline USA_BILLETERA 95% CI | [−0.034, 0.037] | [−0.0338, 0.0368] | ✓ |
| Covariate-adjusted ownership estimate | −0.027 | −0.0270 | ✓ |
| Covariate-adjusted ownership SE | 0.005 | **0.0053** | ✓ (rounding) |
| Covariate-adjusted usage CI | [−0.002, 0.016] | [−0.0020, 0.0164] | ✓ |

**[MAJOR] Income baseline mean — Section 5.3**

> Text: "the jump in per-capita income is −S/47 on a **baseline mean of S/11,700**"

Table 1 shows the control-group (below-threshold) mean for `INGRESO_PC` = **S/11,416.51**, not S/11,700. The discrepancy is ~S/284 and is not explainable by rounding.

**[MAJOR] Population means — Section 3.3**

> Text: TIENE_BILLETERA "Population mean: 7.4%", USA_BILLETERA "Population mean: 15.6%"

Back-calculated from Table 1 (unweighted):
- TIENE_BILLETERA: (99667 × 0.0800 + 14088 × 0.0535) / 113755 ≈ **7.67%** (text says 7.4%)
- USA_BILLETERA: (99667 × 0.1794 + 14088 × 0.0319) / 113755 ≈ **16.1%** (text says 15.6%)

Both overstate how far the stated means are from what the table implies. The data-audit report confirms no survey weight column was found, so the discrepancy is unexplained.

---

### 2. Robustness Table — Two Critical Internal Contradictions

**[CRITICAL] Donut-hole specifications produce identical output (Table 3, Panel B)**

```
Donut 0.5:  −0.0014  SE=0.0213  CI=[−0.0388, 0.0449]  BW=10.65  N=19434
Donut 1.0:  −0.0014  SE=0.0213  CI=[−0.0388, 0.0449]  BW=10.65  N=19434
```

Every single number is identical across the two different exclusion windows. Excluding observations within ±0.5 versus ±1.0 year of the cutoff necessarily produces different samples (different N) and different bandwidth selections. This is a code-level duplication bug. The text cites these as separate results ("estimates of −0.001, removing the small negative point estimate entirely"); the robustness claim rests on a duplicated computation.

**[CRITICAL] Placebo cutoff — typographical error that misidentifies the specification**

> Text (Section 5.2): "Placebo cutoffs at age 53 (i.e., 12 years below the true cutoff) and **age 53** (12 years right)"

The right placebo cutoff is listed as age 53 twice. The parenthetical says "12 years right" of the true cutoff (65), which should be **age 77**, not age 53. This contradicts the description and misidentifies the specification.

**[MAJOR] Heterogeneity subgroup (POBREZA) is identical to baseline (Table 2)**

```
Baseline:         −0.0056  SE=0.0165  CI=[−0.0336, 0.0310]  BW=14.24  N=27809
het_POBREZA_low:  −0.0056  SE=0.0165  CI=[−0.0336, 0.0310]  BW=14.24  N=27809
```

A poverty-restricted subsample cannot have the same N (27,809) and bandwidth as the full sample. This is another apparent code bug where the poverty subgroup estimate was not actually computed.

---

### 3. McCrary Density Test — Missing p-value [MAJOR]

> Text: "The McCrary-style density test of Cattaneo et al. (2018) produces a test statistic of 2.0"

A test statistic of 2.0 in a two-sided density test corresponds to p ≈ 0.046 — borderline rejection of the no-manipulation null. The paper provides no p-value, simply asserting "no evidence of bunching specifically at age 65." The code review further notes the p-value extraction may be silently returning `nan` due to an API bug (`rd_den.p` vs. `rd_den.test['p_jk']`). The paper must either report the p-value explicitly or acknowledge that z = 2.0 is only marginally non-significant.

---

### 4. Figure Description — Impossible Age Reference [MAJOR]

> Text (Section 5.4): "rates rise from approximately 4% at age 50 to a maximum of 11% **near age 35** (younger adults), and decline monotonically with age"

An RDD plot centered at age 65 with bandwidth ~14 years shows roughly ages 51–79. Age 35 does not appear in this figure. The description is internally inconsistent: first it says rates "rise from 4% at age 50 to a maximum at age 35" (moving backward in age), then "decline monotonically with age" (moving forward). The RD figure caption makes no mention of age 35. This appears to be a residual from template text or from confusing the full-sample age distribution with the RDD window.

---

### 5. Missing Citation [CRITICAL]

> Text (Section 2.3): "The closest recent application to our setting... [CITATION MISSING — insert \citet{} key]"

A literal placeholder remains in the manuscript body. Not submittable.

---

### 6. Abstract vs. Body Consistency

| Claim | Abstract | Results Section | Match |
|---|---|---|---|
| Ownership baseline CI | [−0.034, 0.031] | [−0.034, 0.031] | ✓ |
| Usage baseline CI | [−0.034, 0.037] | [−0.034, 0.037] | ✓ |
| Covariate-adjusted ownership | −0.027, SE=0.005 | −0.027, SE=0.005 | ✓ |
| Randomization p-value | 0.434 | 0.434 | ✓ |

Abstract-to-body consistency is otherwise good.

---

### 7. Citation / Bibliography Errors

**[MAJOR] Ardington et al. — wrong year in bibliography body**

```latex
\bibitem[Ardington et~al.2009]{ardington2016}
Ardington, C., Case, A., and Hosegood, V. (2016). ...
\textit{American Economic Journal: Applied Economics}, 8(1):22--48.
```

The actual Ardington, Case, and Hosegood paper (Labor Supply Responses to Large Social Transfers, South Africa) was published in **2009**, not 2016. The natbib label correctly says 2009 but the bibliography body says 2016 and AEJ:AE 8(1) — the correct citation is vol. 1(1):22–61 (2009). Year and volume/issue are both wrong in the body.

**[MAJOR] Banerjee et al. — label mismatch and content misapplication**

```latex
\bibitem[Banerjee et~al.2019]{banerjee2020}
Banerjee, A., Niehaus, P., and Suri, T. (2020). Universal Basic Income...
```

The natbib label says "2019" so in-text citations will render as "Banerjee et al.2019" — wrong year. More substantively, the paper is a global review of UBI, but the text cites it for the specific claim that "direct benefit transfers in Indonesia increase savings only when accompanied by financial-literacy components." This claim does not come from a UBI review article; it appears to conflate this citation with a different empirical study.

**[MAJOR] Deming and Noray — content mismatch**

```latex
\bibitem[Deming and Noray(2023)]{deming2023}
Deming, D.~J. and Noray, K. (2023). Earnings Dynamics, Changing Job Skills, and STEM Careers.
```

Cited in support of "the well-documented age gradient in technology adoption." The actual Deming-Noray paper is about STEM career earnings dynamics; it does not specifically document the age gradient in technology/digital adoption. The year listed (2023) also appears incorrect — this paper was published in the QJE in 2020. The citation is both misapplied and likely misdated.

---

### 8. Unexplained Bandwidth Jump [MINOR]

The baseline specification uses `rdrobust` with optimal BW = **14.24** (N = 27,809). The covariate-adjusted specification uses BW = **34.22** (N = 59,649) — more than double. This is not discussed anywhere in the empirical strategy or results. Readers cannot assess whether the covariate-adjusted estimate is driven by the larger bandwidth rather than the covariate adjustment itself.

---

### 9. Missing Education Observations — Undisclosed [MINOR]

Table 1 shows that `NIVEL_EDUCATIVO` has:
- Treated: N = 13,793 (295 missing out of 14,088)
- Control: N = 92,826 (6,841 missing out of 99,667)

6,841 missing education values in the control group (~6.9%) is non-trivial and is never acknowledged in the data section.

---

### 10. Template Artifact in Table 1 [MINOR]

The summary table renders four `---` columns labeled "---" in the header. This is a formatting artifact, not a substantive error, but it would be flagged by any journal typesetter.

---

## Consolidated Findings

| # | Severity | Issue |
|---|---|---|
| 1 | **CRITICAL** | [CITATION MISSING] placeholder left in manuscript (Section 2.3) |
| 2 | **CRITICAL** | Placebo cutoff "age 53 (12 years right)" — should be age 77 |
| 3 | **CRITICAL** | Donut-hole ±0.5 and ±1.0 produce byte-for-byte identical estimates — code bug |
| 4 | **MAJOR** | McCrary z = 2.0 (p ≈ 0.046) reported without p-value; paper may be suppressing a rejection |
| 5 | **MAJOR** | Figure 1 description references "age 35" — impossible in an RDD plot around age 65 |
| 6 | **MAJOR** | Banerjee et al. (2020) misapplied — UBI review ≠ Indonesia transfers study |
| 7 | **MAJOR** | Ardington bibliography body: year 2016 and vol 8(1) are both wrong (correct: 2009, vol 1) |
| 8 | **MAJOR** | Banerjee natbib label says 2019; in-text will display wrong year |
| 9 | **MAJOR** | Income baseline mean: text S/11,700 vs. Table 1 S/11,416 |
| 10 | **MAJOR** | het_POBREZA_low estimates identical to baseline — code bug |
| 11 | **MAJOR** | TIENE_BILLETERA population mean: text 7.4% vs. implied ~7.7% from Table 1 |
| 12 | **MAJOR** | USA_BILLETERA population mean: text 15.6% vs. implied ~16.1% from Table 1 |
| 13 | **MAJOR** | Deming & Noray: content mismatch (STEM careers ≠ age-technology gradient) + year likely wrong (2020 not 2023) |
| 14 | **MINOR** | Covariate-adjusted BW jumps from 14.24 to 34.22 with no explanation |
| 15 | **MINOR** | ~6,841 missing education values in control group unacknowledged |
| 16 | **MINOR** | Table 1 "---" column headers are template artifacts |

---

```json
{
  "n_critical": 3,
  "n_major": 10,
  "n_minor": 3,
  "top_issues": [
    "[CITATION MISSING] placeholder explicitly visible in Section 2.3 — paper is not submittable",
    "Placebo cutoff text says 'age 53 (12 years right)' — both placebos labeled age 53; right cutoff should be age 77",
    "Donut-hole ±0.5 and ±1.0 produce identical estimates, SE, CI, BW, and N — clear code duplication bug invalidating this robustness check",
    "McCrary density test statistic z=2.0 reported without p-value; p≈0.046 is borderline rejection of no-manipulation, directly contradicting the paper's claim",
    "Banerjee et al. (2020) cited for an Indonesia empirical finding it does not contain — it is a global UBI review article"
  ]
}
```