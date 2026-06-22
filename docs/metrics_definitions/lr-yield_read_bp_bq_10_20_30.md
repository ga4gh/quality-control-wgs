# Yield (read/bp BQ 10/20/30)
- **ID:** yield_bp_q10_q20_q30
- **Description:** The number of reads, or bases derived from reads, whose read-level (arithmetic) mean quality scores meet or exceed specified quality thresholds such as Q10, Q20, and Q30. Under the Phred model, Q10 approximately corresponds to 90% estimated base accuracy, Q20 to 99% accuracy, and Q30 to 99.9% accuracy. In Oxford Nanopore  long read datasets, thresholds are commonly applied based on the arithmetic mean across all base positions as these scores are calibrated specifically to be accurate at this level.
- **Implementation details:** For each read, obtain the arithmetic mean of the per-base quality values across the read from the FASTQ/BAM quality string. Count the number of reads whose read-level mean Q-scores meet the selected threshold, and/or the number of bases contained within those reads. When comparing ONT and PacBio datasets, this metric should be interpreted cautiously because quality-score calibration and error profiles differ between platforms, chemistries, and basecallers.
- **Type:** Integer, bases or reads (eg. 92000000000 bases at Q10)
- **Functionally equivalent implementations:**
  - Dorado summary
  - NanoPlot
  - seqkit stats
  - samtools stats
