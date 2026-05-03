```json
{
  "topic": "Determinantes de adopción de billetera digital en Perú",
  "data_profile": {
    "rows": 117721,
    "cols": 27,
    "structure": "cross-sectional",
    "panel": false,
    "id_cols": ["CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO", "UBIGEO"],
    "time_cols": [],
    "warnings": [
      "Single cross-section: no time variation → panel methods (FE, DiD, event study) are NOT applicable",
      "Low adoption rate (7% for TIENE_BILLETERA): sparse outcome → watch for prediction bias",
      "Missing data: NIVEL_EDUCATIVO (9%), OCUPADO (27%), multiple TIENE/USA vars (avg 18%)",
      "GENERO has blank category (' ') → data quality flag; clean before analysis",
      "Hierarchical clustering (household→individual) but analyzed as flat cross-section → consider clustering SEs",
      "Unequal sampling: FACTOR_EXPANSION suggests survey design → must use survey weights in all models",
      "Endogeneity risk: INTERNET_HOGAR, SMARTPHONE, FORMAL may be jointly determined with adoption",
      "No natural experiments visible → RDD / local natural experiment unlikely without external policy data"
    ],
    "recommended_methods": [
      "IV/2SLS (if valid instruments exist for INTERNET_HOGAR, SMARTPHONE, FORMAL, BANCO_PREVIO)",
      "Propensity Score Matching (PSM) + Oaxaca-Blinder decomposition (attribute gaps by gender, education, formality)",
      "Covariate-balanced matching (CEM) — more robust than PSM to overlap violations",
      "Quantile regression (examine heterogeneous effects across income distribution)",
      "Heckman selection model (if sample is selected — e.g., unemployed underrepresented)",
      "Logit/Probit with robust SEs clustered at household level (baseline: association only)",
      "LASSO variable selection (many predictors; identify true drivers)",
      "Mediation analysis (does SMARTPHONE mediate effect of INTERNET_HOGAR?)"
    ],
    "outcome_variables": {
      "primary": "TIENE_BILLETERA (7% adoption)",
      "secondary": ["USA_BILLETERA (16% usage)", "TIENE_BILLETERA_ALT_E10", "TIENE_BILLETERA_ALT_E6", "USA_BILLETERA_ALT_H6"]
    },
    "key_predictors": {
      "demographics": ["EDAD", "GENERO", "NIVEL_EDUCATIVO"],
      "economic": ["FORMAL", "OCUPADO", "INGHOG2D", "INGRESO_PC", "POBREZA"],
      "technology": ["INTERNET_HOGAR", "SMARTPHONE"],
      "banking_history": ["BANCO_PREVIO"],
      "geographic": ["UBIGEO", "DPTO", "ESTRATO", "DOMINIO"],
      "household": ["MIEPERHO"]
    },
    "critical_assumption": "Unconfoundedness (no unmeasured confounders) — strong assumption in cross-sectional data. Consider sensitivity analysis.",
    "next_steps": [
      "1. Handle missing data: impute NIVEL_EDUCATIVO (9%), OCUPADO (27%); decide on incomplete TIENE/USA vars",
      "2. Identify candidate instruments (external validity, relevance, exclusion restriction)",
      "3. Clean GENERO blanks and verify FACTOR_EXPANSION weighting",
      "4. Check overlap in propensity scores if using matching",
      "5. Conduct balance table (standardized diffs) before/after matching",
      "6. Test for endogeneity (Hausman test for IV vs OLS)",
      "7. Report 95% CIs + robust SEs clustered at household level"
    ]
  }
}
```

**Key insight**: This is **purely associational** — without an instrument, policy discontinuity, or natural experiment, you cannot make causal claims. The best you can do is:

1. **Condition on observables** (matching, regression) — reveals associations under unconfoundedness
2. **Find instruments** — test if variables that affect adoption likelihood don't directly affect outcome (e.g., geographic network effects, policy rollout dates)
3. **Sensitivity analysis** — how large would an unmeasured confounder need to be to flip your conclusion?

The adoption gap by education, formality, and internet access is **real in the data**. Whether it's *causal* depends on whether you can rule out reverse causality and selection. Would you like me to walk through IV identification or matching strategy?