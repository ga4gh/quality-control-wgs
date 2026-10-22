# Percent bases mapped

- **ID:** bp_mapped_pct
- **Description:** 
    - **Post-Alignment Data:**
   The percentage of sequenced query bases from eligible [high quality reads](terminologies.md#high-quality-reads) that align to the selected reference genome.\
   Numerator: Unique query base positions aligned or inserted (such as matches, mismatches, and insertions) across primary and supplementary records, with overlapping query intervals merged to prevent double-counting.\
   Denominator: The total sequenced query length across both mapped and unmapped reads.
        - **Inclusions & Exclusions:**

            **Included:** No minimum mapping quality (MAPQ) threshold is imposed.\
            **Excluded from Denominator::**  [Duplicate reads](terminologies.md#duplicated-reads), Reads failing platform or vendor quality controls.\
            **Excluded from Numerator Only:** [Duplicate reads](terminologies.md#duplicated-reads), secondary alignments, and hard-clipped bases.

            For paired-end and discontiguous sequencing data, query bases from each read end are evaluated individually; unsequenced intervening template spans do not contribute to this metric.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the percentage of mapped bases is computed using [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) on the declared input BAM/CRAM file. The input dataset comprises mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads), "with vendor QC failures (0x200) and secondary alignments (0x100) filtered out" / OR "(vendor QC-failed reads 0x200 are excluded prior to analysis)". The calculation counts query bases consumed by M, I, =, and X CIGAR operations, while soft-clipped (S) and hard-clipped (H) bases are excluded. (Secondary alignments (0x100) are filtered out,) Duplicate reads (0x400) are retained, and no minimum mapping quality (MAPQ) is enforced. The metric is computed from the Summary Numbers (SN) section as 100 × bases mapped (cigar) / total length. When the total length denominator is zero, N/A is reported. The same procedure is used for every sequencing read type./ This procedure is applied independently to each sequencing read type.

In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the percentage of mapped bases is computed from the declared input BAM/CRAM file. The input dataset comprises mapped and unmapped primary records as well as supplementary alignments of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). Reads failing vendor quality checks (0x200) and secondary alignments (0x100) are excluded from both the numerator and the denominator, while duplicate reads (0x400) are retained and no minimum mapping quality (MAPQ) threshold is enforced.

Numerator calculation: For each read, query coordinates $[q_{\text{start}}, q_{\text{end}})$ corresponding to aligned or inserted CIGAR operations (M, I, =, and X) are extracted across its primary and supplementary records. Soft-clipped (S) and hard-clipped (H) bases are excluded. Overlapping query intervals between split or chimeric alignments are merged to ensure each sequenced base position is counted at most once.

Denominator calculation: The total query length is accumulated from the sequence length (length(SEQ)) of all passing primary records (both mapped and unmapped).

The final metric is calculated as: $$\text{Mapped Base Percentage} = 100 \times \frac{\sum \text{merged aligned query bases}}{\sum \text{primary query length}}$$

When the denominator is zero, N/A is reported. The same procedure is used for every sequencing read type. / This procedure is applied independently to each sequencing read type.
- **Comments:**
  - [high quality reads](terminologies.md#high-quality-reads)
For short-read and discontiguous-long-read data, include instrument-filter-passing reads where such a filter exists. For contiguous-long-read data, include reads passing a fixed, platform-appropriate minimum per-read quality threshold. For ONT, use the Dorado or MinKNOW `qs` tag, which contains the per-read mean basecall Q-score, or its documented equivalent. For PacBio, use the `rq` tag, which contains predicted read accuracy, or its documented equivalent.
  - Record the samtools version, reference assembly, quality-inclusion profile, ONT `qs` or PacBio `rq` threshold where applicable, duplicate policy, mapping-quality policy, aligner, and basecaller or consensus-caller version.

```
# Generate summary statistics excluding secondary (256) alignments samtools stats -F 2304 input.bam > sample_stats.txt

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