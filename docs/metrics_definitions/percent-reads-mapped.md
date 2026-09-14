# Percent reads mapped

- **ID:** pct_reads_mapped
- **Description:** The percentage of eligible [high quality reads](terminologies.md#high-quality-reads) represented by primary alignments to the selected reference genome. (//The eligible-read population must be identical to that used for `bp_mapped_pct`). Secondary and supplementary alignments are excluded, while mapped and unmapped primary records are retained in the denominator. Duplicate reads are excluded/included?, and no minimum mapping quality (MAPQ) is imposed. For paired short-read or discontiguous-long-read data, each read end is counted as an individual read rather than counting read pairs or inferred templates.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the percentage of mapped reads is computed using [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) on the declared input BAM/CRAM file. The input dataset includes only mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). Alignments marked as secondary (0x100) and supplementary (0x800) are excluded, while duplicate reads (0x400) are retained, and no minimum mapping quality (MAPQ) threshold is imposed. The metric is calculated from the summary numbers (SN) section as 100 × reads mapped / raw total sequences. When the total sequence denominator is zero, N/A is reported. The same procedure is used for every sequencing read type.
- **Comments:**
  - For short-read and discontiguous-long-read data, include [high quality reads](terminologies.md#high-quality-reads) defined as are instrument-filter-passing reads where such a filter exists. For contiguous-long-read data, include [high quality reads](terminologies.md#high-quality-reads) reads are defined those passing a fixed, platform-appropriate minimum per-read quality threshold. For ONT, use the Dorado or MinKNOW `qs` tag (mean basecall Q-score) or its documented equivalent. For PacBio, use the `rq` tag (predicted read accuracy) or its documented equivalent.
  - Record the samtools version, reference assembly, quality-inclusion profile, ONT `qs` or PacBio `rq` threshold where applicable, duplicate policy, mapping-quality policy, aligner, and basecaller or consensus-caller version.
```
  # Generate summary statistics excluding secondary (256) and supplementary (2048) alignments
samtools stats -F 2304 input.bam > sample_stats.txt

# Extract the mapped and total primary read counts from the SN section
reads_mapped=$(grep "^SN[[:space:]]reads mapped:" sample_stats.txt | cut -f3)
total_reads=$(grep "^SN[[:space:]]raw total sequences:" sample_stats.txt | cut -f3)

# Compute percentage of reads mapped
awk -v mapped="$reads_mapped" -v total="$total_reads" 'BEGIN {
  if (total > 0) printf "%.4f\n", (mapped / total) * 100;
  else print "N/A"
}'
```
- **Type:** Float, 2 decimal precision (eg. 99.78)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO dnaalnqc](References.md#icgc-argo), when it reproduces the same eligible-read population, primary-alignment policy, duplicate policy, mapping-quality policy, numerator, and denominator.
  - [DRAGEN v3.7.6](References.md#dragen), reporting `MAPPING/ALIGNING SUMMARY,,Mapped reads`, for sequencing profiles in which equivalence to the reference implementation has been benchmarked using the same input-read population.
  - [samtools flagstat](https://www.htslib.org/doc/samtools-flagstat.html), after identical upstream read-quality and primary-record filtering and with the same mapped-read numerator and eligible-read denominator.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.

