# Median read quality
- **ID:** median_read_quality
- **Description:** The median of per-read average quality scores across reads in the dataset. For ONT sequencing, this usually reflects the basecaller-estimated confidence for each read, and serves as a central measure of read-level basecalling quality. This metric is useful for comparing reads within a dataset or across datasets in a given platform, but Q-scores may not be directly comparable between sequencing platforms.
- **Implementation details:** Calculate the mean quality score for each read from FASTQ quality strings or use the read-level quality value reported by the basecaller. Then take the median across all included reads. The implementation should define whether failed reads, unclassified reads, unmapped reads, or quality-filtered reads are included.
- **Type:** Float, Phred-scaled quality score (eg. 16.8)
- **Functionally equivalent implementations:**
  - Dorado sequencing summary
  - NanoPlot
  - pycoQC
