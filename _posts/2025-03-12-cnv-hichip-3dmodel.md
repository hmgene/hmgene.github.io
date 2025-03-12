---
layout: post
title:  "Consideration of 3D-based CNV"
date:   2025-03-12 11:54:38 -0400
categories: cnv hichip
---

## Background
- Hint [PMC7087379](https://pmc.ncbi.nlm.nih.gov/articles/PMC7087379/) and HiCnv [PMC8210825](https://pmc.ncbi.nlm.nih.gov/articles/PMC8210825/) calculate CNV profiles from Hi-C
- NeoLoopFinder adds segmentation module using HMM [PMC8191102](https://pmc.ncbi.nlm.nih.gov/articles/PMC8191102/)
- Eigenvector decomposition (ICE) [PMC3816492](https://pmc.ncbi.nlm.nih.gov/articles/PMC3816492/)
- The ICE is biased when applied to cancer data with CNV variation, which can be corrected using NeoLoopFiinder

## Problem Description

How to Account for CNV in 3D Contact Normalization using HiChIP learning from HiC approaches. 
</br>When:
- C[i,j] : unknown contact map between i and j
- D[i,j] : observed contact counts between i and j
- B[i] : Bias term
- S[k] : the average of nonzero marginal sums of bins with copy number equaling to k.

The corrected Contact map $C$ can be calculated by:
| equation | description |
| :-: | :- |
| C[i,j] = B[i] x D[i,j] x B[j] | estimate C  |
| B[i] = B[i] x S[k] / sum(D[i,]) | update B[i] ~ k-copy proportion over all contact flux from i |

NeoLoopFinder incorperates a S[k] term for the bins w/ CNV value is k. 
In brief, this additional term, relative to the marginal contacts sum(D[i,]). 
panelizes the C[i,j] in proportion to the CNV amount.
I interpret this as a CNV-aware track, where biases are factorized into contributions corresponding to multiple CNV levels.
  
### Results
- Focus on Type II CNV Loss
  - segments expanded with 20k binning
  - Condition: CNV input > 0, and for methods in {Blue, Red, Green}, the difference between CNV method and CNV input > 0.5.
- Color Codes:
  - Gold: Input ChIP
  - Blue: CopywriteR HiChIP
  - Red: Our Multi-peak HiChIP
  - Green: NeoloopFinder (3D) HiChIP
  

| Title | figure |
| - | - |
| 35 CNV loss regions | <img width="832" alt="image" src="https://github.com/user-attachments/assets/aa154f09-2701-4b6d-9518-7f87ec816eb2" /> | 
| IGV snapshot at chr8:85,605,879-136,041,554 | <img width="984" alt="image" src="https://github.com/user-attachments/assets/0e1079ae-4598-43f7-9e47-899be1ac13f2" /> | 


- Mpeak recovering the loss
- The 3D-aware method tends to overestimate CNVs in regions with a high degree of 3D contacts.

### Conclusion
Applying a 1D method to HiChIP with proper peak calling reduces Type II errors, whereas incorporating 3D-aware information tends to introduce Type I errors.

