"""03_output.py — RDD tables and figures template.

CRITICAL: This template NEVER writes NaN, blank, or empty cells to tables.
Every cell is filled with a value or '---' with a note explaining why.
"""

import os
import warnings
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECT-SPECIFIC VARIABLES (Claude fills these)
# ═══════════════════════════════════════════════════════════════════════════════
PRIMARY_OUTCOME = "TIENE_BILLETERA"
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
RUNNING_VAR = "running_centered"
CLUSTER_VAR = "DPTO"
COVARIATES = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]

# ═══════════════════════════════════════════════════════════════════════════════
# FIXED CODE
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "data", "clean")
TABLES_DIR = os.path.join(SCRIPT_DIR, "..", "..", "paper", "tables")
FIGURES_DIR = os.path.join(SCRIPT_DIR, "..", "..", "paper", "figures")

os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


def fmt(val, decimals=4):
    """Format a value for LaTeX tables. NEVER returns empty string."""
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return "---"
    try:
        return f"{float(val):.{decimals}f}"
    except (ValueError, TypeError):
        return str(val)


def fmt_stars(pval):
    """Significance stars from p-value."""
    if pval is None or np.isnan(pval):
        return ""
    if pval < 0.01:
        return "***"
    if pval < 0.05:
        return "**"
    if pval < 0.10:
        return "*"
    return ""


def validate_table(content, filename):
    """Check table for NaN or empty cells before saving."""
    problems = []
    if "nan" in content.lower():
        problems.append("Contains 'nan'")
    if "& &" in content:
        problems.append("Contains empty cells (& &)")
    if "& \\\\" in content:
        problems.append("Contains empty last column (& \\\\)")

    if problems:
        print(f"  WARNING in {filename}: {', '.join(problems)}")
        # Auto-fix: replace NaN with ---
        content = content.replace("nan", "---")
        content = content.replace("NaN", "---")
        content = content.replace("None", "---")
        # Fix empty cells
        while "& &" in content:
            content = content.replace("& &", "& --- &")
        content = content.replace("& \\\\", "& --- \\\\")
        print(f"  Auto-fixed: replaced blanks with '---'")

    return content


# ─── LaTeX-safe variable name (escapes underscores for tabular cells) ────────
def texvar(name: str) -> str:
    """Escape underscores in identifier names for inclusion in LaTeX text."""
    return str(name).replace("_", "\\_")


# ═══════════════════════════════════════════════════════════════════════════════
# TABLE 1: Summary Statistics
# ═══════════════════════════════════════════════════════════════════════════════
# Output is the INNER content of a threeparttable block.  main.tex wraps each
# \input{tables/table_X.tex} with its own \begin{table}[H]\centering\caption{}
# \label{}, so this file must NOT also emit a \begin{table} wrapper or LaTeX
# will produce nested float environments and duplicate captions.
# ═══════════════════════════════════════════════════════════════════════════════
def make_table1(df):
    print("Generating Table 1: Summary statistics...")

    treated = df[df["treat"] == 1]
    control = df[df["treat"] == 0]

    # Within-bandwidth split for the table-note numbers.
    h_opt = 14.24
    bw_mask = np.abs(df.get("running_centered", df[RUNNING_VAR] - 65)) <= h_opt
    df_bw = df[bw_mask]
    n_below_bw = int((df_bw.get("running_centered", df_bw[RUNNING_VAR] - 65) < 0).sum())
    n_above_bw = int((df_bw.get("running_centered", df_bw[RUNNING_VAR] - 65) >= 0).sum())

    stat_vars = OUTCOME_VARS + COVARIATES
    stat_vars = [v for v in stat_vars if v in df.columns]

    tex = [
        r"\begin{threeparttable}",
        r"\begin{tabular}{l cccc cccc}",
        r"\toprule",
        r"& \multicolumn{4}{c}{Above Threshold (Treated)} & \multicolumn{4}{c}{Below Threshold (Control)} \\",
        r"\cmidrule(lr){2-5} \cmidrule(lr){6-9}",
        r"Variable & Mean & SD & N & --- & Mean & SD & N & --- \\",
        r"\midrule",
    ]

    for var in stat_vars:
        t_s = treated[var].dropna()
        c_s = control[var].dropna()
        tex.append(
            f"  {texvar(var)} & {fmt(t_s.mean())} & {fmt(t_s.std())} & {len(t_s)} & --- "
            f"& {fmt(c_s.mean())} & {fmt(c_s.std())} & {len(c_s)} & --- \\\\"
        )

    tex += [
        r"\midrule",
        f"  Observations & \\multicolumn{{4}}{{c}}{{{len(treated)}}} & \\multicolumn{{4}}{{c}}{{{len(control)}}} \\\\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} Summary statistics for the full RDD analysis sample (all ages with valid running variable). "
            r"'Above Threshold' (treated$=1$) denotes individuals aged 65 and above (i.e., who cross the Pensi\'on 65 "
            r"age-eligibility cutoff but are not necessarily Pensi\'on 65 recipients, since the program is fuzzy and "
            r"conditional on SISFOH extreme-poverty classification); 'Below Threshold' (treated$=0$) denotes individuals "
            r"under age 65. The treated/control split (" + f"{len(treated):,}".replace(",", "{,}") +
            r" vs.\ " + f"{len(control):,}".replace(",", "{,}") + r") is asymmetric because the control group spans "
            r"the full age range below 65 while the treated group spans only ages 65 and above; within the bandwidth-"
            r"restricted estimation window ($\pm h^{\ast}\!=\!\pm 14.24$ years of age 65) the split is " +
            f"{n_below_bw:,}".replace(",", "{,}") + r" below and " +
            f"{n_above_bw:,}".replace(",", "{,}") + r" above the cutoff, which is the support relevant for "
            r"identification. The N column for \texttt{NIVEL\_EDUCATIVO} is smaller than for other variables because "
            r"education level is missing for individuals below schooling age (the missingness is structural and "
            r"observations are excluded only from rows where the variable enters as a covariate). RDD estimates do "
            r"NOT apply ENAHO survey expansion weights (\texttt{FACPOB07} is present in the cleaned data but not "
            r"used inside \texttt{rdrobust}); population-level interpretation should therefore be made with caution. "
            r"'---' indicates unavailable data."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = "\n".join(tex)
    content = validate_table(content, "table_1_summary.tex")
    path = os.path.join(TABLES_DIR, "table_1_summary.tex")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════════════
# TABLE 2: Main RDD Results
# ═══════════════════════════════════════════════════════════════════════════════
def make_table2(results, robust=None):
    print("Generating Table 2: Main RDD results...")

    tex = [
        r"\begin{threeparttable}",
        r"\begin{tabular}{l ccc}",
        r"\toprule",
    ]

    # Column headers from unique outcomes (with underscores escaped)
    outcomes = results["outcome"].unique().tolist()
    outcome_labels = " & ".join(texvar(o) for o in outcomes)
    tex.append(f"  & {outcome_labels} \\\\")
    tex.append(r"\midrule")

    # Group by specification
    for spec in results["specification"].unique():
        tex.append(r"\addlinespace")
        tex.append(
            f"\\multicolumn{{{len(outcomes)+1}}}{{l}}{{\\textit{{{texvar(spec)}}}}} \\\\"
        )

        spec_data = results[results["specification"] == spec]

        # Estimates row
        row = "  Estimate"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                est = match.iloc[0]["estimate"]
                row += f" & {fmt(est)}"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # SE row
        row = "  SE (robust)"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                se = match.iloc[0].get("se_robust", np.nan)
                row += f" & ({fmt(se)})"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # CI row
        row = "  95\\% CI"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                ci_lo = match.iloc[0].get("ci_lower", np.nan)
                ci_hi = match.iloc[0].get("ci_upper", np.nan)
                row += f" & [{fmt(ci_lo)}, {fmt(ci_hi)}]"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # N and BW row
        row = "  N / BW"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                n = match.iloc[0].get("N_eff", "---")
                bw = match.iloc[0].get("bandwidth", np.nan)
                try:
                    n_str = f"{int(float(n)):,}".replace(",", "{,}")
                except (ValueError, TypeError):
                    n_str = "---"
                row += f" & {n_str} / {fmt(bw, 2)}"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # Method row
        row = "  Method"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                method = match.iloc[0].get("method", "---")
                row += f" & {texvar(method)}"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

    # ─── SISFOH heterogeneity panel from robustness_results.csv ──────────────
    sisfoh_rows = None
    if robust is not None and "test" in robust.columns:
        sisfoh_rows = robust[robust["test"].str.startswith("het_sisfoh_")]
    if sisfoh_rows is not None and len(sisfoh_rows) > 0:
        tex.append(r"\addlinespace")
        tex.append(
            f"\\multicolumn{{{len(outcomes)+1}}}{{l}}"
            r"{\textit{Heterogeneity by SISFOH (POBREZA)}} \\"
        )
        sisfoh_label_map = {
            "het_sisfoh_extreme_poor":     ("Extreme-poor (=1)",     "Pensi\\'on 65 target group"),
            "het_sisfoh_non_extreme_poor": ("Non-extreme-poor (=2)", ""),
            "het_sisfoh_non_poor":         ("Non-poor (=3)",         ""),
        }
        for test_key, (display, _) in sisfoh_label_map.items():
            r = sisfoh_rows[sisfoh_rows["test"] == test_key]
            if len(r) == 0:
                continue
            r0 = r.iloc[0]
            est = fmt(r0.get("estimate", np.nan))
            se = fmt(r0.get("se_robust", np.nan))
            ci_lo = fmt(r0.get("ci_lower", np.nan))
            ci_hi = fmt(r0.get("ci_upper", np.nan))
            try:
                n_eff = f"{int(float(r0.get('N_eff', 0))):,}".replace(",", "{,}")
            except (ValueError, TypeError):
                n_eff = "---"
            tex.append(r"\addlinespace")
            tex.append(f"  {display} (TIENE\\_BILLETERA)  & {est} & --- \\\\")
            tex.append(f"  SE (robust)         & ({se}) & --- \\\\")
            tex.append(f"  95\\% CI             & [{ci_lo}, {ci_hi}] & --- \\\\")
            tex.append(f"  $N_h$               & {n_eff} & --- \\\\")

    tex += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} \textit{Baseline} rows use local linear RDD "
            r"(\texttt{rdrobust}) with triangular kernel and MSE-optimal bandwidth "
            r"(h$^{\ast}\!\approx\!14$--$17$); robust bias-corrected standard errors "
            r"in parentheses; confidence intervals are bias-corrected robust. "
            r"\textit{With covariates} and \textit{Extended covariates} rows use "
            r"\emph{weighted least squares} (\texttt{statsmodels\_WLS}) at "
            r"$h\!=\!34.22$ years (about 2.4$\times$ the MSE-optimal local-linear "
            r"bandwidth)---this was a fallback when \texttt{rdrobust} failed under "
            r"memory constraints; the WLS specification therefore identifies a "
            r"different estimand (a global parametric WLS regression with "
            r"covariates), is \emph{not} a covariate-adjusted local-linear RDD, and "
            r"should not be treated as ``the RDD result.'' The estimator change and "
            r"the bandwidth change are confounded; comparisons between WLS and "
            r"\texttt{rdrobust} rows must be made with caution. SISFOH heterogeneity "
            r"panel splits the bandwidth-restricted sample by household poverty "
            r"classification (1$=$extreme-poor, 2$=$non-extreme-poor, 3$=$non-poor); "
            r"the extreme-poor subsample is the policy-relevant Pensi\'on 65--"
            r"eligible group. \texttt{USA\_BILLETERA} cells in the SISFOH panel are "
            r"'---' because the bandwidth-restricted subsamples contain essentially "
            r"zero active wallet users, yielding degenerate inference. None of the "
            r"bandwidth-restricted RDD estimates is statistically distinguishable "
            r"from zero at the 95\% level. RDD estimates do not apply ENAHO survey "
            r"expansion weights; see Section~\ref{sec:strategy} for caveats on "
            r"population-level interpretation. '---' indicates estimate unavailable."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = "\n".join(tex)
    content = validate_table(content, "table_2_main_results.tex")
    path = os.path.join(TABLES_DIR, "table_2_main_results.tex")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════════════
# TABLE 3: Robustness
# ═══════════════════════════════════════════════════════════════════════════════
def make_table3(robust):
    print("Generating Table 3: Robustness...")

    tex = [
        r"\begin{threeparttable}",
        r"\begin{tabular}{l ccccc}",
        r"\toprule",
        r"Test & Estimate & SE & 95\% CI & BW & N \\",
        r"\midrule",
    ]

    panels = [
        ("Panel A: Bandwidth sensitivity",   "bandwidth"),
        ("Panel B: Donut-hole",                "donut"),
        ("Panel C: Polynomial",                "polynomial"),
        ("Panel D: Placebo (covariates as outcomes)", "placebo"),
    ]

    for panel_name, prefix in panels:
        # Important: het_sisfoh_* tests live in robust too; exclude them
        # from Panel A "bandwidth" so they don't pollute the bandwidth panel.
        panel_data = robust[
            robust["test"].str.startswith(prefix) &
            ~robust["test"].str.startswith("het_sisfoh_")
        ]
        if len(panel_data) == 0:
            continue
        tex.append(f"\\multicolumn{{6}}{{l}}{{\\textit{{{panel_name}}}}} \\\\")
        for _, r in panel_data.iterrows():
            test_name = r.get("test", "")
            if prefix == "donut":
                # donut_0.5 -> "$\pm$0.5 yr"
                tail = test_name.replace("donut_", "")
                label = r"$\pm$" + tail + " yr"
            elif prefix == "placebo":
                outcome = r.get("outcome", "")
                label = texvar(outcome.replace("placebo_", ""))
            else:
                label = test_name.replace(f"{prefix}_", "").replace("_", " ").title()
            try:
                n_eff_int = int(float(r["N_eff"])) if pd.notna(r.get("N_eff")) and float(r["N_eff"]) > 0 else None
            except (ValueError, TypeError):
                n_eff_int = None
            n_str = f"{n_eff_int:,}".replace(",", "{,}") if n_eff_int else "---"
            tex.append(
                f"  {label} & {fmt(r['estimate'])} & {fmt(r.get('se_robust', np.nan))} "
                f"& [{fmt(r.get('ci_lower', np.nan))}, {fmt(r.get('ci_upper', np.nan))}] "
                f"& {fmt(r.get('bandwidth', np.nan), 2)} "
                f"& {n_str} \\\\"
            )
        tex.append(r"\addlinespace")

    tex += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} All specifications use local linear regression with "
            r"triangular kernel and MSE-optimal bandwidth (h$^{\ast}\!=\!14.24$ unless noted). "
            r"Robust bias-corrected confidence intervals reported. Donut-hole specifications "
            r"drop observations within $\pm 0.5$, $\pm 1.0$, and $\pm 2.0$ years of the "
            r"cutoff to assess sensitivity to integer-rounding heaping at age 65. "
            r"\textit{Panel D} uses pre-determined covariates (\texttt{INTERNET\_HOGAR}, "
            r"\texttt{SMARTPHONE}) as outcomes with their own outcome-specific MSE-optimal "
            r"bandwidths (15.23 and 14.29, respectively); these estimates therefore differ "
            r"slightly from the corresponding rows in Table~\ref{tab:balance}, which "
            r"re-estimates the same covariate jumps at the \emph{fixed} primary-outcome "
            r"bandwidth ($h^{\ast}\!=\!14.24$) so that all balance tests share a common "
            r"identifying window. We report both because the placebo logic (Panel D) and "
            r"the balance-test logic (Table~\ref{tab:balance}) are conceptually distinct: "
            r"Panel D asks whether each covariate exhibits a placebo discontinuity at its "
            r"own optimal window; Table~\ref{tab:balance} asks whether the covariates are "
            r"balanced \emph{within the bandwidth used for the primary estimates}. "
            r"Estimates close to zero in either presentation support the no-discontinuity-"
            r"in-pretreatment-characteristics assumption."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = "\n".join(tex)
    content = validate_table(content, "table_3_robustness.tex")
    path = os.path.join(TABLES_DIR, "table_3_robustness.tex")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════════════
# TABLE 4: Covariate Balance (AT BANDWIDTH)
# ═══════════════════════════════════════════════════════════════════════════════
def make_table4(robust):
    print("Generating Table 4: Covariate balance (at bandwidth)...")

    cov_data = robust[robust["test"] == "covariate_balance"]
    if len(cov_data) == 0:
        print("  No covariate balance results. Skipping.")
        return

    tex = [
        r"\begin{threeparttable}",
        r"\begin{tabular}{l ccccc}",
        r"\toprule",
        r"Covariate & RD Estimate & SE & 95\% CI & BW & N \\",
        r"\midrule",
    ]

    for _, r in cov_data.iterrows():
        ci_lo = r.get("ci_lower", np.nan)
        ci_hi = r.get("ci_upper", np.nan)
        sig = ""
        if pd.notna(ci_lo) and pd.notna(ci_hi):
            if ci_lo > 0 or ci_hi < 0:
                sig = "$^{*}$"
        try:
            n_eff_int = int(float(r["N_eff"])) if pd.notna(r.get("N_eff")) and float(r["N_eff"]) > 0 else None
        except (ValueError, TypeError):
            n_eff_int = None
        n_str = f"{n_eff_int:,}".replace(",", "{,}") if n_eff_int else "---"
        tex.append(
            f"  {texvar(r['outcome'])} & {fmt(r['estimate'])}{sig} "
            f"& {fmt(r.get('se_robust', np.nan))} "
            f"& [{fmt(ci_lo)}, {fmt(ci_hi)}] "
            f"& {fmt(r.get('bandwidth', np.nan), 2)} "
            f"& {n_str} \\\\"
        )

    tex += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} RDD estimates with each covariate as the outcome. "
            r"Tests are restricted to observations within the MSE-optimal bandwidth "
            r"(h$^{\ast}\!=\!14.24$). A statistically significant estimate would "
            r"indicate a discontinuity in pre-determined characteristics, threatening "
            r"RD validity. $^{*}$ 95\% CI excludes zero. None of the covariates "
            r"exhibits a discontinuity at the cutoff at the 95\% level (all CIs include "
            r"zero), supporting the local continuity assumption. The \texttt{SMARTPHONE} "
            r"CI is the closest case: the lower bound is essentially zero and the "
            r"interval is asymmetric toward positive values, leaving open the "
            r"possibility of an up-to-8.6 percentage-point smartphone gap at the cutoff "
            r"that we cannot statistically rule out; we therefore caution that the "
            r"smartphone-balance result is the weakest evidence in this table rather "
            r"than treating it as a clean null. Slight numerical differences with "
            r"Table~\ref{tab:robustness} Panel~D arise because Panel~D uses "
            r"outcome-specific MSE-optimal bandwidths (15.23 / 14.29) while this table "
            r"fixes the bandwidth at the primary outcome's $h^{\ast}\!=\!14.24$."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = "\n".join(tex)
    content = validate_table(content, "table_4_covariate_balance.tex")
    path = os.path.join(TABLES_DIR, "table_4_covariate_balance.tex")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1: RD Plot (binned scatter with local linear fit)
# ═══════════════════════════════════════════════════════════════════════════════
def make_figure1(df):
    print("Generating Figure 1: RD plot...")

    sub = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])
    x = sub[RUNNING_VAR].values
    y = sub[PRIMARY_OUTCOME].values

    if len(x) < 20:
        print("  Insufficient data. Skipping.")
        return

    # Restrict plot to ~2.5x bandwidth for clean visualization
    h_approx = 2.0
    x_range = h_approx * 2.5
    mask = np.abs(x) <= x_range
    x_p, y_p = x[mask], y[mask]

    n_bins = 15

    def bin_scatter(xv, yv, nbins):
        if len(xv) < nbins:
            return xv, yv
        bins = np.linspace(xv.min(), xv.max(), nbins + 1)
        cx, cy = [], []
        for i in range(nbins):
            m = (xv >= bins[i]) & (xv < bins[i + 1])
            if i == nbins - 1:
                m = (xv >= bins[i]) & (xv <= bins[i + 1])
            if m.sum() > 0:
                cx.append(xv[m].mean())
                cy.append(yv[m].mean())
        return np.array(cx), np.array(cy)

    x_left, y_left = x_p[x_p < 0], y_p[x_p < 0]
    x_right, y_right = x_p[x_p >= 0], y_p[x_p >= 0]

    fig, ax = plt.subplots(figsize=(8, 5))

    if len(x_left) > 3:
        bx, by = bin_scatter(x_left, y_left, n_bins)
        ax.scatter(bx, by, color="#2166ac", s=60, zorder=3, label="Below threshold")
        coeffs = np.polyfit(x_left, y_left, 1)
        xs = np.linspace(x_left.min(), 0, 100)
        ax.plot(xs, np.poly1d(coeffs)(xs), color="#2166ac", linewidth=2)

    if len(x_right) > 3:
        bx, by = bin_scatter(x_right, y_right, n_bins)
        ax.scatter(bx, by, color="#b2182b", s=60, zorder=3, label="Above threshold")
        coeffs = np.polyfit(x_right, y_right, 1)
        xs = np.linspace(0, x_right.max(), 100)
        ax.plot(xs, np.poly1d(coeffs)(xs), color="#b2182b", linewidth=2)

    ax.axvline(x=0, color="black", linestyle="--", linewidth=1, alpha=0.7, label="Threshold")
    ax.set_xlim(-x_range, x_range)
    ax.set_xlabel("Age centered at 65 (years)", fontsize=12)
    ax.set_ylabel(PRIMARY_OUTCOME.replace("_", " ").title(), fontsize=12)
    ax.set_title("RDD Plot: Digital Wallet Ownership by Age", fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    for ext in ["png", "pdf"]:
        path = os.path.join(FIGURES_DIR, f"figure_1_rdplot.{ext}")
        plt.savefig(path, dpi=150 if ext == "png" else 300, bbox_inches="tight")
    plt.close("all")
    print(f"  Saved: figure_1_rdplot.png/.pdf")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2: Bandwidth Sensitivity
# ═══════════════════════════════════════════════════════════════════════════════
def make_figure2(robust):
    print("Generating Figure 2: Bandwidth sensitivity...")

    bw_data = robust[robust["test"].str.startswith("bandwidth")].copy()
    if len(bw_data) == 0:
        print("  No bandwidth results. Skipping.")
        return

    bw_data = bw_data.sort_values("bandwidth")
    estimates = bw_data["estimate"].values.copy()
    ci_lo = bw_data["ci_lower"].values
    ci_hi = bw_data["ci_upper"].values

    # Fill NaN estimates with CI midpoint
    for i in range(len(estimates)):
        if np.isnan(estimates[i]) and not np.isnan(ci_lo[i]) and not np.isnan(ci_hi[i]):
            estimates[i] = (ci_lo[i] + ci_hi[i]) / 2.0

    labels = []
    for _, r in bw_data.iterrows():
        bw = r.get("bandwidth", np.nan)
        lab = r["test"].replace("bandwidth_", "")
        labels.append(f"{lab}\n(h={bw:.2f})" if pd.notna(bw) else lab)

    yerr_lo = np.where(np.isnan(estimates - ci_lo), 0, estimates - ci_lo)
    yerr_hi = np.where(np.isnan(ci_hi - estimates), 0, ci_hi - estimates)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.errorbar(range(len(estimates)), estimates, yerr=[yerr_lo, yerr_hi],
                fmt="o", color="#2166ac", capsize=5, capthick=2, markersize=8, linewidth=2)
    ax.axhline(y=0, color="black", linestyle="--", linewidth=1, alpha=0.5)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("RD Estimate", fontsize=12)
    ax.set_title("Bandwidth Sensitivity", fontsize=13)
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()

    for ext in ["png", "pdf"]:
        path = os.path.join(FIGURES_DIR, f"figure_2_bandwidth_sensitivity.{ext}")
        plt.savefig(path, dpi=150 if ext == "png" else 300, bbox_inches="tight")
    plt.close("all")
    print(f"  Saved: figure_2_bandwidth_sensitivity.png/.pdf")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 70)
    print("03_output.py — Tables and Figures")
    print("=" * 70)

    df = pd.read_csv(os.path.join(DATA_DIR, "clean_data.csv"))
    print(f"Clean data: {len(df)} rows")

    main_results = pd.read_csv(os.path.join(DATA_DIR, "main_results.csv"))
    print(f"Main results: {len(main_results)} rows")

    robust_path = os.path.join(DATA_DIR, "robustness_results.csv")
    robust = pd.read_csv(robust_path) if os.path.exists(robust_path) else None
    if robust is not None:
        print(f"Robustness: {len(robust)} rows")

    print()
    make_table1(df)
    make_table2(main_results, robust=robust)
    if robust is not None:
        make_table3(robust)
        make_table4(robust)
    print()
    make_figure1(df)
    if robust is not None:
        make_figure2(robust)

    # ── Final validation: check all tables for NaN ────────────────────────
    print("\n--- Final table validation ---")
    all_clean = True
    for tex_file in sorted(os.listdir(TABLES_DIR)):
        if tex_file.endswith(".tex"):
            content = open(os.path.join(TABLES_DIR, tex_file)).read()
            if "nan" in content.lower() or "& &" in content:
                print(f"  PROBLEM: {tex_file} still has blank/NaN cells!")
                all_clean = False
    if all_clean:
        print("  All tables validated: no NaN or blank cells.")

    print("\n" + "=" * 70)
    print("03_output.py complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
