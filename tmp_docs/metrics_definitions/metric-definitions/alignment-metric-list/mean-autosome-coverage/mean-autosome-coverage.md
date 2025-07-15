# Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The mean sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the genome-wide sequencing mean coverage of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [picard 2.27.0 CollectWgsMetrics](#Picard-CollectWgsMetrics), reporting the MEAN_COVERAGE field.
- **Type:** Float 2 decimal precision (eg. 30.94)
- **Functionally equivalent implementations:**
  - [ARGO dnaalnqc v1.1.0](#argo)

