# team-E-p3 — Modelado arquitectónico del Sistema de Transporte Fluvial (FTS)

Lenguaje del Laboratorio 4 adaptado por el equipo E, modelo conjunto `sos.arch` (el acordado por los seis equipos, escrito en el lenguaje base), modelos del FTS antes (`fts-e1.arch`) y después (`fts-e2.arch`) de la Entrega 2, transformaciones y artefactos generados.

## Ejecución

Con Docker, desde la carpeta del proyecto. Primero se construye la imagen (igual en todos los sistemas):

```
docker build -t lssa-team-e .
```

Después se ejecuta montando la carpeta actual en `/app`. La forma de escribir la carpeta actual cambia según el sistema:

**Linux y macOS (bash, zsh)**

```
docker run --rm -v "$PWD:/app" lssa-team-e                            # los tres modelos de models/
docker run --rm -v "$PWD:/app" lssa-team-e invalid/c6-events.arch     # un modelo mal formado
```

**Windows, Símbolo del sistema (CMD)**

```
docker run --rm -v "%cd%:/app" lssa-team-e
docker run --rm -v "%cd%:/app" lssa-team-e invalid/c6-events.arch
```

**Windows, PowerShell**

```
docker run --rm -v "${PWD}:/app" lssa-team-e
docker run --rm -v "${PWD}:/app" lssa-team-e invalid/c6-events.arch
```

Las comillas son necesarias si la ruta tiene espacios. Las rutas de los modelos (`invalid/...`) se escriben con `/` en todos los sistemas.

Sin argumentos se procesan todos los modelos de `models/`. Los artefactos quedan en `out/<modelo>/`: `connectors.md`, `view.mmd` (Mermaid) y `analysis.md`. Un modelo mal formado termina en `REJECTED` con el mensaje de `invalid/expected-rejections.txt`.

Sin Docker (Python 3.11 o superior), en un entorno virtual para no modificar el Python del sistema:

```
python3 -m venv .venv                                  # Windows: python -m venv .venv
.venv/bin/python -m pip install textX==4.3.0           # Windows: .venv\Scripts\python.exe -m pip install textX==4.3.0
.venv/bin/python generation.py                         # Windows: .venv\Scripts\python.exe generation.py
```

Para volver a escribir los modelos del FTS desde las tablas de la Entrega 2: `python3 tools/gen_models.py` (en Windows, `python tools/gen_models.py`).

## Estructura

| Archivo | Contenido |
|---|---|
| `arch.tx` | Gramática (M2). Adaptaciones del equipo marcadas `[E]` |
| `metamodel.py` | Restricciones C1–C7 |
| `transformations.py` | Tabla de conectores, vista C&C y análisis |
| `generation.py` | Lee cada modelo, verifica la conformidad y aplica las transformaciones |
| `models/` | `sos.arch` (conjunto, sin cambios), `fts-e1.arch`, `fts-e2.arch` |
| `invalid/` | Un modelo mal formado por restricción agregada o adaptada, y los mensajes esperados |
| `out/` | Artefactos generados |
| `tools/gen_models.py` | Ayuda que escribe los modelos del FTS a partir de las tablas de la Entrega 2 (`tools/fts_data.json`) |

## Adaptaciones del lenguaje

| Adaptación | Dónde | Para qué |
|---|---|---|
| `role` en componentes (`broker`) | Gramática, C6 | Reconocer al Broker Interno de Eventos, intermediario del estilo orientado a eventos |
| `period` en componentes | Gramática, análisis | Periodo del latido de la Unidad a Bordo (E-QS6) |
| Métrica `detection` con `misses` | Gramática, análisis | Tiempo de detección = latidos ausentes × periodo + propagación (E-QS6) |

## Restricciones

| ID | Restricción | Origen | Modelos rechazados |
|---|---|---|---|
| C1–C4 | Sin cambios (Laboratorio 4) | — | — |
| C5 (extendida) | Un análisis `detection` empieza en un componente con `period` y declara `misses`; sus demás factores tienen `latency` | Escenario E-QS6, Entrega 2 | `c5-period.arch`, `c5-misses.arch` |
| C6 (nueva, estilo) | Un componente de T3 solo publica eventos hacia un componente con `role broker` o hacia un almacén de T4 | Estilo **orientado a eventos** del FTS (Entrega 1, 5.2) | `c6-events.arch` |
| C7 (nueva, estilo) | Una dependencia que sale de un componente de T1 termina en un servicio de T3 | Estilo **cliente-servidor** del FTS (Entrega 1, 5.3) | `c7-client-server.arch` |

C6 solo restringe los eventos que salen de T3: E-K19 (Terminal → Custodia) y E-K38 (App → Seguimiento) salen de T1 y no la violan. Los dos modelos del FTS la cumplen: E-K21 y E-K25 van al Broker; E-K67 y E-K68 van a un almacén de T4 (Registro de Auditoría).

## Convenciones

- Identificadores: `SoS-K5` se escribe `SoS_K5` y `E-K1` se escribe `E_K1`, porque el guion no es válido en un identificador.
- Los componentes de frontera de los otros constituyentes y los conectores globales se copian de `sos.arch` sin cambios. En el modelo del FTS aparecen solo los 13 conectores globales del FTS (SoS-K4a/b, K10a/b, K15, K16, K19a/b, K28a/b, K31a/b y K35) y, para componer M4, SoS-K5 y SoS-K32.
- Componentes: `PAN`, `CAP`, `TMU`, `FGW`, `TRA`, `BRO`, `IOT`, `PRO`, `TUR`, `CUS`, `SEG`, `CON`, `BOF`, `ALT`, `UAB`, `SEN`, `GRU`, `BAR`, `REM` (19, Entrega 1) y `COL`, `BUF`, `TRS`, `AUD` (4 nuevos de la Entrega 2). Conectores internos: `E_K1` a `E_K46` (Entrega 1) y `E_K47` a `E_K69` (Entrega 2).
- Acoplamiento y naturaleza de cada conector internos: los de las tablas 4.1 y 7.3 de la Entrega 2.
- Latencias en ms. Cada etapa de un análisis la lleva un elemento distinto: en E-QS1, los cinco conectores de la cadena de custodia (E-K19, E-K20, E-K21, E-K26, E-K27); en SoS-QS1 (tramo del FTS), E-K32 (consultas), E-K33 (última respuesta) y `CON` (aplicar resultados, 30 s).
- En `fts-e1.arch`, E-K26 lleva la espera en cola FIFO del Traductor (1,6 s) más su servicio: 4 × 10 + 1.660 = 1.700 ms; E-K33 lleva 2 s más 3,2 s de cola. En `fts-e2.arch` la prioridad elimina la espera y cada salto vale 30 ms (10 de servicio + 20 de escritura durable).
- Disponibilidad de una instancia del Traductor: 99,5 %; causa común β = 0,10 (supuesto A4 de la Entrega 2).
- E-QS2 y E-QS6 solo se escriben en `fts-e2.arch`: antes no había almacenamiento a bordo ni latidos. En E-QS2, E-K22 lleva 10 s (detección de la reconexión), E-K58 lleva 18 s (vaciado de 900 posiciones a 50/s, calculado a mano) y E-K59 lleva 2 s (acuse durable).

## Resultados

| Escenario | Antes (e1) | Después (e2) | Entrega 2 | Diferencia |
|---|---|---|---|---|
| E-QS3 (disponibilidad) | 99,500 %, no cumple | 99,948 %, cumple | 99,5 % → 99,948 % | Ninguna |
| E-QS1 (custodia) | 1.700 ms | 150 ms | ≈ 1,7 s → ≤ 0,2 s | Ninguna; la Entrega 2 acota con 0,2 s y el cálculo da 0,15 s |
| E-QS2 (persistencia) | No se puede escribir | 30.000 ms (≤ 60.000) | 30 s | Ninguna |
| E-QS6 (detección) | No se puede escribir | 35.000 ms (≤ 35.000, en el límite) | 35 s | Ninguna |
| SoS-QS1 (M4), tramo del FTS | 75.200 ms | 72.000 ms | ≈ 75 s → 72 s | Redondeo |
| SoS-QS1 (M4), composición | 780.000 ms | 780.000 ms | 780 s | Ninguna; igual que `sos.arch` |

## Lo que el lenguaje no analiza

- **E-QS2:** el vaciado de 900 posiciones (900 / 50 = 18 s) se calculó a mano. Haría falta una métrica de recuperación con capacidad y carga.
- **E-QS4 (seguridad):** haría falta un modelo del atacante y fronteras de confianza.
- **E-QS5 (modificabilidad):** haría falta un análisis de impacto de cambio, con dependencias y esfuerzo.
