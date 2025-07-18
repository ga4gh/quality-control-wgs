# Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in short paired-end sequencing [high quality reads](terminologies.md#high-quality-reads), [primary alignments](terminologies.md#primary-alignments), achieving a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)). [Duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation it is computed using [GATK Picard’s CollectQualityYieldMetrics](terminologies.md#picard-collectqualityyieldmetrics), reporting the PF_Q30_BASES field. Only high quality bases from primary alignments are considered. No filter on duplicated reads, clipped bases or mapping qualiy is applied.
- **Type:** Integer (eg. 102984371235)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`