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