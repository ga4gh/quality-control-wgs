# Reads mapped (%)
- **ID:** bp_mapped_pct
- **Description:** The percentage of bases contained within read alignments to the selected reference genome. In long-read sequencing, this metric reflects the usability of reads for reference-based analysis and is affected by read quality, reference completeness, contamination, structural divergence from the reference, and alignment settings.
- **Implementation details:** Count the number bases contained within either the primary read alignment or within any read alignment and divide by the total number of bases in all reads considered. The implementation should specify whether secondary and supplementary alignments are included or excluded. For ONT and PacBio WGS, primary alignments are usually preferred for sample-level QC. Low mapping percentage can indicate contamination, degraded DNA, poor basecalling quality, wrong reference choice, or library issues.
- **Type:** Float, percentage (eg. 97.3)
- **Functionally equivalent implementations:**
  - samtools flagstat
  - samtools stats
  - mosdepth
