# Median read length
- **ID:** median_read_length
- **Description:** The median length of reads in the dataset. It represents the typical read length and is less sensitive than the mean to the long-tailed read length distribution commonly observed in ONT sequencing.
- **Implementation details:** Measure the length of each read in FASTQ/BAM and report the median value across all included reads. The implementation should specify whether adapters, clipped bases, filtered reads, or unmapped reads are included. Median read length is useful for assessing fragmentation, DNA extraction quality, library preparation consistency, and suitability for long-range applications.
- **Type:** Integer, base pairs (eg. 7800)
- **Functionally equivalent implementations:**
  - seqkit stats
  - NanoPlot
  - pycoQC
  - samtools stats
