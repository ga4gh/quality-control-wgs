# Percent bases mapped

- **ID:** bp_mapped_pct
- **Description:** Percentage of eligible sequenced query bases represented by CIGAR-mapped segments of primary alignments to the selected reference genome. (\\ The eligible-read population must be identical to that used for `pct_reads_mapped`), retaining mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads) in the denominator. Secondary and supplementary alignments are excluded, duplicate reads are included, and no minimum mapping quality (MAPQ) threshold is imposed. For paired-end short-read and discontiguous long-read datasets, query bases from each read end are evaluated individually; unsequenced intervening template spans between pairs or proximity segments do not contribute to this metric.
- **Implementation details:**  In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the percentage of mapped bases is computed using [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) on the declared input BAM/CRAM file. The input dataset comprises mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). The calculations counts query bases consumed by the `M`, `I`, `=` and `X` CIGAR operations, while soft-clipped and hard-clipped bases are not counted as mapped. Secondary (0x100) and supplementary (0x800) alignments are excluded using -F 2304, duplicate reads (0x400) are retained, and no minimum mapping quality (MAPQ) is applied. The metric is calculated from the summary numbers (SN) section as 100 × bases mapped (cigar) / total length. When the total length denominator is zero, N/A is reported. The same procedure is used for every sequencing read type.
- **Comments:**
  - [high quality reads](terminologies.md#high-quality-reads)
For short-read and discontiguous-long-read data, include instrument-filter-passing reads where such a filter exists. For contiguous-long-read data, include reads passing a fixed, platform-appropriate minimum per-read quality threshold. For ONT, use the Dorado or MinKNOW `qs` tag, which contains the per-read mean basecall Q-score, or its documented equivalent. For PacBio, use the `rq` tag, which contains predicted read accuracy, or its documented equivalent.
  - Record the samtools version, reference assembly, quality-inclusion profile, ONT `qs` or PacBio `rq` threshold where applicable, duplicate policy, mapping-quality policy, aligner, and basecaller or consensus-caller version.

```
# Generate summary statistics excluding secondary (256) and supplementary (2048) alignments
samtools stats -F 2304 input.bam > sample_stats.txt

# Extract mapped bases (CIGAR-derived) and total eligible sequenced base yield from the SN section
bases_mapped=$(grep "^SN[[:space:]]bases mapped (cigar):" sample_stats.txt | cut -f3)
total_bases=$(grep "^SN[[:space:]]total length:" sample_stats.txt | cut -f3)

# Compute percentage of bases mapped
awk -v mapped="$bases_mapped" -v total="$total_bases" 'BEGIN {
  if (total > 0) printf "%.4f\n", (mapped / total) * 100;
  else print "N/A"
}'
```
- **Type:** Float, 2 decimal precision (eg. 97.30)
- **Functionally equivalent implementations:**
  - None currently nominated; candidate implementations must reproduce the same eligible-read population, primary-alignment policy, CIGAR operations, clipping policy, duplicate policy, mapping-quality policy, numerator, and denominator before being considered equivalent.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.

