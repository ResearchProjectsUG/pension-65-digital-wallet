# Stage 7 — Integration Test Report

Date: 2026-05-02T20:07:33.526564

## Gate: FAILED
Aggregate: 85.3/85

## Component Scores
- identification: 82/100
- code: 95/100
- paper: 95/100
- polish: 52.900000000000006/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 6/8 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 3 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 4 .tex table(s), inline tables in main.tex
  [SOFT] [PASS] figures_exist: Found 2 figure(s): figure_1_rdplot.pdf, figure_2_bandwidth_sensitivity.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Desktop\papers-HQ- AI\projects\determinantes_de_adopcion_de_billetera_digital_en_peru_20260502_145708\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 10 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 205 numeric values
  [SOFT] [PASS] seed_set:00_clean.py: Random seed found
  [SOFT] [PASS] se_clustering:01_main.py: Clustering pattern found
  [SOFT] [PASS] se_robust:02_robustness.py: HC robust SEs found (appropriate for individual-level RCT)
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [FAIL] referee_checklist_coverage: Referee checklist: 18/42 MUST requirements detected in code (43%)
  [SOFT] [FAIL] referee_checklist_missing: Possibly unimplemented: [DOMAIN] mechanism_verification: Before any regression: cross-tab P65 receipt by; [DOMAIN] first_stage: Run fuzzy RDD first stage: regress P65_receipt on polynomi; [DOMAIN] estimation: Implement fuzzy RDD via 2SLS: instrument = 1(age≥65), endog; [DOMAIN] age_heaping: Audit the age distribution for heaping at multiples of 5 (; [DOMAIN] placebo_cutoffs: Estimate the main specification at four placebo cutoff ... and 19 more

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 5/5 passed  | SOFT checks: 3/4 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 sections found
  [HARD] [PASS] references_bib_exists: references.bib has 15 entries
  [SOFT] [PASS] citation_keys_matched: All 15 citation keys found in .bib
  [HARD] [PASS] table_references_valid: All 4 table references resolved
  [HARD] [PASS] figure_references_valid: All 3 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 4233 words (outside 5000-15000 range)
  [SOFT] [PASS] numbers_consistent: 7 number(s) in abstract match results_summary: 0.005, 0.007, 0.016, 0.018, 0.031

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 7/7 passed  | SOFT checks: 9/9 passed
  [HARD] [PASS] method_alignment: Strategy specifies 'regression discontinuity' — code contains: rdd, bandwidth, rdrobust
  [HARD] [PASS] code_tables_produced: All 4 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 972 words
  [SOFT] [PASS] results_in_paper: 30/69 key numbers from results appear in paper (43%)
  [SOFT] [PASS] abstract_has_results: Abstract contains 7 numbers from results
  [HARD] [PASS] pdf_exists: main.pdf exists (473 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found in main.tex
  [HARD] [PASS] all_citations_resolved: All 15 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 4 table references valid
  [HARD] [PASS] figure_refs_valid: All 3 figure references valid
  [SOFT] [PASS] table_has_data:table_1_summary.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table_2_main_results.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table_3_robustness.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table_4_covariate_balance.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:figure_1_rdplot.pdf: 19 KB
  [SOFT] [PASS] figure_non_trivial:figure_2_bandwidth_sensitivity.pdf: 14 KB