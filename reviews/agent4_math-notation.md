## Formal Review: Mathematical and Notational Content

---

### 1. Mathematical Correctness

**Equation (1) — LATE estimand** [CLEAN]
$$\tau = \lim_{a \downarrow 65} E[Y \mid A = a] - \lim_{a \uparrow 65} E[Y \mid A = a]$$
Standard sharp-RDD estimand. Direction of limits correct (right minus left).

**Equation (2) — Local linear** [CLEAN]
$$Y_i = \alpha + \tau D_i + \beta_1 (A_i - 65) + \beta_2 D_i (A_i - 65) + \varepsilon_i$$
Correct separate-slope local-linear form. The interaction $D_i(A_i-65)$ allows different slopes on each side — this is the textbook Hahn/Todd/Van der Klaauw specification.

**Covariate-adjusted CI check** [CLEAN]
Reported: estimate $-0.027$, SE $0.005$, CI $[-0.037, -0.017]$.
Implied CI: $-0.027 \pm 1.96 \times 0.005 = [-0.0368, -0.0172] \approx [-0.037, -0.017]$. ✓

**Bias-corrected CI for baseline** [CLEAN — but asymmetry must be flagged to reader]
Reported: estimate $-0.006$, robust SE $0.016$, CI $[-0.034, 0.031]$.
The midpoint of the CI is $(-0.034+0.031)/2 = -0.0015$, not $-0.006$. This is correct behaviour for rdrobust bias-corrected CIs (the CI is centred on the bias-corrected estimate, not the conventional one), but the paper never explains why the interval is not centred on the reported point estimate. This is an implicit source of reader confusion — [MINOR].

**Sample arithmetic** [CLEAN]
$117{,}721 - 3{,}966 = 113{,}755$. $3{,}966/117{,}721 = 3.37\% \approx 3.4\%$. $99{,}667 + 14{,}088 = 113{,}755$. ✓

---

### 2. [MAJOR] T-Statistic Inconsistent with Reported Estimate and SE

Section 5.1: *"Permutation-based randomization inference yields a t-statistic of $-5.999$."*

The covariate-adjusted estimate is $-0.027$ with SE $= 0.005$, giving $t = -0.027/0.005 = -5.4$, **not** $-5.999$. The discrepancy is ~10%. If the true (unrounded) estimate were $-0.030$ the t-stat would be $-6.0$, consistent with the displayed value but inconsistent with the rounded estimate $-0.027$.

The paper does not explain whether $-5.999$ is computed from a different specification, from the permutation procedure itself (which might use an alternative test statistic), or whether $-0.027$ is rounded from $-0.030$. As written, the three numbers ($\hat\tau = -0.027$, $\mathrm{SE}=0.005$, $t=-5.999$) are mutually inconsistent.

---

### 3. [MAJOR] Equation (3) Omits the D-Interaction on the Running-Variable Polynomial

Equation (2) correctly allows separate slopes:
$$\beta_1(A_i - 65) + \beta_2 D_i(A_i - 65)$$

Equation (3) collapses this to a single symmetric function:
$$g(A_i - 65)$$
with no $D_i$-interaction. Standard RDD covariate-adjustment (Calonico, Cattaneo, Farrell, Titiunik 2019, cited as `calonico2019`) **preserves** separate-slope (or separate-polynomial) fits on each side; the covariates $\mathbf{X}_i$ enter additively without altering the local polynomial structure. As written, Equation (3) implies a pooled regression on a single global polynomial — inconsistent with both Equation (2) and how `rdrobust` implements the covariate-adjusted estimator.

The correct representation should be:
$$Y_i = \alpha + \tau D_i + \beta_1(A_i-65) + \beta_2 D_i(A_i-65) + \mathbf{X}_i'\boldsymbol{\gamma} + \varepsilon_i$$
(or the analogous higher-order version), not a single $g(\cdot)$.

---

### 4. [MAJOR] Both Placebo Cutoffs Labeled "Age 53"

Section 5.2: *"Placebo cutoffs at age **53** (i.e., 12 years below the true cutoff) and age **53** (12 years right)..."*

Twelve years below 65 is age 53; twelve years above 65 is age **77**. The right-side placebo is erroneously printed as "age 53." This is an internal inconsistency: the text says "12 years right" but gives the same value as "12 years below." The estimates ($-0.007$ and $+0.008$) look plausible for two-sided placebos, so the computation is likely correct, but the description is definitively wrong.

---

### 5. [MAJOR] Explicitly Flagged Missing Citation

Section 2.3: *"[CITATION MISSING — insert \citet{} key]"*

The bracketed placeholder is in the submitted manuscript. No key is provided.

---

### 6. [MAJOR] Wrong Citation for Age–Technology Gradient Claim

Section 5.1 cites `\citet{deming2023}` for *"the well-documented age gradient in technology adoption."*

The listed reference for `deming2023` is:
> Deming, D.J. and Noray, K. (2023). Earnings Dynamics, Changing Job Skills, and STEM Careers. *Quarterly Journal of Economics*, 135(4):1965–2005.

That paper studies STEM earnings and skill depreciation, **not** age differences in digital or technology adoption. The citation is incorrect for the stated claim.

---

### 7. [MINOR] Cohen's d Computation Not Reconcilable with Reported Inputs

Section 5.1: *"The Cohen's $d$ effect size for the primary outcome is $-0.021$."*

For a binary outcome with population mean $p = 0.074$, the standard deviation is $\sqrt{0.074 \times 0.926} \approx 0.262$. Using the baseline estimate: $d = -0.006/0.262 \approx -0.023$. Using the covariate-adjusted estimate: $d = -0.027/0.262 \approx -0.103$. Neither matches $-0.021$. The paper does not state which estimate or which SD was used. The value $-0.021$ would require a denominator of $\approx 0.286$, plausible only for a different subsample or a pooled-SD formula. Source of computation should be disclosed.

---

### 8. [MINOR] Figure Description Contains Reversed Age Direction

Section 5.5: *"rates rise from approximately 4\% at age 50 to a maximum of 11\% near age 35 (younger adults)"*

Rates do not "rise from age 50 to age 35" — that traverses the age axis backwards. The correct description is that ownership declines from ~11% at age 35 to ~4% at age 50 as age increases. As written, the direction-of-change language is inverted.

---

### 9. [MINOR] Potential Outcomes $Y(0), Y(1)$ Not Formally Introduced

Assumption 1 in Section 4.1 references $E[Y(0)\mid A=a]$ and $E[Y(1)\mid A=a]$ without prior definition of the potential-outcome notation. $Y$ is defined in the introduction only as "the outcome of interest." A one-line formal introduction of the Rubin-causal notation before Assumption 1 is needed.

---

### 10. [MINOR] Ardington Bibitem Year Tag Contradicts Body Year

```latex
\bibitem[Ardington et~al.2009]{ardington2016}
Ardington, C., Case, A., and Hosegood, V. (2016). ...
```

The display tag says `2009`; the body year is `(2016)`. The actual Ardington–Case–Hosegood paper appeared in *AEJ: Applied Economics* **1**(1), 2009 (not volume 8, 2016). Both the year in the display tag and the volume/year in the body are inconsistent with each other and with the actual publication. The label `ardington2016` is also inconsistent with a 2009 publication.

---

### 11. [MINOR] Indicator Function Font

`\mathbf{1}\{A_i \ge 65\}` uses **bold upright** for the indicator. The standard in econometrics papers is `\mathbb{1}` (blackboard bold) or `\mathbf{1}_{[\cdot]}`. Minor cosmetic issue.

---

## Summary Table

| # | Severity | Location | Issue |
|---|----------|----------|-------|
| 1 | **MAJOR** | §5.1 | T-statistic $-5.999 \neq -0.027/0.005 = -5.4$ |
| 2 | **MAJOR** | Eq. (3) | $g(A_i-65)$ omits $D_i$-interaction, inconsistent with local-polynomial convention |
| 3 | **MAJOR** | §5.2 | Right-side placebo cutoff listed as "age 53" (should be age 77) |
| 4 | **MAJOR** | §2.3 | Explicit `[CITATION MISSING]` placeholder in manuscript |
| 5 | **MAJOR** | §5.1 | Deming & Noray (2023) cited for age–technology gradient; paper is about STEM earnings |
| 6 | MINOR | §5.1 | Cohen's $d = -0.021$ not reconcilable with stated estimate and SD |
| 7 | MINOR | §5.5 | Figure description inverts direction of age axis |
| 8 | MINOR | §4.1 | $Y(0), Y(1)$ used before formal definition |
| 9 | MINOR | Bib. | Ardington bibitem year tag (2009) contradicts body year (2016) |
| 10 | MINOR | §4.2 | Baseline CI $[-0.034,0.031]$ not centred on $-0.006$; asymmetry unexplained |
| 11 | MINOR | §4.2 | `\mathbf{1}` should be `\mathbb{1}` for indicator function |

---

```json
{
  "n_critical": 0,
  "n_major": 5,
  "n_minor": 6,
  "top_issues": [
    "Equation (3) omits D_i-interaction on running-variable polynomial, making the covariate-adjusted spec inconsistent with local-RDD convention and with Equation (2)",
    "T-statistic -5.999 is inconsistent with the reported estimate (-0.027) divided by the reported SE (0.005), which yields -5.4",
    "Right-side placebo cutoff printed as 'age 53' (should be age 77 = 65+12)",
    "Explicit [CITATION MISSING] placeholder left in the manuscript body (Section 2.3)",
    "Deming & Noray (2023) cited for 'age gradient in technology adoption' but the paper is about STEM earnings dynamics — factually wrong citation for the claim"
  ]
}
```