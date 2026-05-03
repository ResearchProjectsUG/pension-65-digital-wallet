## Copy-Edit Report — *Does Crossing the Pensión 65 Eligibility Threshold Increase Digital Wallet Adoption?*

---

### CRITICAL

**C1. Unfilled citation placeholder — Section 2.3, final paragraph of §2.3**
> "The closest recent application to our setting… documents weak first-stage effects on digital savings [CITATION MISSING — insert \citet{} key]."

A raw editorial note was left in the manuscript. The entire sentence must either be filled with a real citation or deleted before submission.

---

**C2. Both placebo cutoffs listed as "age 53" — Section 5.2**
> "Placebo cutoffs at age 53 (i.e., 12 years below the true cutoff) and age 53 (12 years right)…"

The right-side placebo is stated as "age 53" in both occurrences. Given the parenthetical "12 years right," the intended value is age 77 (65 + 12). This must be corrected; as written it renders the robustness check uninterpretable.

---

**C3. Logically incoherent figure caption / description — Section 5.5**
> "rates rise from approximately 4% at age 50 to a maximum of 11% near age 35 (younger adults), and decline monotonically with age."

Age 35 is *younger* than age 50; rates cannot simultaneously rise from age 50 to age 35 and also decline monotonically with age. The intended reading is almost certainly the reverse — rates peak among younger adults (≈ age 30–35) and *decline* toward age 50 and beyond, reaching ≈ 4% near the cutoff. Rewrite to reflect the actual profile shown in the figure.

---

**C4. Likely citation mismatch — Section 2.2**
> "\citet{banerjee2020} find that direct benefit transfers in Indonesia increase savings only when accompanied by financial-literacy components."

The listed reference for this key is Banerjee, Niehaus & Suri (2020), *Universal Basic Income in the Developing World*, *Annual Review of Economics* 11:959–983 — a general review article that does not contain an Indonesia-specific finding on digital transfers and savings. Verify whether this cite should point to a different paper (e.g., a World Bank study on PKH or Kartu Prakerja) and update accordingly.

---

**C5. Bibitem label/body year inconsistencies — References**

Two entries have mismatched years between the `\bibitem[…]` label and the body of the entry:

| Entry | Label year | Body year |
|---|---|---|
| `ardington2016` | 2009 | 2016 |
| `banerjee2020` | 2019 | 2020 |

For `natbib`, the bracketed label controls how the in-text citation renders. These inconsistencies will produce wrong in-text dates. Also note that the body of the Ardington entry lists volume 8(1):22–48, whereas the well-known Ardington, Case & Hosegood paper on labor supply responses in South Africa appeared in *AEJAE* **1**(1):22–48 (2009) — the volume number appears incorrect.

---

### MAJOR

**M1. Wrong word: "insufficient" — Section 1, penultimate paragraph**
> "Existing literature is insufficient on two fronts."

"Insufficient" means *inadequate in quality or quantity*; the authors mean the literature *does not address* these topics, not that it is of poor quality. Replace with "The existing literature is sparse on two fronts" or "The literature is silent on two fronts."

---

**M2. British / American spelling inconsistency — Abstract vs. Section 5.1**
> Abstract: "both estimates are tightly bounded and **centred** on zero."
> Section 5.1: "The estimate is **centered** very close to zero."

Choose one convention and apply it throughout. American ("centered") is standard for U.S. journals; British ("centred") for UK journals.

---

**M3. Redundant compound "urban metropolitan" — Section 1**
> "with explosive growth concentrated in **urban metropolitan** areas."

Metropolitan already denotes urban. Use either "urban areas" or "metropolitan areas."

---

**M4. Vague pronoun "this" after semicolon — Section 3.5**
> "The age-65 eligibility threshold is administratively sharp; **this** provides a natural experiment…"

"This" has no explicit antecedent. Rewrite: "This sharp threshold provides a natural experiment for estimating…"

---

**M5. Non-standard collocation "absorbs into" — Section 5.1**
> "the secular age-related trend that **absorbs into** the nonparametric estimator at the optimal bandwidth."

"Absorbs into" is not idiomatic here. Use "is absorbed by the nonparametric estimator" or "is captured by the nonparametric fit."

---

**M6. Incorrect punctuation: semicolon before subordinating "while" — Section 5.2**
> "produces a test statistic of 2.0**; while** the implementation flags mass-points at integer ages…"

A semicolon cannot precede a subordinating conjunction that opens a dependent clause. Break into two sentences: "…produces a test statistic of 2.0. While the implementation flags mass-points at integer ages, inspection of…"

---

**M7. Colloquial idiom in results — Section 5.4**
> "institutional eligibility does not **move the dial** on digital adoption in any observable subgroup."

"Move the dial" is informal. Replace with "has no detectable effect on" or "does not measurably shift."

---

**M8. Informal register in policy section — Section 6.2**
> "Policymakers **betting on** transfer digitization as a primary financial-inclusion lever…"

"Betting on" is too casual for a policy-implications paragraph. Use "relying on" or "counting on."

---

**M9. Grammatically awkward "policy attention on… should focus" — Section 6.2**
> "policy attention **on** the elderly poor population should focus on the underlying determinants…"

"Policy attention on X should focus on Y" is awkward and produces a doubled "on." Rewrite: "policy directed at the elderly poor should target the underlying determinants…"

---

**M10. Non-parallel structure in future-research list — Section 7**
> "(i) merging Pensión 65 administrative data…; (ii) panel data tracking the same individuals…; (iii) evaluation of complementary policies…"

Items (i) and (iii) are gerund phrases; item (ii) is a bare noun phrase. Revise to "(ii) collecting panel data to track the same individuals over time" to restore parallelism.

---

### MINOR

**m1. Non-standard preposition in "transactions outside cash" — Section 1**
> "roughly one in five adult transactions **outside cash** involved a digital wallet."

"Outside cash" is non-standard. Use "non-cash transactions" or "transactions excluding cash."

---

**m2. Unnecessary hyphen in "age-window" — Section 4.3**
> "within **an age-window** of $[55, 75]$."

No hyphen needed in an attributive noun phrase when the first element is itself a noun. Write "an age window."

---

**m3. Unhyphenated "cashout point" — Section 6.1**
> "beneficiaries treat the disbursement account as a passive **cashout** point."

Hyphenate: "cash-out point."

---

**m4. Unusual phrasing "bear emphasis" — Section 6.2**
> "Three limitations **bear emphasis**."

"Bear emphasis" is not idiomatic. Prefer "Three limitations merit emphasis" or "We note three limitations."

---

**m5. Redundant "the act of" — Section 3.4**
> "they are not affected by **the act of** crossing the eligibility threshold."

"The act of" adds no information. Delete: "they are not affected by crossing the eligibility threshold."

---

**m6. Informal "headline numbers" — Section 2.2**
> "downstream effects… are smaller than **headline numbers** suggest."

"Headline numbers" is informal. Use "aggregate estimates" or "top-line figures."

---

**m7. Awkward "passed through" for digital-platform users — Section 2.1**
> "more than 50% of monthly active adult users of any digital channel **passed through** one of these three platforms."

"Passed through" suggests transit rather than usage. Use "transacted through" or "used" or "were active on."

---

**m8. Inconsistent \bibitem label formatting — References**

Some entries parenthesize the year in the label (`\bibitem[Bachas et~al.(2018)]`) while others do not (`\bibitem[Ardington et~al.2009]`, `\bibitem[Banerjee et~al.2019]`). The `natbib` `authoryear` style requires consistent formatting. Standardize across all entries.

---

### Summary Table

| Section | Issue | Tag |
|---|---|---|
| §2.3 | Unfilled citation placeholder | CRITICAL |
| §5.2 | Both placebo cutoffs listed as "age 53" | CRITICAL |
| §5.5 | Figure description logically incoherent | CRITICAL |
| §2.2 | Banerjee et al. 2020 citation mismatch | CRITICAL |
| References | Bibitem label/body year inconsistencies | CRITICAL |
| §1 | "Existing literature is insufficient" — wrong word | MAJOR |
| Abstract / §5.1 | "centred" vs "centered" | MAJOR |
| §1 | "urban metropolitan" — redundant | MAJOR |
| §3.5 | Vague "this" after semicolon | MAJOR |
| §5.1 | "absorbs into" → "is absorbed by" | MAJOR |
| §5.2 | Semicolon before subordinating "while" | MAJOR |
| §5.4 | "move the dial" — colloquial | MAJOR |
| §6.2 | "Policymakers betting on" — informal | MAJOR |
| §6.2 | "policy attention on… should focus" — awkward | MAJOR |
| §7 | Non-parallel future research list | MAJOR |
| §1 | "outside cash" — non-standard | MINOR |
| §4.3 | "age-window" — unnecessary hyphen | MINOR |
| §6.1 | "cashout" → "cash-out" | MINOR |
| §6.2 | "bear emphasis" → "merit emphasis" | MINOR |
| §3.4 | Redundant "the act of" | MINOR |
| §2.2 | "headline numbers" — informal | MINOR |
| §2.1 | "passed through" — awkward collocation | MINOR |
| References | \bibitem label formatting inconsistency | MINOR |

---

```json
{
  "n_critical": 5,
  "n_major": 10,
  "n_minor": 8,
  "top_issues": [
    "Unfilled citation placeholder '[CITATION MISSING]' left verbatim in Section 2.3 — must be resolved before submission",
    "Both placebo cutoffs identified as 'age 53'; the right-side placebo should be age 77 (65 + 12), rendering the robustness check as written nonsensical",
    "Figure 1 age-profile description is internally contradictory — wallet rates cannot simultaneously 'rise from age 50 to age 35' and 'decline monotonically with age'"
  ]
}
```