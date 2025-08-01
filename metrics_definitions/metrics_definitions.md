# Metric definitions

In this document, the QC of WGS workgroup intends to identify a set of key QC metrics and spell out their detailed definitions. Whilst doing so, we expect to encounter recurrent information fields that apply to many metrics. Those can then be used as the basis for standardised guidelines for reporting QC metrics.

## General notes

In terms of scope, the workgroup has agreed to focus on QC of germline WGS first. While all of the workgroup participants are working with short-read data at the moment, we wish to make the definitions general enough to be applicable to other technologies as well. The workgroup also acknowledges that there are multiple stages in the analysis pipeline at which one may want to perform QC (e.g. post-FASTQ generation, post-alignment, post-variant calling). For the first iteration of the guidelines, the workgroup has agreed to focus on metrics that can be obtained from a BAM/CRAM file. Thus, metrics such as contamination or variant counts remain out of scope at the moment.

## Controlled vocabulary

This section lists several example metrics in an attempt to capture which fields would be required to accurately describe how each metric has been calculated. When defining each metric, we attempt to align to the following general template:

- Id (mandatory): Metric identifier
- Description (mandatory): Metric description.
- Implementation details (mandatory): Tool and version used to calculate the metric & insights into the metric implementation, where possible.
- Functionally equivalent implementations (optional): A description of what constitute a valid alternative implementation producing values within an acceptable range of variation when compared to value(s) reported by the reference implementation when computing the metric i.e Validated equivalent implementations. We welcome the inclusion of candidate equivalent implementations

## Alignment metric list

### Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 30 or greater ([Phred scale](#phred-scale)). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation it is computed using [GATK Picard’s CollectQualityYieldMetrics](#picard-collectqualityyieldmetrics), reporting the PF_Q30_BASES field. Only high quality bases from primary alignments are considered. No filter on duplicated reads, clipped bases or mapping qualiy is applied.
- **Type:** Integer (eg. 102984371235)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`

### Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The mean sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the genome-wide sequencing mean coverage of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [GATK Picard’s CollectWgsMetrics](#picard-collectwgsmetrics), reporting the MEAN_COVERAGE field.
- **Type:** Float 2 decimal precision (eg. 30.94)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)

### Percent autosomes covered ≥ 15 X

- **ID:** pct_autosomes_15x
- **Description:** The percentage of bases attaining at least 15X sequencing coverage in short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the genome-wide sequencing coverage percentage of bases attaining at least 15X of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [GATK Picard’s CollectWgsMetrics](#picard-collectwgsmetrics), reporting the PCT_15X field.
- **Type:** Float 2 decimal precision (eg. 96.02)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)

### Percent reads mapped

- **ID:** pct_reads_mapped
- **Description:** The percentage of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation it is computed using [samtools stats](#samtools-stats), reporting the percentage of reads mapped on GRCh38 assembly. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 2 decimal precision (eg. 99.78)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Mapped reads`

### Percent reads properly paired

- **ID:** pct_reads_properly_paired
- **Description:** The percentage of short paired-end sequencing [high quality](#high-quality-reads), properly paired reads, [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation it is computed using [samtools stats](#samtools-stats), reporting the percentage of properly paired reads mapped on GRCh38 assembly. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 2 decimal precision (eg. 98.33)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Properly paired reads`

### Mean insert size

- **ID:** mean_insert_size
- **Description:** The mean insert size of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation it is computed using [samtools stats](#samtools-stats), reporting the insert_size_average field. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 1 decimal precision (eg. 430.1)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: mean`

### Insert size standard deviation

- **ID:** insert_size_std_deviation
- **Description:** The insert size standard deviation of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation it is computed using [samtools stats](#samtools-stats), reporting the insert_size_standard_deviation field. Duplicated reads are included. No mapping qualiy is applied.
- **Type:** Float 1 decimal precision (eg. 99.4)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)

### Genome coverage uniformity

- **ID:** mad_autosome_coverage
- **Description:** The median absolute deviation of sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the genome-wide sequencing median absolute deviation coverage of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [GATK Picard’s CollectWgsMetrics](#picard-collectwgsmetrics), reporting the MAD_COVERAGE field.
- **Type:** Integer (eg. 4)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)

### Cross contamination

- **ID:** cross_contamination_rate
- **Description:** Estimation of inter-sample contamination rate of short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). No minimum [mapping quality](#mapping-quality) is imposed. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, the estimation of inter-sample DNA contamination of short paired-end sequencing high quality, aligned sequence reads (BAM/CRAM) mapped on GRCh38 assembly with pre-calculated reference panel of [1000 Genome Project](#verifybamid-reference-panel) dataset from the VerifyBamID resource using [VerifyBamID2](#verifybamid2) with NumPC “4” (# of Principal Components used in estimation), the key information “FREEMIX” in “.selfSM” in the results indicates the estimated contamination level.
- **Type:** Float 4 decimal precision (eg. 0.0007)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO dnaalnqc](#icgc-argo)
  - [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Estimated sample contamination`

## Variant calling metric list

### Count: SNVs

- **ID:** count_snvs
- **Description:** The number of variant of type SNVs in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the number of variant of type SNVs in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v snps -f PASS`).
- **Type:** Integer (eg. 3906868)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Count: Insertions

- **ID:** count_insertions
- **Description:** The number of variant of type indels categorized as short insertions (less than 50bp) in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the number of variant of type indels categorized as insertions in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v indels -f PASS....INS`).
- **Type:** Integer (eg. 490511)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Count: Deletions

- **ID:** count_deletions
- **Description:** The number of variant type indels categorized as short deletions (less than 50bp) in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the number of variant of type indels categorized as deletions in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v indels -f PASS....DEL`).
- **Type:** Integer (eg. 444892)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Ratio: Insertions/Deletions

- **ID:** ratio_insertion_deletion
- **Description:** The ratio between number of short insertion and deletion (less than 50bp) in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the ratio of insertions and deletion in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v indels -f PASS....INS / bcftools view -H -v indels -f PASS....DEL`).
- **Type:** Float 2 decimal precision (eg. 1.13)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Ratio: Heterozygous/Homozygous (SNVs)

- **ID:** ratio_heterozygous_homzygous_snv
- **Description:** The ratio of heterozygous and homozygous variant of type SNVs in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the ratio of heterozygous and homozygous variant of type SNVs in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v snps -f PASS -g het / bcftools view -H -v snps -f PASS -g hom`).
- **Type:** Float 2 decimal precision (eg. 1.64)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Ratio: Heterozygous/Homozygous (indels)

- **ID:** ratio_heterozygous_homzygous_indel
- **Description:** The ratio of heterozygous and homozygous variant of type indels in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the ratio of heterozygous and homozygous variant of type indels in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v indels -f PASS -g het / bcftools view -H -v indels -f PASS -g hom`).
- **Type:** Float 2 decimal precision (eg. 2.02)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

### Ratio: Transitions/Transversions (ti/tv)

- **ID:** ratio_transitions_transversions_snv
- **Description:** The ratio of transitions and transversions of bi-allelic SNVs in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the ratio of transitions and transversions of bi-allelic SNVs in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality-variants](#high-quality-variants) by `bcftools stats`, (`bcftools stats -f PASS ... TSTV`).
- **Type:** Float 2 decimal precision (eg. 1.12)
- **Functionally equivalent implementations:**
  - [NPM sample qc](#npm-sample-qc)
  - [ICGC-ARGO vcfqc](#icgc-argo)

## Terminologies & Concepts

### High quality reads

High quality reads refers to sequencing instrument filter. For Illumina sequencer, leverages internal quality filtering procedure called [chastity filter](https://gatk.broadinstitute.org/hc/en-us/articles/360035890991-PF-reads-Illumina-chastity-filter). Reads that pass this filter are called "PF" for "pass-filter"

### Primary alignments

Primary alignments refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2 ”Terminologies and Concepts”, “Multiple mapping“ & section 1.4 “The alignment section: mandatory fields”, “FLAG: Combination of bitwise FLAGs”

### Base quality score

Base quality score refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4: “The alignment section: mandatory fields”, “QUAL”

### Mapping quality

Mapping qualityscore refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4 “The alignment section: mandatory fields”, “MAPQ: MAPping Quality”

### Phred scale

PHRED scale refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2 ”Terminologies and Concepts”, “Phred scale“

### Duplicated reads

Duplicated reads refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4: “The alignment section: mandatory fields”, “FLAG: Combination of bitwise FLAGs”

### Clipped bases

Clipped bases refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2: ”Terminologies and Concepts”, “Linear alignment“ & section 1.4 “The alignment section: mandatory fields”, “CIGAR: CIGAR string”

### Picard CollectQualityYieldMetrics

Picard CollectQualityYieldMetrics refers to [GATK documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360040507031-CollectQualityYieldMetrics-Picard-), section "CollectQualityYieldMetrics (Picard)" & [GATK specifications](https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectQualityYieldMetrics.QualityYieldMetrics)

### Picard CollectInsertSizeMetrics

Picard CollectInsertSizeMetrics refers to [GATK documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360037055772-CollectInsertSizeMetrics-Picard-), section "CollectInsertSizeMetrics (Picard)" & [GATK specifications](https://broadinstitute.github.io/picard/picard-metric-definitions.html#InsertSizeMetrics)

### Picard CollectWgsMetrics

Picard CollectWgsMetrics refers to [GATK documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360036804671-CollectWgsMetrics-Picard), section "CollectWgsMetrics (Picard)" & [GATK specifications](https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectWgsMetrics.WgsMetrics)

### Autosomes non gap regions

Autosomes non gap regions refers to the selection of chromosome 1 to 22, excluding chromosome X, Y, M and alternative contigs. In addition, gap regions as defined by UCSC are excluded. See [NPM-sample-qc documentation](https://github.com/c-BIG/NPM-sample-qc/blob/master/resources/README.rst)

### GRCh38 assembly

GRCh38 assembly refers to [1000genome-dragen-3.7.6 reference](https://1000genomes-dragen-3.7.6.s3.amazonaws.com/references/fasta/hg38.fa)

### Overlapping bases

Overlapping bases refers to [mosdepth documentation](https://github.com/brentp/mosdepth), section "how it works"

### High quality variants

High quality variants (`PASS FILTER`) refers to [VCF Format Specicification v4.2](https://samtools.github.io/hts-specs/VCFv4.2.pdf), section 1.4.1 "FILTER - filter status:" & [GATK generic hard-filtering recommendations](https://gatk.broadinstitute.org/hc/en-us/articles/360035890471-Hard-filtering-germline-short-variants)

## References

### ICGC ARGO

dnaalnqc: [https://github.com/icgc-argo-workflows/dnaalnqc](https://github.com/icgc-argo-workflows/dnaalnqc)

vcfqc: [https://github.com/icgc-argo-workflows/vcfqc](https://github.com/icgc-argo-workflows/vcfqc)

### DRAGEN

[Illumina DRAGEN Bio-IT Platform 3.7 User Guide](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/dragen-bio-it/Illumina-DRAGEN-Bio-IT-Platform-User-Guide-1000000141465-00.pdf)

### Bedtools subtract

[https://bedtools.readthedocs.io/en/latest/content/tools/subtract.html](https://bedtools.readthedocs.io/en/latest/content/tools/subtract.html)

### NPM-sample-qc
[https://github.com/c-BIG/NPM-sample-qc](https://github.com/c-BIG/NPM-sample-qc)

### Samtools stats

[http://www.htslib.org/doc/samtools-stats.html](http://www.htslib.org/doc/samtools-stats.html)

### Samtools view

[http://www.htslib.org/doc/samtools-view.html](http://www.htslib.org/doc/samtools-view.html)

### VCF Format

[https://samtools.github.io/hts-specs/VCFv4.2.pdf]

### VerifyBamID2

[https://github.com/Griffan/VerifyBamID](https://github.com/Griffan/VerifyBamID)

### VerifyBamID reference panel

Pre-calculated reference panel of 1000 Genome Project phase 3 dataset: 100,000 sites mapped on GRCh38

- UDPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.UD](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.UD)
- BedPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.bed](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.bed)
- MeanPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.mu](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.mu)
