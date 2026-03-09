---
title: QuPath Cell Count Pipeline
layout: project
---

## Problem

Manual cell counting across large histology batches was too slow and inconsistent for rapid iteration. The project goal was to automatically ingest full study folders, run consistent counting, and export analysis-ready outputs with minimal manual preprocessing.

## Pipeline Overview

This workflow uses QuPath scripting and batch execution to standardize image ingestion, detection, and export:

1. Recursively load all images inside a given root folder (including nested subfolders).
2. Apply consistent naming rules to map samples and reduce preprocessing overhead.
3. Run tissue/cell detection with fixed, documented parameters across the full batch.
4. Export per-image and aggregate cell counts to CSV for downstream statistical analysis.
5. Review overlays and QC snapshots before final reporting.

Repository: [BeatCancerLabQuPath](https://github.com/kelbakkouri/BeatCancerLabQuPath/tree/treain)

## Visual Workflow

![QuPath pipeline figure 1](../../assets/img/qupath/page_003_img_03.png)
*Workflow stage for automated region processing and detection setup.*

![QuPath pipeline figure 2](../../assets/img/qupath/page_005_img_02.png)
*Batch execution view for running large image sets with consistent rules.*

![QuPath pipeline figure 3](../../assets/img/qupath/page_006_img_01.png)
*Detection output snapshot used for quality-control checks.*

![QuPath pipeline figure 4](../../assets/img/qupath/page_006_img_02.png)
*Example analysis state showing counted objects and annotations.*

![QuPath pipeline figure 5](../../assets/img/qupath/page_007_img_02.png)
*Export-oriented view for transferring results into summary tables.*

## Outcome

The pipeline replaced repetitive manual counting with a reproducible process that scales to hundreds of images. Recursive folder ingestion and consistent naming conventions meant almost no manual preprocessing, while automated CSV export made downstream analysis significantly faster and cleaner.
