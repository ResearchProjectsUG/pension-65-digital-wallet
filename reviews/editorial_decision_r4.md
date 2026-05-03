# Editorial Decision: MAJOR_REVISIONS

**Score**: 53/100
**Fatal issues**: No
**Round**: _r4

## CODE ISSUES (require re-running scripts)

These issues require modifying Python scripts and re-executing them.
After fixing scripts, re-run ALL scripts to regenerate results,
then update main.tex with the new numbers.

1. [MUST] [Contribution] Discrete running variable correction (Kolesar-Rothe 2018 or equivalent) — standard rdrobust assumes continuous density, violated by integer ages
2. [MUST] [Contribution] Covariate-adjusted vs. local-linear bandwidth-sensitivity curve to explain the -0.006 vs -0.027 discrepancy
3. [SHOULD] [Contribution] Minimum detectable effect calculation to formally benchmark the precision of the null
4. [SHOULD] [Contribution] Urban/rural heterogeneity split within the MSE-optimal bandwidth
5. [SHOULD] [Contribution] Placebo outcome on non-wallet financial products to test for general age-65 financial-access effects
6. [SHOULD] [Tables/Figures] MAJOR-2: Permutation p=0.434, McCrary/Cattaneo t=2.0, and both placebo-cutoff estimates appear only 
7. [SHOULD] [Tables/Figures] MAJOR-3: Table 2 'extended_covariates' specification (N=57,039, BW=33.46) is never described or refe
8. [SHOULD] [Tables/Figures] MAJOR-4: H Double CI [−0.027, +0.026] is centered at ~0, not on the reported estimate −0.020; no not
9. [SHOULD] [Referee Question] The covariate-adjusted estimate (-0.027) differs from the local-linear baseline (-0.006) by 21 percentage points — can y
10. [SHOULD] [Referee Question] What is the minimum detectable effect at 80% power within your MSE-optimal bandwidth, and how does it compare to the eff

## TEXT ISSUES (edit main.tex)

These issues require editing the paper text only.

1. [MUST] [Contribution] Remove template boilerplate from Table 1 footnotes and Figure 1 axis labels before any submission
2. [MUST] [Claims] Causal overclaiming: crossing the eligibility threshold does not, on average, induce active wallet adoption
3. [MUST] [Claims] Causal overclaiming: institutional channels for transfer digitization being insufficient, on their own, to overcome the a
4. [MUST] [Claims] Causal overclaiming: the intent-to-treat estimates are small, precisely bounded, and consistent with zero across every sp
5. [MUST] [Claims] Causal overclaiming: the data support the conclusion that any positive effect of the program on digital adoption, if it e
6. [MUST] [Consistency] CRITICAL: Table 3 Panel D vs. Table 4 report incompatible BW/N/CI for INTERNET_HOGAR (N=29,668 vs 27
7. [MUST] [Consistency] MAJOR: H Double row in Table 3 Panel A shows bias-corrected CI centered at -0.0004 while conventiona
8. [MUST] [Consistency] MAJOR: Population means in §3.2 (TIENE_BILLETERA 7.4%, USA_BILLETERA 15.6%) do not reconcile with Ta
9. [SHOULD] [Contribution] First-stage approximation using administrative coverage to bound the LATE and rule out a low-compliance explanation for the null
10. [SHOULD] [Contribution] AFP retirement co-occurrence check at age 65 to address running-variable contamination
11. [SHOULD] [Claims] Missing caveat: The 3 pp upper bound applies to the ITT discontinuity, not the program LATE; the complier effect cou
12. [SHOULD] [Claims] Missing caveat: The permutation p-value scope (rdrobust vs. WLS statistic) is not stated, so it cannot logically ove
13. [SHOULD] [Claims] Missing caveat: McCrary test statistic of 2.0 is reported without a p-value; conclusion of no bunching is unsupporte
14. [SHOULD] [Claims] Missing caveat: Table 3 and Table 4 report INTERNET_HOGAR under materially different bandwidths (15.23 vs. 14.24) an
15. [SHOULD] [Claims] Missing caveat: The WLS specification is a methodological fallback due to computational constraints, not a robustnes
16. [SHOULD] [Math] CRITICAL: Population mean for active wallet use (15.6%) exceeds ownership (7.4%) — logically impossi
17. [SHOULD] [Math] MAJOR: Equation (3) omits the D_i * g(A_i-65) slope-interaction term, imposing equal polynomial slop
18. [SHOULD] [Math] MAJOR: Randomization inference permutes treatment assignment D_i within [55,75] rather than permutin
19. [SHOULD] [Math] MINOR: h* reported as 14.24 and 14.2 interchangeably across sections
20. [SHOULD] [Math] MINOR: Equation (3) carries no bandwidth qualifier despite using h=34.2 instead of h*=14.24
21. [SHOULD] [Tables/Figures] CRITICAL-1: Table 2 baseline and Table 3 H Optimal/Linear report SE=0.0165/0.0179 and different CIs 
22. [SHOULD] [Tables/Figures] CRITICAL-2: Section 4.2 states both ±0.5 and ±1.0 donut-hole specs yield −0.001, but Table 3 shows −
23. [SHOULD] [Tables/Figures] MAJOR-1: Table 1 retains unfilled '---' placeholder as a fourth sub-column header and data value thr
24. [SHOULD] [Referee Question] Why was the Kolesar-Rothe (2018) honest CI procedure not applied given that age is a discrete integer-valued running var
25. [SHOULD] [Referee Question] Using the 30% administrative coverage figure, what is the implied LATE under a 2SLS scaling, and is it still economicall
26. [SHOULD] [Referee Question] Do AFP-related retirement transitions co-occur at age 65 in your ENAHO sample, and if so, how do you separate that effec
27. [SHOULD] [Referee Question] Can you confirm and correct the template boilerplate in Table 1 footnotes and Figure 1 axis labels?
28. [SHOULD] [Referee Question] Does the null hold uniformly across urban and rural subsamples, or is it driven by a rural subpopulation with structural

## MUST-ADDRESS (blockers — fix ALL of these)

1. [Contribution] Discrete running variable correction (Kolesar-Rothe 2018 or equivalent) — standard rdrobust assumes continuous density, violated by integer ages
2. [Contribution] Covariate-adjusted vs. local-linear bandwidth-sensitivity curve to explain the -0.006 vs -0.027 discrepancy
3. [Contribution] Remove template boilerplate from Table 1 footnotes and Figure 1 axis labels before any submission
4. [Claims] Causal overclaiming: crossing the eligibility threshold does not, on average, induce active wallet adoption
5. [Claims] Causal overclaiming: institutional channels for transfer digitization being insufficient, on their own, to overcome the a
6. [Claims] Causal overclaiming: the intent-to-treat estimates are small, precisely bounded, and consistent with zero across every sp
7. [Claims] Causal overclaiming: the data support the conclusion that any positive effect of the program on digital adoption, if it e
8. [Consistency] CRITICAL: Table 3 Panel D vs. Table 4 report incompatible BW/N/CI for INTERNET_HOGAR (N=29,668 vs 27
9. [Consistency] MAJOR: H Double row in Table 3 Panel A shows bias-corrected CI centered at -0.0004 while conventiona
10. [Consistency] MAJOR: Population means in §3.2 (TIENE_BILLETERA 7.4%, USA_BILLETERA 15.6%) do not reconcile with Ta

## SHOULD-ADDRESS (important but not blockers)

1. [Contribution] First-stage approximation using administrative coverage to bound the LATE and rule out a low-compliance explanation for the null
2. [Contribution] Minimum detectable effect calculation to formally benchmark the precision of the null
3. [Contribution] Urban/rural heterogeneity split within the MSE-optimal bandwidth
4. [Contribution] Placebo outcome on non-wallet financial products to test for general age-65 financial-access effects
5. [Contribution] AFP retirement co-occurrence check at age 65 to address running-variable contamination
6. [Claims] Missing caveat: The 3 pp upper bound applies to the ITT discontinuity, not the program LATE; the complier effect cou
7. [Claims] Missing caveat: The permutation p-value scope (rdrobust vs. WLS statistic) is not stated, so it cannot logically ove
8. [Claims] Missing caveat: McCrary test statistic of 2.0 is reported without a p-value; conclusion of no bunching is unsupporte
9. [Claims] Missing caveat: Table 3 and Table 4 report INTERNET_HOGAR under materially different bandwidths (15.23 vs. 14.24) an
10. [Claims] Missing caveat: The WLS specification is a methodological fallback due to computational constraints, not a robustnes
11. [Math] CRITICAL: Population mean for active wallet use (15.6%) exceeds ownership (7.4%) — logically impossi
12. [Math] MAJOR: Equation (3) omits the D_i * g(A_i-65) slope-interaction term, imposing equal polynomial slop
13. [Math] MAJOR: Randomization inference permutes treatment assignment D_i within [55,75] rather than permutin
14. [Math] MINOR: h* reported as 14.24 and 14.2 interchangeably across sections
15. [Math] MINOR: Equation (3) carries no bandwidth qualifier despite using h=34.2 instead of h*=14.24
16. [Tables/Figures] CRITICAL-1: Table 2 baseline and Table 3 H Optimal/Linear report SE=0.0165/0.0179 and different CIs 
17. [Tables/Figures] CRITICAL-2: Section 4.2 states both ±0.5 and ±1.0 donut-hole specs yield −0.001, but Table 3 shows −
18. [Tables/Figures] MAJOR-1: Table 1 retains unfilled '---' placeholder as a fourth sub-column header and data value thr
19. [Tables/Figures] MAJOR-2: Permutation p=0.434, McCrary/Cattaneo t=2.0, and both placebo-cutoff estimates appear only 
20. [Tables/Figures] MAJOR-3: Table 2 'extended_covariates' specification (N=57,039, BW=33.46) is never described or refe
21. [Tables/Figures] MAJOR-4: H Double CI [−0.027, +0.026] is centered at ~0, not on the reported estimate −0.020; no not
22. [Referee Question] Why was the Kolesar-Rothe (2018) honest CI procedure not applied given that age is a discrete integer-valued running var
23. [Referee Question] The covariate-adjusted estimate (-0.027) differs from the local-linear baseline (-0.006) by 21 percentage points — can y
24. [Referee Question] Using the 30% administrative coverage figure, what is the implied LATE under a 2SLS scaling, and is it still economicall
25. [Referee Question] Do AFP-related retirement transitions co-occur at age 65 in your ENAHO sample, and if so, how do you separate that effec
26. [Referee Question] Can you confirm and correct the template boilerplate in Table 1 footnotes and Figure 1 axis labels?
27. [Referee Question] What is the minimum detectable effect at 80% power within your MSE-optimal bandwidth, and how does it compare to the eff
28. [Referee Question] Does the null hold uniformly across urban and rural subsamples, or is it driven by a rural subpopulation with structural

## MAY-ADDRESS (polish)

1. [Style] MAJOR (unresolved from Round 2): 'centred'/'centered' inconsistency throughout — standardize to Amer
2. [Style] MAJOR: Introduction calls the design 'a sharp regression discontinuity' despite the paper explicitly
3. [Style] MAJOR: Circular self-reference in §4 — 'As discussed in Section~\ref{sec:strategy}' appears within t
4. [Style] MAJOR: Limitations section promises five items but delivers two with bold headers and three as unlab
5. [Style] MAJOR: Abstract phrase 'other age-65-specific changes on the running variable' is ambiguous — revise
6. [Style] MAJOR: §1 missing words — 'an ITT estimate of institutional access on digital adoption' should read 

## REFEREE QUESTIONS (must answer in revised paper)

1. Why was the Kolesar-Rothe (2018) honest CI procedure not applied given that age is a discrete integer-valued running variable? How do the CIs change under that correction?
2. The covariate-adjusted estimate (-0.027) differs from the local-linear baseline (-0.006) by 21 percentage points — can you plot the bandwidth-sensitivity curve for the unadjusted estimator and show that this gap is entirely attributable to the wider bandwidth?
3. Using the 30% administrative coverage figure, what is the implied LATE under a 2SLS scaling, and is it still economically negligible?
4. Do AFP-related retirement transitions co-occur at age 65 in your ENAHO sample, and if so, how do you separate that effect from the Pensión 65 ITT?
5. Can you confirm and correct the template boilerplate in Table 1 footnotes and Figure 1 axis labels?
6. What is the minimum detectable effect at 80% power within your MSE-optimal bandwidth, and how does it compare to the effect size a policymaker would consider meaningful?
7. Does the null hold uniformly across urban and rural subsamples, or is it driven by a rural subpopulation with structurally near-zero wallet adoption?

## Summary
- Must-address: 10 issues
- Should-address: 28 issues
- May-address: 6 issues
- Code issues: 10
- Text issues: 28
- Has fatal: False
- Contribution rating: Incremental
- Recommendation: Revise before sending
