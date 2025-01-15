---
layout: post
title:  "CNV-HiCHIP Performance Comparisons"
date:   2025-01-08 11:54:38 -0400
categories: cnv hichip
---


### Off-Target CNV Prediction Approaches:
- ChIP-seq Input: Considered the gold standard.
- ChIP-seq Treatment: Used as the standard comparison.
- HiChIP-1D Treatment: Treated as standard ChIP-seq data.
- HiChIP-3D Treatment (Loop): Utilizes looping information exclusively (Neoloop).

### Comparison of MG63 Datasets with MG63 ChIP-seq Input
- Informative Value: The HiChIP Loop method provides less informative results compared to other approaches.
- Noise Levels: HiChIP 1D data is less noisy than ChIP-seq, primarily due to its higher sequencing depth.
- False Negatives: Both ChIP-seq and HiChIP off-target selection results in more false negatives, leading to missed CNVs that are detected by the input.
- False Positives: ChIP-seq exhibits a higher rate of false positives when calling CNV gains.
<img width="1453" alt="image" src="https://github.com/user-attachments/assets/5402dbde-f68b-4ea7-aed0-d72bb8638196" />



**Average Plots**
- TP segments : Input CNV > 1 and | Target CNV - Input CNV | < 0.5 
- FN segments : Input CNV > 1 and  Target CNV - Input CNV < - 0.5
- Signals (Color) : normalized log2 FC ( after correcting GC bias, Off-target, mappability)

Table
| Sample | number |
|---|---|---|
| region_fn.bed | 15 |
| region_fn_MG63_ChIP.bed | 7 |
| region_fn_MG63_HiChIP.bed | 15 |
| region_tp.bed | 188 |
| region_tp_MG63_ChIP.bed | 188 |
| region_tp_MG63_HiChIP.bed | 188 |

<img width="335" alt="image" src="https://github.com/user-attachments/assets/f6a5c71d-4641-4e4f-a820-67b9e31ce1db" />
