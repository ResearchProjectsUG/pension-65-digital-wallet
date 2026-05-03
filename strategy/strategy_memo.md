# Strategy Memo — Pensión 65 RDD on Digital Wallet Adoption

**Question.** Does crossing the age-65 Pensión 65 institutional eligibility
threshold increase digital wallet ownership and active use among Peruvian
adults?

**Hypothesis.** Pensión 65 disburses bimonthly cash transfers through Banco
de la Nación accounts, which since 2023 have been integrated with the
Cuenta DNI digital-wallet infrastructure. If institutional digitization of
government transfers can substitute for behavioural-change interventions
(à la Bachas et al. 2018; Muralidharan et al. 2016), we should observe a
positive jump in digital wallet ownership and/or active use right at the
age-65 cutoff.

---

## 1. Identification

- **Design.** Regression discontinuity at age 65 (the program's
  age-eligibility cutoff). Sharp on the age dimension; **fuzzy** with
  respect to actual program receipt because the second eligibility
  criterion is SISFOH classification as extreme-poor (and, separately,
  take-up is incomplete: roughly 25% of eligible individuals are not on
  MIDIS rolls).
- **Estimand.** Local intent-to-treat (ITT) effect of crossing the age-65
  threshold. We do **not** identify a sharp local average treatment effect
  on actual program compliers because (a) ENAHO 2024 does not record
  Pensión 65 receipt directly, and (b) we cannot merge with MIDIS
  administrative data.
- **Bandwidth.** MSE-optimal h\* = 14.24 years (Calonico, Cattaneo &
  Titiunik 2014), giving an estimation window of ages 50–79.
- **Estimator.** `rdrobust` local-linear with triangular kernel and
  bias-corrected robust CIs as the **primary** specification. Statsmodels
  WLS at h = 34.22 used as a secondary descriptive specification when the
  local-polynomial pathway hits memory limits; this is **not** the RDD
  result.
- **Inference.** Permutation-based randomization inference (500 valid
  permutations on the [55, 75] window) is the **primary** test, because
  the integer running variable creates discrete mass-points that violate
  the asymptotic-SE assumptions of WLS. Robust bias-corrected CIs from
  `rdrobust` are reported alongside.
- **Identifying assumptions.** (i) Continuity of potential outcomes at
  age 65; (ii) no precise manipulation of reported age (tested with the
  Cattaneo–Jansson–Ma 2018 density test); (iii) continuity of
  predetermined covariates (tested via Table 4 within-bandwidth balance).

## 2. Outcomes

- **`TIENE_BILLETERA`** (primary): binary, equal to 1 if ENAHO module 5
  question P558E1 is coded 9 ("digital wallet"). Population mean 7.4%.
- **`USA_BILLETERA`** (secondary): binary, equal to 1 if any of the twelve
  P558H consumption-category items has its payment-method code equal to 7
  ("paid with a digital wallet"). Population mean 15.6%.

These two outcomes are by design distinct: ownership ≠ active use, and
the policy-relevant question for financial inclusion is whether the
program induces both (or only the former, leading to a "dormant accounts"
pattern documented by Bachas et al. 2018).

## 3. Predetermined covariates (used in covariate-adjusted spec and
balance tests)

- `INTERNET_HOGAR` — household has internet access
- `SMARTPHONE` — respondent owns a smartphone
- `POBREZA` — SISFOH poverty classification (1 extreme-poor, 2
  non-extreme-poor, 3 non-poor)
- `INGRESO_PC` — household per-capita income
- `NIVEL_EDUCATIVO` — highest education level achieved

## 4. Robustness battery (Table 3 in paper, all reproducible from
`02_robustness.py`)

1. Bandwidth sensitivity: h\*/2, h\*, 2 h\*.
2. Donut-hole at ±0.5, ±1.0, ±2.0 yrs (assess sensitivity to integer
   heaping at age 65; donut window applied as strict inequality on the
   integer running variable).
3. Polynomial sensitivity: linear vs quadratic.
4. Placebo cutoffs at age 15 (left) and age 53 (right).
5. Placebo outcomes: covariates as outcomes (Panel D).
6. McCrary-style density test (Cattaneo–Jansson–Ma).
7. Heterogeneity by SISFOH (POBREZA = 1, 2, 3) — the policy-relevant
   split because Pensión 65 conditions eligibility on extreme-poverty
   classification.
8. Permutation randomization inference.

## 5. Sample restrictions and weighting

- Drop individuals with missing age (3,966 obs, almost all infants under
  one year). Final RDD sample: 113,755 individuals.
- Treated/control split is **asymmetric** (14,088 vs 99,667) because the
  control side spans all ages below 65 down to 25 while the treated side
  spans 65–85+. Within the bandwidth-restricted window the split is
  17,047 below / 10,762 above the cutoff — the support relevant for
  identification.
- ENAHO survey expansion weights (`FACPOB07`, renamed
  `FACTOR_EXPANSION` in the cleaned file) are **present but not applied
  inside `rdrobust`**. Estimates therefore identify the discontinuity in
  the survey sample, not a population-weighted effect; population-level
  language is avoided in the paper or explicitly caveated.

## 6. What this design **cannot** answer

- The effect of *receiving* a Pensión 65 benefit (TOT/LATE on actual
  compliers). That requires administrative data merging MIDIS
  beneficiary rolls with ENAHO records, which is not available.
- Long-run / cumulative effects — ENAHO 2024 is a single
  cross-sectional wave; cohort vs age effects cannot be separately
  identified.
- The mechanism (telehealth-like substitution into the digital channel
  vs. genuine adoption). Without panel data on the same individuals
  before and after threshold-crossing, this is not testable.

## 7. Pre-analysis decisions (to be reported transparently)

- Primary outcome: `TIENE_BILLETERA`. Secondary: `USA_BILLETERA`.
- Primary inference: randomization p-value (vs. asymptotic CIs).
- Heterogeneity is exploratory; no multiple-testing correction was
  pre-specified, so the SISFOH gradient is described as "suggestive"
  rather than "evidence of heterogeneity."
- The covariate-adjusted WLS spec is descriptive, not the RDD result.
