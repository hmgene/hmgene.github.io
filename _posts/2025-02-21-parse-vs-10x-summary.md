---
layout: post
title:  "Parse-seq vs 10X Summary : with Details"
date:   2025-02-21 6:46:00 -0400
categories: parse-seq single-cell cnmf 10xflex
---
# Parse-Seq vs 10X

## Methods

| platform | methods |
| :-- | :-- |
| parse-seq | trailmaker |
| 10xflex | cellranger multi |

## Summary

| platform | reads or probes | avg. cells | avg. reads/cell | med. genes/cell | seq. saturation | details |
| -- |:--| :-- | :-- | :-- | :-- | :-- |
| parse-seq| 2,547,170,863 |78,278 | 32,540 | 2,952 | 24.1% | [tm01](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm01_analysis_summary.html),[tm02](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm02_analysis_summary.html),[tm03](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm03_analysis_summary.html),[tm04](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm04_analysis_summary.html),[tm05](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm05_analysis_summary.html),[tm06](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm06_analysis_summary.html),[tm07](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm07_analysis_summary.html),[tm08](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm08_analysis_summary.html),[tm09](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm09_analysis_summary.html),[tm10](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm10_analysis_summary.html),[tm11](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm11_analysis_summary.html),[tm12](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm12_analysis_summary.html),[tm13](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm13_analysis_summary.html),[tm14](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm14_analysis_summary.html),[tm15](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm15_analysis_summary.html),[tm16](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm16_analysis_summary.html),[tm17](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm17_analysis_summary.html),[tm18](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm18_analysis_summary.html),[tm19](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm19_analysis_summary.html),[tm20](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm20_analysis_summary.html),[tm21](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm21_analysis_summary.html),[tm22](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm22_analysis_summary.html),[tm23](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm23_analysis_summary.html),[tm24](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm24_analysis_summary.html),[tm25](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm25_analysis_summary.html),[tm26](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm26_analysis_summary.html),[tm27](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm27_analysis_summary.html),[tm28](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm28_analysis_summary.html),[tm29](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm29_analysis_summary.html),[tm30](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm30_analysis_summary.html),[tm31](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm31_analysis_summary.html),[tm32](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm32_analysis_summary.html),[tm33](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm33_analysis_summary.html),[tm34](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/parse/tm34_analysis_summary.html) | 
| 10x pool1 | 978,088,688 | 76,319 | 12,816 | 2189 | 28%  | [UH14](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool1_UH14_web_summary.html),[UH16](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool1_UH16_web_summary.html),[UH17](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool1_UH17_web_summary.html),[UH19](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool1_UH19_web_summary.html) |
| 10x pool2 | 869,856,573 | 94,342 | 9,220 | 2153 | 19.8% | [pool2_UH23](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool2_UH23_web_summary.html),[UH24](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool2_UH24_web_summary.html),[UH25](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool2_UH25_web_summary.html),[UH26](https://raw.githack.com/hmgene/parse-vs-10x-pub/main/data/10x/pool2_UH26_web_summary.html) |


