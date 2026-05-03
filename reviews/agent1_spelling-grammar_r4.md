## Copy-Edit Report — Round 4

**Scope**: Language, style, typography, and number formatting only. Prior round numerical/table issues (Round 3 CRITICAL-1: Table 3 vs Table 4 covariate discrepancy) are not re-raised here but remain unaddressed in the body text.

---

### Round 2 Carry-Forward

**[MAJOR-CARRY] "centred" / "centered" inconsistency — unresolved from Round 2.**
Both spellings appear in the same document. American "centered" is used in §5 ("The estimate is centered very close to zero"), while British "centred" appears in §1 ("centred on zero"), §5 ("centred near zero"), and §5 heterogeneity ("centred near zero"). Choose one orthography throughout and apply it consistently. Given that other American spellings are used (e.g., "behavior," "labor"), the correct choice is **"centered"**.

---

### Abstract

**[MAJOR-1] Ambiguous phrase: "other age-65-specific changes on the running variable."**
The sentence reads: *"the combined effect of crossing the institutional threshold associated with Pensi\'on 65 and other age-65-specific changes on the running variable."* The phrase "changes on the running variable" is opaque — a reader cannot tell whether this modifies "threshold" or "changes." Intended meaning is likely: *"…and any other institutional changes that occur at the age-65 threshold."* Revise accordingly.

**[MINOR-1] "Governments worldwide are betting…" — informal register.**
"Betting" is colloquial in an abstract submitted to a top-field journal. Replace with "positing," "hypothesizing," or "premised on the assumption."

---

### Section 1 (Introduction)

**[MAJOR-2] Terminological contradiction: "sharp regression discontinuity."**
The sentence reads: *"We exploit this design with a sharp regression discontinuity (RDD) using the 2024 round of ENAHO."* The paper has just explained, in the preceding paragraph, that the design is *fuzzy* with respect to program receipt. Calling it a "sharp RDD" contradicts the stated characterization. Drop "sharp": *"We exploit this design with a regression discontinuity (RDD)…"*

**[MAJOR-3] Missing words: "an ITT estimate of institutional access on digital adoption."**
The phrase is grammatically incomplete. Should read: *"an ITT estimate of the effect of institutional access on digital adoption."*

**[MINOR-2] Flag word: "Critically, the disbursement mechanism is digital."**
"Critically" functions here as a rhetorical intensifier, not an analytical judgment. Delete it and restructure: *"The disbursement mechanism is digital:…"*

**[MINOR-3] Awkward preposition: "outside cash."**
*"roughly one in five adult transactions outside cash"* — "outside cash" is non-standard. Use "non-cash" or "beyond cash."

**[MINOR-4] Word choice: "Existing literature is insufficient on two fronts."**
"Insufficient" does not accurately describe an existing body of work; it describes a gap within it. Use "thin," "limited," or "incomplete" instead.

---

### Section 2 (Literature Review)

**[MINOR-5] Hyphenation error: "sharply-identified evidence."**
Adverbs ending in *-ly* do not take hyphens before adjectives. Write **"sharply identified evidence"**.

---

### Section 4 (Empirical Strategy)

**[MAJOR-4] Circular self-reference.**
Within §4 (labeled `\label{sec:strategy}`), the estimation-equations subsection states: *"As discussed in Section~\ref{sec:strategy}, $\tau$ is interpreted as a local ITT effect…"* This is a forward reference to the section the reader is already in. Change to *"As discussed above,"* or refer to the specific subsection/assumption that was laid out earlier (Equation~\ref{eq:itt} or the three assumptions enumerated in §4.1).

---

### Section 5 (Results)

**[MINOR-6] Flag word: "Importantly, this covariate-adjusted specification uses a wider bandwidth."**
Delete "Importantly." The sentence is already clear without the intensifier: *"This covariate-adjusted specification uses a wider bandwidth…"*

**[MINOR-7] Ambiguous single value for two donut-hole specifications.**
*"yield estimates of $-0.001$"* — both the $\pm 0.5$ and $\pm 1.0$ donut-hole specs apparently yield the same value. If they differ, report both. If they genuinely agree, write *"both yield $-0.001$"* to make the equality explicit rather than leaving readers to infer it.

**[MINOR-8] Confusing "largest/smallest" for signed estimates.**
*"the largest subgroup point estimate is $-0.021$…and the smallest is $+0.004$"* — in the context of a policy effect where positive is the predicted direction, calling $-0.021$ the "largest" is counterintuitive. Revise to: *"the most negative estimate is $-0.021$…and the most positive is $+0.004$."*

**[MINOR-9] "centred near zero"** — see MAJOR carry-forward above. Standardize to "centered."

**[MINOR-10] Redundant statement about no discontinuity.**
In §5.4 (visual evidence): *"…with no visible jump at the threshold. There is no visible discontinuity at age 65."* The second sentence repeats the first verbatim. Delete one.

---

### Section 6 (Discussion)

**[MAJOR-5] Limitations section structure contradicts stated count.**
The paper states *"Five limitations bear emphasis"* but delivers them inconsistently: the first two carry bold headers (**Integer running variable**, **Dual eligibility**) while the remaining three are labeled **First / Second / Third** without headers — and are structurally run together under the **Dual eligibility** paragraph, making it unclear whether "First" continues the dual-eligibility discussion or opens a new limitation. Apply bold headers to all five, or renumber them uniformly as a numbered list.

**[MINOR-11] Awkward construction: "dilutes…by the factor of non-take-up."**
*"The intent-to-treat estimate dilutes whatever effect exists among actual recipients by the factor of non-take-up."* More natural: *"…is attenuated by the rate of non-take-up."*

**[MINOR-12] Informal: "passive cashout point."**
"Cashout" is informal. Replace with *"cash-withdrawal point"* or *"a passive mechanism for withdrawing cash."*

**[MINOR-13] "works best when paired" — "best" is unjustified.**
The paper documents a null under the standalone institutional channel; it does not document a paired condition for comparison. *"Best"* implies a tested ranking. Use *"is more likely to be effective when paired"* or *"works better when paired."*

**[MINOR-14] Informal: "Policymakers betting on transfer digitization."**
Same register issue as the abstract. Replace with *"Policymakers relying on"* or *"Policymakers counting on."*

**[MINOR-15] Preposition: "policy attention on the elderly poor."**
*"Policy attention on the elderly poor population should focus on…"* — "attention on" is non-standard. Write *"Policy attention directed at the elderly poor"* or *"Policymakers targeting the elderly poor."*

---

### Section 7 (Conclusion)

**[MINOR-16] "bound it above" → "bound it from above."**
*"our intent-to-treat estimates in the ENAHO sample bound it above by approximately three percentage points"* — the standard idiom is **"bound it from above."**

---

### Summary

| Location | Issue | Tag |
|---|---|---|
| Throughout | "centred" / "centered" inconsistency (unresolved from Round 2) | **MAJOR** |
| Abstract | "other age-65-specific changes on the running variable" — ambiguous | **MAJOR** |
| §1 | "sharp regression discontinuity" contradicts fuzzy design characterization | **MAJOR** |
| §1 | "an ITT estimate of institutional access on digital adoption" — missing words | **MAJOR** |
| §4 | Circular self-reference: `\ref{sec:strategy}` within `sec:strategy` | **MAJOR** |
| §6 | Limitations: 5 stated, inconsistently formatted | **MAJOR** |
| Abstract | "betting" — informal | MINOR |
| §1 | "Critically" — intensifier, delete | MINOR |
| §1 | "outside cash" → "non-cash" | MINOR |
| §1 | "insufficient on two fronts" → "incomplete/limited" | MINOR |
| §2 | "sharply-identified" → "sharply identified" | MINOR |
| §5 | "Importantly" — delete | MINOR |
| §5 | Ambiguous singular value for two donut specs | MINOR |
| §5 | "largest/smallest" confusing for signed estimates | MINOR |
| §5 | "centred near zero" — standardize | MINOR |
| §5 | Redundant no-discontinuity statement | MINOR |
| §6 | "dilutes…by the factor of" → "attenuated by the rate of" | MINOR |
| §6 | "cashout point" → "cash-withdrawal point" | MINOR |
| §6 | "works best" → "works better" | MINOR |
| §6 | "betting on transfer digitization" → "relying on" | MINOR |
| §6 | "policy attention on" → "policy attention directed at" | MINOR |
| §7 | "bound it above" → "bound it from above" | MINOR |

```json
{
  "n_critical": 0,
  "n_major": 6,
  "n_minor": 16,
  "top_issues": [
    "MAJOR (unresolved from Round 2): 'centred'/'centered' inconsistency throughout — standardize to American 'centered'",
    "MAJOR: Introduction calls the design 'a sharp regression discontinuity' despite the paper explicitly characterizing it as fuzzy — contradicts the methodology",
    "MAJOR: Circular self-reference in §4 — 'As discussed in Section~\\ref{sec:strategy}' appears within that same section; change to 'As discussed above'",
    "MAJOR: Limitations section promises five items but delivers two with bold headers and three as unlabeled First/Second/Third items — apply uniform formatting",
    "MAJOR: Abstract phrase 'other age-65-specific changes on the running variable' is ambiguous — revise to 'any other institutional changes at the age-65 threshold'",
    "MAJOR: §1 missing words — 'an ITT estimate of institutional access on digital adoption' should read 'an ITT estimate of the effect of institutional access on digital adoption'"
  ]
}
```