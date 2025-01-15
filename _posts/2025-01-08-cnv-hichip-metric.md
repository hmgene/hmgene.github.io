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

**Summary**

| Sample | number | length distribution |
|---|---|---|
| region_fn.bed | 15 | min=40000, med=310000, avg=405957, max=2680000  |
| region_fn_MG63_ChIP.bed | 7 | |
| region_fn_MG63_HiChIP.bed | 15 | |
| region_tp.bed | 188 | min=40000, med=180000, avg=444000, max=2280000  |
| region_tp_MG63_ChIP.bed | 188 | |
| region_tp_MG63_HiChIP.bed | 188 | |

<img width="335" alt="image" src="https://github.com/user-attachments/assets/f6a5c71d-4641-4e4f-a820-67b9e31ce1db" />

**FN bed***
```
chr1	122500001	124780000
chr1	143180001	143320000
chr1	219580001	219620000
chr13	16020001	18040000
chr5	49660001	49860000
chr8	108700001	108960000
chr8	117840001	117960000
chr8	117960001	118240000
chr9	13860001	14020000
chr9	14020001	14200000
chr9	14200001	14580000
chr9	14580001	14700000
chr9	21500001	21860000
chrX	141000001	141040000
chrY	56680001	56760000
```
| Figure 1           | Figure 2           | Figure 3  |
|---------------------|---------------------|----------------------|
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/0ddc3029-2a10-4f17-9c0e-fb71169d67b4" /> | <img width="300" alt="image" src="https://github.com/user-attachments/assets/c5728cda-e25b-435d-828b-2294340f6e6e" /> | <img width="300" alt="image" src="https://github.com/user-attachments/assets/3e6b673b-a973-47b4-a612-3f20a9ebc5db" /> |
| chr1	122500001	124780000 | chr1	143180001	143320000 | chr13	16020001	18040000 |

