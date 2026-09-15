# Read N50

- **ID:** read_n50
- **Description:** The length-weighted median read length in a sequencing dataset. It is defined as the read length L such that 50% of the total sequenced bases are contained in reads with length greater than or equal to L. For short-read and discontiguous-long-read paired-end datasets, each read end is treated as an individual read rather than using the read-pair or inferred template length. For short-read datasets, Read N50 can describe the observed read-length distribution after optional trimming or clipping. For contiguous-long-read datasets, it is primarily a measure of library construction and input-DNA integrity rather than sequencing accuracy.
- **Implementation details:** In the [SeqKit v2.13.0](https://bioinf.shenwei.me/seqkit/usage/) reference implementation, run `seqkit stats --all --tabular reads.fastq.gz` on the complete logical sample and report the `N50` column. Alignment is not required. Use the read sequences present in the declared input dataset; the calculation must state whether adapter trimming, quality trimming, clipping, instrument filtering, or platform-specific pass/fail filtering was performed before the metric was calculated. Do not downsample. If a sample spans multiple files, combine all included read lengths or concatenate the files losslessly before calculation; never average per-file N50 values. For paired short-read or discontiguous-long-read data, include the eligible reads from both mates in one sample-level calculation and count each mate separately.
- **Type:** Integer, base pairs (eg. 150)
- **Functionally equivalent implementations:**
  - [SeqFu `stats`](https://telatin.github.io/seqfu2/tools/stats.html), using the identical read set and reporting N50
  - [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) read-length distribution with exact N50 post-processing, when BAM or CRAM contains the same read population and each read is counted once
  - [NanoPlot](https://github.com/wdecoster/NanoPlot), without downsampling, for contiguous-long-read data
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** N/A
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** N/A
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
