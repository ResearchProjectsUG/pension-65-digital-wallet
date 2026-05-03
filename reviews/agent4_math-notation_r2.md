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