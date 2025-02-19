---
layout: post
title:  "CNV-HiCHIP Average Plot and Peak Calling"
date:   2025-02-19 12:38:00 -0400
categories: cnv hichip
---

### Data 

Data Considered
| type | file |
| --- | --- |
| Input | MG63.3_input_GSE74230.bam |
| ChIP | MG63-GFP_H3K27ac_020823_NovoG.bam |
| HiChIP | MG63_H3K27ac_OsteoAQuA.bam |

### Average Plots
Selected regions by CNV >= 1 

**Average Plots at each selected region**

Number of Regions  
| counts | regions |
|---|---|
|     311  | input_gt1seg.bed |
|     311 |  chip_gt1seg.bed |
|      280 | hichip_gt1seg.bed |


![input](https://github.com/user-attachments/assets/fe813d1b-0011-404b-a38a-14868438688d)
- ChIP tends to overestimate, except in HiChIP-only regions.
- HiChIP is similar to Input.
- HiChIP overestimates in HiChIP regions.


**Average Plots at exclusive reginos**

Number of Regions
| counts | regions |
|----|---|
|     234  | input_or_chip_only.bed |
|      59 | hichip_only.bed |
|     194  | common.bed |

![only](https://github.com/user-attachments/assets/5ea4b2f9-7141-4fa5-b0d9-6db1d4dc3fe6)
- In Input or ChIP regions, HiChIP predicts well, while ChIP tends to overestimate CNV.
- In the HiChIP only regions, HiChIP tends to overestimate.

### Our Peak Calling  
- Homer is too broad.
- MACS is too narrow and fails to detect peaks.
- Copywriter peaks overhang across segments, resulting in missed segments.
- Fundamental Model
<img width="381" alt="image" src="https://github.com/user-attachments/assets/776eb149-de9d-4859-8993-71d5278a5ef2" />

- Our method iteratively re-calls after removing those identified in the previous step.

**Mismatching CNV regions** 
<img width="959" alt="image" src="https://github.com/user-attachments/assets/c20fcc48-5ab4-4234-81bc-9c2e7da06fda" />

**Our Peak Caller**

| 1-iter | 3-iter |
|---|---|
| ![newplot1](https://github.com/user-attachments/assets/8005e229-e123-41b4-a9b5-1339f333fed0) |![newplot3](https://github.com/user-attachments/assets/28455fc5-d1c1-49a1-a0fd-7cbb8000017f) |

