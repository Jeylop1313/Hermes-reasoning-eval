# HERMES — Ablation Benchmarks (Chain-of-Thought (CoT))

**Archivo fuente:** `ablation_cot_tass2019PE.json`  
**Técnica:** Chain-of-Thought (CoT)  
**Dataset:** TASS 2019 Perú  
**Clases:** P, N, NEU, NONE  
**Total evaluados:** 966 (omitidos: 0)  
**Correctos:** 449  
**Errores:** 517  

## Métricas

| Métrica | Valor |
|---------|-------|
| AvgRec    | 0.5138 |
| Macro-F1  | 0.4044 |
| F1^PN     | 0.6334 |
| Accuracy  | 0.4648 |
| Micro-F1  | 0.4648 |

## Métricas por Clase

| Clase | Precision | Recall | F1 | Gold | Pred |
|-------|-----------|--------|----|------|------|
| P | 0.4174 | 0.9352 | 0.5771 | 216 | 484 |
| N | 0.5882 | 0.8333 | 0.6897 | 228 | 323 |
| NEU | 0.2929 | 0.2412 | 0.2645 | 170 | 140 |
| NONE | 0.8421 | 0.0455 | 0.0863 | 352 | 19 |

## Matriz de Confusión

| Gold \ Pred | Positivo | Negativo | Neutral | Sin sentimiento |
|------------|-------:|-------:|-------:|-------:|
| P | 202 | 11 | 3 | 0 |
| N | 26 | 190 | 11 | 1 |
| NEU | 87 | 40 | 41 | 2 |
| NONE | 169 | 82 | 85 | 16 |

## Distribución de Errores

| Patrón | Count | % de Errores | Archivo |
|--------|-------|-------------:|---------|
| NONE>P | 169 | 32.7% | `errors_NONE_to_P.md` |
| NEU>P | 87 | 16.8% | `errors_NEU_to_P.md` |
| NONE>NEU | 85 | 16.4% | `errors_NONE_to_NEU.md` |
| NONE>N | 82 | 15.9% | `errors_NONE_to_N.md` |
| NEU>N | 40 | 7.7% | `errors_NEU_to_N.md` |
| N>P | 26 | 5.0% | `errors_N_to_P.md` |
| P>N | 11 | 2.1% | `errors_P_to_N.md` |
| N>NEU | 11 | 2.1% | `errors_N_to_NEU.md` |
| P>NEU | 3 | 0.6% | `errors_P_to_NEU.md` |
| NEU>NONE | 2 | 0.4% | `errors_NEU_to_NONE.md` |
| N>NONE | 1 | 0.2% | `errors_N_to_NONE.md` |

## Uso de Recursos

| Métrica | Total | Avg por Tweet |
|---------|------:|--------------:|
| Tiempo (segundos) | 861.8 | 0.89 |
