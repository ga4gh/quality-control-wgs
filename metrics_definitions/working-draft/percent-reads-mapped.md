# Percent reads mapped

- **ID:** pct_reads_mapped
- **Description:** 
    - **Post-Alignment Data:**
   The percentage of eligible [high quality reads](terminologies.md#high-quality-reads) represented by primary alignments mapped to the selected reference genome.\
   Numerator: Mapped primary records of high-quality reads.\
   Denominator: All primary records (both mapped and unmapped) of high-quality reads.
        - **Inclusions & Exclusions:**

            **Included:** Mapped and unmapped primary records. No minimum mapping quality (MAPQ) threshold is imposed. (Note: It is critical that alignment files have duplicate reads properly marked).\
            **Excluded from both Numerator and Denominator::** Secondary alignments, supplementary alignments, reads failing platform or vendor quality controls, and duplicate reads.

            For paired-end and discontiguous sequencing data, each read end is counted as an individual read rather than counting read pairs or inferred templates.

        **Inferred Template Percent Mapped (Discontiguous Long-Read)** (`inferred_template_pct_mapped`)
         The percentage of eligible inferred physical templates (molecules) derived from discontiguous long-read sequencing datasets that are successfully represented by primary alignments on the reference genome.\
        &ensp;Numerator: Inferred templates that have at least one qualifying mapped primary segment/record.\
        &ensp;Denominator: All eligible inferred templates (both mapped and unmapped).
        - **Inclusions & Exclusions:**

            **Included:** 
            Mapped and unmapped inferred templates. No minimum mapping quality (MAPQ) threshold is imposed. (Note: Alignment files must have duplicate templates/reads properly marked).\
            **Excluded from both Numerator and Denominator:** Secondary alignments, supplementary alignments from initiating new template counts, reads failing platform or vendor quality controls, and duplicate templates. Secondary and supplementary alignments from initiating new template length calculations.\
            \
            Chimeric segments or paired/multiplexed read segments originating from the same physical molecule are grouped and evaluated as a single template unit. A template is typically considered mapped if its constituent primary records yield a successful alignment.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the percentage of mapped reads is computed using [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) on the declared input BAM/CRAM file. The input dataset includes only mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). Alignments marked as secondary (0x100) and supplementary (0x800) are excluded, while duplicate reads (0x400) are retained, and no minimum mapping quality (MAPQ) threshold is imposed. The metric is calculated from the summary numbers (SN) section as 100 × reads mapped / raw total sequences. When the total sequence denominator is zero, N/A is reported. The same procedure is used for every sequencing read type.
OR use samtools flagstat 'primary mapped' percentage - mapped primary alignments against the total unique physical reads.(preferred)  equivalent to samtools stats's 'raw total sequences' and primary mapped count is equivalent to samtools stats -F 2304's 'reads mapped'.
OR 'raw total sequences' - 'reads unmapped' / 'raw total sequences' x 100
OR 'reads mapped' - 'non-primary alignments' - 'supplementary alignments' /'raw total sequences' x 100
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

