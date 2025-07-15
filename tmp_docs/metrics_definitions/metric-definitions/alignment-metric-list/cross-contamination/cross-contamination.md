# Cross contamination

- **ID:** cross_contamination_rate
- **Description:** Estimation of inter-sample contamination rate of short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). No minimum [mapping quality](#mapping-quality) is imposed. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the estimation of inter-sample DNA contamination of short paired-end sequencing high quality, aligned sequence reads (BAM/CRAM) mapped on GRCh38 assembly with pre-calculated reference panel of [1000 Genome Project](#verifybamid-reference-panel) dataset from the VerifyBamID resource using [VerifyBamID2](#verifybamid2) with NumPC “4” (# of Principal Components used in estimation), the key information “FREEMIX” in “.selfSM” in the results indicates the estimated contamination level.
- **Type:** Float 4 decimal precision (eg. 0.0007)
- **Functionally equivalent implementations:**
  - [ARGO dnaalnqc v1.1.0](#argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Estimated sample contamination`

