# Percent autosomes with ≥N-fold coverage

- **ID:** pct_autosomes_n_fold_coverage
- **Description:** The percentages of bases in the defined autosomal non-gap evaluation regions of the selected reference genome attaining sequencing depth ≥5×, ≥10×, and ≥15× after applying sequencing-read-type-specific inclusion criteria. The denominator is fixed as the total base count of the evaluation intervals, ensuring that unsequenced and zero-coverage positions ($0\times$) are fully retained rather than omitted.

Short reads and discontiguous-long reads: Coverage is derived from non-duplicate primary alignments of [high-quality reads](terminologies.md#high-quality-reads). Unmapped (0x4), secondary (0x100), QC-failed (0x200), duplicate (0x400)(, and supplementary (0x800) alignments?) are excluded (-F 1796 (-F 3844?)). Overlapping paired-end segments are counted only once per physical molecule. For discontiguous long reads, only directly sequenced and mapped bases of read pairs contribute to coverage; inferred intervening template spans must not be counted as continuous sequence coverage. It is critical that the (BAM/CRAM) alignment files be readily marked for duplicated reads.

Contiguous-long reads: Coverage is derived from non-duplicate primary alignments of high-quality reads passing a fixed, platform-specific minimum per-read quality threshold. For ONT, read filtering uses the basecaller-generated per-read mean Q-score tag (qs) or its documented equivalent. For PacBio, read filtering uses the predicted accuracy tag (rq) or its documented equivalent. No individual-base quality filtering is applied. The specific threshold value, tag, and caller version must be recorded.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, coverage thresholds are calculated using `mosdepth` evaluated strictly across the autosomal non-gap interval file (`--by autosomes_non_gap.bed`) with threshold cutoffs set via `--thresholds 5,10,15`. Alignments are filtered using `--flag 1796` (3844?) to retain only primary, non-duplicate, (non-supplementary?) records from [high-quality reads](terminologies.md#high-quality-reads). For short paired-end reads and discontiguous long reads, overlapping mate segments are resolved natively by mosdepth without double counting(, and exclude non-supplementary records?). For contiguous long reads, the fast BAM-parsing mode (`--fast-mode`) is enabled. Percentage values are derived directly from the generated `*.thresholds.bed.gz` summary row (`total`), dividing the base count at each threshold index by the total evaluated interval base count ($N_{\text{total}}$, including $0\times$ positions) multiplied by 100. If the total evaluated non-gap length is zero, N/A is reported for all thresholds.
- **Comments:**
```
# ------------------------------------------------------------------------------
# 1. Short-Read & Discontiguous Long-Read Evaluation
# ------------------------------------------------------------------------------
mosdepth \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --thresholds 5,10,15 \
  --flag 3844 \
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
  --thresholds 5,10,15 \
  --flag 3844 \
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
```
- **Type:** Structured float percentages, 2 decimal precision (eg. pct_5x: 99.10; pct_10x: 98.20; pct_15x: 96.02)
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
