# HERMES — Ablation Benchmarks (Zero-Shot)

**Archivo fuente:** `ablation_zero_shot_tass2019PE.json`  
**Técnica:** Zero-Shot  
**Dataset:** TASS 2019 Perú  
**Clases:** P, N, NEU, NONE  
**Total evaluados:** 966 (omitidos: 0)  
**Correctos:** 433  
**Errores:** 533  

## Métricas

| Métrica | Valor |
|---------|-------|
| AvgRec    | 0.5001 |
| Macro-F1  | 0.3730 |
| F1^PN     | 0.6334 |
| Accuracy  | 0.4482 |
| Micro-F1  | 0.4482 |

## Métricas por Clase

| Clase | Precision | Recall | F1 | Gold | Pred |
|-------|-----------|--------|----|------|------|
| P | 0.4107 | 0.9583 | 0.5750 | 216 | 504 |
| N | 0.5872 | 0.8421 | 0.6919 | 228 | 327 |
| NEU | 0.2576 | 0.2000 | 0.2252 | 170 | 132 |
| NONE | 0.0000 | 0.0000 | 0.0000 | 352 | 3 |

## Matriz de Confusión

| Gold \ Pred | Positivo | Negativo | Neutral | Sin sentimiento |
|------------|-------:|-------:|-------:|-------:|
| P | 207 | 6 | 3 | 0 |
| N | 24 | 192 | 11 | 1 |
| NEU | 91 | 43 | 34 | 2 |
| NONE | 182 | 86 | 84 | 0 |

## Distribución de Errores

| Patrón | Count | % de Errores | Archivo |
|--------|-------|-------------:|---------|
| NONE>P | 182 | 34.1% | `errors_NONE_to_P.md` |
| NEU>P | 91 | 17.1% | `errors_NEU_to_P.md` |
| NONE>N | 86 | 16.1% | `errors_NONE_to_N.md` |
| NONE>NEU | 84 | 15.8% | `errors_NONE_to_NEU.md` |
| NEU>N | 43 | 8.1% | `errors_NEU_to_N.md` |
| N>P | 24 | 4.5% | `errors_N_to_P.md` |
| N>NEU | 11 | 2.1% | `errors_N_to_NEU.md` |
| P>N | 6 | 1.1% | `errors_P_to_N.md` |
| P>NEU | 3 | 0.6% | `errors_P_to_NEU.md` |
| NEU>NONE | 2 | 0.4% | `errors_NEU_to_NONE.md` |
| N>NONE | 1 | 0.2% | `errors_N_to_NONE.md` |

## Uso de Recursos

| Métrica | Total | Avg por Tweet |
|---------|------:|--------------:|
| Tiempo (segundos) | 247.9 | 0.26 |
