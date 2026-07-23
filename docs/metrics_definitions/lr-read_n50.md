# Read N50
- **ID:** read_n50
- **Description:** The length-weighted median read length in a long-read sequencing dataset. It is defined as the read length L such that 50% of the total sequenced bases are contained in reads with length greater than or equal to L. For ONT and PacBio datasets, Read length N50 is primarily a library and input-DNA integrity metric rather than a direct measure of sequencing accuracy.
- **Implementation details:** Compute the length of every read, sort reads in descending order by length, and calculate the cumulative sum of bases. The Read N50 is the read length at which the cumulative sum first reaches at least 50% of the total base yield. For ONT workflows this can be computed from FASTQ/BAM read lengths after basecalling, and should be reported together with total yield and read quality because a high N50 alone does not imply high accuracy. Ultra-long reads can increase N50, so the full read length distribution should also be reviewed.
- **Type:** Integer, base pairs (eg. 24500)
- **Functionally equivalent implementations:**
  - seqkit stats
  - NanoPlot
  - samtools stats
  - mosdepth
