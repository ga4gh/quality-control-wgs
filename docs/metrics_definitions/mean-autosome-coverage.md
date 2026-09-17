# Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The arithmetic mean sequencing depth evaluated across all base positions within the defined autosomal non-gap evaluation intervals of the selected reference genome. The denominator is fixed as the total base count across these target intervals, fully accounting for positions with zero coverage ($0\times$) rather than excluding unsequenced regions.

 Short reads and discontiguous long reads: Derived from non-duplicate primary alignments of [high-quality reads](terminologies.md#high-quality-reads). Alignments that are unmapped (0x4), secondary (0x100), QC-failed (0x200), duplicate (0x400), or supplementary (0x800) are excluded (-F 1796 (-F 3844?)). Overlapping paired-end read segments are counted only once per physical molecule. For discontiguous long reads, only directly sequenced and aligned segments contribute to depth; the inferred template distance between paired observations must not be counted as sequence coverage.

 Contiguous long reads: Derived from non-duplicate primary alignments of [high-quality reads](terminologies.md#high-quality-reads) reads meeting platform-specific per-read quality thresholds using read-level tags (`qs` for ONT, `rq` for PacBio) without per-base quality filtering. Unmapped, secondary, QC-failed, and duplicate records are excluded (-F 3844). The applied quality score threshold, caller version, and tag definition must be recorded.

## - **Implementation details:** In the [samtools depth v1.24](https://www.htslib.org/doc/samtools-depth.html) 
reference implementation, calculate depth only across the agreed, non-overlapping autosomal non-gap BED intervals.
  - For short-read and discontiguous-long-read data, use a minimum base quality of 20, minimum mapping quality of 20, exclusion flags `UNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY`, and paired-end overlap removal. A representative command is `samtools depth -b autosomal_non_gap.bed -q 20 -Q 20 -s -G UNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY aligned.bam`.
  - For contiguous-long-read data, first select reads using the agreed technology-specific per-read quality threshold. ONT BAM records may be selected using the `qs` tag and PacBio BAM records using the `rq` tag through `samtools view --expr`. Run `samtools depth` on the resulting alignments with a minimum base quality of 0, minimum mapping quality of 20, and the same exclusion flags. Do not apply paired-end overlap removal to unpaired contiguous reads.
  - Sum the reported depth values and divide by the total length of the BED intervals. Positions absent from the `samtools depth` output have zero depth; they contribute zero to the numerator but remain in the denominator. Record the samtools version, reference assembly, BED-file checksum, mapping-quality threshold, read- or base-quality profile, per-read quality threshold, aligner, and basecaller or consensus-caller version.

  - **Implementation details: Working** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, mean autosome coverage is computed using `mosdepth` across the autosomal non-gap interval file (`--by autosomes_non_gap.bed`). Input records are restricted to primary alignments of [high-quality reads](terminologies.md#high-quality-reads) by excluding unmapped, secondary, QC-failed, duplicates using --flag 1796. Overlapping mate-pair bases for short reads and discontiguous long reads are resolved natively by mosdepth. (For short reads exclude non-supplementary records?). For contiguous long reads, fast BAM parsing (--fast-mode) is enabled. Mean coverage is parsed directly from the total_region entry (column 4) in the generated `*.mosdepth.summary.txt` report. If the evaluated non-gap interval file contains zero valid bases, N/A is reported. 

- **Comments:**
```
# ------------------------------------------------------------------------------
# 1. Short-Read & Discontiguous Long-Read Evaluation
# ------------------------------------------------------------------------------
mosdepth \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --flag 3844 \
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
  --flag 3844 \
  --no-per-base \
  long_read_cov \
  input_long_read.bam

lr_mean_cov=$(awk '$1 == "total_region" { printf "%.2f\n", $4 }' long_read_cov.mosdepth.summary.txt)
if [ -z "$lr_mean_cov" ]; then lr_mean_cov="N/A"; fi

printf "Mean Autosome Coverage: %s\n" "$lr_mean_cov"
```
- **Type:** Float, 2 decimal precision (eg. 30.94)
- **Functionally equivalent implementations:**
  - [GATK Picard CollectWgsMetrics](https://gatk.broadinstitute.org/hc/en-us/articles/360036804671-CollectWgsMetrics-Picard), reporting `MEAN_COVERAGE`, for short-read and discontiguous-long-read profiles when the same evaluation regions, base-quality threshold, mapping-quality threshold, duplicate policy, primary-alignment policy, and overlap policy are used.
  - [mosdepth](https://github.com/brentp/mosdepth) for the contiguous-long-read profile after identical technology-specific per-read quality and alignment filtering. Mosdepth is not considered equivalent for the short-read or discontiguous-long-read profile unless base quality ≥20 filtering is reproduced and benchmarked.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
