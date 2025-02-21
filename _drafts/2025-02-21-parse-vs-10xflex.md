---
layout: post
title:  "Parse-seq vs 10X and TrailMaker vs Scanpy : Fixed All Programs"
date:   2025-01-21 6:46:00 -0400
categories: parse-seq single-cell cnmf   
---
# Parse-Seq vs 10X

## Methods

| platform | methods |
| :--: | :--: |
| parse-seq | trailmaker |
| 10xflex | cellranger multi |

## Summary

| platform | reads or probes | avg. cells | avg. reads/cell | med. genes/cell | seq. saturation | 
|:--: |:--:| :--: | :--: | :--: | :--: |
| parse-seq| 2,547,170,863 |78,278 | 32,540 | 2,952 | 24.1% |
| 10x pool1 | 978,088,688 | 76,319 | 12,816 | 2189 | 28%  |
| 10x pool2 | 869,856,573 | 94,342 | 9,220 | 2153 | 19.8% |
