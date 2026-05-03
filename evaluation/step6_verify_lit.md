Tengo todo lo que necesito. Acá está el reporte completo de fact-checking.

---

## FACT-CHECKER REPORT — Literatura sobre adopción de billetera digital en Perú

---

### 1. VERIFICACIÓN DE CITAS

#### Cita 1: Bachas et al. 2021 QJE (México)
**ESTADO: REAL, PERO JOURNAL INCORRECTO**

El paper existe y es el correcto para este contexto: *"How Debit Cards Enable the Poor to Save More"* por Pierre Bachas, Paul Gertler, Sean Higgins y Enrique Seira. Los autores son correctos, el año es correcto, el país (México, programa Oportunidades/Prospera) es correcto, y el hallazgo (debit cards → mayor ahorro vía reducción de costos de transacción y monitoreo) es correcto.

**El error**: fue publicado en el **Journal of Finance** (2021), **NO en el QJE**. Esto no es un paper fabricado — es un error de atribución de revista. Para un referee, esto es una señal de que la revisión de literatura fue hecha de memoria o por terceros. El paper del mismo grupo sobre costos de transacción e inclusión financiera sí apareció en *AEA Papers & Proceedings* (2018), lo que puede ser la fuente de la confusión.

> **Corrección**: Bachas, P., Gertler, P., Higgins, S., & Seira, E. (2021). How Debit Cards Enable the Poor to Save More. *Journal of Finance*, 76(4), 1913–1957.

---

#### Cita 2: Muralidharan et al. 2016 AER (India Smartcard)
**ESTADO: CONFIRMADO COMPLETAMENTE**

*"Building State Capacity: Evidence from Biometric Smartcards in India"* por Karthik Muralidharan, Paul Niehaus y Sandip Sukhtankar. Publicado en *American Economic Review* 106(10), 2016, pp. 2895–2929. Autores, revista, año y descripción del hallazgo son todos correctos.

---

### 2. PAPERS CLAVE FALTANTES

La literatura review tiene solo dos citas explícitas. Eso es críticamente escaso. Los siguientes papers son ausencias graves:

| Paper | Por qué falta importa |
|---|---|
| **Lee & Lemieux (2010, JEL)** *"Regression Discontinuity Designs in Economics"* | La referencia canónica de RDD. Cualquier paper que use esta metodología DEBE citarla. Su ausencia en el borrador es una señal de alerta para editores. |
| **Calonico, Cattaneo & Titiunik (2014, Econometrica)** *rdrobust* | El evaluador menciona que el proposal usa CCT bandwidth selection y `rdrobust`, pero si no se cita el paper metodológico de respaldo, el método queda sin ancla bibliográfica. |
| **McCrary (2008, JoE)** *"Manipulation of the running variable in the regression discontinuity design"* | El evaluador menciona el McCrary test como herramienta propuesta. Si se usa, se cita. Sin esta cita, el robustness check queda técnicamente incompleto. |
| **Dupas & Robinson (2013, AEJ:Applied)** *"Savings Constraints and Microenterprise Development"* | Paper seminal en la literatura de inclusión financiera forzada. No citarlo es un hueco en el framing del contribution. |
| **Suri & Jack (2016, Science)** *"The Long-Run Poverty and Gender Impacts of Mobile Money"* | El paper más citado sobre efectos de largo plazo de servicios financieros digitales en pobres rurales. Ausente = revisión incompleta. |
| **IPA/Pensión 65 RDD existente** | Hay trabajo previo de IPA usando RDD en Pensión 65 (efectos en consumo, depresión, bienestar). Si el proposal no lo cita y se diferencia, un referee lo va a señalar inmediatamente como omisión estratégica o ignorancia. |
| **Bachas et al. (2018, AEA P&P)** *"Digital Financial Services Go a Long Way"* | El companion paper del mismo grupo sobre costos de transacción. Más directamente relevante que el de 2021 para el mecanismo propuesto. |

---

### 3. EVALUACIÓN DEL GAP RECLAMADO

**El gap es parcialmente genuino, pero requiere mayor defensa.**

Lo que existe: hay RDD previo sobre Pensión 65 centrado en bienestar, consumo y salud (trabajo de IPA, 2012–2015). Lo que no existe publicado: un estudio que use la discontinuidad de Pensión 65 específicamente para identificar adopción de *billeteras digitales* (Yape/Plin) en adultos mayores rurales.

El problema es que el gap puede ser un artefacto de timing: las billeteras digitales en Perú se masificaron post-2019. Cualquier wave de ENAHO anterior a ese año haría el outcome trivialmente cero. Esto no invalida la investigación — en realidad la acota — pero el paper debe hacer este argumento explícito: "usamos la wave X de ENAHO porque es la primera donde el outcome es no-trivial."

**Riesgo de working papers que llenen el gap**: MEDIO. No encontré un paper ya publicado que replique exactamente este diseño, pero el IDB tiene un programa activo de investigación en pagos digitales en LAC y Pensión 65 es suficientemente conocida para atraer atención. El riesgo de competencia existe.

---

### 4. EVALUACIÓN DE RIESGOS

**Riesgo de resultado nulo (null result)**:

La literatura base (Bachas et al., Muralidharan et al.) muestra efectos positivos de la inclusión financiera forzada vía transferencias, pero en esos contextos el mecanismo es "acceso a cuenta bancaria → ahorro". El mecanismo aquí es distinto: "transferencia digital → adopción de billetera (Yape/Plin)". Para adultos mayores rurales con baja alfabetización digital, el salto de "recibir en cuenta" a "usar activamente una billetera" es más grande y más incierto. El null result es plausible.

Adicionalmente: si Pensión 65 no paga vía billetera digital (muchos beneficiarios reciben en efectivo vía agente BIM o ventanilla), el mecanismo se rompe. Esto apuntala el riesgo de resultado nulo y el problema de SUTVA identificado por el meta-evaluador.

---

### VEREDICTO FINAL DEL FACT-CHECKER

El error de mayor impacto es el **journal incorrecto para Bachas et al.** (JF, no QJE). No invalida el argumento, pero daña la credibilidad ante un referee que conoce la literatura. Los **papers faltantes** son la segunda debilidad más seria — especialmente Lee & Lemieux (2010) y el trabajo previo de IPA/Pensión 65 en bienestar, cuya ausencia podría interpretarse como desconocimiento del campo.

```json
{
  "citations_verified": false,
  "suspicious_citations": [
    "Bachas et al. 2021 citado como QJE — es Journal of Finance. Paper real, journal incorrecto."
  ],
  "missing_key_papers": [
    "Lee & Lemieux (2010, JEL) — referencia canónica de RDD, inexcusablemente ausente",
    "Calonico, Cattaneo & Titiunik (2014, Econometrica) — fundamento metodológico de rdrobust, mencionado como herramienta pero no citado",
    "McCrary (2008, JoE) — test propuesto como robustness check pero no referenciado",
    "Dupas & Robinson (2013, AEJ:Applied) — seminal en la literatura de inclusión financiera forzada",
    "Suri & Jack (2016, Science) — referencia estándar sobre efectos de largo plazo de pagos digitales en rurales pobres",
    "IPA/Pensión 65 RDD previo (consumo, bienestar, depresión) — trabajo relacionado no citado, posible omisión estratégica",
    "Bachas et al. (2018, AEA P&P) — companion paper más directamente relevante para el mecanismo propuesto"
  ],
  "gap_confirmed": true,
  "gap_caveats": "Gap genuino pero condicionado a usar wave ENAHO post-2019; debe argumentarse explícitamente. Diferenciación del trabajo previo de IPA en Pensión 65 es obligatoria.",
  "null_result_risk": "MEDIUM",
  "competition_risk": "MEDIUM"
}
```

---

Sources:
- [How Debit Cards Enable the Poor to Save More — Journal of Finance (Wiley)](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13021)
- [Digital Financial Services Go a Long Way — AEA P&P](https://www.aeaweb.org/articles?id=10.1257/pandp.20181013)
- [Building State Capacity: Biometric Smartcards in India — AER](https://pubs.aeaweb.org/doi/10.1257/aer.20141346)
- [Savings Constraints and Microenterprise Development — AEJ:Applied](https://www.aeaweb.org/articles?id=10.1257/app.5.1.163)
- [The Long-Run Poverty and Gender Impacts of Mobile Money — Science](https://www.science.org/doi/10.1126/science.aah5309)
- [Regression Discontinuity Designs in Economics — Lee & Lemieux, JEL](https://www.aeaweb.org/articles?id=10.1257/jel.48.2.281)
- [Robust Nonparametric Confidence Intervals for RD Designs — Econometrica](https://onlinelibrary.wiley.com/doi/10.3982/ECTA11757)
- [Impact of Pension 65 on Senior Citizens — IPA](https://poverty-action.org/study/impact-pension-program-senior-citizens%E2%80%99-wellbeing-peru)