# Cross contamination

- **ID:** cross_contamination_rate
- **Description:** Estimation of inter-sample contamination rate of short paired-end sequencing [high quality](terminologies.md#high-quality-reads), [non duplicated](terminologies.md#duplicated-reads) reads, [primary alignments](terminologies.md#primary-alignments), mapped on [GRCh38 assembly](terminologies.md#grch38-assembly). No minimum [mapping quality](terminologies.md#mapping-quality) is imposed. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](terminologies.md#duplicated-reads) and [clipped bases](terminologies.md#clipped-bases).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, the estimation of inter-sample DNA contamination of short paired-end sequencing high quality, aligned sequence reads (BAM/CRAM) mapped on GRCh38 assembly with pre-calculated reference panel of [1000 Genome Project](terminologies.md#verifybamid-reference-panel) dataset from the VerifyBamID resource using [VerifyBamID2](terminologies.md#verifybamid2) with NumPC “4” (terminologies.md# of Principal Components used in estimation), the key information “FREEMIX” in “.selfSM” in the results indicates the estimated contamination level.
- **Type:** Float 4 decimal precision (eg. 0.0007)
- **Functionally equivalent implementations:**
    - [ARGO dnaalnqc v1.1.0](terminologies.md#argo)
    - [DRAGEN v3.7.6](terminologies.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Estimated sample contamination`

