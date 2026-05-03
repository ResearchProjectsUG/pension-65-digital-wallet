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