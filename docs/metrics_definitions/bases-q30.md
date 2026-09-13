
# Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** Total number of bases with a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)) from primary alignments of [high quality reads](terminologies.md#high-quality-reads) in short-read or discontiguous long-read paired-end sequencing data. [Duplicated reads](terminologies.md#duplicated-reads) and [soft-clipped bases](terminologies.md#clipped-bases) are included, and no minimum [mapping quality](terminologies.md#mapping-quality) is imposed. For discontiguous long-read sequencing, only physically sequenced (observed) bases are counted; the unsequenced span of the inferred proximity molecule or template does not contribute to this metric.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, this metric is computed using [samtools stats](terminologies.md#samtools-stats), coupled with a custom parser that sums bases with [base quality score](terminologies.md#base-quality-score) 30 or greater from the First Fragment Quality (FFQ) and Last Fragment Quality (LFQ) tables. This implementation is identical for short-read and discontiguous-long-read data:
  -  Only primary alignments of [high quality reads](terminologies.md#high-quality-reads) are evaluated;secondary and supplementary alignments are excluded.
  - No filtering of [Duplicated reads](terminologies.md#duplicated-reads) is performed, [soft-clipped bases](terminologies.md#clipped-bases) are retained, and no minimum [mapping quality](terminologies.md#mapping-quality) threshold is applied.
  - For discontiguous-long-read data,  paired-end read records are processed identically to short reads, counting only observed sequenced bases and excluding the unsequenced span intervals between read ends.
- **Comments:** Use samtools stats and custom script alternate to GATK Picard’s CollectQualityYieldMetrics PF_Q30_BASES used in v1.0.
#open to both SE and PE accounting Ultima sequencing?
#high quality reads (reads passing the sequencing instrument/vendor quality filter; SAM flag 0x200 not set)
#keep clipped bases to invoke unaligned bam/cram; explicitly soft-clipped only applicable to aligned bam/cram and our std expect aligned bam/cram.
For discontiguous-long-read sequencing, bases shall be computed and reported only at the read level or from reads, not at the template level.
If this metric is also applicable to discontiguous-long-read sequencing at the template level, the computation method shall be specified.
Technology-specific implementation details (e.g., BX tags, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition/Implementaion.
- **Type:** Integer (eg. 102984371235)
- **Functionally equivalent implementations:**
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`
- **Sequencing read type:** short-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN aligner (Illumina short-read) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** 