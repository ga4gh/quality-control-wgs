# Percent autosomes with ≥N-fold coverage

- **ID:** pct_autosomes_n_fold_coverage
- **Description:** 
    - **Post-Alignment Data:**
   The percentage of bases within the defined [autosomal non gap](#autosomes-non-gap-regions) evaluation intervals of the selected reference genome that attain a sequencing depth of at least N-fold (specifically evaluated at thresholds such as > 5X, > 10X, > 15X, and > 20X).\
   Numerator: The total number of base positions within the evaluation intervals meeting or exceeding the specified depth threshold (N-fold).\
   Denominator: Fixed as the total base count across target autosomal evaluation intervals, fully accounting for positions with zero coverage (0X) rather than omitting unsequenced regions.
  
        - **Inclusions & Exclusions:**

            **Included:** Primary and supplementary alignments of eligible [high-quality reads](terminologies.md#high-quality-reads).\
            **Excluded::**  Unmapped records, secondary alignments, reads failing platform or vendor quality controls, [duplicate reads](terminologies.md#duplicated-reads), and clipped bases. (Note: Alignment files must have duplicate reads properly marked).\
            **Overlapping Segments:** Overlapping read segments (such as overlapping paired-end reads or overlapping primary/supplementary alignment segments from the same physical molecule) are counted only once per genomic position to prevent double-counting.\
            **Applicability:** Applies universally across short reads, contiguous long reads, and discontiguous long reads. Discontiguous long read only directly sequenced and aligned segments contribute to sequence depth; unsequenced intervening template spans between pairs or proximity segments do not count toward coverage.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, coverage thresholds are calculated using `mosdepth` evaluated strictly across the autosomal non-gap interval file (`--by autosomes_non_gap.bed`) with threshold cutoffs set via `--thresholds 5,10,15,20`. Alignments are filtered using `--flag 1796` to retain only primary, non-duplicate, supplementary records from [high-quality reads](terminologies.md#high-quality-reads). For short paired-end reads and discontiguous long reads, overlapping mate segments are resolved natively by mosdepth without double counting. 
For contiguous long reads, the fast BAM-parsing mode (`--fast-mode`) is enabled.
For contiguous long reads, overlapping supplementary reads in the bam/cram filtered/counted once using BAM parsing... .
Percentage values are derived directly from the generated `*.thresholds.bed.gz` summary row (`total`), dividing the base count at each threshold index by the total evaluated interval base count ($N_{\text{total}}$, including $0\times$ positions) multiplied by 100. If the total evaluated non-gap length is zero, N/A is reported for all thresholds.
- **Comments:**
high quality reads - reads passing the sequencing instrument/vendor quality filter / instrument-filter-passing reads where such a filter exists; SAM flag 0x200 not set!\
Contiguous Long Reads: Derived from non-duplicate primary alignments of high-quality reads that meet a platform-specific minimum per-read quality threshold (utilizing platform-standard read quality or predicted accuracy metrics).\
For ONT, read filtering uses the basecaller-generated per-read mean Q-score tag (qs) or its documented equivalent. For PacBio, read filtering uses the predicted accuracy tag (rq) or its documented equivalent. The specific threshold value, tag, and caller version must be recorded.
```
# ------------------------------------------------------------------------------
# 1. Short-Read & Discontiguous Long-Read Evaluation
# ------------------------------------------------------------------------------
mosdepth \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --thresholds 5,10,15,20 \
  --flag 1796 \
  --no-per-base \
  short_read_cov \
  input_short_read.bam

# Parse percentages from the 'total' row of the threshold file
# $2 contains the entire interval space (all bases, including 0x coverage)
read pct_5x pct_10x pct_15x < <(awk '
  $1 == "total" {
    total_bases = $2
    if (total_bases > 0) {
      printf "%.2f %.2f %.2f\n", ($4 / total_bases) * 100, ($5 / total_bases) * 100, ($6 / total_bases) * 100
    } else {
      print "N/A N/A N/A"
    }
  }' short_read_cov.thresholds.bed.gz)

printf "Autosomes >= 5x:  %s%%\n" "$pct_5x"
printf "Autosomes >= 10x: %s%%\n" "$pct_10x"
printf "Autosomes >= 15x: %s%%\n" "$pct_15x"

# ------------------------------------------------------------------------------
# 2. Contiguous Long-Read Evaluation (with -x)
# ------------------------------------------------------------------------------
mosdepth \
  -x \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --thresholds 5,10,15,20 \
  --flag 1796 \
  --no-per-base \
  long_read_cov \
  input_long_read.bam

read lr_pct_5x lr_pct_10x lr_pct_15x < <(awk '
  $1 == "total" {
    total_bases = $2
    if (total_bases > 0) {
      printf "%.2f %.2f %.2f\n", ($4 / total_bases) * 100, ($5 / total_bases) * 100, ($6 / total_bases) * 100
    } else {
      print "N/A N/A N/A"
    }
  }' long_read_cov.thresholds.bed.gz)

printf "Autosomes >= 5x:  %s%%\n" "$lr_pct_5x"
printf "Autosomes >= 10x: %s%%\n" "$lr_pct_10x"
printf "Autosomes >= 15x: %s%%\n" "$lr_pct_15x"

## https://gemini.google.com/app/6ec13625ee2270a0
```
- **Type:** Structured float percentages, 2 decimal precision (eg. pct_5x: 99.10; pct_10x: 98.20; pct_15x: 96.02; pct_20x: 95.10;)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO dnaalnqc](References.md#icgc-argo) for short-read or discontiguous-long-read data when it reproduces the reference implementation's evaluation regions, filtering, and all three depth thresholds.
  - [samtools depth](https://www.htslib.org/doc/samtools-depth.html), followed by counting evaluated positions with depth ≥5, ≥10, and ≥15 and division by the total evaluation-region length, when the same sequencing-read-type-specific filters, overlap policy, and zero-coverage denominator are used.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
