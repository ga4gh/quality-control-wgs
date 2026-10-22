# Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** 
    - **Post-Alignment Data:**
   The arithmetic mean sequencing depth evaluated across all base positions within the defined [autosomal non gap](#autosomes-non-gap-regions) evaluation intervals of the selected reference genome.\
   Denominator: Fixed as the total base count across target autosomal intervals, fully accounting for positions with zero coverage (0X) rather than excluding unsequenced regions.
  
        - **Inclusions & Exclusions:**

            **Included:** Primary and supplementary alignments of eligible [high-quality reads](terminologies.md#high-quality-reads).\
            **Excluded::**  Unmapped records, secondary alignments, reads failing platform or vendor quality controls, [duplicate reads](terminologies.md#duplicated-reads), and clipped bases. (Note: Alignment files must have duplicate reads properly marked).\
            **Overlapping Segments:** Overlapping read segments (such as overlapping paired-end reads or overlapping primary/supplementary alignment segments from the same physical molecule) are counted only once per genomic position to prevent double-counting.\
            **Applicability:** Applies universally across short reads, contiguous long reads, and discontiguous long reads. Discontiguous long read only directly sequenced and aligned segments contribute to sequence depth; unsequenced intervening template spans between pairs or proximity segments do not count toward coverage.

  - **Implementation details: Working** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, mean autosome coverage is computed using `mosdepth` across the autosomal non-gap interval file (`--by autosomes_non_gap.bed`). Input records are restricted to primary and supplementary alignments of [high-quality reads](terminologies.md#high-quality-reads) by excluding unmapped, secondary, QC-failed, duplicates using --flag 1796. Overlapping mate-pair bases for short reads and discontiguous long reads are resolved natively by mosdepth. For contiguous long reads, overlapping supplementary reads in the bam/cram filtered/counted once using BAM parsing... . Mean coverage is parsed directly from the total_region entry (column 4) in the generated `*.mosdepth.summary.txt` report. If the evaluated non-gap interval file contains zero valid bases, N/A is reported. 

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
