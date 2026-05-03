## Technical Coherence Review — Round 4

I'll work through the paper systematically, checking every numerical claim against the evidence packet.

---

### Abstract vs. Table 2 (Baseline)

| Claim | Text | Table 2 | Verdict |
|---|---|---|---|
| Ownership estimate | −0.006 | −0.0056 | ✓ |
| Ownership SE | 0.016 | (0.0165) | ✓ |
| Ownership CI | [−0.034, 0.031] | [−0.0336, 0.0310] | ✓ |
| Active use estimate | +0.007 | 0.0066 | ✓ |
| Active use SE | 0.018 | (0.0180) | ✓ |
| Active use CI | [−0.034, 0.037] | [−0.0338, 0.0368] | ✓ |
| Cov-adjusted ownership | −0.027, SE=0.005 | −0.0270, (0.0053) | ✓ |
| Permutation p | 0.434 | (body text consistent) | ✓ |

---

### Sample Arithmetic (§3.1–3.2)

- 117,721 − 3,966 = 113,755 ✓ ; 3,966/117,721 = 3.37% ≈ 3.4% ✓
- 99,667 + 14,088 = 113,755 ✓ ; matches Table 1 ✓
- Bandwidth split: 17,047 + 10,762 = 27,809 ✓ ; BW = 14.24 ✓

**[MAJOR-1] Population means in §3.2 don't reconcile with Table 1 group means.**

Text states:
- `TIENE_BILLETERA` population mean = **7.4%**
- `USA_BILLETERA` population mean = **15.6%**

Back-calculation from Table 1 (unweighted, no weights column per audit):

```
TIENE_BILLETERA: (99,667×0.0800 + 14,088×0.0535) / 113,755
               = (7,973 + 754) / 113,755 = 8,727 / 113,755 = 7.67%

USA_BILLETERA:  (99,667×0.1794 + 14,088×0.0319) / 113,755
               = (17,882 + 449) / 113,755 = 18,331 / 113,755 = 16.1%
```

Discrepancies: **0.27 pp** for ownership and **0.5 pp** for active use. The most likely cause is that some respondents have missing values on the outcome variables, reducing the effective denominator below 113,755 — but this is never disclosed in the paper. Undisclosed item non-response on the primary outcomes is a data-quality issue that should be reported in the sample-construction section.

---

### Covariate Balance: §4.3 vs. Table 4

| Claim | Text | Table 4 | Verdict |
|---|---|---|---|
| SMARTPHONE jump | +0.014, CI [−0.015, 0.086] | 0.0139, [−0.0146, 0.0857] | ✓ |
| INTERNET\_HOGAR jump | +0.015, CI [−0.061, 0.131] | 0.0147, [−0.0607, 0.1308] | ✓ |
| INGRESO\_PC jump | −S/47, CI [−2,079, 3,172] | −47.12, [−2078.60, 3171.92] | ✓ |

**[MINOR-1] Baseline income figure unverified.** Section 4.3 describes the income jump as "−S/47 on a baseline mean of S/11,700." Table 1 shows the below-cutoff full-sample mean for `INGRESO_PC` is S/11,416.51 — a discrepancy of S/283 (~2.5%). The paper may be citing a bandwidth-restricted control mean (ages 50–64) rather than the full below-cutoff mean, which is plausible but not stated. The source of S/11,700 is unspecified.

---

### [CRITICAL-1] Table 3 Panel D vs. Table 4 — Unresolved from Round 3

This issue was flagged as CRITICAL in Round 3. It remains unresolved. Both `INTERNET_HOGAR` and `SMARTPHONE` appear as RDD outcomes in Table 3 Panel D ("Placebo — covariates as outcomes") and Table 4 ("Covariate Balance") with **irreconcilable numbers**:

| Variable | Table | Estimate | SE | CI | BW | N |
|---|---|---|---|---|---|---|
| INTERNET\_HOGAR | Table 3 Panel D | 0.0139 | 0.0487 | [−0.0615, 0.1296] | **15.23** | **29,668** |
| INTERNET\_HOGAR | Table 4 | 0.0147 | 0.0489 | [−0.0607, 0.1308] | **14.24** | **27,809** |
| SMARTPHONE | Table 3 Panel D | 0.0138 | 0.0246 | [**−0.0218, 0.0748**] | 14.29 | 27,809 |
| SMARTPHONE | Table 4 | 0.0139 | 0.0256 | [**−0.0146, 0.0857**] | 14.24 | 27,809 |

For `INTERNET_HOGAR`: BW diverges by 0.99 years; N diverges by **1,859 observations**; estimates are not identical. For `SMARTPHONE`: the CI upper bounds differ by **0.011** (0.0748 vs. 0.0857 — a 14% gap in interval width), despite identical N. Neither table contains a note explaining the discrepancy.

The body text (§4.3) cites the Table 4 values when describing the balance test, making Table 3 Panel D internally redundant and inconsistent. **A referee comparing these two tables will flag the paper as containing an unreported specification switch.**

---

### [MAJOR-2] Table 3 Panel A — H Double CI Anomaly

The bias-corrected CI for `H Double` shows an unusually large shift from the conventional estimate:

| Spec | Estimate | CI | CI midpoint | Shift |
|---|---|---|---|---|
| H Half | −0.0056 | [−0.0499, 0.0370] | −0.0065 | −0.0009 |
| H Optimal | −0.0056 | [−0.0397, 0.0306] | −0.0046 | +0.0010 |
| **H Double** | **−0.0204** | **[−0.0272, 0.0264]** | **−0.0004** | **+0.0200** |

For `H Half` and `H Optimal`, the rdrobust bias-correction shifts the CI midpoint by less than 0.001 from the conventional estimate — negligible. For `H Double`, the shift is **+0.020**: the bias-corrected CI is centered near 0, not near −0.0204. This implies the estimated bias at `h = 28.48` is approximately equal to the conventional point estimate itself — the bias-correction absorbs essentially the entire signal.

This is a substantively important finding. At twice the optimal bandwidth the bias grows large enough that the conventional estimate (−2.0 pp) and the bias-corrected estimate (~0 pp) are telling very different stories. The text currently says only "all 95% confidence intervals overlapping zero" without acknowledging that the H Double estimate is anomalous in this respect. This deserves explicit discussion: either the wider bandwidth is too far from the cutoff for the local linear to be unbiased, or the estimate at that bandwidth is unreliable. The paper's own bandwidth-selection procedure chose `h* = 14.24` precisely to balance bias and variance; the H Double result illustrates why that choice matters.

---

### Robustness Checks: §4.2 vs. Table 3

**[MINOR-2] Donut-hole rounding.** Text: "yield estimates of −0.001, removing the small negative point estimate entirely." Table 3: ±0.5 yr estimate = −0.0001. That rounds to −0.000, not −0.001. A ten-fold difference in the last digit may seem trivial but is inconsistent with the paper's standard of 3-decimal precision.

**[MINOR-3] Bandwidth rounding.** Text states h*/2 = 7.1 (Table 3: 7.12) and 2h* = 28.5 (Table 3: 28.48). Minor, but inconsistent with the paper's own 2-decimal precision for bandwidths.

---

### USA\_BILLETERA Bandwidth Not Disclosed

**[MINOR-4]** Table 2 shows that `USA_BILLETERA` baseline uses **BW = 17.29, N = 33,267** — materially different from `TIENE_BILLETERA`'s BW = 14.24, N = 27,809. The paper consistently refers to "the optimal bandwidth h* = 14.24" as a single figure (Abstract, §3.2, §4.1, §5.1) without ever noting that the second outcome has a distinct optimal bandwidth. A reader comparing bandwidth sensitivity or replication output will find the numbers for active use do not reproduce under h* = 14.24.

---

### Remaining Checks: All Pass

- Sample split arithmetic, heterogeneity subgroup numbers (Table 2 vs. §4.4–4.5), and covariate balance CIs in §4.3 all match the tables after rounding.
- The `deming2023` phantom citation (CRITICAL-2 in Round 3) does not appear in the current manuscript — **resolved**.
- The WLS bandwidth-switch disclosure (MAJOR-1 in Round 3) is addressed in §4.1 with an explicit warning about the wider bandwidth and secular age gradient interpretation — **adequately disclosed**.
- Permutation p = 0.434 and Cohen's d = −0.021 are internally consistent with the estimate magnitudes, though not directly verifiable from the tables.

---

## Summary

The three outstanding numerical integrity problems are the Table 3/Table 4 duplication with incompatible values (unresolved from Round 3), the H Double bias-correction anomaly (suggesting the 2h* robustness check is essentially uninformative and should be discussed as such), and the undisclosed item non-response on the primary outcomes. The remaining issues are minor presentational matters.

```json
{
  "n_critical": 1,
  "n_major": 2,
  "n_minor": 4,
  "top_issues": [
    "CRITICAL: Table 3 Panel D vs. Table 4 report incompatible BW/N/CI for INTERNET_HOGAR (N=29,668 vs 27,809) and SMARTPHONE (CI upper bound 0.0748 vs 0.0857) — same test, irreconcilable numbers, no explanatory note; unresolved from Round 3",
    "MAJOR: H Double row in Table 3 Panel A shows bias-corrected CI centered at -0.0004 while conventional estimate is -0.0204 — a bias-correction shift 20x larger than all other bandwidth rows, implying estimated bias ≈ point estimate at h=28.48; not disclosed in text",
    "MAJOR: Population means in §3.2 (TIENE_BILLETERA 7.4%, USA_BILLETERA 15.6%) do not reconcile with Table 1 group means (back-calculation yields 7.67% and 16.1%); discrepancy implies undisclosed item non-response on both primary outcome variables"
  ]
}
```