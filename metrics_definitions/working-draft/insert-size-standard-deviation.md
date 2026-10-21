# Insert size standard deviation

- **ID:** insert_size_std_deviation
- **Description:** 
    - **Post-Alignment Data:**
   The standard deviation of the insert size (fragment length variability between paired-end read ends) derived from the outermost aligned genomic coordinates of eligible paired-end [high quality reads](terminologies.md#high-quality-reads) with primary alignments mapped to the selected reference genome.\
        - **Inclusions & Exclusions:**

            **Included:** Primary alignments. No minimum mapping quality (MAPQ) threshold is imposed.\
            **Excluded:** [Duplicate reads](terminologies.md#duplicated-reads), reads failing platform or vendor quality controls, secondary alignments, supplementary alignments, unmapped reads and clipped bases (since calculations rely strictly on aligned genomic coordinates rather than full query lengths).

            Applicable to short paired-end sequencing datasets, measuring the dispersion and variability of physical fragment lengths across the paired read ends on the reference genome.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation it is computed using [samtools stats](References.md#samtools-stats), reporting the insert_size_standard_deviation field. Duplicated reads are included. No mapping qualiy is applied.
- **Data Type:** Float 1 decimal precision (eg. 99.4)
- **Comments:** 
mapped on Reference genome instead of GRCh38/37
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
- **Sequencing read type:** short-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read); DRAGEN TruPath pipeline (Illumina proximity mapped reads); record exact version and parameters.
- **Associated variant caller:**
- **Associated basecaller:** N/A