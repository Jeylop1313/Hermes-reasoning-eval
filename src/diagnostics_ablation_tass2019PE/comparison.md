# HERMES — Comparativa de Ablación (TASS 2019 Perú)

## Métricas Principales

| Técnica | N | AvgRec | Macro-F1 | F1^PN | Accuracy | Micro-F1 |
|---------|---|--------|----------|-------|----------|----------|
| Chain-of-Thought (CoT) | 966 | 0.5138 | 0.4044 | 0.6334 | 0.4648 | 0.4648 |
| Zero-Shot | 966 | 0.5001 | 0.3730 | 0.6334 | 0.4482 | 0.4482 |

## Mejor Técnica por Métrica

- **AvgRec**: Chain-of-Thought (CoT) (0.5138)
- **Macro-F1**: Chain-of-Thought (CoT) (0.4044)
- **F1^PN**: Zero-Shot (0.6334)
- **Accuracy**: Chain-of-Thought (CoT) (0.4648)
- **Micro-F1**: Chain-of-Thought (CoT) (0.4648)

## Métricas por Clase (por Técnica)

### Positivo

| Técnica | Precision | Recall | F1 | Gold | Pred |
|---------|-----------|--------|----|------|------|
| Chain-of-Thought (CoT) | 0.4174 | 0.9352 | 0.5771 | 216 | 484 |
| Zero-Shot | 0.4107 | 0.9583 | 0.5750 | 216 | 504 |

### Negativo

| Técnica | Precision | Recall | F1 | Gold | Pred |
|---------|-----------|--------|----|------|------|
| Chain-of-Thought (CoT) | 0.5882 | 0.8333 | 0.6897 | 228 | 323 |
| Zero-Shot | 0.5872 | 0.8421 | 0.6919 | 228 | 327 |

### Neutral

| Técnica | Precision | Recall | F1 | Gold | Pred |
|---------|-----------|--------|----|------|------|
| Chain-of-Thought (CoT) | 0.2929 | 0.2412 | 0.2645 | 170 | 140 |
| Zero-Shot | 0.2576 | 0.2000 | 0.2252 | 170 | 132 |

### Sin sentimiento

| Técnica | Precision | Recall | F1 | Gold | Pred |
|---------|-----------|--------|----|------|------|
| Chain-of-Thought (CoT) | 0.8421 | 0.0455 | 0.0863 | 352 | 19 |
| Zero-Shot | 0.0000 | 0.0000 | 0.0000 | 352 | 3 |
