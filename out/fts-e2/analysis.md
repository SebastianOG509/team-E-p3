# Analysis of FTS

## EQS3 (Scenario E-QS3 (disponibilidad del Traductor))

| Factor | Unavailability | Share |
|--------|----------------|-------|
| TRA, TRS (β = 0.1) | 0.0520 % | 100 % |

Chain availability: **99.948 %** (4.6 h/year); target 99.9: **met**

## EQS1 (Scenario E-QS1 (custodia oportuna))

| Stage | Budget |
|-------|--------|
| E_K19 | 30 ms |
| E_K20 | 30 ms |
| E_K21 | 30 ms |
| E_K26 | 30 ms |
| E_K27 | 30 ms |

Chain latency: **150 ms**; target 30000: **met**

## EQS2 (Scenario E-QS2 (persistencia de posiciones))

| Stage | Budget |
|-------|--------|
| E_K22 | 10000 ms |
| E_K58 | 18000 ms |
| E_K59 | 2000 ms |

Chain latency: **30000 ms**; target 60000: **met**

## EQS6 (Scenario E-QS6 (detección del silencio))

| Stage | Time |
|-------|------|
| UAB: 3 missed heartbeats × 10000 ms | 30000 ms |
| E_K25 (propagation) | 5000 ms |

Detection time: **35000 ms**; target 35000: **met**

## FTSQS1 (Scenario SoS-QS1 (M4, tramo del FTS))

| Stage | Budget |
|-------|--------|
| E_K32 | 40000 ms |
| E_K33 | 2000 ms |
| CON | 30000 ms |

Chain latency: **72000 ms**; target 300000: **met**

## SoSQS1M4 (Scenario SoS-QS1 (M4))

| Stage | Budget |
|-------|--------|
| RGW | 200000 ms |
| SoS_K5 | 40000 ms |
| NCG | 230000 ms |
| SoS_K32 | 10000 ms |
| CGW | 300000 ms |

Chain latency: **780000 ms**; target 900000: **met**
