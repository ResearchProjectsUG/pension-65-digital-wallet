"""
Pre-procesamiento ENAHO 2024 para análisis de adopción de billetera digital.

Mergea 6 módulos de ENAHO 2024 a nivel de persona y construye las variables
del paper sobre determinantes de adopción de billetera digital en Perú.

INPUT:
    C:/Users/jesus/Documents/Enaho_data/
        Enaho01-2024-100.csv    (Módulo 1: Vivienda)
        Enaho01-2024-200.csv    (Módulo 2: Miembros del hogar)
        Enaho01A-2024-300.csv   (Módulo 3: Educación)
        Enaho01a-2024-500.csv   (Módulo 5: Empleo + Billetera)
        Enaho01-2024-612.csv    (Módulo 18: Equipamiento del hogar)
        Sumaria-2024.csv        (Sumaria: Variables calculadas)

OUTPUT:
    C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv

VARIABLES CONSTRUIDAS:
    tiene_billetera   — tenencia (P558E1_10 == 10)  [HIPÓTESIS — verificar codebook]
    usa_billetera     — uso como medio de pago (cualquier P558HX_7 == 7) [HIPÓTESIS]
    edad, genero, nivel_educativo, ingreso_pc, smartphone, internet_hogar,
    formal, banco_previo, dpto, ubigeo, factor07
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────
INPUT_DIR = Path("C:/Users/jesus/Documents/Enaho_data")
OUTPUT_PATH = Path("C:/Users/jesus/Desktop/papers-HQ- AI/data/enaho_2024_clean.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

FILES = {
    "m01": INPUT_DIR / "Enaho01-2024-100.csv",
    "m02": INPUT_DIR / "Enaho01-2024-200.csv",
    "m03": INPUT_DIR / "Enaho01A-2024-300.csv",
    "m05": INPUT_DIR / "Enaho01a-2024-500.csv",
    "m18": INPUT_DIR / "Enaho01-2024-612.csv",
    "sum": INPUT_DIR / "Sumaria-2024.csv",
}

# Billetera digital codes (validated via correlation with smartphone + banco previo)
# - E1_9: 10.15% prevalencia, +6.9pp smartphone, +31.9pp banco previo
#   (matches BCRP active digital wallet ownership ~10%)
# - H_X_7: any of P558H1_7..P558H12_7, 15.57% prevalencia, +7.1pp smartphone,
#   +70.1pp banco previo (people who use billetera ALL have banco)
BILLETERA_E1_CODE = 9   # tenencia
BILLETERA_H_CODE = 7    # uso como medio de pago

KEYS_PERSON = ["CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO"]
KEYS_HOUSEHOLD = ["CONGLOME", "VIVIENDA", "HOGAR"]


def load(label: str, path: Path) -> pd.DataFrame:
    print(f"  [load] {label}: {path.name}")
    df = pd.read_csv(path, encoding="latin-1", low_memory=False)
    df.columns = [c.upper() for c in df.columns]
    print(f"         shape: {df.shape}")
    return df


def detect_billetera_tenencia(m05: pd.DataFrame) -> pd.Series:
    """tiene_billetera = 1 if person selected option BILLETERA_E1_CODE in P558E1.

    The variable is multi-response: P558E1_X == X if option X selected, '0' if
    not, ' ' if not applicable.
    """
    col = f"P558E1_{BILLETERA_E1_CODE}"
    if col not in m05.columns:
        print(f"  [warn] {col} not found — tiene_billetera will be all 0")
        return pd.Series(0, index=m05.index)
    return (m05[col].astype(str).str.strip() == str(BILLETERA_E1_CODE)).astype(int)


def detect_billetera_uso(m05: pd.DataFrame) -> pd.Series:
    """usa_billetera = 1 if person selected option BILLETERA_H_CODE in ANY of
    the 12 P558H groups (one per spending category).
    """
    use = pd.Series(0, index=m05.index)
    for g in range(1, 13):
        col = f"P558H{g}_{BILLETERA_H_CODE}"
        if col in m05.columns:
            sel = (m05[col].astype(str).str.strip() == str(BILLETERA_H_CODE)).astype(int)
            use = use | sel
    return use


def main():
    print("=" * 70)
    print("ENAHO 2024 — Merge a nivel persona")
    print("=" * 70)

    # ── 1. Load all modules ────────────────────────────────────────────
    print("\n[1] Loading modules...")
    m01 = load("m01-Vivienda", FILES["m01"])
    m02 = load("m02-Miembros", FILES["m02"])
    m03 = load("m03-Educacion", FILES["m03"])
    m05 = load("m05-Empleo+Billetera", FILES["m05"])
    m18 = load("m18-Equipamiento", FILES["m18"])
    sumaria = load("sumaria", FILES["sum"])

    # ── 2. Build derived variables in m05 (the heart) ──────────────────
    print("\n[2] Building billetera variables from m05...")
    m05["TIENE_BILLETERA"] = detect_billetera_tenencia(m05)
    m05["USA_BILLETERA"] = detect_billetera_uso(m05)

    # Alternative interpretations kept for codebook verification by professor
    m05["TIENE_BILLETERA_ALT_E10"] = (
        m05["P558E1_10"].astype(str).str.strip() == "10"
    ).astype(int) if "P558E1_10" in m05.columns else 0
    m05["TIENE_BILLETERA_ALT_E6"] = (
        m05["P558E1_6"].astype(str).str.strip() == "6"
    ).astype(int) if "P558E1_6" in m05.columns else 0

    # Use any H_6 (alternative — matches "transferencia"?)
    use_h6 = pd.Series(0, index=m05.index)
    for g in range(1, 13):
        col = f"P558H{g}_6"
        if col in m05.columns:
            use_h6 = use_h6 | (m05[col].astype(str).str.strip() == "6").astype(int)
    m05["USA_BILLETERA_ALT_H6"] = use_h6

    print(f"  tiene_billetera (E1_{BILLETERA_E1_CODE}): {m05['TIENE_BILLETERA'].mean()*100:.1f}%")
    print(f"  usa_billetera (any H_{BILLETERA_H_CODE}): {m05['USA_BILLETERA'].mean()*100:.1f}%")
    print(f"  ALT tiene (E1_10): {m05['TIENE_BILLETERA_ALT_E10'].mean()*100:.1f}%")
    print(f"  ALT tiene (E1_6):  {m05['TIENE_BILLETERA_ALT_E6'].mean()*100:.1f}%")
    print(f"  ALT usa (any H_6): {m05['USA_BILLETERA_ALT_H6'].mean()*100:.1f}%")

    # ── 3. Build other m05 variables ───────────────────────────────────
    # Cuenta bancaria previa: P558E1_1 (cuenta de ahorros) OR P558E1_8 (debito)
    m05["BANCO_PREVIO"] = (
        ((m05["P558E1_1"].astype(str).str.strip() == "1").astype(int)) |
        ((m05["P558E1_8"].astype(str).str.strip() == "8").astype(int))
        if "P558E1_1" in m05.columns and "P558E1_8" in m05.columns
        else pd.Series(0, index=m05.index)
    ).astype(int)

    # Formalidad: P514 == 1 (afiliado a sistema de pensión).
    # NOTE: P513T son horas trabajadas, no formalidad — usar P514.
    if "P514" in m05.columns:
        m05["FORMAL"] = (
            pd.to_numeric(m05["P514"], errors="coerce") == 1
        ).astype(int)
    else:
        m05["FORMAL"] = 0

    # Ocupado (proxy de trabajar): OCU500 == 1
    if "OCU500" in m05.columns:
        m05["OCUPADO"] = (
            pd.to_numeric(m05["OCU500"], errors="coerce") == 1
        ).astype(int)
    else:
        m05["OCUPADO"] = 0

    # Person-level subset of m05
    m05_keep = [c for c in (KEYS_PERSON + [
        "TIENE_BILLETERA", "USA_BILLETERA",
        "TIENE_BILLETERA_ALT_E10", "TIENE_BILLETERA_ALT_E6", "USA_BILLETERA_ALT_H6",
        "BANCO_PREVIO", "FORMAL", "OCUPADO"
    ]) if c in m05.columns]
    m05_p = m05[m05_keep].drop_duplicates(subset=KEYS_PERSON, keep="first")
    print(f"  m05 person-level: {m05_p.shape}")

    # ── 4. Module 02: edad, genero, factor de expansion ────────────────
    # FACPOB07 = factor de expansión a nivel PERSONA (no FACTOR07 que es hogar).
    # Esencial para inferencia poblacional representativa.
    print("\n[3] Extracting m02 demographics + FACPOB07...")
    m02_keep = [c for c in (KEYS_PERSON + ["P207", "P208A", "FACPOB07"])
                if c in m02.columns]
    m02_p = m02[m02_keep].copy()
    m02_p = m02_p.rename(columns={
        "P207": "GENERO",
        "P208A": "EDAD",
        "FACPOB07": "FACTOR_EXPANSION",
    })
    if "FACTOR_EXPANSION" in m02_p.columns:
        print(f"  FACTOR_EXPANSION (FACPOB07) present: mean={m02_p['FACTOR_EXPANSION'].mean():.1f}")
    else:
        print(f"  [warn] FACPOB07 not found in m02")

    # ── 5. Module 03: educación ────────────────────────────────────────
    print("\n[4] Extracting m03 education...")
    m03_keep = [c for c in (KEYS_PERSON + ["P301A"]) if c in m03.columns]
    m03_p = m03[m03_keep].copy().rename(columns={"P301A": "NIVEL_EDUCATIVO"})

    # ── 6. Module 18: smartphone (long format pivot) ───────────────────
    # m18 is in LONG format: one row per (household, equipment item).
    # P612N = item code (10 = smartphone/celular based on prevalence 85.5%)
    # P612 = ¿tiene este item? (1=Sí, 2=No, 9=No sabe)
    print("\n[5] Extracting m18 smartphone (long-format pivot)...")
    SMARTPHONE_ITEM_CODE = 10  # P612N==10 (verify with codebook)
    smart_rows = m18[m18["P612N"] == SMARTPHONE_ITEM_CODE].copy()
    smart_rows["SMARTPHONE"] = (
        pd.to_numeric(smart_rows["P612"], errors="coerce") == 1
    ).astype(int)
    m18_h = smart_rows[KEYS_HOUSEHOLD + ["SMARTPHONE"]].drop_duplicates(
        subset=KEYS_HOUSEHOLD, keep="first"
    )
    print(f"  smartphone (P612N={SMARTPHONE_ITEM_CODE}): "
          f"{m18_h['SMARTPHONE'].mean()*100:.1f}% of households")

    # ── 7. Module 01: internet hogar, ubigeo ───────────────────────────
    # P114B2 = internet en hogar (1=Sí, 0=No, blank=N/A)
    # P1141 era OTRA cosa (~3.6% prevalencia, no es internet)
    print("\n[6] Extracting m01 housing/internet...")
    if "P114B2" in m01.columns:
        m01["INTERNET_HOGAR"] = (
            m01["P114B2"].astype(str).str.strip() == "1"
        ).astype(int)
    else:
        m01["INTERNET_HOGAR"] = 0
    print(f"  internet_hogar (P114B2=1): "
          f"{m01['INTERNET_HOGAR'].mean()*100:.1f}% of households")

    m01_keep = [c for c in (KEYS_HOUSEHOLD + ["UBIGEO", "ESTRATO", "DOMINIO",
                                              "INTERNET_HOGAR"])
                if c in m01.columns]
    m01_h = m01[m01_keep].drop_duplicates(subset=KEYS_HOUSEHOLD, keep="first")

    # ── 8. Sumaria: ingreso per cápita ─────────────────────────────────
    print("\n[7] Extracting sumaria income...")
    sum_keep = [c for c in (KEYS_HOUSEHOLD + ["INGHOG2D", "GASHOG2D",
                                              "MIEPERHO", "POBREZA"])
                if c in sumaria.columns]
    sum_h = sumaria[sum_keep].drop_duplicates(subset=KEYS_HOUSEHOLD, keep="first")
    sum_h["INGRESO_PC"] = (
        pd.to_numeric(sum_h["INGHOG2D"], errors="coerce") /
        pd.to_numeric(sum_h["MIEPERHO"], errors="coerce").replace(0, np.nan)
    )

    # ── 9. Merge everything ────────────────────────────────────────────
    print("\n[8] Merging all modules at person level...")

    # Start from m02 (the roster)
    df = m02_p.copy()
    print(f"  Start (m02): {df.shape}")

    # Merge person-level: m03, m05
    df = df.merge(m03_p, on=KEYS_PERSON, how="left")
    print(f"  + m03: {df.shape}")
    df = df.merge(m05_p, on=KEYS_PERSON, how="left")
    print(f"  + m05: {df.shape}")

    # Merge household-level: m01, m18, sumaria
    df = df.merge(m01_h, on=KEYS_HOUSEHOLD, how="left")
    print(f"  + m01: {df.shape}")
    df = df.merge(m18_h, on=KEYS_HOUSEHOLD, how="left")
    print(f"  + m18: {df.shape}")
    df = df.merge(sum_h, on=KEYS_HOUSEHOLD, how="left")
    print(f"  + sumaria: {df.shape}")

    # ── 10. Build dpto from ubigeo ─────────────────────────────────────
    if "UBIGEO" in df.columns:
        df["DPTO"] = df["UBIGEO"].astype(str).str.zfill(6).str[:2]

    # ── 11. Fill missing billetera (people not in m05) with 0 ─────────
    for col in ["TIENE_BILLETERA", "USA_BILLETERA", "BANCO_PREVIO", "FORMAL"]:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    # ── 12. Validation: print summary ──────────────────────────────────
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Final shape: {df.shape}")
    print(f"\nKey variable means:")
    keyvars = ["TIENE_BILLETERA", "USA_BILLETERA",
               "TIENE_BILLETERA_ALT_E10", "TIENE_BILLETERA_ALT_E6",
               "USA_BILLETERA_ALT_H6",
               "SMARTPHONE", "INTERNET_HOGAR", "FORMAL", "OCUPADO", "BANCO_PREVIO"]
    for v in keyvars:
        if v in df.columns:
            print(f"  {v:30s}: {df[v].mean()*100:>6.2f}%")

    print(f"\nNumeric vars (mean):")
    for v in ["EDAD", "INGRESO_PC"]:
        if v in df.columns:
            mean = pd.to_numeric(df[v], errors="coerce").mean()
            print(f"  {v:30s}: {mean:>10.2f}")

    if "DPTO" in df.columns:
        print(f"\nN by departamento (top 10):")
        print(df["DPTO"].value_counts().head(10).to_string())

    # Cross-tab: billetera × smartphone (sanity check)
    if "SMARTPHONE" in df.columns and "TIENE_BILLETERA" in df.columns:
        print(f"\nBilletera × Smartphone cross-tab:")
        ct = pd.crosstab(df["TIENE_BILLETERA"], df["SMARTPHONE"], normalize="index") * 100
        print(ct.round(1).to_string())
        # Expected: people with billetera should have HIGHER smartphone rate
        # If not, billetera code interpretation may be wrong

    # ── 13. Save ───────────────────────────────────────────────────────
    print(f"\n[9] Saving to {OUTPUT_PATH}...")
    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    size_mb = OUTPUT_PATH.stat().st_size / 1024 / 1024
    print(f"  Saved: {OUTPUT_PATH} ({size_mb:.1f} MB)")
    print("\nDone.")


if __name__ == "__main__":
    main()
