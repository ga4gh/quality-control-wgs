# Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in short paired-end sequencing [high quality reads](terminologies.md#high-quality-reads), [primary alignments](terminologies.md#primary-alignments), achieving a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)). [Duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation it is computed using [GATK Picard’s CollectQualityYieldMetrics](terminologies.md#picard-collectqualityyieldmetrics), reporting the PF_Q30_BASES field. Only high quality bases from primary alignments are considered. No filter on duplicated reads, clipped bases or mapping qualiy is applied.
- **Type:** Integer (eg. 102984371235)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`
- **Sequencing read type:** short-read|long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:**
- **Associated aligner**
- **Associated basecaller**

# comments
- **Description:** The number of bases in [high quality reads](terminologies.md#high-quality-reads) from short paired-end sequencing and synthetic long-read sequencing (read level), considering only [primary alignments](terminologies.md#primary-alignments), with a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)). [Duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation this metric is computed using [samtools stats](terminologies.md#samtools-stats), reporting the number of bases achieving a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale). Only bases from high quality reads and primary alignments are considered. No filtering is applied to duplicated reads, clipped bases or mapping qualiy. 

For synthetic long-read sequencing, bases shall be computed and reported only at the read level or from reads, not at the template level.

If this metric is also applicable to synthetic long-read sequencing at the template level, the computation method shall be specified.

Technology-specific implementation details (e.g., BX tags, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition.
- **Type:** Integer
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`
- **Sequencing read type:** short-read|synthetic long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:**
- **Associated aligner:**
- **Associated basecaller:**
- **Associated variant caller:**