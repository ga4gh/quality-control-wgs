# Metric definitions

In this document, the QC of WGS workgroup intends to identify a set of key QC metrics and spell out their detailed definitions. Whilst doing so, we expect to encounter recurrent information fields that apply to many metrics. Those can then be used as the basis for standardised guidelines for reporting QC metrics.

## General notes

- The document is just a first draft to capture conversations from our regular meetings. It provides some templated sections as a guide, but those may not be exhaustive. As such, feel free to make as many changes as needed; we can always recover previous versions of the document using the file history.
- In terms of scope, the workgroup has agreed to focus on QC of germline WGS first. While all of the workgroup participants are working with short-read data at the moment, we wish to make the definitions general enough to be applicable to other technologies as well. The workgroup also acknowledges that there are multiple stages in the analysis pipeline at which one may want to perform QC (e.g. post-FASTQ generation, post-alignment, post-variant calling).

## Controlled vocabulary

This section lists several example metrics in an attempt to capture which fields would be required to accurately describe how each metric has been calculated. When defining each metric, we attempt to align to the following general template:

- Id (mandatory): Metric identifier
- Description (mandatory): Metric description.
- Implementation details (mandatory): Tool and version used to calculate the metric & insights into the metric implementation, where possible.
- Functionally equivalent implementations (optional): A description of what constitute a valid alternative implementation producing values within an acceptable range of variation when compared to value(s) reported by the reference implementation when computing the metric i.e Validated equivalent implementations. We welcome the inclusion of candidate equivalent implementations

## Post Alignment Metric list

### Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 30 or greater ([Phred scale](#phred-scale)). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [GATK Picard’s CollectQualityYieldMetrics](#picard-collectqualityyieldmetrics), reporting the PF_Q30_BASES field. Only high quality bases from primary alignments are considered. No filter on duplicated reads, clipped bases or mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`

### Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The mean sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing mean coverage of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [picard 2.27.0 CollectWgsMetrics](#Picard-CollectWgsMetrics).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].wgs_coverage_metrics.csv, key name: `COVERAGE SUMMARY,,Average autosomal coverage over genome`
  - [Candidate] [argodnaalnqc vx.x.x](#ARGO). Extracted from [sample-id].metrics.json, key name: `mean_autosome_coverage`

### Percent autosomes covered ≥ 15 X

- **ID:** pct_autosomes_15x
- **Description:** The percentage of bases attaining at least 15X sequencing coverage in short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage percentage of bases attaining at least 15X of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [picard 2.27.0 CollectWgsMetrics](#Picard-CollectWgsMetrics).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [argodnaalnqc vx.x.x](#ARGO). Extracted from [sample-id].metrics.json, key name: `pct_autosomes_15x`

### Percent reads mapped

- **ID:** pct_reads_mapped
- **Description:** The percentage of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [samtools stats](#samtools-stats), reporting the percentage of reads mapped on GRCh38 assembly. Duplicated reads are included. No mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Mapped reads`

### Percent reads properly paired

- **ID:** pct_reads_properly_paired
- **Description:** The percentage of short paired-end sequencing [high quality](#high-quality-reads), properly paired reads, [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [samtools stats](#samtools-stats), reporting the percentage of properly paired reads mapped on GRCh38 assembly. Duplicated reads are included. No mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Properly paired reads`

### Mean insert size

- **ID:** mean_insert_size
- **Description:** The mean insert size of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [samtools stats](#samtools-stats), reporting the insert_size_average field. Duplicated reads are included. No mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: mean`

### Insert size standard deviation

- **ID:** insert_size_std_deviation
- **Description:** The insert size standard deviation of short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [samtools stats](#samtools-stats), reporting the insert_size_standard_deviation field. Duplicated reads are included. No mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: standard deviation`

### Genome coverage uniformity

- **ID:** mad_autosome_coverage
- **Description:** The median absolute deviation of sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 20 or greater ([Phred scale](#phred-scale)) and [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing median absolute deviation coverage of the non gap regions of GRCh38 assembly, autosomes only using [bedtools subtract](#bedtools-subtract), non duplicated reads, non overlapping bases, primary alignments, achieving a base quality of 20 or greater and mapping quality of 20 or greater is derived from [picard 2.27.0 CollectWgsMetrics](#Picard-CollectWgsMetrics).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [argodnaalnqc vx.x.x](#ARGO). Extracted from [sample-id].metrics.json, key name: `mad_autosome_coverage`

### Cross contamination

- **ID:** cross_contamination_rate
- **Description:** Estimation of inter-sample contamination rate of short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), mapped on [GRCh38 assembly](#grch38-assembly). No minimum [mapping quality](#mapping-quality) is imposed. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** The estimation of inter-sample DNA contamination of short paired-end sequencing high quality, aligned sequence reads (BAM/CRAM) mapped on GRCh38 assembly with pre-calculated reference panel of [1000 Genome Project](#verifybamid-reference-panel) dataset from the VerifyBamID resource using [VerifyBamID2](#verifybamid2) with NumPC “4” (# of Principal Components used in estimation), the key information “FREEMIX” in “.selfSM” in the results indicates the estimated contamination level.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark resources
 - [Candidate] All Of Us QC Report: Q2 2022 release. QC key name : key information `FREEMIX` in “.selfSM”


## Post Variant Calling Metric list

### Count: SNVs

- **ID:** count_snvs
- **Description:** The number of variant type SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER).
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the number of variant type SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using [bcftools view](#Samtools-view). (`bcftools view -H -v snps -f PASS`)
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] 


### Count: Insertions

- **ID:** count_insertions
- **Description:** The number of variant type indels only insertions in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER). 
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the number of variant type indels only insertions in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using [bcftools view](#Samtools-view), (`bcftools view -H -v indels -f PASS....INS`). Insertions are only considered in this metric short, less than 50bp, insertions as commonly identified by most short reads variant callers. Structural variations which include insertions larger than 50bp and which are typically identified using dedicated SV callers are not considered.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]

### Count: Deletions

- **ID:** count_deletions
- **Description:** The number of variant type indels only deletions in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER).
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the number of variant type indels only deletions in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using [bcftools view](#Samtools-view), (`bcftools view -H -v indels -f PASS....DEL`). Deletions are only considered in this metric short, less than 50bp, deletion as commonly identified by most short reads variant callers. Structural variations which include deletions larger than 50bp and which are typically identified using dedicated SV callers are not considered
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]

### Ratio: Insertions/Deletions

- **ID:** ratio_insertion_deletion
- **Description:** The ration between number of insertion and deletion in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER).
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the ratio of insertions and deletion in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using `bcftools view`, (`bcftools view -H -v indels -f PASS....INS/bcftools view -H -v indels -f PASS....DEL`). Insertions and Deletions are only considered in this metric short, less than 50bp, insertions, deletion as commonly identified by most short reads variant callers. Structural variations which include insertions, deletions larger than 50bp and which are typically identified using dedicated SV callers are not considered
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]

### Ratio: Heterozygous/Homozygous (SNVs)

- **ID:** ratio_heterozygous_homzygous_snv
- **Description:** The ratio of heterozygous and homozygous variant type SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER). 
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the ratio of heterozygous and homozygous variant type SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using `bcftools view`, (`bcftools view -H -v snps -f PASS -g het / bcftools view -H -v snps -f PASS -g hom`).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]

### Ratio: Heterozygous/Homozygous (indels)

- **ID:** ratio_heterozygous_homzygous_indel
- **Description:** The ratio of heterozygous and homozygous variant type indels in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER).
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the ratio of heterozygous and homozygous variant type indels in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using `bcftools view`, (`bcftools view -H -v indels -f PASS -g het / bcftools view -H -v indels -f PASS -g hom`).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]

### Ratio: Transitions/Transversions (ti/tv)

- **ID:** ratio_transitions_transversions
- **Description:** The ratio of transitions and transversions of bi-allelic SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) of variant calls [PASS FILTER](#PASS-FILTER).
- **Implementation details:** In the NPM-sample-QC reference implementation, calculate the ratio of transitions and transversions of bi-allelic SNVs in short paired-end sequencing, only in [autosomal regions](#Autosomes-non-gap-regions) variant calls, PASS the [FILTER](#PASS-FILTER) using `bcftools stats`, (bcftools stats -f PASS ... TSTV).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate]


### 
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

### PASS FILTER
PASS FILTER refers to [VCF Format Specicification v4.2](https://samtools.github.io/hts-specs/VCFv4.2.pdf), section 1.4.1 "FILTER - filter status:" & [GATK generic hard-filtering recommendations](https://gatk.broadinstitute.org/hc/en-us/articles/360035890471-Hard-filtering-germline-short-variants)

## References

### ARGO

[]()

### DRAGEN

[https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform.html](https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform.html)

### Bedtools subtract

[https://bedtools.readthedocs.io/en/latest/content/tools/subtract.html](https://bedtools.readthedocs.io/en/latest/content/tools/subtract.html)

### Datamash

[https://www.gnu.org/software/datamash/](https://www.gnu.org/software/datamash/)

### Samtools stats

[http://www.htslib.org/doc/samtools-stats.html](http://www.htslib.org/doc/samtools-stats.html)

### Samtools view

[http://www.htslib.org/doc/samtools-view.html](http://www.htslib.org/doc/samtools-view.html)

### VerifyBamID2

[https://github.com/Griffan/VerifyBamID](https://github.com/Griffan/VerifyBamID)

### VerifyBamID reference panel

Pre-calculated reference panel of 1000 Genome Project phase 3 dataset: 100,000 sites mapped on GRCh38

- UDPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.UD](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.UD)
- BedPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.bed](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.bed)
- MeanPath: [https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.mu](https://raw.githubusercontent.com/Griffan/VerifyBamID/master/resource/1000g.phase3.100k.b38.vcf.gz.dat.mu)
