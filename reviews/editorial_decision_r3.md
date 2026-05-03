# Editorial Decision: MAJOR_REVISIONS

**Score**: 50/100
**Fatal issues**: YES
**Round**: _r3

## CODE ISSUES (require re-running scripts)

These issues require modifying Python scripts and re-executing them.
After fixing scripts, re-run ALL scripts to regenerate results,
then update main.tex with the new numbers.

1. [MUST] [Contribution] Clarify whether Table 1 uses the full sample or the bandwidth-restricted sample; provide RDD estimates restricted to the optimal bandwidth with balanced treated/control counts
2. [MUST] [Consistency] [MAJOR-1] Table 2 switches from rdrobust (BW ≈ 14–17) to statsmodels_WLS (BW ≈ 34) for covariate-adj
3. [SHOULD] [Contribution] Explicitly explain the negative unconditional correlation between treatment status and digital adoption (age gradient vs. selection) in the descriptive section
4. [SHOULD] [Contribution] Replace hardcoded absolute path in 00_clean.py:16 with a relative path or PROJECT_ROOT environment variable
5. [SHOULD] [Claims] Missing caveat: Estimator mismatch: the baseline rdrobust and the covariate-adjusted WLS are not comparable specific
6. [SHOULD] [Tables/Figures] Table 3 Panel A: H Half and H Optimal point estimates are bit-for-bit identical (-0.0056) — near-cer
7. [SHOULD] [Tables/Figures] Table 3 Panel D and Table 4 both test covariate balance but report different estimates/bandwidths wi
8. [SHOULD] [Referee Question] The submitted main.tex contains no paper body. Please confirm Round 2 textual corrections were implemented and resubmit 

## TEXT ISSUES (edit main.tex)

These issues require editing the paper text only.

1. [MUST] [Contribution] Apply ENAHO survey weights throughout or provide weighted robustness checks and restrict population claims accordingly
2. [MUST] [Claims] Causal overclaiming: Any sentence claiming Pensión 65 eligibility increases digital wallet ownership or usage — the prima
3. [MUST] [Claims] Causal overclaiming: Any sentence presenting the statsmodels_WLS estimates as 'the RDD result' — WLS at h=34.22 is a para
4. [MUST] [Claims] Causal overclaiming: Any population-level claim about 'elderly poor in Peru' — ENAHO survey weights are absent and unweig
5. [MUST] [Claims] Causal overclaiming: Any claim of heterogeneous effects by SISFOH poverty status — all subgroup estimates span zero and N
6. [MUST] [Claims] Causal overclaiming: Any claim that 'the McCrary density test shows no manipulation' — the p-value extraction is potentia
7. [MUST] [Claims] Causal overclaiming: Any inference attributed to Figure 1 or Table 4 if the x-axis still reads 'Vote Margin' or 'Electora
8. [MUST] [Consistency] [CRITICAL-1] INTERNET_HOGAR and SMARTPHONE appear in both Table 3 Panel D and Table 4 with different
9. [MUST] [Consistency] [MAJOR-2] Paper body is absent from the submitted main.tex — 8 Round 2 issues (Figure 1 direction, p
10. [SHOULD] [Contribution] Remove all electoral-RDD template boilerplate from table notes and figure labels in 03_output.py before any submission
11. [SHOULD] [Contribution] Investigate and report the differential missingness rate in NIVEL_EDUCATIVO across treated and control groups near the cutoff
12. [SHOULD] [Contribution] Add README.md with sequential execution order and requirements.txt/environment.yml for end-to-end reproducibility
13. [SHOULD] [Claims] Missing caveat: No survey weights: ENAHO is a stratified multi-stage cluster design; unweighted results are not popu
14. [SHOULD] [Claims] Missing caveat: Severe sample imbalance (14,088 treated vs. 99,667 control) is unexplained and untested; the RDD den
15. [SHOULD] [Claims] Missing caveat: USA_BILLETERA heterogeneity data is entirely missing — no estimates exist for this outcome in the SI
16. [SHOULD] [Claims] Missing caveat: The negative significant estimate on TIENE_BILLETERA (−2.7 pp) in the covariate-adjusted spec is the
17. [SHOULD] [Claims] Missing caveat: ITT vs. LATE distinction: if Pensión 65 enrollment is incomplete, the ITT is attenuated relative to 
18. [SHOULD] [Claims] Missing caveat: Bandwidth sensitivity shows the estimate nearly quadruples from optimal to double bandwidth (−0.006 
19. [SHOULD] [Math] Missing \begin{document} — document is entirely non-compilable
20. [SHOULD] [Math] Missing \begin{thebibliography} — unmatched \end{thebibliography} will halt compilation
21. [SHOULD] [Math] Jack & Suri (2014) \bibitem command accidentally placed inside a LaTeX comment — citation key jack20
22. [SHOULD] [Math] Document body absent — mathematical content (equations, specifications, notation) could not be revie
23. [SHOULD] [Tables/Figures] Table 1: Columns 4 and 8 are headed '---' with all cells reading '---' — phantom placeholder columns
24. [SHOULD] [Tables/Figures] Table 1: All row labels are raw code names (TIENE_BILLETERA etc.) — must be replaced with human-read
25. [SHOULD] [Tables/Figures] Table 2: Method labels 'rdrobust' and 'statsmodels_WLS' are software package names — replace with ec
26. [SHOULD] [Tables/Figures] main.tex body absent from submitted excerpt — figure captions cannot be verified; Round 2 Figure 1 c
27. [SHOULD] [Referee Question] Table 1 sums to exactly 113,755 observations — the full sample. Was any bandwidth restriction applied before constructin
28. [SHOULD] [Referee Question] ENAHO is a stratified probability sample requiring expansion weights for representative inference. Why are no survey wei
29. [SHOULD] [Referee Question] Do any other Peruvian social programs change eligibility at the same threshold that identifies Pensión 65? How do you ru
30. [SHOULD] [Referee Question] What is the Pensión 65 take-up rate among eligibles near the cutoff? Please provide the first-stage discontinuity so rea
31. [SHOULD] [Referee Question] Table 1 shows treated individuals have lower wallet usage (3.19%) than controls (17.94%). Is this a pre-program age grad
32. [SHOULD] [Referee Question] NIVEL_EDUCATIVO has 2.1% missing in treated vs. 6.9% in control. Is this differential rate smooth through the cutoff? Do

## MUST-ADDRESS (blockers — fix ALL of these)

1. [Contribution] Clarify whether Table 1 uses the full sample or the bandwidth-restricted sample; provide RDD estimates restricted to the optimal bandwidth with balanced treated/control counts
2. [Contribution] Apply ENAHO survey weights throughout or provide weighted robustness checks and restrict population claims accordingly
3. [Claims] Causal overclaiming: Any sentence claiming Pensión 65 eligibility increases digital wallet ownership or usage — the prima
4. [Claims] Causal overclaiming: Any sentence presenting the statsmodels_WLS estimates as 'the RDD result' — WLS at h=34.22 is a para
5. [Claims] Causal overclaiming: Any population-level claim about 'elderly poor in Peru' — ENAHO survey weights are absent and unweig
6. [Claims] Causal overclaiming: Any claim of heterogeneous effects by SISFOH poverty status — all subgroup estimates span zero and N
7. [Claims] Causal overclaiming: Any claim that 'the McCrary density test shows no manipulation' — the p-value extraction is potentia
8. [Claims] Causal overclaiming: Any inference attributed to Figure 1 or Table 4 if the x-axis still reads 'Vote Margin' or 'Electora
9. [Consistency] [CRITICAL-1] INTERNET_HOGAR and SMARTPHONE appear in both Table 3 Panel D and Table 4 with different
10. [Consistency] [MAJOR-1] Table 2 switches from rdrobust (BW ≈ 14–17) to statsmodels_WLS (BW ≈ 34) for covariate-adj
11. [Consistency] [MAJOR-2] Paper body is absent from the submitted main.tex — 8 Round 2 issues (Figure 1 direction, p

## SHOULD-ADDRESS (important but not blockers)

1. [Contribution] Remove all electoral-RDD template boilerplate from table notes and figure labels in 03_output.py before any submission
2. [Contribution] Explicitly explain the negative unconditional correlation between treatment status and digital adoption (age gradient vs. selection) in the descriptive section
3. [Contribution] Investigate and report the differential missingness rate in NIVEL_EDUCATIVO across treated and control groups near the cutoff
4. [Contribution] Replace hardcoded absolute path in 00_clean.py:16 with a relative path or PROJECT_ROOT environment variable
5. [Contribution] Add README.md with sequential execution order and requirements.txt/environment.yml for end-to-end reproducibility
6. [Claims] Missing caveat: No survey weights: ENAHO is a stratified multi-stage cluster design; unweighted results are not popu
7. [Claims] Missing caveat: Estimator mismatch: the baseline rdrobust and the covariate-adjusted WLS are not comparable specific
8. [Claims] Missing caveat: Severe sample imbalance (14,088 treated vs. 99,667 control) is unexplained and untested; the RDD den
9. [Claims] Missing caveat: USA_BILLETERA heterogeneity data is entirely missing — no estimates exist for this outcome in the SI
10. [Claims] Missing caveat: The negative significant estimate on TIENE_BILLETERA (−2.7 pp) in the covariate-adjusted spec is the
11. [Claims] Missing caveat: ITT vs. LATE distinction: if Pensión 65 enrollment is incomplete, the ITT is attenuated relative to 
12. [Claims] Missing caveat: Bandwidth sensitivity shows the estimate nearly quadruples from optimal to double bandwidth (−0.006 
13. [Math] Missing \begin{document} — document is entirely non-compilable
14. [Math] Missing \begin{thebibliography} — unmatched \end{thebibliography} will halt compilation
15. [Math] Jack & Suri (2014) \bibitem command accidentally placed inside a LaTeX comment — citation key jack20
16. [Math] Document body absent — mathematical content (equations, specifications, notation) could not be revie
17. [Tables/Figures] Table 3 Panel A: H Half and H Optimal point estimates are bit-for-bit identical (-0.0056) — near-cer
18. [Tables/Figures] Table 1: Columns 4 and 8 are headed '---' with all cells reading '---' — phantom placeholder columns
19. [Tables/Figures] Table 3 Panel D and Table 4 both test covariate balance but report different estimates/bandwidths wi
20. [Tables/Figures] Table 1: All row labels are raw code names (TIENE_BILLETERA etc.) — must be replaced with human-read
21. [Tables/Figures] Table 2: Method labels 'rdrobust' and 'statsmodels_WLS' are software package names — replace with ec
22. [Tables/Figures] main.tex body absent from submitted excerpt — figure captions cannot be verified; Round 2 Figure 1 c
23. [Referee Question] Table 1 sums to exactly 113,755 observations — the full sample. Was any bandwidth restriction applied before constructin
24. [Referee Question] ENAHO is a stratified probability sample requiring expansion weights for representative inference. Why are no survey wei
25. [Referee Question] Do any other Peruvian social programs change eligibility at the same threshold that identifies Pensión 65? How do you ru
26. [Referee Question] What is the Pensión 65 take-up rate among eligibles near the cutoff? Please provide the first-stage discontinuity so rea
27. [Referee Question] Table 1 shows treated individuals have lower wallet usage (3.19%) than controls (17.94%). Is this a pre-program age grad
28. [Referee Question] NIVEL_EDUCATIVO has 2.1% missing in treated vs. 6.9% in control. Is this differential rate smooth through the cutoff? Do
29. [Referee Question] The submitted main.tex contains no paper body. Please confirm Round 2 textual corrections were implemented and resubmit 

## MAY-ADDRESS (polish)

1. [Style] Paper body is entirely absent from the provided file — review impossible
2. [Style] No \begin{document} tag present; preamble runs directly into bibliography
3. [Style] Cannot verify resolution of any Round 2 issues without body text

## REFEREE QUESTIONS (must answer in revised paper)

1. Table 1 sums to exactly 113,755 observations — the full sample. Was any bandwidth restriction applied before constructing this table? Please provide treated/control counts within the optimal bandwidth alongside the full-sample table.
2. ENAHO is a stratified probability sample requiring expansion weights for representative inference. Why are no survey weights applied? Please provide weighted estimates or restrict all population claims to the in-sample population.
3. Do any other Peruvian social programs change eligibility at the same threshold that identifies Pensión 65? How do you rule out compound discontinuities driving the estimated effect?
4. What is the Pensión 65 take-up rate among eligibles near the cutoff? Please provide the first-stage discontinuity so readers can scale the ITT estimate to a treatment-on-the-treated effect.
5. Table 1 shows treated individuals have lower wallet usage (3.19%) than controls (17.94%). Is this a pre-program age gradient in technology adoption? Please clarify the counterfactual logic and how the RDD recovers a causal estimate given this unconditional pattern.
6. NIVEL_EDUCATIVO has 2.1% missing in treated vs. 6.9% in control. Is this differential rate smooth through the cutoff? Does it affect covariate balance tests?
7. The submitted main.tex contains no paper body. Please confirm Round 2 textual corrections were implemented and resubmit the complete draft.

## Summary
- Must-address: 11 issues
- Should-address: 29 issues
- May-address: 3 issues
- Code issues: 8
- Text issues: 32
- Has fatal: True
- Contribution rating: Incremental
- Recommendation: Revise before sending
