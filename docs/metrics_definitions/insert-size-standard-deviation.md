# Insert size standard deviation

- **ID:** insert_size_std_deviation
- **Description:** The insert size standard deviation of short paired-end sequencing [high quality reads](terminologies.md#high-quality-reads), [primary alignments](terminologies.md#primary-alignments), mapped on [GRCh38 assembly](terminologies.md#grch38-assembly). [Duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases) are included. No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation it is computed using [samtools stats](terminologies.md#samtools-stats), reporting the insert_size_standard_deviation field. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 1 decimal precision (eg. 99.4)
- **Functionally equivalent implementations:**
    - [ARGO dnaalnqc v1.1.0](terminologies.md#argo)

