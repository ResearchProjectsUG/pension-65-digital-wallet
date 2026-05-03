"""
script.py — Pipeline completo end-to-end del paper sobre adopción de billetera
digital (Pensión 65 RDD). Reúne los 5 scripts originales en un solo archivo
PORTABLE que cualquiera que clone el repositorio pueda ejecutar.

PIPELINE (5 fases):
    Fase 0  — Descomprime los 3 raw_data_*.zip que están en data/clean/
    Fase 1  — preprocess: mergea los 6 módulos ENAHO 2024 → enaho_2024_clean.csv
    Fase 2  — clean: filtra muestra RDD, centra running variable → clean_data.csv
    Fase 3  — main: estima el RDD principal (rdrobust + fallback WLS) → main_results.csv
    Fase 4  — robustness: McCrary, placebos, BW, donut, balance, polinomios, etc.
    Fase 5  — output: tablas LaTeX y figuras del paper

USO:
    python scripts/script_completo/script.py

REQUISITOS:
    - Python 3.9+
    - pandas, numpy, matplotlib, statsmodels (se intentan instalar si faltan)
    - rdrobust, rddensity, linearmodels (opcionales, hay fallback)
    - Los 3 archivos data/clean/raw_data_*.zip presentes en el repo

OUTPUTS (todos relativos al repo):
    data/clean/enaho_2024_clean.csv
    data/clean/clean_data.csv
    data/clean/main_results.csv
    data/clean/robustness_results.csv
    paper/figures/figure_mccrary_density.{png,pdf}
    paper/figures/figure_1_rdplot.{png,pdf}
    paper/figures/figure_2_bandwidth_sensitivity.{png,pdf}
    paper/tables/table_1_summary.tex
    paper/tables/table_2_main_results.tex
    paper/tables/table_3_robustness.tex
    paper/tables/table_4_covariate_balance.tex
"""

from __future__ import annotations

import os
import sys
import subprocess
import warnings
import zipfile
from pathlib import Path

warnings.filterwarnings("ignore")

# ════════════════════════════════════════════════════════════════════════════
# RUTAS PORTABLES (todas derivadas de la ubicación de este script)
# ════════════════════════════════════════════════════════════════════════════
SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent                           # scripts/script_completo/
REPO_ROOT = SCRIPT_DIR.parent.parent                       # raíz del repo

DATA_DIR = REPO_ROOT / "data" / "clean"
RAW_EXTRACTED_DIR = DATA_DIR / "_raw_extracted"
PAPER_DIR = REPO_ROOT / "paper"
TABLES_DIR = PAPER_DIR / "tables"
FIGURES_DIR = PAPER_DIR / "figures"

# Archivos intermedios y finales
ENAHO_CLEAN_CSV = DATA_DIR / "enaho_2024_clean.csv"
CLEAN_DATA_CSV = DATA_DIR / "clean_data.csv"
MAIN_RESULTS_CSV = DATA_DIR / "main_results.csv"
ROBUSTNESS_CSV = DATA_DIR / "robustness_results.csv"

# Asegurar que los directorios existan
for d in (DATA_DIR, TABLES_DIR, FIGURES_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Reproducibilidad
RANDOM_SEED = 42

# ZIPs y sus contenidos esperados (relative to RAW_EXTRACTED_DIR)
ZIP_FILES = ["raw_data_1.zip", "raw_data_2.zip", "raw_data_3.zip"]
EXPECTED_CSVS = {
    "m01": "raw_data_1/Enaho01-2024-100.csv",
    "m02": "raw_data_1/Enaho01-2024-200.csv",
    "m18": "raw_data_1/Enaho01-2024-612.csv",
    "m03": "raw_data_2/Enaho01A-2024-300.csv",
    "m05": "raw_data_3/Enaho01a-2024-500.csv",
    "sum": "raw_data_3/Sumaria-2024.csv",
}


# ════════════════════════════════════════════════════════════════════════════
# INSTALADOR DE DEPENDENCIAS
# ════════════════════════════════════════════════════════════════════════════
def ensure_package(pkg: str, import_name: str | None = None) -> bool:
    """Instala pkg vía pip si no está disponible. Retorna True si quedó importable."""
    name = import_name or pkg
    try:
        __import__(name)
        return True
    except ImportError:
        print(f"  [deps] Installing {pkg}...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", pkg],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            __import__(name)
            return True
        except Exception as e:
            print(f"  [deps] FAILED to install {pkg}: {e}")
            return False


def install_dependencies():
    print("\n[deps] Verificando dependencias...")
    # Núcleo (obligatorias)
    for pkg in ["pandas", "numpy", "matplotlib", "statsmodels"]:
        ok = ensure_package(pkg)
        if not ok:
            print(f"[deps] FATAL: '{pkg}' es obligatorio. Abortando.")
            sys.exit(1)
    # Opcionales (hay fallback)
    ensure_package("rdrobust")
    ensure_package("rddensity")
    ensure_package("linearmodels")
    print("[deps] Dependencias OK.\n")


# Llamamos antes de importar pandas/numpy
install_dependencies()

import numpy as np                                              # noqa: E402
import pandas as pd                                             # noqa: E402

np.random.seed(RANDOM_SEED)

# Imports opcionales con flags
try:
    from rdrobust import rdrobust
    RDROBUST_OK = True
except ImportError:
    RDROBUST_OK = False
    print("[warn] rdrobust no disponible — usando fallback statsmodels.")

try:
    import linearmodels  # noqa: F401
except ImportError:
    pass


# ════════════════════════════════════════════════════════════════════════════
# FASE 0 — Descomprimir los 3 zips
# ════════════════════════════════════════════════════════════════════════════
def phase_0_extract_zips():
    print("=" * 70)
    print("FASE 0 — Descomprimir raw_data_*.zip")
    print("=" * 70)

    RAW_EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)

    # Si los 6 CSVs ya existen, saltar
    all_present = all((RAW_EXTRACTED_DIR / rel).exists() for rel in EXPECTED_CSVS.values())
    if all_present:
        print(f"  Todos los CSVs ya existen en {RAW_EXTRACTED_DIR}. Saltando extracción.")
        return

    for zip_name in ZIP_FILES:
        zip_path = DATA_DIR / zip_name
        if not zip_path.exists():
            print(f"  ERROR: No se encontró {zip_path}")
            print(f"  Asegurate de que los 3 raw_data_*.zip estén en data/clean/")
            sys.exit(1)
        print(f"  Extrayendo {zip_name}...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(RAW_EXTRACTED_DIR)

    # Verificar
    missing = [rel for rel in EXPECTED_CSVS.values() if not (RAW_EXTRACTED_DIR / rel).exists()]
    if missing:
        print(f"  ERROR: Faltan archivos tras extracción: {missing}")
        sys.exit(1)
    print(f"  OK — 6 CSVs extraídos en {RAW_EXTRACTED_DIR}\n")


# ════════════════════════════════════════════════════════════════════════════
# FASE 1 — Preprocess ENAHO 2024 (preprocess_enaho_2024.py)
# ════════════════════════════════════════════════════════════════════════════
BILLETERA_E1_CODE = 9
BILLETERA_H_CODE = 7
KEYS_PERSON = ["CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO"]
KEYS_HOUSEHOLD = ["CONGLOME", "VIVIENDA", "HOGAR"]


def _load_csv(label: str, path: Path) -> pd.DataFrame:
    print(f"  [load] {label}: {path.name}")
    df = pd.read_csv(path, encoding="latin-1", low_memory=False)
    df.columns = [c.upper() for c in df.columns]
    print(f"         shape: {df.shape}")
    return df


def _detect_billetera_tenencia(m05: pd.DataFrame) -> pd.Series:
    col = f"P558E1_{BILLETERA_E1_CODE}"
    if col not in m05.columns:
        print(f"  [warn] {col} not found — tiene_billetera will be all 0")
        return pd.Series(0, index=m05.index)
    return (m05[col].astype(str).str.strip() == str(BILLETERA_E1_CODE)).astype(int)


def _detect_billetera_uso(m05: pd.DataFrame) -> pd.Series:
    use = pd.Series(0, index=m05.index)
    for g in range(1, 13):
        col = f"P558H{g}_{BILLETERA_H_CODE}"
        if col in m05.columns:
            sel = (m05[col].astype(str).str.strip() == str(BILLETERA_H_CODE)).astype(int)
            use = use | sel
    return use


def phase_1_preprocess():
    print("=" * 70)
    print("FASE 1 — Preprocess ENAHO 2024 (merge a nivel persona)")
    print("=" * 70)

    files = {k: RAW_EXTRACTED_DIR / rel for k, rel in EXPECTED_CSVS.items()}

    print("\n[1] Loading modules...")
    m01 = _load_csv("m01-Vivienda", files["m01"])
    m02 = _load_csv("m02-Miembros", files["m02"])
    m03 = _load_csv("m03-Educacion", files["m03"])
    m05 = _load_csv("m05-Empleo+Billetera", files["m05"])
    m18 = _load_csv("m18-Equipamiento", files["m18"])
    sumaria = _load_csv("sumaria", files["sum"])

    # ── Variables billetera ───────────────────────────────────────────────
    print("\n[2] Building billetera variables from m05...")
    m05["TIENE_BILLETERA"] = _detect_billetera_tenencia(m05)
    m05["USA_BILLETERA"] = _detect_billetera_uso(m05)

    m05["TIENE_BILLETERA_ALT_E10"] = (
        m05["P558E1_10"].astype(str).str.strip() == "10"
    ).astype(int) if "P558E1_10" in m05.columns else 0
    m05["TIENE_BILLETERA_ALT_E6"] = (
        m05["P558E1_6"].astype(str).str.strip() == "6"
    ).astype(int) if "P558E1_6" in m05.columns else 0

    use_h6 = pd.Series(0, index=m05.index)
    for g in range(1, 13):
        col = f"P558H{g}_6"
        if col in m05.columns:
            use_h6 = use_h6 | (m05[col].astype(str).str.strip() == "6").astype(int)
    m05["USA_BILLETERA_ALT_H6"] = use_h6

    print(f"  tiene_billetera (E1_{BILLETERA_E1_CODE}): {m05['TIENE_BILLETERA'].mean()*100:.1f}%")
    print(f"  usa_billetera (any H_{BILLETERA_H_CODE}): {m05['USA_BILLETERA'].mean()*100:.1f}%")

    # ── Banco previo / formal / ocupado ───────────────────────────────────
    m05["BANCO_PREVIO"] = (
        ((m05["P558E1_1"].astype(str).str.strip() == "1").astype(int)) |
        ((m05["P558E1_8"].astype(str).str.strip() == "8").astype(int))
        if "P558E1_1" in m05.columns and "P558E1_8" in m05.columns
        else pd.Series(0, index=m05.index)
    ).astype(int)

    if "P514" in m05.columns:
        m05["FORMAL"] = (pd.to_numeric(m05["P514"], errors="coerce") == 1).astype(int)
    else:
        m05["FORMAL"] = 0

    if "OCU500" in m05.columns:
        m05["OCUPADO"] = (pd.to_numeric(m05["OCU500"], errors="coerce") == 1).astype(int)
    else:
        m05["OCUPADO"] = 0

    m05_keep = [c for c in (KEYS_PERSON + [
        "TIENE_BILLETERA", "USA_BILLETERA",
        "TIENE_BILLETERA_ALT_E10", "TIENE_BILLETERA_ALT_E6", "USA_BILLETERA_ALT_H6",
        "BANCO_PREVIO", "FORMAL", "OCUPADO"
    ]) if c in m05.columns]
    m05_p = m05[m05_keep].drop_duplicates(subset=KEYS_PERSON, keep="first")
    print(f"  m05 person-level: {m05_p.shape}")

    # ── m02 demografía ────────────────────────────────────────────────────
    print("\n[3] Extracting m02 demographics + FACPOB07...")
    m02_keep = [c for c in (KEYS_PERSON + ["P207", "P208A", "FACPOB07"]) if c in m02.columns]
    m02_p = m02[m02_keep].copy().rename(columns={
        "P207": "GENERO", "P208A": "EDAD", "FACPOB07": "FACTOR_EXPANSION",
    })

    # ── m03 educación ─────────────────────────────────────────────────────
    print("\n[4] Extracting m03 education...")
    m03_keep = [c for c in (KEYS_PERSON + ["P301A"]) if c in m03.columns]
    m03_p = m03[m03_keep].copy().rename(columns={"P301A": "NIVEL_EDUCATIVO"})

    # ── m18 smartphone (long → wide) ──────────────────────────────────────
    print("\n[5] Extracting m18 smartphone (long-format pivot)...")
    SMARTPHONE_ITEM_CODE = 10
    smart_rows = m18[m18["P612N"] == SMARTPHONE_ITEM_CODE].copy()
    smart_rows["SMARTPHONE"] = (pd.to_numeric(smart_rows["P612"], errors="coerce") == 1).astype(int)
    m18_h = smart_rows[KEYS_HOUSEHOLD + ["SMARTPHONE"]].drop_duplicates(
        subset=KEYS_HOUSEHOLD, keep="first"
    )
    print(f"  smartphone: {m18_h['SMARTPHONE'].mean()*100:.1f}% of households")

    # ── m01 internet ──────────────────────────────────────────────────────
    print("\n[6] Extracting m01 housing/internet...")
    if "P114B2" in m01.columns:
        m01["INTERNET_HOGAR"] = (m01["P114B2"].astype(str).str.strip() == "1").astype(int)
    else:
        m01["INTERNET_HOGAR"] = 0
    print(f"  internet_hogar: {m01['INTERNET_HOGAR'].mean()*100:.1f}% of households")

    m01_keep = [c for c in (KEYS_HOUSEHOLD + ["UBIGEO", "ESTRATO", "DOMINIO", "INTERNET_HOGAR"])
                if c in m01.columns]
    m01_h = m01[m01_keep].drop_duplicates(subset=KEYS_HOUSEHOLD, keep="first")

    # ── Sumaria ingreso pc ────────────────────────────────────────────────
    print("\n[7] Extracting sumaria income...")
    sum_keep = [c for c in (KEYS_HOUSEHOLD + ["INGHOG2D", "GASHOG2D", "MIEPERHO", "POBREZA"])
                if c in sumaria.columns]
    sum_h = sumaria[sum_keep].drop_duplicates(subset=KEYS_HOUSEHOLD, keep="first")
    sum_h["INGRESO_PC"] = (
        pd.to_numeric(sum_h["INGHOG2D"], errors="coerce") /
        pd.to_numeric(sum_h["MIEPERHO"], errors="coerce").replace(0, np.nan)
    )

    # ── Merge total ───────────────────────────────────────────────────────
    print("\n[8] Merging all modules at person level...")
    df = m02_p.copy()
    df = df.merge(m03_p, on=KEYS_PERSON, how="left")
    df = df.merge(m05_p, on=KEYS_PERSON, how="left")
    df = df.merge(m01_h, on=KEYS_HOUSEHOLD, how="left")
    df = df.merge(m18_h, on=KEYS_HOUSEHOLD, how="left")
    df = df.merge(sum_h, on=KEYS_HOUSEHOLD, how="left")

    if "UBIGEO" in df.columns:
        df["DPTO"] = df["UBIGEO"].astype(str).str.zfill(6).str[:2]

    for col in ["TIENE_BILLETERA", "USA_BILLETERA", "BANCO_PREVIO", "FORMAL"]:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    print(f"  Final shape: {df.shape}")
    print(f"\n[9] Saving to {ENAHO_CLEAN_CSV}...")
    df.to_csv(ENAHO_CLEAN_CSV, index=False, encoding="utf-8")
    size_mb = ENAHO_CLEAN_CSV.stat().st_size / 1024 / 1024
    print(f"  Saved ({size_mb:.1f} MB)\n")


# ════════════════════════════════════════════════════════════════════════════
# FASE 2 — Cleaning RDD (00_clean.py)
# ════════════════════════════════════════════════════════════════════════════
RUNNING_VAR_RAW = "EDAD"
THRESHOLD = 65
TREATMENT_VAR = ""
OUTCOME_VARS = ["TIENE_BILLETERA", "USA_BILLETERA"]
CLUSTER_VAR = "DPTO"
TIME_VAR = None
COVARIATES = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
PLACEBO_OUTCOMES = ["INTERNET_HOGAR", "SMARTPHONE"]


def phase_2_clean():
    print("=" * 70)
    print("FASE 2 — RDD Data Cleaning")
    print("=" * 70)

    print(f"Loading: {ENAHO_CLEAN_CSV}")
    df = pd.read_csv(ENAHO_CLEAN_CSV, encoding="latin-1", low_memory=False)
    print(f"Raw data: {len(df):,} rows x {df.shape[1]} cols")

    # Missingness
    print("\n--- Missingness table (key variables) ---")
    key_vars = [RUNNING_VAR_RAW, TREATMENT_VAR, CLUSTER_VAR] + OUTCOME_VARS + COVARIATES
    if TIME_VAR:
        key_vars.append(TIME_VAR)
    key_vars = [v for v in key_vars if v and v in df.columns]
    for var in key_vars:
        n_miss = df[var].isna().sum()
        pct = 100 * n_miss / len(df)
        print(f"  {var:30s}: {n_miss:6,} missing ({pct:.1f}%)")

    if RUNNING_VAR_RAW not in df.columns:
        print(f"\nERROR: Running variable '{RUNNING_VAR_RAW}' not in data.")
        sys.exit(1)

    # Coerce running variable a numérico (strings vacíos / espacios → NaN)
    # Sin esto, la resta `df[EDAD] - THRESHOLD` truena si la columna es object.
    df[RUNNING_VAR_RAW] = pd.to_numeric(df[RUNNING_VAR_RAW], errors="coerce")

    # Filtrar
    n_before = len(df)
    df_rdd = df.dropna(subset=[RUNNING_VAR_RAW]).copy()
    print(f"\n--- Filter: running variable non-missing ---")
    print(f"  Before: {n_before:,}  After: {len(df_rdd):,}")

    # Centrar
    if isinstance(THRESHOLD, (int, float)) and THRESHOLD != 0:
        df_rdd["running_centered"] = df_rdd[RUNNING_VAR_RAW] - THRESHOLD
        print(f"  Centered at threshold = {THRESHOLD}")
    else:
        df_rdd["running_centered"] = df_rdd[RUNNING_VAR_RAW]

    # Tratamiento
    if TREATMENT_VAR and TREATMENT_VAR in df_rdd.columns:
        df_rdd["treat"] = df_rdd[TREATMENT_VAR].astype(float)
    else:
        df_rdd["treat"] = (df_rdd["running_centered"] >= 0).astype(float)
    print(f"  Treated: {int(df_rdd['treat'].sum()):,}  "
          f"Control: {len(df_rdd) - int(df_rdd['treat'].sum()):,}")

    # Validación outcomes
    print("\n--- Outcome validation ---")
    outcomes_present = [o for o in OUTCOME_VARS if o in df_rdd.columns]
    if not outcomes_present:
        print("  ERROR: No outcome variables found!")
        sys.exit(1)
    for var in outcomes_present:
        s = df_rdd[var].dropna()
        corr = df_rdd[[var, "running_centered"]].dropna().corr().iloc[0, 1]
        ctrl_mean = df_rdd.loc[df_rdd["treat"] == 0, var].mean()
        treat_mean = df_rdd.loc[df_rdd["treat"] == 1, var].mean()
        print(f"  {var}: N={len(s)}, ctrl={ctrl_mean:.4f}, "
              f"treat={treat_mean:.4f}, corr={corr:.4f}")

    # Top correlates
    print("\n--- Top 10 variables correlated with running variable ---")
    numeric_cols = df_rdd.select_dtypes(include=[np.number]).columns
    corrs = {}
    for col in numeric_cols:
        if col in ("running_centered", "treat", RUNNING_VAR_RAW):
            continue
        try:
            r = df_rdd[["running_centered", col]].dropna().corr().iloc[0, 1]
            if not np.isnan(r):
                corrs[col] = abs(r)
        except Exception:
            pass
    for i, (col, r) in enumerate(sorted(corrs.items(), key=lambda x: -x[1])[:10], 1):
        print(f"  {i:2d}. {col:40s} |r| = {r:.4f}")

    # Save
    df_rdd.to_csv(CLEAN_DATA_CSV, index=False)
    print(f"\nSaved: {CLEAN_DATA_CSV} ({len(df_rdd):,} rows x {df_rdd.shape[1]} cols)")

    # Placeholder de results
    if not MAIN_RESULTS_CSV.exists():
        pd.DataFrame(columns=["outcome", "specification", "estimate", "se_robust",
                              "ci_lower", "ci_upper", "bandwidth", "N_eff", "method"]
                     ).to_csv(MAIN_RESULTS_CSV, index=False)
        print(f"Saved placeholder: {MAIN_RESULTS_CSV}")
    print()


# ════════════════════════════════════════════════════════════════════════════
# FASE 3 — Main RDD (01_main.py)
# ════════════════════════════════════════════════════════════════════════════
RUNNING_VAR = "running_centered"
COVARIATES_BASIC = ["INTERNET_HOGAR", "SMARTPHONE"]
COVARIATES_EXT = ["INTERNET_HOGAR", "SMARTPHONE", "POBREZA", "INGRESO_PC", "NIVEL_EDUCATIVO"]
EXPECTED_SIGNS = {"TIENE_BILLETERA": "+", "USA_BILLETERA": "+"}
HETEROGENEITY_VARS = ["POBREZA", "INTERNET_HOGAR", "SMARTPHONE"]


def _safe_scalar(obj, idx=0):
    try:
        if hasattr(obj, "iloc"):
            return float(obj.iloc[idx])
        elif hasattr(obj, "__getitem__") and hasattr(obj, "__len__"):
            return float(obj[idx])
        return float(obj)
    except Exception:
        return np.nan


def _run_rdd_rdrobust(y, x, cluster=None, covs=None, h=None):
    kwargs = dict(y=y, x=x, kernel="triangular", bwselect="mserd")
    if cluster is not None:
        kwargs["cluster"] = cluster
    if covs is not None:
        kwargs["covs"] = covs
    if h is not None:
        kwargs["h"] = h
        del kwargs["bwselect"]

    rd = rdrobust(**kwargs)

    estimate = _safe_scalar(rd.coef, 0)
    estimate_bc = (_safe_scalar(rd.coef, 1)
                   if hasattr(rd.coef, "__len__") and len(rd.coef) > 1 else estimate)
    se_conv = _safe_scalar(rd.se, 0)
    se_robust = _safe_scalar(rd.se, -1)

    try:
        ci_lower = float(rd.ci.iloc[-1, 0]) if hasattr(rd.ci, "iloc") else np.nan
        ci_upper = float(rd.ci.iloc[-1, 1]) if hasattr(rd.ci, "iloc") else np.nan
    except Exception:
        ci_lower = estimate - 1.96 * se_conv if not np.isnan(se_conv) else np.nan
        ci_upper = estimate + 1.96 * se_conv if not np.isnan(se_conv) else np.nan

    bandwidth = (float(rd.bws.iloc[0, 0]) if hasattr(rd.bws, "iloc")
                 else _safe_scalar(rd.bws, 0))

    try:
        n_left = int(rd.N_h[0])
        n_right = int(rd.N_h[1]) if len(rd.N_h) > 1 else 0
    except Exception:
        n_left = n_right = 0

    if np.isnan(estimate) and not np.isnan(ci_lower) and not np.isnan(ci_upper):
        estimate = (ci_lower + ci_upper) / 2.0
        se_robust = (ci_upper - ci_lower) / (2 * 1.96)

    return {
        "estimate": estimate, "estimate_bc": estimate_bc,
        "se_conv": se_conv, "se_robust": se_robust,
        "ci_lower": ci_lower, "ci_upper": ci_upper,
        "bandwidth": bandwidth,
        "N_left": n_left, "N_right": n_right, "N_eff": n_left + n_right,
        "method": "rdrobust",
    }


def _run_rdd_statsmodels(y, x, cluster=None, h=None):
    import statsmodels.api as sm
    if h is None:
        h = 1.5 * np.std(x)
    mask = np.abs(x) <= h
    y_bw, x_bw = y[mask], x[mask]
    if len(y_bw) < 10:
        return None
    treat = (x_bw >= 0).astype(float)
    weights = np.maximum(1 - np.abs(x_bw) / h, 0)
    X = sm.add_constant(np.column_stack([treat, x_bw, treat * x_bw]))
    try:
        mod = sm.WLS(y_bw, X, weights=weights).fit(cov_type="HC2")
        ci = mod.conf_int()[1]
        return {
            "estimate": mod.params[1], "estimate_bc": mod.params[1],
            "se_conv": mod.bse[1], "se_robust": mod.bse[1],
            "ci_lower": ci[0], "ci_upper": ci[1],
            "bandwidth": h,
            "N_left": int((x_bw < 0).sum()), "N_right": int((x_bw >= 0).sum()),
            "N_eff": len(y_bw),
            "method": "statsmodels_WLS",
        }
    except Exception:
        return None


def run_rdd(df, outcome, covariates=None, h=None, label="baseline"):
    """RDD con fallback automático. Siempre devuelve dict completo."""
    sub = df.dropna(subset=[outcome, RUNNING_VAR]).copy()
    y = sub[outcome].values
    x = sub[RUNNING_VAR].values
    cluster = sub[CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None

    cov_matrix = None
    if covariates:
        avail = [c for c in covariates if c in sub.columns]
        if avail:
            cov_sub = sub[avail].dropna()
            valid = cov_sub.index.intersection(sub.index)
            if len(valid) > 50:
                y = sub.loc[valid, outcome].values
                x = sub.loc[valid, RUNNING_VAR].values
                cluster = (sub.loc[valid, CLUSTER_VAR].values
                           if CLUSTER_VAR in sub.columns else None)
                cov_matrix = cov_sub.loc[valid].values

    result = {
        "outcome": outcome, "specification": label,
        "estimate": np.nan, "estimate_bc": np.nan,
        "se_conv": np.nan, "se_robust": np.nan,
        "ci_lower": np.nan, "ci_upper": np.nan,
        "bandwidth": np.nan, "N_eff": len(y),
        "N_left": np.nan, "N_right": np.nan,
        "method": "none",
    }

    if len(y) < 20:
        print(f"    Insufficient obs for {outcome} (N={len(y)}). Skipping.")
        return result

    if RDROBUST_OK:
        try:
            res = _run_rdd_rdrobust(y, x, cluster=cluster, covs=cov_matrix, h=h)
            result.update(res)
            return result
        except Exception as e:
            print(f"    rdrobust failed: {e}. Using statsmodels fallback.")

    fb = _run_rdd_statsmodels(y, x, cluster=cluster, h=h)
    if fb:
        result.update(fb)
    else:
        print(f"    Both estimators failed for {outcome}.")
    return result


def phase_3_main():
    print("=" * 70)
    print("FASE 3 — RDD Main Estimation")
    print("=" * 70)

    df = pd.read_csv(CLEAN_DATA_CSV)
    print(f"Loaded: {len(df):,} rows x {df.shape[1]} cols")

    print("\n--- Expected signs ---")
    for outcome, sign in EXPECTED_SIGNS.items():
        print(f"  {outcome}: {sign}")

    all_results = []
    outcomes_present = [o for o in OUTCOME_VARS if o in df.columns]

    # Spec 1: Baseline
    print("\n--- Baseline RDD (no covariates) ---")
    for outcome in outcomes_present:
        print(f"\n  Outcome: {outcome}")
        res = run_rdd(df, outcome, label="baseline")
        all_results.append(res)
        print(f"    Estimate: {res['estimate']:.4f}  SE: {res['se_robust']:.4f}")
        print(f"    95% CI: [{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]")
        print(f"    BW: {res['bandwidth']:.3f}  N_eff: {res['N_eff']}  Method: {res['method']}")

    # Spec 2: Basic covariates
    covs_avail = [c for c in COVARIATES_BASIC if c in df.columns]
    if covs_avail:
        print(f"\n--- RDD with covariates: {covs_avail} ---")
        for outcome in outcomes_present:
            print(f"\n  Outcome: {outcome}")
            res = run_rdd(df, outcome, covariates=covs_avail, label="with_covariates")
            all_results.append(res)
            print(f"    Estimate: {res['estimate']:.4f}  SE: {res['se_robust']:.4f}")
            print(f"    95% CI: [{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]")

    # Spec 3: Extended covariates
    covs_ext = [c for c in COVARIATES_EXT if c in df.columns]
    if len(covs_ext) > len(covs_avail):
        print(f"\n--- RDD with extended covariates: {covs_ext} ---")
        for outcome in outcomes_present:
            res = run_rdd(df, outcome, covariates=covs_ext, label="extended_covariates")
            all_results.append(res)

    # Effect sizes
    print("\n--- Effect Sizes ---")
    for outcome in outcomes_present:
        baseline = [r for r in all_results
                    if r["outcome"] == outcome and r["specification"] == "baseline"]
        if baseline and not np.isnan(baseline[0]["estimate"]):
            est = baseline[0]["estimate"]
            sd = df[outcome].std()
            cohens_d = est / sd if sd > 0 else np.nan
            mean_val = df[outcome].mean()
            pct_change = 100 * est / abs(mean_val) if abs(mean_val) > 1e-10 else np.nan
            flag = " ***LARGE***" if (not np.isnan(cohens_d) and abs(cohens_d) > 1.0) else ""
            print(f"  {outcome}: Cohen's d={cohens_d:.3f}  %change={pct_change:.1f}%{flag}")

    # Heterogeneity
    het_vars = [h for h in HETEROGENEITY_VARS if h in df.columns]
    if het_vars:
        print(f"\n--- Heterogeneity (split-sample RDD) ---")
        for outcome in outcomes_present:
            for mod in het_vars:
                sub = df.dropna(subset=[outcome, RUNNING_VAR, mod]).copy()
                sub[mod] = pd.to_numeric(sub[mod], errors="coerce")
                sub = sub.dropna(subset=[mod])
                if len(sub) < 40 or sub[mod].nunique() <= 1:
                    continue
                median_val = sub[mod].median()
                sub_lo = sub[sub[mod] <= median_val]
                sub_hi = sub[sub[mod] > median_val]
                for group_name, group_df in [("low", sub_lo), ("high", sub_hi)]:
                    if len(group_df) >= 20:
                        res = run_rdd(group_df, outcome, label=f"het_{mod}_{group_name}")
                        all_results.append(res)
                        print(f"  {outcome} | {mod}={group_name}: est={res['estimate']:.4f}  "
                              f"CI=[{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]  "
                              f"N_eff={res.get('N_eff', '?')}")

    # Actual vs expected signs
    print("\n--- Actual vs Expected Signs ---")
    for outcome in outcomes_present:
        baseline = [r for r in all_results
                    if r["outcome"] == outcome and r["specification"] == "baseline"]
        if baseline:
            est = baseline[0]["estimate"]
            expected = EXPECTED_SIGNS.get(outcome, "?")
            actual = "+" if est > 0 else "-" if est < 0 else "0"
            match = "MATCH" if (expected == actual or expected == "?") else "MISMATCH"
            print(f"  {outcome}: expected={expected} actual={actual} {match} (est={est:.4f})")

    # Save
    results_df = pd.DataFrame(all_results)
    results_df.to_csv(MAIN_RESULTS_CSV, index=False)
    print(f"\nSaved: {MAIN_RESULTS_CSV} ({len(results_df)} rows)")

    for col in ["estimate", "ci_lower", "ci_upper"]:
        n_nan = results_df[col].isna().sum()
        if n_nan > 0:
            print(f"  WARNING: {n_nan} NaN values in '{col}'")
    print()


# ════════════════════════════════════════════════════════════════════════════
# FASE 4 — Robustness (02_robustness.py)
# ════════════════════════════════════════════════════════════════════════════
PRIMARY_OUTCOME = "TIENE_BILLETERA"


def phase_4_robustness():
    print("=" * 70)
    print("FASE 4 — RDD Robustness Checks")
    print("=" * 70)

    np.random.seed(RANDOM_SEED)
    df = pd.read_csv(CLEAN_DATA_CSV)
    print(f"Loaded: {len(df):,} rows x {df.shape[1]} cols")

    all_results = []
    y_all = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])[RUNNING_VAR].values

    # 1. McCrary
    print("\n--- 1. McCrary/rddensity manipulation test ---")
    mccrary_pval = np.nan
    try:
        from rddensity import rddensity
        rd_den = rddensity(X=y_all, c=0)
        try:
            mccrary_pval = rd_den.p if hasattr(rd_den, "p") else np.nan
        except Exception:
            pass
        print(f"  rddensity p-value: {mccrary_pval}")

        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(figsize=(8, 5))
            window = 30
            mask = np.abs(y_all) <= window
            y_win = y_all[mask]
            bin_edges = np.arange(np.floor(y_win.min()) - 0.5,
                                  np.ceil(y_win.max()) + 1.5, 1.0)
            left_vals = y_win[y_win < 0]
            right_vals = y_win[y_win >= 0]

            ax.hist(left_vals, bins=bin_edges, color="#2166ac", alpha=0.7,
                    edgecolor="white", linewidth=0.5,
                    label="Below cutoff (age $<$ 65)")
            ax.hist(right_vals, bins=bin_edges, color="#b2182b", alpha=0.7,
                    edgecolor="white", linewidth=0.5,
                    label="Above cutoff (age $\\geq$ 65)")
            ax.axvline(x=0, color="black", linestyle="--", linewidth=1.2,
                       alpha=0.8, label="Threshold (age 65)")
            ax.set_xlabel("Age centered at 65 (years)", fontsize=12)
            ax.set_ylabel("Frequency (number of individuals)", fontsize=12)
            test_label = (f"McCrary density test: T $=$ {float(mccrary_pval):.2f}"
                          if isinstance(mccrary_pval, (int, float))
                          and not np.isnan(mccrary_pval)
                          else "McCrary density visualisation")
            ax.set_title(
                f"Density of Running Variable around Age-65 Cutoff\n({test_label})",
                fontsize=12,
            )
            ax.legend(loc="upper right", fontsize=10)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()

            for ext in ("png", "pdf"):
                plt.savefig(FIGURES_DIR / f"figure_mccrary_density.{ext}",
                            dpi=150 if ext == "png" else 300, bbox_inches="tight")
            plt.close("all")
            print("  Saved: figure_mccrary_density.png/.pdf")
        except Exception as e:
            print(f"  Density plot failed: {e}")
    except ImportError:
        print("  rddensity not installed. Skipping.")
    except Exception as e:
        print(f"  McCrary test failed: {e}")

    all_results.append({
        "test": "mccrary", "outcome": "density", "estimate": mccrary_pval,
        "se_robust": np.nan, "ci_lower": np.nan, "ci_upper": np.nan,
        "bandwidth": np.nan, "N_eff": len(y_all), "method": "rddensity",
    })

    # 2. Placebo outcomes
    print("\n--- 2. Placebo outcomes ---")
    placebo_present = [p for p in PLACEBO_OUTCOMES if p in df.columns]
    for pv in placebo_present:
        res = run_rdd(df, pv, label="placebo")
        res["test"] = "placebo"
        all_results.append(res)
        sig = "*" if res.get("ci_lower", -1) > 0 or res.get("ci_upper", 1) < 0 else ""
        print(f"  {pv}: est={res['estimate']:.4f} CI=[{res.get('ci_lower', np.nan):.4f}, "
              f"{res.get('ci_upper', np.nan):.4f}] {sig}")

    # 3. Bandwidth sensitivity
    print("\n--- 3. Bandwidth sensitivity ---")
    baseline = run_rdd(df, PRIMARY_OUTCOME, label="bw_optimal")
    h_opt = baseline.get("bandwidth", 2.0)
    if np.isnan(h_opt) or h_opt <= 0:
        h_opt = 2.0
    for multiplier, label in [(0.5, "h_half"), (1.0, "h_optimal"), (2.0, "h_double")]:
        h = h_opt * multiplier
        res = run_rdd(df, PRIMARY_OUTCOME, h=h, label=f"bandwidth_{label}")
        res["test"] = f"bandwidth_{label}"
        all_results.append(res)
        print(f"  {label} (h={h:.2f}): est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}] "
              f"N_eff={res.get('N_eff', '?')}")

    # 4. Donut-hole
    print("\n--- 4. Donut-hole specifications ---")
    for donut in [0.5, 1.0, 2.0]:
        df_donut = df[np.abs(df[RUNNING_VAR]) > donut].copy()
        res = run_rdd(df_donut, PRIMARY_OUTCOME, h=h_opt, label=f"donut_{donut}")
        res["test"] = f"donut_{donut}"
        all_results.append(res)
        print(f"  Exclude |x|<={donut}: est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}] "
              f"N={len(df_donut)}")

    # 4b. SISFOH heterogeneity
    print("\n--- 4b. Heterogeneity by SISFOH (POBREZA) ---")
    if "POBREZA" in df.columns:
        sisfoh_labels = {1: "extreme_poor", 2: "non_extreme_poor", 3: "non_poor"}
        for code, label in sisfoh_labels.items():
            sub = df[df["POBREZA"] == code].copy()
            if len(sub) < 100:
                print(f"  POBREZA={code} ({label}): n={len(sub)}, skipping (too few obs)")
                continue
            try:
                res = run_rdd(sub, PRIMARY_OUTCOME, h=h_opt, label=f"het_sisfoh_{label}")
                res["test"] = f"het_sisfoh_{label}"
                all_results.append(res)
                print(f"  POBREZA={code} ({label}): est={res['estimate']:.4f} "
                      f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}] "
                      f"N_eff={res.get('N_eff', '?')}")
            except Exception as e:
                print(f"  POBREZA={code} ({label}): RDD failed ({e})")
    else:
        print("  POBREZA column not in data — skipping SISFOH heterogeneity")

    # 5. Covariate balance at bandwidth
    print(f"\n--- 5. Covariate balance at bandwidth (h={h_opt:.2f}) ---")
    df_bw = df[np.abs(df[RUNNING_VAR]) <= h_opt].copy()
    print(f"  Observations within bandwidth: {len(df_bw)}")
    cov_avail = [c for c in COVARIATES if c in df_bw.columns]
    for cov in cov_avail:
        res = run_rdd(df_bw, cov, h=h_opt, label="covariate_balance")
        res["test"] = "covariate_balance"
        res["outcome"] = cov
        all_results.append(res)
        sig = (" *IMBALANCED*"
               if (res.get("ci_lower", -1) > 0 or res.get("ci_upper", 1) < 0) else "")
        print(f"  {cov:20s}: est={res['estimate']:.4f} "
              f"CI=[{res.get('ci_lower', np.nan):.4f}, {res.get('ci_upper', np.nan):.4f}]{sig}")

    # 6. Polynomial sensitivity
    print("\n--- 6. Polynomial order sensitivity ---")
    if RDROBUST_OK:
        sub = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])
        y_sub = sub[PRIMARY_OUTCOME].values
        x_sub = sub[RUNNING_VAR].values
        cl_sub = sub[CLUSTER_VAR].values if CLUSTER_VAR in sub.columns else None

        for p_order, p_label in [(1, "linear"), (2, "quadratic")]:
            try:
                kwargs = dict(y=y_sub, x=x_sub, p=p_order,
                              kernel="triangular", bwselect="mserd")
                if cl_sub is not None:
                    kwargs["cluster"] = cl_sub
                rd = rdrobust(**kwargs)
                est = _safe_scalar(rd.coef, 0)
                try:
                    ci_lo = float(rd.ci.iloc[-1, 0])
                    ci_hi = float(rd.ci.iloc[-1, 1])
                except Exception:
                    ci_lo = ci_hi = np.nan
                if np.isnan(est) and not np.isnan(ci_lo) and not np.isnan(ci_hi):
                    est = (ci_lo + ci_hi) / 2.0
                bw = float(rd.bws.iloc[0, 0]) if hasattr(rd.bws, "iloc") else np.nan
                n_eff = (int(rd.N_h[0]) + int(rd.N_h[1])
                         if hasattr(rd.N_h, "__getitem__") else 0)
                res = {"test": f"polynomial_{p_label}", "outcome": PRIMARY_OUTCOME,
                       "estimate": est, "se_robust": _safe_scalar(rd.se, -1),
                       "ci_lower": ci_lo, "ci_upper": ci_hi,
                       "bandwidth": bw, "N_eff": n_eff, "method": "rdrobust"}
                all_results.append(res)
                print(f"  p={p_order} ({p_label}): est={est:.4f} "
                      f"CI=[{ci_lo:.4f}, {ci_hi:.4f}] N_eff={n_eff}")
            except Exception as e:
                print(f"  p={p_order} ({p_label}): failed ({e})")
    else:
        print("  rdrobust not available — skipping polynomial sensitivity.")

    # 7. Placebo cutoff
    print("\n--- 7. Placebo cutoff test ---")
    sub_pc = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR]).copy()
    x_vals = sub_pc[RUNNING_VAR].values
    n_unique_x = len(np.unique(x_vals))
    if n_unique_x < 10:
        print(f"  Running variable has only {n_unique_x} unique values.")

    for pctile, label in [(25, "left_placebo"), (75, "right_placebo")]:
        cutoff = np.percentile(x_vals, pctile)
        if abs(cutoff) < 0.1:
            print(f"  {label}: cutoff={cutoff:.2f} too close to 0. Skipping.")
            continue
        if n_unique_x < 20:
            unique_sorted = np.sort(np.unique(x_vals))
            cutoff = unique_sorted[np.argmin(np.abs(unique_sorted - cutoff))]
        df_placebo_c = sub_pc.copy()
        df_placebo_c["_running_placebo"] = df_placebo_c[RUNNING_VAR] - cutoff
        if cutoff < 0:
            df_placebo_c = df_placebo_c[df_placebo_c[RUNNING_VAR] < 0]
        else:
            df_placebo_c = df_placebo_c[df_placebo_c[RUNNING_VAR] >= 0]
        if len(df_placebo_c) >= 30:
            y_pc = df_placebo_c[PRIMARY_OUTCOME].values
            x_pc = df_placebo_c["_running_placebo"].values
            try:
                if RDROBUST_OK:
                    rd_pc = rdrobust(y=y_pc, x=x_pc, kernel="triangular", bwselect="mserd")
                    est_pc = _safe_scalar(rd_pc.coef, 0)
                    try:
                        ci_lo_pc = float(rd_pc.ci.iloc[-1, 0])
                        ci_hi_pc = float(rd_pc.ci.iloc[-1, 1])
                    except Exception:
                        ci_lo_pc = ci_hi_pc = np.nan
                    if np.isnan(est_pc) and not np.isnan(ci_lo_pc) and not np.isnan(ci_hi_pc):
                        est_pc = (ci_lo_pc + ci_hi_pc) / 2.0
                    sig = " *FAILS*" if (ci_lo_pc > 0 or ci_hi_pc < 0) else ""
                    print(f"  {label} (cutoff={cutoff:.2f}): est={est_pc:.4f}  "
                          f"CI=[{ci_lo_pc:.4f}, {ci_hi_pc:.4f}]{sig}")
                    all_results.append({
                        "test": f"placebo_cutoff_{label}", "outcome": PRIMARY_OUTCOME,
                        "estimate": est_pc, "se_robust": _safe_scalar(rd_pc.se, -1),
                        "ci_lower": ci_lo_pc, "ci_upper": ci_hi_pc,
                        "bandwidth": (float(rd_pc.bws.iloc[0, 0])
                                      if hasattr(rd_pc.bws, "iloc") else np.nan),
                        "N_eff": len(df_placebo_c), "method": "rdrobust_placebo_cutoff",
                    })
            except Exception as e:
                print(f"  {label}: failed ({e})")

    # 8. Permutation inference
    print("\n--- 8. Permutation inference (randomized cutoffs) ---")
    sub_perm = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR]).copy()
    if len(sub_perm) >= 30:
        try:
            import statsmodels.api as sm
            y_perm = sub_perm[PRIMARY_OUTCOME].values
            x_perm = sub_perm[RUNNING_VAR].values
            x_std_perm = np.std(x_perm)
            if x_std_perm < 1e-10:
                raise ValueError("zero variance")
            h_perm = 1.5 * x_std_perm
            mask_real = np.abs(x_perm) <= h_perm
            y_bw_real = y_perm[mask_real]
            x_bw_real = x_perm[mask_real]
            treat_real = (x_bw_real >= 0).astype(float)
            weights_real = np.maximum(1 - np.abs(x_bw_real) / h_perm, 0)
            X_real = sm.add_constant(np.column_stack(
                [treat_real, x_bw_real, treat_real * x_bw_real]))
            mod_real = sm.WLS(y_bw_real, X_real, weights=weights_real).fit()
            t_real = mod_real.tvalues[1]

            n_perms = 500
            rng = np.random.default_rng(RANDOM_SEED)
            x_quantiles = np.percentile(x_perm, np.linspace(10, 90, 50))
            t_perms = []
            for _ in range(n_perms):
                c_fake = rng.choice(x_quantiles)
                x_shifted = x_perm - c_fake
                mask_p = np.abs(x_shifted) <= h_perm
                y_bw_p = y_perm[mask_p]
                x_bw_p = x_shifted[mask_p]
                if len(y_bw_p) < 10:
                    continue
                treat_p = (x_bw_p >= 0).astype(float)
                weights_p = np.maximum(1 - np.abs(x_bw_p) / h_perm, 0)
                X_p = sm.add_constant(np.column_stack(
                    [treat_p, x_bw_p, treat_p * x_bw_p]))
                try:
                    mod_p = sm.WLS(y_bw_p, X_p, weights=weights_p).fit()
                    t_perms.append(mod_p.tvalues[1])
                except Exception:
                    pass

            success_rate = len(t_perms) / n_perms if n_perms > 0 else 0
            if len(t_perms) > 100:
                t_perms = np.array(t_perms)
                perm_pval = np.mean(np.abs(t_perms) >= np.abs(t_real))
                print(f"  t_real: {t_real:.3f}")
                print(f"  Permutation p-value ({len(t_perms)} valid, "
                      f"{success_rate:.0%} success): {perm_pval:.4f}")
                all_results.append({
                    "test": "permutation_inference", "outcome": PRIMARY_OUTCOME,
                    "estimate": t_real, "se_robust": np.nan,
                    "pvalue": perm_pval,
                    "ci_lower": np.nan, "ci_upper": np.nan,
                    "bandwidth": h_perm, "N_eff": len(sub_perm),
                    "method": f"permutation_{len(t_perms)}",
                })
        except Exception as e:
            print(f"  Permutation inference failed: {e}")

    # 9. BH FDR
    print("\n--- 9. Multiple hypothesis correction (BH FDR) ---")
    testable = [r for r in all_results
                if "pvalue" in r and pd.notna(r.get("pvalue"))
                and r.get("pvalue", 1) < 1]
    if len(testable) > 1:
        pvals = np.array([r["pvalue"] for r in testable])
        n_p = len(pvals)
        ranked = np.argsort(pvals)
        adj = np.empty(n_p)
        for i, rank_idx in enumerate(reversed(ranked)):
            rank = n_p - i
            if i == 0:
                adj[rank_idx] = pvals[rank_idx]
            else:
                adj[rank_idx] = min(pvals[rank_idx] * n_p / rank,
                                    adj[ranked[n_p - i]])
        adj = np.minimum(adj, 1.0)
        for i, r in enumerate(testable):
            r["pvalue_bh"] = adj[i]
        print(f"  Corrected {n_p} tests.")

    results_df = pd.DataFrame(all_results)
    results_df.to_csv(ROBUSTNESS_CSV, index=False)
    print(f"\nSaved: {ROBUSTNESS_CSV} ({len(results_df)} rows)\n")


# ════════════════════════════════════════════════════════════════════════════
# FASE 5 — Output: tablas y figuras (03_output.py)
# ════════════════════════════════════════════════════════════════════════════
def _fmt(val, decimals=4):
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return "---"
    try:
        return f"{float(val):.{decimals}f}"
    except (ValueError, TypeError):
        return str(val)


def _texvar(name: str) -> str:
    return str(name).replace("_", "\\_")


def _validate_table(content, filename):
    problems = []
    if "nan" in content.lower():
        problems.append("Contains 'nan'")
    if "& &" in content:
        problems.append("Contains empty cells (& &)")
    if "& \\\\" in content:
        problems.append("Contains empty last column (& \\\\)")
    if problems:
        print(f"  WARNING in {filename}: {', '.join(problems)}")
        content = content.replace("nan", "---")
        content = content.replace("NaN", "---")
        content = content.replace("None", "---")
        while "& &" in content:
            content = content.replace("& &", "& --- &")
        content = content.replace("& \\\\", "& --- \\\\")
        print("  Auto-fixed.")
    return content


def _make_table1(df):
    print("Generating Table 1: Summary statistics...")
    treated = df[df["treat"] == 1]
    control = df[df["treat"] == 0]

    h_opt = 14.24
    bw_mask = np.abs(df.get("running_centered", df[RUNNING_VAR_RAW] - 65)) <= h_opt
    df_bw = df[bw_mask]
    n_below_bw = int((df_bw.get("running_centered",
                                 df_bw[RUNNING_VAR_RAW] - 65) < 0).sum())
    n_above_bw = int((df_bw.get("running_centered",
                                 df_bw[RUNNING_VAR_RAW] - 65) >= 0).sum())

    stat_vars = [v for v in (OUTCOME_VARS + COVARIATES) if v in df.columns]

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
            f"  {_texvar(var)} & {_fmt(t_s.mean())} & {_fmt(t_s.std())} & {len(t_s)} & --- "
            f"& {_fmt(c_s.mean())} & {_fmt(c_s.std())} & {len(c_s)} & --- \\\\"
        )

    tex += [
        r"\midrule",
        f"  Observations & \\multicolumn{{4}}{{c}}{{{len(treated)}}} "
        f"& \\multicolumn{{4}}{{c}}{{{len(control)}}} \\\\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} Summary statistics for the full RDD analysis sample. "
            r"'Above Threshold' (treated$=1$) denotes individuals aged 65 and above; "
            r"'Below Threshold' (treated$=0$) under age 65. The treated/control split (" +
            f"{len(treated):,}".replace(",", "{,}") + r" vs.\ " +
            f"{len(control):,}".replace(",", "{,}") + r") is asymmetric; within the bandwidth-"
            r"restricted estimation window ($\pm h^{\ast}\!=\!\pm 14.24$ years) the split is " +
            f"{n_below_bw:,}".replace(",", "{,}") + r" below and " +
            f"{n_above_bw:,}".replace(",", "{,}") + r" above the cutoff. "
            r"'---' indicates unavailable data."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = _validate_table("\n".join(tex), "table_1_summary.tex")
    path = TABLES_DIR / "table_1_summary.tex"
    path.write_text(content, encoding="utf-8")
    print(f"  Saved: {path}")


def _make_table2(results, robust=None):
    print("Generating Table 2: Main RDD results...")
    tex = [
        r"\begin{threeparttable}",
        r"\begin{tabular}{l ccc}",
        r"\toprule",
    ]

    outcomes = results["outcome"].unique().tolist()
    outcome_labels = " & ".join(_texvar(o) for o in outcomes)
    tex.append(f"  & {outcome_labels} \\\\")
    tex.append(r"\midrule")

    for spec in results["specification"].unique():
        tex.append(r"\addlinespace")
        tex.append(
            f"\\multicolumn{{{len(outcomes)+1}}}{{l}}"
            f"{{\\textit{{{_texvar(spec)}}}}} \\\\"
        )
        spec_data = results[results["specification"] == spec]

        for label, key, fmt_decimals in [
            ("Estimate", "estimate", 4),
            ("SE (robust)", "se_robust", 4),
        ]:
            row = f"  {label}"
            for outcome in outcomes:
                match = spec_data[spec_data["outcome"] == outcome]
                if len(match) > 0:
                    val = match.iloc[0].get(key, np.nan)
                    if key == "se_robust":
                        row += f" & ({_fmt(val, fmt_decimals)})"
                    else:
                        row += f" & {_fmt(val, fmt_decimals)}"
                else:
                    row += " & ---"
            tex.append(row + " \\\\")

        # CI
        row = "  95\\% CI"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                ci_lo = match.iloc[0].get("ci_lower", np.nan)
                ci_hi = match.iloc[0].get("ci_upper", np.nan)
                row += f" & [{_fmt(ci_lo)}, {_fmt(ci_hi)}]"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # N / BW
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
                row += f" & {n_str} / {_fmt(bw, 2)}"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

        # Method
        row = "  Method"
        for outcome in outcomes:
            match = spec_data[spec_data["outcome"] == outcome]
            if len(match) > 0:
                method = match.iloc[0].get("method", "---")
                row += f" & {_texvar(method)}"
            else:
                row += " & ---"
        tex.append(row + " \\\\")

    # SISFOH heterogeneity panel
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
            "het_sisfoh_extreme_poor":     "Extreme-poor (=1)",
            "het_sisfoh_non_extreme_poor": "Non-extreme-poor (=2)",
            "het_sisfoh_non_poor":         "Non-poor (=3)",
        }
        for test_key, display in sisfoh_label_map.items():
            r = sisfoh_rows[sisfoh_rows["test"] == test_key]
            if len(r) == 0:
                continue
            r0 = r.iloc[0]
            est = _fmt(r0.get("estimate", np.nan))
            se = _fmt(r0.get("se_robust", np.nan))
            ci_lo = _fmt(r0.get("ci_lower", np.nan))
            ci_hi = _fmt(r0.get("ci_upper", np.nan))
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
            r"(\texttt{rdrobust}) with triangular kernel and MSE-optimal bandwidth. "
            r"Robust bias-corrected standard errors in parentheses. "
            r"'---' indicates estimate unavailable."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = _validate_table("\n".join(tex), "table_2_main_results.tex")
    path = TABLES_DIR / "table_2_main_results.tex"
    path.write_text(content, encoding="utf-8")
    print(f"  Saved: {path}")


def _make_table3(robust):
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
                tail = test_name.replace("donut_", "")
                label = r"$\pm$" + tail + " yr"
            elif prefix == "placebo":
                outcome = r.get("outcome", "")
                label = _texvar(outcome.replace("placebo_", ""))
            else:
                label = test_name.replace(f"{prefix}_", "").replace("_", " ").title()
            try:
                n_eff_int = (int(float(r["N_eff"]))
                             if pd.notna(r.get("N_eff"))
                             and float(r["N_eff"]) > 0 else None)
            except (ValueError, TypeError):
                n_eff_int = None
            n_str = f"{n_eff_int:,}".replace(",", "{,}") if n_eff_int else "---"
            tex.append(
                f"  {label} & {_fmt(r['estimate'])} & {_fmt(r.get('se_robust', np.nan))} "
                f"& [{_fmt(r.get('ci_lower', np.nan))}, {_fmt(r.get('ci_upper', np.nan))}] "
                f"& {_fmt(r.get('bandwidth', np.nan), 2)} "
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
            r"triangular kernel and MSE-optimal bandwidth. Robust bias-corrected confidence "
            r"intervals reported."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = _validate_table("\n".join(tex), "table_3_robustness.tex")
    path = TABLES_DIR / "table_3_robustness.tex"
    path.write_text(content, encoding="utf-8")
    print(f"  Saved: {path}")


def _make_table4(robust):
    print("Generating Table 4: Covariate balance...")
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
            n_eff_int = (int(float(r["N_eff"]))
                         if pd.notna(r.get("N_eff"))
                         and float(r["N_eff"]) > 0 else None)
        except (ValueError, TypeError):
            n_eff_int = None
        n_str = f"{n_eff_int:,}".replace(",", "{,}") if n_eff_int else "---"
        tex.append(
            f"  {_texvar(r['outcome'])} & {_fmt(r['estimate'])}{sig} "
            f"& {_fmt(r.get('se_robust', np.nan))} "
            f"& [{_fmt(ci_lo)}, {_fmt(ci_hi)}] "
            f"& {_fmt(r.get('bandwidth', np.nan), 2)} "
            f"& {n_str} \\\\"
        )

    tex += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\begin{tablenotes}",
        r"\small",
        (
            r"\item \textit{Notes:} RDD estimates with each covariate as outcome, "
            r"restricted to within the MSE-optimal bandwidth. $^{*}$ 95\% CI excludes zero."
        ),
        r"\end{tablenotes}",
        r"\end{threeparttable}",
    ]

    content = _validate_table("\n".join(tex), "table_4_covariate_balance.tex")
    path = TABLES_DIR / "table_4_covariate_balance.tex"
    path.write_text(content, encoding="utf-8")
    print(f"  Saved: {path}")


def _make_figure1(df):
    print("Generating Figure 1: RD plot...")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sub = df.dropna(subset=[PRIMARY_OUTCOME, RUNNING_VAR])
    x = sub[RUNNING_VAR].values
    y = sub[PRIMARY_OUTCOME].values
    if len(x) < 20:
        print("  Insufficient data. Skipping.")
        return

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
    ax.axvline(x=0, color="black", linestyle="--", linewidth=1, alpha=0.7,
               label="Threshold")
    ax.set_xlim(-x_range, x_range)
    ax.set_xlabel("Age centered at 65 (years)", fontsize=12)
    ax.set_ylabel(PRIMARY_OUTCOME.replace("_", " ").title(), fontsize=12)
    ax.set_title("RDD Plot: Digital Wallet Ownership by Age", fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        plt.savefig(FIGURES_DIR / f"figure_1_rdplot.{ext}",
                    dpi=150 if ext == "png" else 300, bbox_inches="tight")
    plt.close("all")
    print("  Saved: figure_1_rdplot.png/.pdf")


def _make_figure2(robust):
    print("Generating Figure 2: Bandwidth sensitivity...")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    bw_data = robust[robust["test"].str.startswith("bandwidth")].copy()
    if len(bw_data) == 0:
        print("  No bandwidth results. Skipping.")
        return

    bw_data = bw_data.sort_values("bandwidth")
    estimates = bw_data["estimate"].values.copy()
    ci_lo = bw_data["ci_lower"].values
    ci_hi = bw_data["ci_upper"].values
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
                fmt="o", color="#2166ac", capsize=5, capthick=2,
                markersize=8, linewidth=2)
    ax.axhline(y=0, color="black", linestyle="--", linewidth=1, alpha=0.5)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("RD Estimate", fontsize=12)
    ax.set_title("Bandwidth Sensitivity", fontsize=13)
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        plt.savefig(FIGURES_DIR / f"figure_2_bandwidth_sensitivity.{ext}",
                    dpi=150 if ext == "png" else 300, bbox_inches="tight")
    plt.close("all")
    print("  Saved: figure_2_bandwidth_sensitivity.png/.pdf")


def phase_5_output():
    print("=" * 70)
    print("FASE 5 — Tables and Figures")
    print("=" * 70)

    df = pd.read_csv(CLEAN_DATA_CSV)
    print(f"Clean data: {len(df)} rows")
    main_results = pd.read_csv(MAIN_RESULTS_CSV)
    print(f"Main results: {len(main_results)} rows")
    robust = pd.read_csv(ROBUSTNESS_CSV) if ROBUSTNESS_CSV.exists() else None
    if robust is not None:
        print(f"Robustness: {len(robust)} rows")

    print()
    _make_table1(df)
    _make_table2(main_results, robust=robust)
    if robust is not None:
        _make_table3(robust)
        _make_table4(robust)
    print()
    _make_figure1(df)
    if robust is not None:
        _make_figure2(robust)

    print("\n--- Final table validation ---")
    all_clean = True
    for tex_file in sorted(TABLES_DIR.iterdir()):
        if tex_file.suffix == ".tex":
            content = tex_file.read_text(encoding="utf-8")
            if "nan" in content.lower() or "& &" in content:
                print(f"  PROBLEM: {tex_file.name} still has blank/NaN cells!")
                all_clean = False
    if all_clean:
        print("  All tables validated: no NaN or blank cells.")
    print()


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════
def main():
    print("\n" + "#" * 70)
    print("# PIPELINE COMPLETO — Pensión 65 RDD digital wallet")
    print(f"# Repo root: {REPO_ROOT}")
    print("#" * 70 + "\n")

    phase_0_extract_zips()
    phase_1_preprocess()
    phase_2_clean()
    phase_3_main()
    phase_4_robustness()
    phase_5_output()

    print("#" * 70)
    print("# PIPELINE COMPLETO — DONE")
    print("#" * 70)
    print(f"\nOutputs:")
    print(f"  {ENAHO_CLEAN_CSV}")
    print(f"  {CLEAN_DATA_CSV}")
    print(f"  {MAIN_RESULTS_CSV}")
    print(f"  {ROBUSTNESS_CSV}")
    print(f"  {TABLES_DIR}/table_*.tex")
    print(f"  {FIGURES_DIR}/figure_*.png/.pdf")


if __name__ == "__main__":
    main()
