# Mean insert size

- **ID:** mean_insert_size
- **Description:** The mean insert size of short paired-end sequencing [high quality reads](terminologies.md#high-quality-reads), [primary alignments](terminologies.md#primary-alignments), mapped on [GRCh38 assembly](terminologies.md#grch38-assembly). [Duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation it is computed using [samtools stats](terminologies.md#samtools-stats), reporting the insert_size_average field. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 1 decimal precision (eg. 430.1)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: mean`

