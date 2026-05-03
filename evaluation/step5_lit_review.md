## Literature Review: Digital Wallet Adoption via Government Transfer Digitization — Pensión 65 RDD

> **Note on sourcing**: The Semantic Scholar query returned zero verified results. Per the task instructions, I will not fabricate citations. The closest-papers section draws from my training knowledge and is clearly labeled as unverified — treat those references as leads to confirm, not citable sources. The methodological and gap analysis stands independently.

---

## 1. Closest Existing Papers

**No verified citations were returned by Semantic Scholar.** From training-time knowledge, the following are plausible close matches — *verify before citing*:

| Lead | Why relevant | Likely difference |
|------|-------------|------------------|
| Bernal, Rigolini & Maguiña (various years) on Pensión 65 | Impact evaluations of the same program | Focus on consumption/health, not financial inclusion |
| Dupas & Robinson (2013, JPE) — savings accounts Kenya | Demand-side barriers to formal finance | Supply-side push via G2P, not voluntary take-up |
| Bachas, Gertler, Higgins & Seira (2021, AER) — Mexico OPORTUNIDADES debit cards | Closest structural analog: G2P digitization → formal finance | Mexican context, different program, different outcome (savings behavior) |
| Jack & Suri (2014, AER) — M-Pesa Kenya | Foundational: mobile money → welfare | Not G2P-driven; market-led diffusion mechanism |
| Muralidharan, Niehaus & Sukhtankar (2016, AER) — Andhra Pradesh smart cards | G2P → leakage reduction, not adoption per se | India, different outcome variable |

The **Bachas et al. (2021)** paper is almost certainly the anchor reference this paper would sit next to — it uses Bansefi/OPORTUNIDADES debit card rollout in Mexico to show G2P digitization generates savings behavior even among first-time account holders. The Peru/Pensión 65 version would contribute a different country, elderly population, and wallet-specific (not account-specific) outcome.

---

## 2. Methodological Precedents

### RDD on Pension Age Thresholds

Age-65 cutoffs have been used credibly in other contexts (US Social Security, Brazilian BPC, Chilean PBS). The identification logic is well-established: the running variable (age) is not manipulated because people cannot choose their birthdate. Standard concerns:

- **Density test**: McCrary (2008) is appropriate; bunching at 65 would suggest strategic misreporting, which in Peru's context with poor civil registration in rural areas is a genuine concern — *in reverse* (people slightly below 65 may claim to be older to access benefits)
- **Compound discontinuities**: Age 65 triggers other things simultaneously (formal retirement eligibility, health behavior changes, reduced labor force participation). Any jump in digital adoption at 65 may reflect retirement-induced technology adoption, not Pensión 65 specifically.

### G2P Digitization as Forced Inclusion

The Bachas et al. design (rollout variation across municipalities over time) is methodologically stronger than a single cross-section RDD because it can difference out age trends. Their first-stage is clean: account ownership jumps mechanically when the card is issued. The proposed design lacks this clean first-stage unless it can show that *receiving Pensión 65* (not just crossing age 65) discretely predicts wallet ownership.

---

## 3. Gap Analysis

### What gap does this fill?
The literature on G2P digitization mostly comes from Africa (M-Pesa context) and South Asia (Andhra Pradesh). Latin American evidence is sparse outside Mexico. Peru's Pensión 65 targets a particularly hard-to-reach population (rural elderly poor) where the "forced inclusion" hypothesis is most plausible — there are no physical payment alternatives, so digital or nothing.

### Is the gap genuine?

**Partly genuine, partly structural.** Three reasons the gap may exist for non-trivial reasons:

1. **Data problem**: ENAHO is cross-sectional. Observing a jump in digital wallet adoption at age 65 in a single cross-section conflates the *program effect* with *cohort effects*. People born in 1961 (age 65 today) adopted smartphones at a different life stage than people born in 1962 (age 64). This is not identified away by RDD — it is a violation of the continuity assumption that is inherently untestable in a single cross-section.

2. **Fuzzy, not sharp**: Pensión 65 is *means-tested and requires registration*. Not everyone who crosses age 65 receives it. The proposed design conflates Intent-to-Treat (turning 65) with Treatment (receiving digitized payments). A sharp RDD on age 65 estimates the reduced-form effect of *eligibility*, not of *digital payment receipt*. That's defensible but requires a clean first stage to be credible — does wallet ownership jump specifically among Pensión 65 recipients?

3. **Mechanism uncertainty**: Has Pensión 65 actually fully digitized payments? If a substantial fraction of beneficiaries still receive cash through agents or physical kiosks, the forcing mechanism collapses. This is a first-order empirical question the idea does not address.

### Could the gap be artificial?
Yes — the most likely reason this hasn't been done is the **cross-sectional identification problem**. A panel version of ENAHO, or a rollout design using MIDIS district-level digitization waves, would be far more credible. The single cross-section makes cohort effects an unresolvable confound.

---

## 4. Identification Assessment

| Dimension | Assessment |
|-----------|-----------|
| **Source of variation** | Age-65 cutoff for Pensión 65 eligibility — clearly stated, plausible in principle |
| **Identification tier** | Nominally **Tier 1** (sharp RDD), but degrades to **Tier 2-3** in practice |
| **Main threat** | Cohort effects in a cross-section: people aged 64 vs. 65 belong to different birth cohorts with different lifetime digital exposure — RDD does NOT difference this out |
| **Second threat** | Compound discontinuities at 65 (retirement, health, labor supply) |
| **Third threat** | Non-random selection into Pensión 65 receipt conditional on crossing 65 (means-testing + registration barriers) → fuzzy design |
| **Pre-trends** | Cannot be tested — single cross-section provides one time point; no pre/post |
| **Manipulation** | Unlikely to be *downward* (no one delays aging), but upward misreporting of age (claiming 65+ to access benefits) is possible in rural Peru with weak civil registration |
| **Overall** | The RDD logic is sound in principle, but cross-sectional data makes the continuity assumption unverifiable. The cohort confound is the paper's single biggest vulnerability. |

**Bottom line on identification**: This would be a respectable Tier 1 design *with panel data or a rollout design*. With a single cross-section and age as the running variable, the cohort effect confound is severe enough that many referees will reject the continuity assumption outright. The paper needs either (a) panel data to compare the same individual before/after turning 65, or (b) a rollout design using MIDIS district-level digitization waves as the shock, or (c) a very careful argument for why cohort effects cannot explain the jump — which is difficult given the plausibility of digital adoption rising steadily across younger cohorts.

---

## 5. Positioning Statement

If this paper successfully addresses the cohort confound — either through a fuzzy RDD that conditions on Pensión 65 receipt or through auxiliary tests ruling out cohort effects — it would be cited in future G2P literature as: *"Among the few causal estimates of government transfer digitization on financial inclusion in Latin America, [Author] exploits Peru's Pensión 65 age eligibility cutoff to show that [result], consistent with/in contrast to the forced-inclusion findings of Bachas et al. (2021) in Mexico."* Without resolving the identification weakness, it would likely only appear in grey literature or descriptive reports, not a top-field journal.

---

```json
{
  "closest_papers": [
    "Bachas, Gertler, Higgins & Seira (2021, AER) — OPORTUNIDADES debit cards Mexico",
    "Muralidharan, Niehaus & Sukhtankar (2016, AER) — Andhra Pradesh G2P smart cards",
    "Jack & Suri (2014, AER) — M-Pesa mobile money Kenya",
    "Dupas & Robinson (2013, JPE) — savings account take-up Kenya"
  ],
  "gap_is_genuine": false,
  "gap_reason": "The gap is partly artificial: the single cross-sectional data structure makes the cohort effect an unresolvable confound in an age-running-variable RDD. The identification problem is likely why this specific design has not been published — not because the question is unimportant, but because the data structure cannot credibly answer it. The question itself is genuine and policy-relevant; the proposed identification strategy is not strong enough to fill it credibly.",
  "novelty_assessment": "MEDIUM",
  "methodological_risk": "HIGH",
  "positioning": "This paper would be the first to apply an RDD design to Pensión 65 age eligibility as a source of exogenous variation in digital wallet adoption in Peru — but its contribution to the causal literature on G2P digitization and financial inclusion hinges entirely on whether the cohort effect confound can be ruled out, which single cross-sectional data cannot do."
}
```