# Mean insert size

- **ID:** mean_insert_size
- **Description:** 
    - **Post-Alignment Data:**
   The mean insert size (fragment length between paired-end read ends) derived from the outermost aligned genomic coordinates of eligible paired-end [high quality reads](terminologies.md#high-quality-reads) with primary alignments mapped to the selected reference genome.\
        - **Inclusions & Exclusions:**

            **Included:** Primary alignments. No minimum mapping quality (MAPQ) threshold is imposed.\
            **Excluded:** [Duplicate reads](terminologies.md#duplicated-reads), reads failing platform or vendor quality controls, secondary alignments, supplementary alignments, unmapped reads and clipped bases (since calculations rely strictly on aligned genomic coordinates rather than full query lengths).

            Applicable to short paired-end sequencing datasets, evaluating proper pairing status based on platform- or aligner-defined orientation and distance criteria.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation it is computed using [samtools stats](References.md#samtools-stats), reporting the insert_size_average field. Duplicated reads are included. No mapping qualiy is applied.
- **Comments:** 
mapped on Reference genome instead of GRCh38/37
- **Type:** Float 1 decimal precision (eg. 430.1)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: mean`
- **Sequencing read type:** short-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read); DRAGEN TruPath pipeline (Illumina proximity mapped reads); record exact version and parameters.
- **Associated variant caller:**
- **Associated basecaller:** N/A