# Percent autosomes covered ≥ 15 X

- **ID:** pct_autosomes_15x
- **Description:** The percentage of bases attaining at least 15X sequencing coverage in short paired-end sequencing [high quality](terminologies.md#high-quality-reads), [non duplicated](terminologies.md#duplicated-reads) reads, [primary alignments](terminologies.md#primary-alignments), achieving a [base quality score](terminologies.md#base-quality-score) of 20 or greater ([Phred scale](terminologies.md#phred-scale)) and [mapping quality](terminologies.md#mapping-quality) of 20 or greater, in [autosomes non gap regions](terminologies.md#autosomes-non-gap-regions) of [GRCh38 assembly](terminologies.md#grch38-assembly). [Overlapping bases](terminologies.md#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](terminologies.md#duplicated-reads).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, the genome-wide sequencing coverage percentage of bases attaining at least 15X of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](terminologies.md#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [GATK Picard’s CollectWgsMetrics](terminologies.md#picard-collectwgsmetrics), reporting the PCT_15X field.
- **Type:** Float 2 decimal precision (eg. 96.02)
- **Functionally equivalent implementations:**
    - [ARGO dnaalnqc v1.1.0](terminologies.md#argo)

