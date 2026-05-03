## Mathematical & Formal Review — Round 4

**Scope**: Full paper body is present for the first time (Round 3 was unreviable due to absent body text). I can now assess the formal content directly.

---

### 1. Equation Correctness and Specification

**[CRITICAL-1] Logical impossibility in reported population means**

Section 3.3 reports:
- `TIENE_BILLETERA` (ownership): population mean = **7.4%**
- `USA_BILLETERA` (active use): population mean = **15.6%**

Active use requires ownership by the paper's own causal logic ("ownership reflects access… active use reflects behavioral integration"). A person using a digital wallet as a payment channel must first own one. It is formally impossible that $P(\text{active use}) > P(\text{ownership})$ in the same population under these definitions.

The within-bandwidth figures are internally consistent (ownership 12.9% > use 12.4% for controls; 6.4% > 4.0% for treated), which makes the whole-sample reversal more suspicious—likely a mislabeling, a denominator mismatch between the two mean calculations, or an error in how `USA_BILLETERA` was constructed. The abstract repeats the ordering implicitly ("wallet ownership and use") without resolving the contradiction. A referee will catch this immediately.

---

**[MAJOR-1] Equation (3) omits the slope interaction — specification inconsistency with Equation (2)**

Equation (2) correctly specifies separate slopes on each side of the cutoff:

$$Y_i = \alpha + \tau D_i + \beta_1(A_i-65) + \beta_2 D_i(A_i-65) + \varepsilon_i$$

Equation (3) writes only:

$$Y_i = \alpha + \tau D_i + g(A_i-65) + \mathbf{X}_i'\boldsymbol{\gamma} + \varepsilon_i$$

The interaction $D_i \cdot g(A_i-65)$ is absent. As written, this constrains the polynomial to be identical on both sides of the cutoff — a pooled-slope restriction that is inconsistent with the local-linear RDD framework and with the Calonico et al. (2019) covariate-adjusted estimator the paper cites. A constrained common slope conflates the discontinuity $\tau$ with differential curvature across the cutoff. Either the equation should include $D_i \cdot g_1(A_i-65)$ or the text must defend the restriction explicitly.

---

**[MAJOR-2] Randomization inference procedure is non-standard for RDD and potentially invalid**

Section 4.3 states: *"for each of 500 random permutations of the treatment assignment within an age-window of [55, 75], we re-estimate τ."* 

Permuting $D_i = \mathbf{1}\{A_i \ge 65\}$ while holding age fixed destroys the structural feature of the RDD (that treatment is a deterministic function of the running variable), creating a null distribution that is only valid if the outcome is unrelated to age within $[55, 75]$. The paper itself documents a strong negative age gradient in wallet adoption, so this assumption fails by construction. The correct procedure for RDD randomization inference is to permute the **cutoff location** (placebo cutoffs), not treatment assignment. As a result, the reported $p = 0.434$ may reflect the size distortions of an inappropriate permutation scheme rather than genuine failure to reject the null. Placebo cutoffs are already reported in Table 3 and could serve this function with proper aggregation.

---

### 2. Minor Issues

**[MINOR-1] Inconsistent reporting of optimal bandwidth**

The MSE-optimal bandwidth is stated as $h^* = 14.24$ in the abstract, Section 3.2, Section 5.1, and Section 6.1, but written as $h^* = 14.2$ in Section 5.2. Should be standardized throughout.

**[MINOR-2] Equation (3): degree of $g(\cdot)$ unspecified**

The text calls $g(\cdot)$ a "flexible polynomial" without specifying the degree. The baseline uses $p=1$ (consistent with Equation (2)), but a reader comparing Equations (2) and (3) cannot infer this. Specifying $g(\cdot) = \beta_1(\cdot) + \beta_2 D_i(\cdot)$ for $p=1$, or stating the degree explicitly, removes the ambiguity.

**[MINOR-3] Equation (3) notation does not reflect the bandwidth change**

The covariate-adjusted specification uses $h = 34.2$ years, disclosed in Section 5.1. However, Equation (3) carries no bandwidth subscript or qualifier to distinguish it from Equation (2)'s $h^* = 14.24$ window. Writing $|A_i - 65| \le h_{\text{cov}}$ in Equation (3) and defining $h_{\text{cov}} = 34.2$ in the text would eliminate the ambiguity.

---

### 3. What Was Resolved from Round 3

The Round 3 review was limited to the three bibliography entries visible before truncation. With the full body now present:
- Equation (1)'s limit notation ($\downarrow$/$\uparrow$) is correct.
- Equation (2) specification is internally consistent.
- All three equation cross-references (`\ref{eq:itt}`, `\ref{eq:rdd}`, `\ref{eq:rdd_covariates}`) match their labels.
- The $t$-statistic claim ($-0.027/0.005 = -5.4$) is arithmetically correct.
- The covariate-adjusted CI arithmetic checks out: $-0.027 \pm 1.96 \times 0.005 = [-0.037, -0.017]$ ✓

The Round 3 table numerical inconsistencies (INTERNET_HOGAR appearing in both Table 3 and Table 4 with different $N$ and CI widths) remain **unverifiable** from `main.tex` alone since both tables are `\input{}` references — those files were not supplied.

---

```json
{
  "n_critical": 1,
  "n_major": 2,
  "n_minor": 3,
  "top_issues": [
    "CRITICAL: Population mean for active wallet use (15.6%) exceeds ownership (7.4%) — logically impossible since use requires ownership; likely a mislabeling or denominator error in mean computation",
    "MAJOR: Equation (3) omits the D_i * g(A_i-65) slope-interaction term, imposing equal polynomial slopes on both sides of the cutoff — contradicts Equation (2) and Calonico et al. (2019) specification",
    "MAJOR: Randomization inference permutes treatment assignment D_i within [55,75] rather than permuting the cutoff location; invalid under the documented strong age gradient in adoption — p=0.434 may be unreliable",
    "MINOR: h* reported as 14.24 and 14.2 interchangeably across sections",
    "MINOR: Equation (3) carries no bandwidth qualifier despite using h=34.2 instead of h*=14.24"
  ]
}
```