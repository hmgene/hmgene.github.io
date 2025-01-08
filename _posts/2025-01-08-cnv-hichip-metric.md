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




