# Percent reads properly paired

- **ID:** pct_reads_properly_paired
- **Description:** The percentage of short paired-end sequencing [high quality](terminologies.md#high-quality-reads), properly paired reads, [primary alignments](terminologies.md#primary-alignments), to the selected reference genome / mapped on [GRCh38 assembly](terminologies.md#grch38-assembly). Secondary and supplementary alignments are excluded, while mapped and unmapped primary records are retained in the denominator. [Duplicated reads](terminologies.md#duplicated-reads) are included/excluded (and reads not passing platform/vendor quality controls (0x200) are excluded). No minimum [mapping quality](terminologies.md#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation it is computed using [samtools stats](References.md#samtools-stats), reporting the percentage of properly paired reads mapped on GRCh38 assembly. Duplicated reads are included/excluded. No mapping qualiy is applied.
- **Comments:** 
mapped on Reference genome instead of GRCh38/37
- use raw total sequences (filter sec and suppl, contain dup and qc-failed reads), samtools stats filter duplicates, qc-failed gives 'properly paired reads (filtered dup, qc-failed,sec and suppl). If need to filter qc-failed in 'raw total sequences' as well..
```
# 1. Denominator: Primary alignments (excludes 0x900) and NOT QC-failed (excludes 0x200)
# This keeping duplicates (0x400) included.
DENOMINATOR=$(samtools view -c -F 0x900 -F 0x200 input.bam)

# 2. Numerator: Must be properly paired (0x2), primary (excludes 0x900), 
# NOT duplicate (excludes 0x400), and NOT QC-failed (excludes 0x200). 
# Combined filter: -F 0xF00 (0x100+0x200+0x400+0x800)
NUMERATOR=$(samtools view -c -f 0x2 -F 0xF00 input.bam)

# 3. Calculate custom percentage
awk -v n="$NUMERATOR" -v d="$DENOMINATOR" 'BEGIN {printf "Custom Percentage: %.2f%%\n", (n/d)*100}'

```
- **Type:** Float 2 decimal precision (eg. 98.33)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Properly paired reads`
- **Sequencing read type:** short-read | discontiguous-long-read
- **c assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read); DRAGEN TruPath pipeline (Illumina proximity mapped reads); record exact version and parameters.
- **Associated basecaller:** N/A

