# Editorial Decision: MAJOR_REVISIONS

**Score**: 51/100
**Fatal issues**: YES
**Round**: _r2

## CODE ISSUES (require re-running scripts)

These issues require modifying Python scripts and re-executing them.
After fixing scripts, re-run ALL scripts to regenerate results,
then update main.tex with the new numbers.

1. [SHOULD] [Contribution] Fix covariate-adjusted specification to use h*=14.2 bandwidth by pre-restricting sample to ages 50-80 before calling rdrobust; current WLS fallback with h=34.2 is a different estimand, not a robustness check
2. [SHOULD] [Contribution] Heterogeneity by SISFOH poverty classification: estimate RDD separately for extreme-poor vs. non-extreme-poor subsamples to test the core mechanism
3. [SHOULD] [Contribution] Report expansion-factor-weighted population means for outcomes and clarify whether RDD estimates use survey weights
4. [SHOULD] [Math] Arithmetic error: paper explicitly states 't ≈ -5.1, computed as -0.027/0.005' but -0.027/0.005 = -5
5. [SHOULD] [Tables/Figures] Table 3 Panel B: donut-hole estimates for 0.5-year and 1.0-year exclusions are byte-for-byte identic
6. [SHOULD] [Tables/Figures] Permutation randomization p-value (p=0.434) — the primary inference result — appears only in prose; 
7. [SHOULD] [Tables/Figures] McCrary density test statistic (T=2.0) reported in text but absent from all tables and figures
8. [SHOULD] [Referee Question] Does ENAHO 2024 record Pensión 65 receipt? If so, what is the first-stage RDD estimate of the take-up jump at age 65 wit
9. [SHOULD] [Referee Question] Can you rerun the covariate-adjusted local-polynomial specification on a pre-restricted sample of ages 50-80 to avoid th
10. [SHOULD] [Referee Question] Can you show the full permutation distribution of the WLS t-statistic and confirm that the empirical t≈-5.4 falls within

## TEXT ISSUES (edit main.tex)

These issues require editing the paper text only.

1. [MUST] [Contribution] First-stage discontinuity in Pensión 65 take-up at age 65 must be shown or demonstrated to be infeasible with available data
2. [MUST] [Contribution] Sharp vs. fuzzy design must be resolved: either recharacterize as fuzzy RDD with ITT and scaled LATE, or demonstrate SISFOH share is continuous through the cutoff; remove LATE label from Equation (1)
3. [MUST] [Contribution] Replace full-sample Table 1 with bandwidth-restricted summary statistics (ages within h*=14.2 of the cutoff); the current table is misleading about who the identifying comparison is between
4. [MUST] [Claims] Causal overclaiming: These findings imply that institutional digitization of government transfers, on its own, is an insu
5. [MUST] [Claims] Causal overclaiming: The well-documented age gradient in technology adoption appears to dominate any program-specific eff
6. [MUST] [Claims] Causal overclaiming: institutional digitization works best when paired with explicit digital-literacy support, smartphone
7. [MUST] [Claims] Causal overclaiming: policy attention on the elderly poor population should focus on the underlying determinants of digit
8. [MUST] [Claims] Causal overclaiming: Both placebos are economically negligible and consistent with the absence of a discontinuity specifi
9. [MUST] [Consistency] Donut-hole ±0.5 and ±1.0 produce byte-for-byte identical rows in Table 3 — coding error, one spec wa
10. [MUST] [Consistency] Local-linear baseline SE and CI differ between Table 2 (SE=0.0165, CI=[−0.034, 0.031]) and Table 3 H
11. [MUST] [Consistency] Banerjee et al. bibitem label says '2019', body text says '2020', citation key is banerjee2020 — yea
12. [SHOULD] [Contribution] Apply Kolesár-Rothe (2018) confidence intervals for discrete running variables or commit to randomization inference as the primary inference procedure throughout, not as a post-hoc correction
13. [SHOULD] [Contribution] Correct all electoral-RDD boilerplate in table notes and figure labels before resubmission; code review confirms these artifacts survive in the output pipeline
14. [SHOULD] [Claims] Missing caveat: Survey expansion weights are absent from the cleaned data despite claims of population-representativ
15. [SHOULD] [Claims] Missing caveat: The first placebo cutoff (age 15) produces a CI that excludes zero; the paper dismisses this with a 
16. [SHOULD] [Claims] Missing caveat: The WLS confidence intervals [-0.037, -0.017] rest on an SE the paper identifies as incorrect; these
17. [SHOULD] [Claims] Missing caveat: The donut-hole robustness checks at 0.5 and 1.0 years produce identical estimates, SEs, and sample s
18. [SHOULD] [Claims] Missing caveat: With ~22.5% joint eligibility and ~75% take-up, the ITT dilutes the effect on compliers by a factor 
19. [SHOULD] [Claims] Missing caveat: No extreme-poor individual aged 65-75 in the sample actively uses a digital wallet; the active-use o
20. [SHOULD] [Claims] Missing caveat: The McCrary density test p-value is potentially NaN due to a confirmed API extraction bug in the cod
21. [SHOULD] [Claims] Missing caveat: The cohort-versus-age confound is acknowledged only in the limitations section; the local-linear est
22. [SHOULD] [Math] Equation (3) omits D_i interaction with the polynomial g(·), forcing equal slopes on both sides — in
23. [SHOULD] [Math] Galiani et al. (2020) characterized as 'positive but heterogeneous effects' in the Introduction and 
24. [SHOULD] [Math] Orphan bibitem 'deming2023' (Deming and Noray 2023) appears in the bibliography but is never cited i
25. [SHOULD] [Math] Banerjee et al. bibitem label reads '2019' while the bibliography entry and citation key say '2020',
26. [SHOULD] [Tables/Figures] All four table .tex files contain a egin{table} wrapper, creating illegal nested floats when \input
27. [SHOULD] [Tables/Figures] Label mismatch tab:main vs tab:main_results (Table 2) and tab:balance vs tab:cov_balance (Table 4) p
28. [SHOULD] [Tables/Figures] Table 2: het_POBREZA_low and het_SMARTPHONE_low subgroup rows repeat the full-sample baseline estima
29. [SHOULD] [Tables/Figures] Table 3 Panel D: two TIENE_BILLETERA placebo-cutoff rows are indistinguishable (no labels for age-15
30. [SHOULD] [Tables/Figures] Figure 1 prose states wallet ownership peaks 'near age 35 (younger adults)' — internally inconsisten
31. [SHOULD] [Tables/Figures] Bibitem key for Ardington et al. (2016) missing parentheses around year — malformed natbib author-ye
32. [SHOULD] [Referee Question] How do you justify calling the design sharp when only SISFOH-classified extreme-poor individuals aged 65+ are eligible, 
33. [SHOULD] [Referee Question] Is there evidence that SISFOH poverty classification itself is continuous at age 65, or could age-related reclassificati
34. [SHOULD] [Referee Question] Were the electoral-RDD boilerplate labels in Table 4 and Figure 1 corrected in the submitted version, or do those artifa
35. [SHOULD] [Referee Question] Given that the identifying variation is local to ages 51-79 (h*=14.2) and the population of interest is elderly extreme-

## MUST-ADDRESS (blockers — fix ALL of these)

1. [Contribution] First-stage discontinuity in Pensión 65 take-up at age 65 must be shown or demonstrated to be infeasible with available data
2. [Contribution] Sharp vs. fuzzy design must be resolved: either recharacterize as fuzzy RDD with ITT and scaled LATE, or demonstrate SISFOH share is continuous through the cutoff; remove LATE label from Equation (1)
3. [Contribution] Replace full-sample Table 1 with bandwidth-restricted summary statistics (ages within h*=14.2 of the cutoff); the current table is misleading about who the identifying comparison is between
4. [Claims] Causal overclaiming: These findings imply that institutional digitization of government transfers, on its own, is an insu
5. [Claims] Causal overclaiming: The well-documented age gradient in technology adoption appears to dominate any program-specific eff
6. [Claims] Causal overclaiming: institutional digitization works best when paired with explicit digital-literacy support, smartphone
7. [Claims] Causal overclaiming: policy attention on the elderly poor population should focus on the underlying determinants of digit
8. [Claims] Causal overclaiming: Both placebos are economically negligible and consistent with the absence of a discontinuity specifi
9. [Consistency] Donut-hole ±0.5 and ±1.0 produce byte-for-byte identical rows in Table 3 — coding error, one spec wa
10. [Consistency] Local-linear baseline SE and CI differ between Table 2 (SE=0.0165, CI=[−0.034, 0.031]) and Table 3 H
11. [Consistency] Banerjee et al. bibitem label says '2019', body text says '2020', citation key is banerjee2020 — yea

## SHOULD-ADDRESS (important but not blockers)

1. [Contribution] Fix covariate-adjusted specification to use h*=14.2 bandwidth by pre-restricting sample to ages 50-80 before calling rdrobust; current WLS fallback with h=34.2 is a different estimand, not a robustness check
2. [Contribution] Apply Kolesár-Rothe (2018) confidence intervals for discrete running variables or commit to randomization inference as the primary inference procedure throughout, not as a post-hoc correction
3. [Contribution] Heterogeneity by SISFOH poverty classification: estimate RDD separately for extreme-poor vs. non-extreme-poor subsamples to test the core mechanism
4. [Contribution] Correct all electoral-RDD boilerplate in table notes and figure labels before resubmission; code review confirms these artifacts survive in the output pipeline
5. [Contribution] Report expansion-factor-weighted population means for outcomes and clarify whether RDD estimates use survey weights
6. [Claims] Missing caveat: Survey expansion weights are absent from the cleaned data despite claims of population-representativ
7. [Claims] Missing caveat: The first placebo cutoff (age 15) produces a CI that excludes zero; the paper dismisses this with a 
8. [Claims] Missing caveat: The WLS confidence intervals [-0.037, -0.017] rest on an SE the paper identifies as incorrect; these
9. [Claims] Missing caveat: The donut-hole robustness checks at 0.5 and 1.0 years produce identical estimates, SEs, and sample s
10. [Claims] Missing caveat: With ~22.5% joint eligibility and ~75% take-up, the ITT dilutes the effect on compliers by a factor 
11. [Claims] Missing caveat: No extreme-poor individual aged 65-75 in the sample actively uses a digital wallet; the active-use o
12. [Claims] Missing caveat: The McCrary density test p-value is potentially NaN due to a confirmed API extraction bug in the cod
13. [Claims] Missing caveat: The cohort-versus-age confound is acknowledged only in the limitations section; the local-linear est
14. [Math] Arithmetic error: paper explicitly states 't ≈ -5.1, computed as -0.027/0.005' but -0.027/0.005 = -5
15. [Math] Equation (3) omits D_i interaction with the polynomial g(·), forcing equal slopes on both sides — in
16. [Math] Galiani et al. (2020) characterized as 'positive but heterogeneous effects' in the Introduction and 
17. [Math] Orphan bibitem 'deming2023' (Deming and Noray 2023) appears in the bibliography but is never cited i
18. [Math] Banerjee et al. bibitem label reads '2019' while the bibliography entry and citation key say '2020',
19. [Tables/Figures] All four table .tex files contain a egin{table} wrapper, creating illegal nested floats when \input
20. [Tables/Figures] Label mismatch tab:main vs tab:main_results (Table 2) and tab:balance vs tab:cov_balance (Table 4) p
21. [Tables/Figures] Table 3 Panel B: donut-hole estimates for 0.5-year and 1.0-year exclusions are byte-for-byte identic
22. [Tables/Figures] Table 2: het_POBREZA_low and het_SMARTPHONE_low subgroup rows repeat the full-sample baseline estima
23. [Tables/Figures] Permutation randomization p-value (p=0.434) — the primary inference result — appears only in prose; 
24. [Tables/Figures] Table 3 Panel D: two TIENE_BILLETERA placebo-cutoff rows are indistinguishable (no labels for age-15
25. [Tables/Figures] McCrary density test statistic (T=2.0) reported in text but absent from all tables and figures
26. [Tables/Figures] Figure 1 prose states wallet ownership peaks 'near age 35 (younger adults)' — internally inconsisten
27. [Tables/Figures] Bibitem key for Ardington et al. (2016) missing parentheses around year — malformed natbib author-ye
28. [Referee Question] Does ENAHO 2024 record Pensión 65 receipt? If so, what is the first-stage RDD estimate of the take-up jump at age 65 wit
29. [Referee Question] How do you justify calling the design sharp when only SISFOH-classified extreme-poor individuals aged 65+ are eligible, 
30. [Referee Question] Can you rerun the covariate-adjusted local-polynomial specification on a pre-restricted sample of ages 50-80 to avoid th
31. [Referee Question] Is there evidence that SISFOH poverty classification itself is continuous at age 65, or could age-related reclassificati
32. [Referee Question] Can you show the full permutation distribution of the WLS t-statistic and confirm that the empirical t≈-5.4 falls within
33. [Referee Question] Were the electoral-RDD boilerplate labels in Table 4 and Figure 1 corrected in the submitted version, or do those artifa
34. [Referee Question] Given that the identifying variation is local to ages 51-79 (h*=14.2) and the population of interest is elderly extreme-

## MAY-ADDRESS (polish)

1. [Style] CRITICAL: Fig. 1 description states rates 'rise from age 50 to age 35' — logically inverted; age 35 
2. [Style] MAJOR: 'Importantly' in §5.1 (Main Results, ¶2) violates journal style — delete or rephrase.
3. [Style] MAJOR: 'centred' (British) vs. 'centered' (American) used inconsistently — standardize to 'centered'
4. [Style] MAJOR: Banerjee et al. bibliography entry carries year label '2019' but citation key and inline date
5. [Style] MAJOR: §6.2 Limitations announces five limitations but only two have bold headers; the remaining thr
6. [Style] MAJOR: 'Existing literature is insufficient on two fronts' (§1) — literature is not 'insufficient'; 

## REFEREE QUESTIONS (must answer in revised paper)

1. Does ENAHO 2024 record Pensión 65 receipt? If so, what is the first-stage RDD estimate of the take-up jump at age 65 within the optimal bandwidth?
2. How do you justify calling the design sharp when only SISFOH-classified extreme-poor individuals aged 65+ are eligible, meaning the treatment probability jump at the cutoff is substantially below 1?
3. Can you rerun the covariate-adjusted local-polynomial specification on a pre-restricted sample of ages 50-80 to avoid the memory constraint while preserving local identification?
4. Is there evidence that SISFOH poverty classification itself is continuous at age 65, or could age-related reclassification introduce a discontinuity in the running variable's joint distribution with poverty status?
5. Can you show the full permutation distribution of the WLS t-statistic and confirm that the empirical t≈-5.4 falls within the null distribution, making the randomization p=0.434 credible?
6. Were the electoral-RDD boilerplate labels in Table 4 and Figure 1 corrected in the submitted version, or do those artifacts survive in the actual output files?
7. Given that the identifying variation is local to ages 51-79 (h*=14.2) and the population of interest is elderly extreme-poor Peruvians, do the authors view this as a top-field submission or a field-journal submission, and how do they frame the contribution accordingly?

## Summary
- Must-address: 11 issues
- Should-address: 34 issues
- May-address: 6 issues
- Code issues: 10
- Text issues: 35
- Has fatal: True
- Contribution rating: Incremental
- Recommendation: Revise before sending
