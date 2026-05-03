# Research Ideation: Determinantes de Adopción de Billetera Digital en Perú

**Junshi here.** Let me be real with you: this is a SINGLE CROSS-SECTION. That's the binding constraint. No DiD, no event study, no FE. But here's the thing — cross-section with 117,721 observations and rich household identifiers (CONGLOME, UBIGEO, HOGAR) actually opens some seriously underexplored identification strategies. Let's find the best variation IN this data.

---

## Key Themes and Gaps in the Literature

**What's been done:**
- OLS/probit adoption models with standard demographics (age, income, education)
- Supply-side studies: agent network density, bank branch proximity
- Demand-side: financial literacy, trust, risk aversion
- Gender gaps in mobile money (mostly Africa)
- COVID shock and government transfer digitization

**What's missing:**
- Causal estimates of **peer network effects** within households (mostly correlational)
- Clean identification of **infrastructure vs. demand constraints** (chicken-and-egg smartphone/internet)
- **Intensive vs. extensive margin** — having a wallet vs. actually using it (TIENE vs. USA)
- How **social protection transfers** (Pensión 65, Juntos) causally drive adoption
- Whether fintech is **complement or substitute** for formal banking in Peru's context

---

## 10 Research Ideas

---

### Idea 1 — Intra-Household Peer Effects on Digital Wallet Adoption
**Sub-topic:** Social Networks & Peer Effects

**Research Question:** Do household peer effects causally drive digital wallet adoption in Peru, and are these effects stronger for women or lower-income households?

**Method:** IV (Tier 1) — Bramoullé et al. (2009) approach. Instrument for *other household members' adoption* using **their predetermined characteristics** (age, sex, education of others in the HOGAR) that affect own adoption ONLY through peers' adoption decisions. Compute leave-one-out mean adoption rate within household.

**Identification Level: A**
- Source of variation: Characteristics of co-residents (age, gender, education) are plausibly exogenous to individual adoption decisions but strongly predict peers' adoption (first stage)
- Exclusion restriction: Other household member's age/education affects MY adoption only through their wallet adoption — plausible given no direct technology channel
- N = 117,721 with HOGAR identifier → many multi-person households to exploit
- First stage F-stat testable; peer characteristics are pre-determined at birth/arrival

**Data Sources:** ENAHO cross-section (current data — CONGLOME, VIVIENDA, HOGAR, CODPERSO identify household members)

**Novelty:** Peer effects in digital finance are assumed but rarely identified with clean instruments. Peru's multi-generational household structure is PERFECT for this. Untapped in FinTech literature.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 5 | 4 | 5 | 4  | 4  | **4.30**  |

---

### Idea 2 — Pensión 65 Age Cutoff: Government Transfer Digitization (RDD)
**Sub-topic:** Social Protection & Forced Adoption

**Research Question:** Does reaching the Pensión 65 eligibility threshold (age 65) causally increase digital wallet adoption, and does this effect persist beyond initial enrollment?

**Method:** RDD (Tier 1) — Sharp discontinuity at age 65. EDAD is continuous in ENAHO. Individuals just below vs. just above 65 are similar in all predetermined characteristics, but differ in program eligibility. During/post-COVID, Peru's transfers were increasingly paid digitally.

**Identification Level: A**
- Source: Age 65 cutoff for Pensión 65 is legally mandated and cannot be manipulated by individuals
- Running variable: EDAD (continuous, dense around 65 with N=117K)
- McCrary density test to rule out heaping at 65
- Optimal bandwidth via Calonico-Cattaneo-Titiunik (CCT)
- Pre-trends: Not applicable (cross-section), but can test for other discontinuities at placebo ages (60, 70)

**Data Sources:** Current data + verify Pensión 65 district coverage (MIDIS public data for first-stage validation)

**Novelty:** First clean RDD estimate of how RECEIVING government transfers via digital channels causes wallet adoption — not just correlation. Hugely policy-relevant for governments pushing cashless transfers.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 5 | 4 | 5 | 4  | 4  | **4.30**  |

---

### Idea 3 — Internet Infrastructure as Binding Constraint: Cluster-Level IV
**Sub-topic:** Digital Infrastructure

**Research Question:** What is the causal effect of home internet access on digital wallet adoption, separately from demand-side factors?

**Method:** IV (Tier 1) — Use **leave-one-out cluster-level internet penetration rate** (computed from other households in the same CONGLOME) as instrument for individual INTERNET_HOGAR. Then estimate LATE of internet access on TIENE/USA_BILLETERA.

**Identification Level: B**
- Source: Cluster-level internet penetration reflects supply-side infrastructure rollout (geographic reach of ISPs) rather than individual demand
- Exclusion restriction: Mean internet access of neighbors affects MY adoption only through MY internet access (moderate concern: correlated with local development — test with controls for ESTRATO, DOMINIO)
- Strong first stage expected: cluster internet predicts individual internet strongly
- Robustness: Test exclusion via over-ID (add UBIGEO-level characteristics as controls and verify IV stability)

**Data Sources:** Current data — CONGLOME enables exact cluster-level computation

**Novelty:** Disentangles supply constraint (infrastructure) from demand constraint (digital literacy, trust) — the central policy question for connectivity expansion programs.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 4 | 5 | 5 | 3  | 4  | **3.95**  |

---

### Idea 4 — The Adoption-Use Gap: Heckman Selection Model
**Sub-topic:** Adoption Intensity (Extensive vs. Intensive Margin)

**Research Question:** Are the determinants of HAVING a digital wallet (TIENE_BILLETERA) fundamentally different from the determinants of ACTIVELY USING it (USA_BILLETERA), and how large is the selection-corrected usage premium?

**Method:** Heckman two-stage (Tier 2) — First stage: probit for TIENE_BILLETERA; Second stage: conditional on ownership, what drives USA_BILLETERA. Exclusion restriction: find a variable that predicts ownership but not conditional usage.

**Identification Level: C** (selection on observables — moderate threats)
- Candidate exclusion restriction: BANCO_PREVIO (prior bank account) may predict wallet acquisition through bank-offered products like Yape, but less so for active usage conditional on ownership
- Selectivity issue: Can test Mills ratio significance

**Data Sources:** Current data — both TIENE and USA variables available

**Novelty:** The "financial inclusion theater" critique — people have wallets but don't use them. This gap is unstudied in Peru specifically and matters for policy.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 4 | 5 | 4 | 2  | 4  | **3.45**  |

---

### Idea 5 — Informality Penalty in FinTech: Matching + Sensitivity Analysis
**Sub-topic:** Labor Informality & Financial Exclusion

**Research Question:** Does formal employment causally increase digital wallet adoption, and by how much does informality suppress Peru's FinTech market?

**Method:** CEM/PSM matching (Tier 2) — Match formal (FORMAL=1) vs informal (FORMAL=0) workers on EDAD, GENERO, NIVEL_EDUCATIVO, INGHOG2D, DOMINIO. Estimate ATT of formality on adoption. Add Rosenbaum bounds sensitivity analysis.

**Identification Level: C** (selection on observables — endogeneity of formality choice is real)
- Main threat: Selection into formality correlated with unobservables (motivation, social capital) that also drive adoption
- Robustness: Restrict to wage workers only (less selection than self-employed)

**Data Sources:** Current data — FORMAL, OCUPADO, and matching covariates all available

**Novelty:** Informality is Peru's structural fact (70%+ informal). Quantifying the FinTech exclusion it creates is policy-critical and understudied.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 3 | 5 | 5 | 2  | 4  | **3.45**  |

---

### Idea 6 — Gender Gap Decomposition in Digital Finance (Oaxaca-Blinder)
**Sub-topic:** Gender

**Research Question:** What fraction of Peru's gender gap in digital wallet adoption is explained by observable endowments (income, education, smartphone access) vs. unexplained discrimination/behavioral differences?

**Method:** Oaxaca-Blinder decomposition (nonlinear extension for binary outcomes via Fairlie) on TIENE_BILLETERA ~ GENERO. Decompose endowment, coefficient, and interaction effects.

**Identification Level: C** (descriptive decomposition — no causal claim on the unexplained gap)
- Well-established methodology, transparently descriptive
- Policy-relevant: tells you WHETHER to invest in supply (endowments) vs. demand (cultural change)

**Data Sources:** Current data — GENERO, all covariates available

**Novelty:** Fairlie decomposition applied to Latin American FinTech adoption is rare. Peru's gender dynamics (machismo + high female informality) make this especially interesting.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 3 | 5 | 4 | 2  | 4  | **3.30**  |

---

### Idea 7 — Bank Account as Complement or Substitute: IV on Prior Banking
**Sub-topic:** Traditional Banking Complementarity

**Research Question:** Does having a prior formal bank account (BANCO_PREVIO) cause higher digital wallet adoption — complementarity — or does it crowd out adoption among those who already have financial access?

**Method:** IV (Tier 1) — Instrument for BANCO_PREVIO using UBIGEO-level bank branch density (external SBS data). Bank density in one's district at some pre-period predicted prior banking access but is exogenous to individual wallet adoption.

**Identification Level: A-B**
- Source: District bank branch density is a supply-side variable determined by bank expansion decisions, not individual preferences
- Need: External SBS (Superintendencia de Banca) data on branches by UBIGEO — publicly available
- Threat: Bank density also proxies economic development → control for INGHOG2D, POBREZA, DOMINIO; test sensitivity

**Data Sources:** Current data + SBS district-level branch data (public)

**Novelty:** Complement vs. substitute debate is OPEN in the literature. If fintech substitutes banking, it democratizes access. If it complements, it deepens existing inequality.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 4 | 3 | 5 | 3  | 4  | **3.65**  |

---

### Idea 8 — Income Heterogeneity: Quantile Treatment Effects on Adoption
**Sub-topic:** Income Distribution & Poverty

**Research Question:** Are the marginal returns to digital infrastructure (smartphone, internet) uniform across the income distribution, or are adoption barriers uniquely binding for near-poor households?

**Method:** Quantile regression of TIENE/USA_BILLETERA on INGHOG2D, SMARTPHONE, INTERNET_HOGAR — estimate at p10, p25, p50, p75, p90. Test equality of coefficients across quantiles.

**Identification Level: C** (no causal claim — descriptive heterogeneity)
- Cleanly descriptive but HIGH value for policy targeting
- N=117K ensures tight quantile estimates even in tails

**Data Sources:** Current data — INGHOG2D, GASHOG2D, POBREZA available

**Novelty:** Most adoption studies report average effects. Peru's extreme income inequality means the DISTRIBUTION of effects matters enormously for universal access policies.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 3 | 5 | 4 | 2  | 3  | **3.10**  |

---

### Idea 9 — Poverty Line Discontinuity and Welfare Transfer Digitization (RDD)
**Sub-topic:** Poverty Targeting & Conditional Programs

**Research Question:** Is there a discontinuity in digital wallet adoption at the poverty line — driven by Juntos/Bono Yanapay program eligibility — that reveals how conditional transfer digitization forces financial inclusion?

**Method:** RDD (Tier 1) — Running variable: INGHOG2D normalized around poverty line threshold. Sharp or fuzzy depending on program design.

**Identification Level: A (if poverty line is binding eligibility cutoff)**
- Critical assumption: Peru's cash transfer programs use poverty threshold as eligibility criterion AND disbursed digitally (partially true for Bono Yanapay)
- Threat: Poverty misclassification and measurement error in income (ENAHO well-known for this) → fuzzy RDD specification
- Bandwidth: Use CCT optimal bandwidth; test donut RDD to address bunching

**Data Sources:** Current data — POBREZA already constructed, INGHOG2D is continuous running variable

**Novelty:** RDD on poverty line to study forced financial inclusion through transfers — sharp natural experiment embedded in welfare state design.

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 4 | 3 | 4 | 3  | 3  | **3.30**  |

---

### Idea 10 — Smartphone as Gateway: Stratum IV for Infrastructure Demand Separation
**Sub-topic:** Mobile Technology Access

**Research Question:** What is the LATE of smartphone ownership on digital wallet adoption among Peruvians, separating infrastructure supply from consumer demand?

**Method:** IV (Tier 1) — Instrument for SMARTPHONE using **ESTRATO** (socioeconomic stratum classification, determined by ENAHO using dwelling characteristics, NOT individual income or preferences). Stratum affects smartphone ownership through neighborhood wealth but is exogenous to individual wallet preferences conditional on own income.

**Identification Level: B**
- Source: ESTRATO is assigned based on dwelling census characteristics — supply-side, not individual decision
- Exclusion restriction: ESTRATO affects adoption only through smartphone ownership, not directly (debatable; control for INGHOG2D, NIVEL_EDUCATIVO)
- First stage: Strong — stratum is one of the strongest predictors of smartphone ownership

**Data Sources:** Current data — SMARTPHONE, ESTRATO directly available

**Novelty:** Separates the chicken-and-egg problem: does low adoption reflect no smartphones, or no demand even WITH smartphones?

| N | F | I | ID | EE | **Total** |
|---|---|---|----|----|-----------|
| 3 | 5 | 4 | 3  | 4  | **3.70**  |

---

## Summary Ranking

| Rank | Idea | Sub-topic | ID Level | Score |
|------|------|-----------|----------|-------|
| 1 | Intra-Household Peer Effects (IV) | Social Networks | A | **4.30** |
| 2 | Pensión 65 Age RDD | Social Protection | A | **4.30** |
| 3 | Cluster Internet IV | Digital Infrastructure | B | **3.95** |
| 4 | Smartphone Stratum IV | Mobile Technology | B | **3.70** |
| 5 | Banking Complementarity IV | Traditional Banking | A-B | **3.65** |
| 6 | Heckman Extensive/Intensive | Adoption Intensity | C | **3.45** |
| 7 | Formality Matching | Labor Informality | C | **3.45** |
| 8 | Poverty Line RDD | Poverty Targeting | A | **3.30** |
| 9 | Gender Oaxaca-Blinder | Gender | C | **3.30** |
| 10 | Income Quantile Regression | Income Distribution | C | **3.10** |

---

## TOP 3 ELABORATED IDEAS

---

### #1 — Intra-Household Peer Effects on Digital Wallet Adoption
**Sub-topic: Social Networks | Identification: Level A | Score: 4.30**

**The Core Argument:** Digital wallet adoption is a social technology — the value of Yape or Plin depends on who ELSE uses it. Peru's multi-generational households (average MIEPERHO > 3) create a natural laboratory for peer effects. But every correlational study suffers from the reflection problem (Manski, 1993): you can't tell if household members adopt together because of peer influence OR because they share the same income, neighborhood, and access.

**The Identification Strategy:**
The Bramoullé et al. (2009) exclusion of network characteristics solves this. Specifically:
- **First stage:** Regress household member j's wallet adoption on j's own characteristics (age_j, educ_j, gender_j) — these predict j's adoption
- **Second stage:** Use predicted adoption of j as instrument for actual adoption of j → effect on i's adoption
- The exclusion restriction: peer i's age and education affect MY (ego's) adoption ONLY through peer's adoption, not directly

**Estimation:**
```
Stage 1: adopt_j = α·age_j + β·educ_j + γ·gender_j + δ·income_j + ε_j
Stage 2: adopt_i = φ·adopt_j_hat + X_i'θ + u_i  (2SLS)
```
Control for shared household characteristics (INGHOG2D, INTERNET_HOGAR) to isolate the peer channel.

**Expected Results:**
- Peer effects in mobile money adoption are large in Africa (Jack & Suri, 2014): 10-20 pp spillovers
- Peru's data with MIEPERHO allows estimation of spillovers by type: young→old, male→female, educated→less-educated
- Strong policy implication: targeting specific household members (young, educated) with adoption incentives creates multiplier effects

**Week 1 Plan:**
1. Merge individual records to household level using CONGLOME+VIVIENDA+HOGAR
2. Compute household peer variables: mean adopt, characteristics of all OTHER members
3. Run first-stage F-stat to confirm instrument strength
4. Report 2SLS vs. OLS comparison to quantify upward/downward bias

---

### #2 — Pensión 65 Age Cutoff: Does Government Transfer Digitization Drive Adoption?
**Sub-topic: Social Protection | Identification: Level A | Score: 4.30**

**The Core Argument:** Peru's Pensión 65 program provides S/250/month to citizens aged 65+. During COVID, the Peruvian government aggressively pushed digital disbursement of transfers (Bono Yanapay was fully digital). If Pensión 65 recipients were pushed to get wallets to receive transfers, we'd expect a DISCONTINUOUS jump in adoption at age 65 — the cleanest natural experiment in this dataset.

**The Identification Strategy:**
Sharp RDD at age 65. EDAD is continuous in ENAHO; N=117K means dense coverage around the threshold.

**Estimation:**
```
adopt_i = α + τ·1(EDAD≥65) + f(EDAD-65) + ε_i
```
- Local linear regression on both sides of the cutoff
- CCT optimal bandwidth selection
- McCrary test for heaping at 65 (manipulation check)
- Placebo discontinuities at ages 60, 70 (falsification)

**What Makes This Especially Interesting:**
- The effect should be stronger for people with DOMINIO=rural (where digital was the ONLY disbursement option, no physical agent nearby)
- Heterogeneity by INTERNET_HOGAR and SMARTPHONE — does the effect disappear for those without infrastructure? This tells you about barriers to digital inclusion EVEN WHEN INCENTIVIZED

**Threats and Robustness:**
- Sorting: Can older people manipulate their reported age? Unlikely in ENAHO's registry-based data
- Donut RDD: Exclude ±1 year from cutoff to test for bunching sensitivity
- Bandwidth sensitivity: Report ITK, CCT, half-bandwidth, double-bandwidth

**Week 1 Plan:**
1. Plot adoption rate by EDAD — visual check for discontinuity at 65
2. McCrary density test on EDAD
3. Run rdrobust with CCT bandwidth; report reduced-form estimate
4. Heterogeneity: split by DOMINIO (urban/rural), INTERNET_HOGAR, SMARTPHONE

---

### #3 — Infrastructure as Fate: Cluster-Level Internet Penetration IV
**Sub-topic: Digital Infrastructure | Identification: Level B | Score: 3.95**

**The Core Argument:** Is low digital wallet adoption in Peru a DEMAND problem (people don't want wallets) or a SUPPLY problem (they can't use them without internet)? OLS of internet access on adoption is hopelessly endogenous — richer, more educated, more motivated households both have internet AND adopt wallets. Disentangling this is the #1 policy question for universal financial inclusion.

**The Identification Strategy:**
Use the CONGLOME (cluster of ~12-15 households) as the source of supply-side variation. Internet penetration in one's cluster reflects ISP rollout decisions, geographic terrain, and infrastructure investment — NOT individual household demand preferences.

**Instrument Construction:**
```
Z_ij = (1/(n_j-1)) · Σ_{k≠i} INTERNET_HOGAR_k  [leave-one-out cluster mean]
```
This is valid because: (1) ISP rollout decisions target clusters, not individuals; (2) neighbors' internet access doesn't directly cause MY wallet adoption — it only matters through MY access.

**The Two-Stage Story:**
- First stage: Z_ij → INTERNET_HOGAR_i (strong — F > 100 expected with 117K obs)
- Second stage: INTERNET_HOGAR_i_hat → TIENE/USA_BILLETERA_i (LATE)
- Interpretation: The effect of internet access for people induced to connect by cluster-level infrastructure

**Key Heterogeneity Tests:**
- Split by DOMINIO — does the IV effect disappear in Lima (saturated market) but remain strong in provinces?
- Test complementarity with SMARTPHONE — does internet matter MORE when households also have smartphones?
- Separate effects for TIENE vs USA — does infrastructure solve the ownership gap or the usage gap?

**Threats:**
- Cluster-level internet is correlated with cluster development (ESTRATO) → control for ESTRATO, POBREZA, and DOMINIO
- Spillovers: neighbors' internet use might directly increase my adoption through social demonstration → addresses Idea #1 mechanism

**Week 1 Plan:**
1. Compute leave-one-out cluster internet rate using CONGLOME identifier
2. Run first stage: regress INTERNET_HOGAR on Z_ij; report F-stat
3. Run 2SLS; compare to OLS to assess bias direction
4. Report reduced-form (cluster internet → adoption) as robustness check

---

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "Intra-Household Peer Effects on Digital Wallet Adoption: IV Evidence from Peru",
      "research_question": "Do household peers causally drive digital wallet adoption in Peru, and are spillover effects asymmetric by gender and age?",
      "method": "2SLS IV using peers' predetermined characteristics (age, education, gender of co-residents) as instruments for peers' adoption",
      "identification_level": "A",
      "identification_source": "Bramoullé et al. (2009) exclusion: other household members' predetermined characteristics predict their adoption (first stage) but affect ego's adoption only through the peer's adoption decision, not directly",
      "sub_topic": "Social Networks & Peer Effects",
      "data_sources": ["ENAHO cross-section (current data) — CONGLOME, VIVIENDA, HOGAR, CODPERSO enable household member linkage"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "identification": 4,
      "expected_effect": 4,
      "total_score": 4.30,
      "pitch": "Peru's multi-generational households are a natural laboratory for peer effects in FinTech adoption. Using co-residents' predetermined characteristics as instruments for their wallet adoption, we can estimate causal spillovers — critical for designing targeted adoption subsidies that exploit household network multipliers.",
      "first_experiment": "Merge individual records at CONGLOME+VIVIENDA+HOGAR level, compute leave-one-out peer characteristics, run 2SLS with Kleibergen-Paap F-stat, and compare to OLS to assess the reflection problem bias"
    },
    {
      "rank": 2,
      "title": "Does Receiving Government Transfers Digitally Force Financial Inclusion? RDD at Pensión 65 Eligibility",
      "research_question": "Does crossing the Pensión 65 age eligibility threshold (age 65) cause a discrete jump in digital wallet adoption among Peruvian adults?",
      "method": "Sharp RDD using EDAD as the continuous running variable with cutoff at age 65",
      "identification_level": "A",
      "identification_source": "Age 65 is a legally mandated, administratively sharp eligibility threshold for Pensión 65. Individuals just below and above 65 are similar in all pre-determined characteristics — the only difference is program eligibility and the associated push toward digital transfer receipt.",
      "sub_topic": "Social Protection & Forced Financial Inclusion",
      "data_sources": ["ENAHO cross-section (EDAD variable) — N=117K ensures dense observations around age 65; MIDIS district coverage for first-stage validation (supplementary)"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "identification": 4,
      "expected_effect": 4,
      "total_score": 4.30,
      "pitch": "Governments worldwide are betting that digitizing cash transfers will force financial inclusion — but does it actually work? The Pensión 65 age cutoff provides a rare clean experiment: does an exogenous push to receive money digitally cause wallet adoption, especially in rural areas with no physical payment alternatives?",
      "first_experiment": "Plot raw adoption rate by EDAD year-by-year to visually inspect the discontinuity at 65, run McCrary density test to rule out manipulation, then estimate rdrobust with CCT bandwidth and report the reduced-form jump"
    },
    {
      "rank": 3,
      "title": "Infrastructure as Fate: Causal Effect of Internet Access on Digital Wallet Adoption via Cluster-Level IV",
      "research_question": "What is the causal effect of household internet access on digital wallet adoption, and does infrastructure supply fully explain the urban-rural adoption gap?",
      "method": "2SLS IV using leave-one-out cluster-level internet penetration rate (computed from other households in the same CONGLOME) as instrument for individual INTERNET_HOGAR",
      "identification_level": "B",
      "identification_source": "ISP rollout decisions target geographic clusters based on terrain, population density, and infrastructure cost — not individual household demand preferences. Cluster-level internet penetration is a supply-side shifter, exogenous to individual adoption decisions.",
      "sub_topic": "Digital Infrastructure & Connectivity",
      "data_sources": ["ENAHO cross-section (current data) — CONGLOME identifier enables exact leave-one-out cluster mean computation"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "identification": 3,
      "expected_effect": 4,
      "total_score": 3.95,
      "pitch": "Is low FinTech adoption in Peru a demand failure or a supply failure? This IV design — using neighbors' internet access as a supply-side instrument — separates what people CAN'T do (no connectivity) from what they WON'T do (no demand). The answer determines whether the policy fix is infrastructure investment or behavioral nudges.",
      "first_experiment": "Compute leave-one-out cluster internet rate by CONGLOME, run first-stage regression and report Kleibergen-Paap F-stat, then compare 2SLS vs OLS estimates for TIENE_BILLETERA and USA_BILLETERA separately"
    }
  ],
  "identification_warning": null
}
```