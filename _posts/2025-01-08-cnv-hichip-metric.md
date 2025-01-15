---
layout: post
title:  "CNV-HiCHIP Performance Comparisons"
date:   2025-01-15 12:38:00 -0400
categories: cnv hichip
---


### Off-Target CNV Prediction Approaches:
- ChIP-seq Input: Considered the gold standard.
- ChIP-seq Treatment: Used as the standard comparison.
- HiChIP-1D Treatment: Treated as standard ChIP-seq data.
- HiChIP-3D Treatment (Loop): Utilizes looping information exclusively (Neoloop).

### Proper Fragment Realignment Scoring
```
   [b          e]           # input score x
[a       c]   [d        f]  # target score y,z
=> # score of target on [b    e]

   [b          e]           # w1 = |c-b|/|e-b|, w2= |e-d|/|e-b| 
                            # score = (w1*x + w2*y) / (w1+w2)  ## w1 + w2 is not always 1
```



### Comparison of MG63 Datasets with MG63 ChIP-seq Input
- Informative Value: The HiChIP Loop method provides less informative results compared to other approaches.
- Noise Levels: HiChIP 1D data is less noisy than ChIP-seq, primarily due to its higher sequencing depth.
- False Negatives: Both ChIP-seq and HiChIP off-target selection results in more false negatives, leading to missed CNVs that are detected by the input.
- False Positives: ChIP-seq exhibits a higher rate of false positives when calling CNV gains.
<img width="1453" alt="image" src="https://github.com/user-attachments/assets/5402dbde-f68b-4ea7-aed0-d72bb8638196" />



### Average Plots
- TP segments : Input CNV > 1 and | Target CNV - Input CNV | < 0.5 
- FN segments : Input CNV > 1 and  Target CNV - Input CNV < - 0.5
- FP segments : Target CNV > 1 and Input CNV < 0.5
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
| region_fp.bed | 20 | |
| region_fp_MG63_ChIP.bed | 13 | |
| region_fp_MG63_HiChIP.bed | 7 | |

| Input | ChIP | HiChIP |
|----------------|----------------|----------------|
| <img width="241" alt="image" src="https://github.com/user-attachments/assets/82aab57c-cc0f-421d-acc0-c23233883d70" /> | <img width="248" alt="image" src="https://github.com/user-attachments/assets/7971e90c-6b76-4193-8d0c-a83c75685cbe" /> | <img width="237" alt="image" src="https://github.com/user-attachments/assets/f6c92fff-eae0-4c68-aea5-988e5ab4cc19" /> |



**False Negative (region_fn.bed, * in the figures)**
```
chr1	122500001	124780000 *
chr1	143180001	143320000 *
chr1	219580001	219620000 *
chr13	16020001	18040000
chr5	49660001	49860000 *
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


**Examples**
| Figures         | Genomic Loc           | Comments  |
|---------------------|---------------------|----------------------|
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/0ddc3029-2a10-4f17-9c0e-fb71169d67b4" /> | chr1	122500001	124780000 | Off-target fragmented |
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/c5728cda-e25b-435d-828b-2294340f6e6e" /> | chr1	143180001	143320000 | Off-target missing |
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/3e6b673b-a973-47b4-a612-3f20a9ebc5db" /> | chr1	219580001	219620000  | Off-target missing+fragmented  |
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/1f3acc71-ce71-4437-bc6e-3c4773303c4c" /> | chr5	49660001	49860000 | Low signal |

**False Positives**
```
chr1	120280001	120320000 *
chr1	120320001	120600000
chr1	144380001	144580000
chr1	144880001	145300000
chr1	148820001	149320000
chr10	16940001	17240000 *
chr11	123060001	123260000
chr12	80240001	80680000
chr13	16000001	16020000
chr13	33100001	33300000
chr13	75620001	75800000
chr17	47460001	47560000 *
chr2	150460001	150680000
chr2	187540001	187600000
chr2	97380001	97440000
chr4	65480001	65680000
chr5	42980001	43080000
chr9	340001	820000
chr9	40700001	41820000
chrX	3840001	3920000
```
**Examples**
| Figures         | Genomic Loc           | Comments  |
|---------------------|---------------------|----------------------|
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/019a1c6b-5463-4810-b1fc-dfc9e545307c" /> | chr1	120280001	120320000 | |
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/f5d4e1cc-d5b9-4ea9-8a7d-7c53db5fc4c0" /> | chr10	16940001	17240000 | | 
| <img width="300" alt="image" src="https://github.com/user-attachments/assets/fe52cecc-401b-4e3a-8388-cd300721a047" /> | chr17	47460001	47560000 | |


### Summary
- The causes of false positives can be categorized by comparison with the INPUT sample.
- Peak calling with various window sizes is a significant factor (impact factor=4).
- 3D off-target effects (loops) need to be investigated (impact factor > 4).

