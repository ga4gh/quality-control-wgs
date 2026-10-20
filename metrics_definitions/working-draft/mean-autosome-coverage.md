# Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The arithmetic mean sequencing depth evaluated across all base positions within the defined autosomal non-gap evaluation intervals of the selected reference genome. The denominator is fixed as the total base count across these target intervals, fully accounting for positions with zero coverage ($0\times$) rather than excluding unsequenced regions.

 Short reads, discontiguous long reads and Contiguous long reads: Derived from non-duplicate primary and supplementraty alignments of [high-quality reads](terminologies.md#high-quality-reads). Alignments that are unmapped (0x4), secondary (0x100), QC-failed (0x200), duplicate (0x400) are excluded (-F 1796). Clipped bases are excluded. Overlapping read segments are counted only once per physical molecule. For discontiguous long reads, only directly sequenced and aligned segments contribute to depth; the inferred template distance between paired observations must not be counted as sequence coverage. It is critical that the (BAM/CRAM) alignment files be readily marked for duplicated reads.

  - **Implementation details: Working** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, mean autosome coverage is computed using `mosdepth` across the autosomal non-gap interval file (`--by autosomes_non_gap.bed`). Input records are restricted to primary and supplementary alignments of [high-quality reads](terminologies.md#high-quality-reads) by excluding unmapped, secondary, QC-failed, duplicates using --flag 1796. Overlapping mate-pair bases for short reads and discontiguous long reads are resolved natively by mosdepth. For contiguous long reads, overlapping supplementary reads in the bam/cram filtered/counted once using BAM parsing... . Mean coverage is parsed directly from the total_region entry (column 4) in the generated `*.mosdepth.summary.txt` report. If the evaluated non-gap interval file contains zero valid bases, N/A is reported. 

## Fast Mode (--fast-mode): Even when using --fast-mode (which skips detailed internal CIGAR micro-parsing for speed), mosdepth relies on the standard mapped boundaries from the BAM/CRAM record rather than including unmapped soft-clipped tails.

- **Comments:**
```
# ------------------------------------------------------------------------------
# 1. Short-Read & Discontiguous Long-Read Evaluation
# ------------------------------------------------------------------------------
mosdepth \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --flag 1796 \
  --no-per-base \
  short_read_cov \
  input_short_read.bam

# Extract mean depth from the summary report (column 4 of total_region)
mean_cov=$(awk '$1 == "total_region" { printf "%.2f\n", $4 }' short_read_cov.mosdepth.summary.txt)
if [ -z "$mean_cov" ]; then mean_cov="N/A"; fi

printf "Mean Autosome Coverage: %s\n" "$mean_cov"

# ------------------------------------------------------------------------------
# 2. Contiguous Long-Read Evaluation (with -x)
# ------------------------------------------------------------------------------
mosdepth \
  --fast-mode \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --flag 1796 / 3844 \
  --no-per-base \
  long_read_cov \
  input_long_read.bam

lr_mean_cov=$(awk '$1 == "total_region" { printf "%.2f\n", $4 }' long_read_cov.mosdepth.summary.txt)
if [ -z "$lr_mean_cov" ]; then lr_mean_cov="N/A"; fi

printf "Mean Autosome Coverage: %s\n" "$lr_mean_cov"
```
- **Type:** Float, 2 decimal precision (eg. 30.94)
- **Functionally equivalent implementations:**
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
