# Yield (reads ≥ N bp or reads ≥ P25, P50, P75)
- **ID:** yield_reads_ge_n_bp_ge_n_quartile
- **Description:** The number, fraction, or total bases of reads with length greater than or equal to user-defined read length thresholds such as 10 kb, 25 kb, or 50 kb or summarized using read-length distribution percentiles/quartiles. This metric is useful for assessing the amount of long-range sequence information available in ONT and PacBio datasets for downstream applications such as structural variant detection, repeat resolution, assembly, and phasing.
- **Implementation details:** Choose one or more read length thresholds and count reads whose observed read length is greater than or equal to each threshold. Report either the read count, the corresponding number of bases, or the fraction of the total dataset represented by those reads. Thresholds should be explicitly specified in the report because different projects may define different cutoffs for long-read applications.
- **Type:** Integer or Float (eg. 125000 reads ≥ 10000 bp; 0.42 fraction of reads)
- **Functionally equivalent implementations:**
  - seqkit stats
  - NanoPlot
  - pycoQC
