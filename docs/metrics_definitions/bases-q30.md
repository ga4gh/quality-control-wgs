
# Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** Total number of bases with a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)) derived from 
primary alignmnets and unmapped reads of [high quality reads](terminologies.md#high-quality-reads) in short-read or discontiguous-long-read sequencing data. Secondary and supplementary alignments are excluded. [Duplicated reads](terminologies.md#duplicated-reads) and [soft-clipped bases](terminologies.md#clipped-bases) are included, and no minimum [mapping quality](terminologies.md#mapping-quality) is imposed. For discontiguous long-read sequencing, only physically sequenced (observed) bases are counted; the unsequenced span of the inferred proximity molecule or template does not contribute to this metric.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, this metric is computed using [samtools stats](terminologies.md#samtools-stats), coupled with a custom parser that sums bases with [base quality score](terminologies.md#base-quality-score) 30 or greater from the First Fragment Quality (FFQ) and Last Fragment Quality (LFQ) tables. This implementation is identical for short-read and discontiguous-long-read data: evaluation is restricted to primary alignments and unmapped reads from [high quality reads](terminologies.md#high-quality-reads) (filtering out 0x100, (0x200?), and 0x800 via (-F 0x900?) -F 2816), while secondary and supplementary alignments are excluded. [Duplicate reads](terminologies.md#duplicated-reads) are retained, [soft-clipped bases](terminologies.md#clipped-bases) are included, and no [mapping quality](terminologies.md#mapping-quality) filter is applied.
For discontiguous-long-read data,  paired-end read records are processed identically to short reads, counting only observed sequenced bases and excluding the unsequenced span intervals between read ends.
- **Comments:** 
    - Use samtools stats and custom script alternate to GATK Picard’s CollectQualityYieldMetrics PF_Q30_BASES used in v1.0. which includes both mapped primary alignemnt and unmapped reads and duplicate reads. Exclude secondary, supplemetary reads.
    - open to both single-end (SE) and paired-end (PE), accounting Ultima single-end (SE) sequencing?
    - high quality reads - reads passing the sequencing instrument/vendor quality filter / instrument-filter-passing reads where such a filter exists; SAM flag 0x200 not set!
    - **Right to use only from primary alignments (0x904) or primary records including unmapped reads? and include/exclude duplicate reads?**
    - keep clipped bases to invoke unaligned bam/cram; explicitly soft-clipped only applicable to aligned bam/cram and our std implementation expect aligned bam/cram input.
    - For discontiguous-long-read sequencing, bases shall be computed and reported only at the read level or from reads, not at the template level.
    - If this metric is also applicable to discontiguous-long-read sequencing at the template level, the computation method shall be specified.
    - Technology-specific implementation details (e.g., BX tags, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition/Implementaion.
    ```
    samtools stats -F 0x900 in.bam > in.stats // exclude secondary and supplementary alignments while preserving all unmapped, mapped, duplicate reads, and soft-clipped bases. To exclude vendor quality check (QC-failed 0x200) use -F 2816 instead of -F 0x900.
    awk '$1 ~ /^[FL]FQ$/ { for (i = 33; i <= NF; i++) sum += $i } END { print "Total >=Q30 bases (PE):", sum }' stats.txt
    ```
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