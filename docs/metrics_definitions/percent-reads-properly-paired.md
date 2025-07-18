# Percent reads properly paired

- **ID:** pct_reads_properly_paired
- **Description:** The percentage of short paired-end sequencing [high quality](terminologies.md#high-quality-reads), properly paired reads, [primary alignments](terminologies.md#primary-alignments), mapped on [GRCh38 assembly](terminologies.md#grch38-assembly). [Duplicated reads](terminologies.md#duplicated-reads) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation it is computed using [samtools stats](terminologies.md#samtools-stats), reporting the percentage of properly paired reads mapped on GRCh38 assembly. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 2 decimal precision (eg. 98.33)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ARGO dnaalnqc](References.md#argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Properly paired reads`

