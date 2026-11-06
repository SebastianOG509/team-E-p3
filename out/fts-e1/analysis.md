# Analysis of FTS

## EQS3 (Scenario E-QS3 (disponibilidad del Traductor))

| Factor | Unavailability | Share |
|--------|----------------|-------|
| TRA | 0.5000 % | 100 % |

Chain availability: **99.500 %** (43.8 h/year); target 99.9: **NOT met**

## EQS1 (Scenario E-QS1 (custodia oportuna))

| Stage | Budget |
|-------|--------|
| E_K19 | 10 ms |
| E_K20 | 10 ms |
| E_K21 | 10 ms |
| E_K26 | 1660 ms |
| E_K27 | 10 ms |

Chain latency: **1700 ms**; target 30000: **met**

## FTSQS1 (Scenario SoS-QS1 (M4, tramo del FTS))

| Stage | Budget |
|-------|--------|
| E_K32 | 40000 ms |
| E_K33 | 5200 ms |
| CON | 30000 ms |

Chain latency: **75200 ms**; target 300000: **met**

## SoSQS1M4 (Scenario SoS-QS1 (M4))

| Stage | Budget |
|-------|--------|
| RGW | 200000 ms |
| SoS_K5 | 40000 ms |
| NCG | 230000 ms |
| SoS_K32 | 10000 ms |
| CGW | 300000 ms |

Chain latency: **780000 ms**; target 900000: **met**
