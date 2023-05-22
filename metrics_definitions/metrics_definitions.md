# Metric definitions

In this document, the QC of WGS workgroup intends to identify a set of key QC metrics and spell out their detailed definitions. Whilst doing so, we expect to encounter recurrent information fields that apply to many metrics. Those can then be used as the basis for standardised guidelines for reporting QC metrics.

## General notes

- The document is just a first draft to capture conversations from our regular meetings. It provides some templated sections as a guide, but those may not be exhaustive. As such, feel free to make as many changes as needed; we can always recover previous versions of the document using the file history.
- In terms of scope, the workgroup has agreed to focus on QC of germline WGS first. While all of the workgroup participants are working with short-read data at the moment, we wish to make the definitions general enough to be applicable to other technologies as well. The workgroup also acknowledges that there are multiple stages in the analysis pipeline at which one may want to perform QC (e.g. post-FASTQ generation, post-alignment, post-variant calling). For the first iteration of the guidelines, the workgroup has agreed to focus on metrics that can be obtained from a BAM/CRAM file. Thus, metrics such as contamination or variant counts remain out of scope at the moment.

## Controlled vocabulary

This section lists several example metrics in an attempt to capture which fields would be required to accurately describe how each metric has been calculated. When defining each metric, we attempt to align to the following general template:

- Id (mandatory): Metric identifier
- Description (mandatory): Metric description.
- Implementation details (mandatory): Tool and version used to calculate the metric & insights into the metric implementation, where possible.
- Functionally equivalent implementations (optional): A description of what constitute a valid alternative implementation producing values within an acceptable range of variation when compared to value(s) reported by the reference implementation when computing the metric i.e Validated equivalent implementations. We welcome the inclusion of candidate equivalent implementations

## Metric list

### Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in short paired-end sequencing [high quality reads](#high-quality-reads), [primary alignments](#primary-alignments), achieving a [base quality score](#base-quality-score) of 30 or greater ([Phred scale](#phred-scale)). [Duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases) are included. No minimum [mapping quality](#mapping-quality) is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using [GATK Picard’s CollectQualityYieldMetrics](#picard-collectqualityyieldmetrics), reporting the PF_Q30_BASES field. Only high quality bases from primary alignments are considered. No filter on duplicated reads, clipped bases or mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] [DRAGEN v3.7.6](#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`

### Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The mean sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads),  [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Clipped bases](#clipped-bases) are excluded. [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage of non duplicated reads, non clipped bases, non overlapping bases, primary alignments, achieving a mapping quality of 20 or greater is derived from [mosdepth v0.3.2](#mosdepth). It is further narrowed down to the non gap regions of GRCh38 assembly, autosomes only using [bedtools intersect](#bedtools-intersect). The mean coverage is then computed on 1,000bp windows and averaged for the selected region using [datamash](#datamash).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources

### Percent autosomes covered ≥ 15 X

- **ID:** pct_autosomes_15x
- **Description:** The percentage of bases attaining at least 15X sequencing coverage in short paired-end sequencing [high quality](#high-quality-reads),  [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Clipped bases](#clipped-bases) are excluded. [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage of non duplicated reads, non clipped bases, non overlapping bases, primary alignments, achieving a mapping quality of 20 or greater is derived from [mosdepth v0.3.2](#mosdepth). It is further narrowed down to the non gap regions of GRCh38 assembly, autosomes only using [bedtools intersect](#bedtools-intersect). The percentage of bases attaining at least 15X coverage is then calculated using [datamash](#datamash).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources

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

### Genome coverage uniformity

- **ID:** autosome_coverage_uniformity
- **Description:** The median absolute deviation of sequencing coverage derived from short paired-end sequencing [high quality](#high-quality-reads), [non duplicated](#duplicated-reads) reads, [primary alignments](#primary-alignments), achieving a [mapping quality](#mapping-quality) of 20 or greater, in [autosomes non gap regions](#autosomes-non-gap-regions) of [GRCh38 assembly](#grch38-assembly). [Clipped bases](#clipped-bases) are excluded. [Overlapping bases](#overlapping-bases) are counted only once. It is critical that the (BAM/CRAM) alignment files be readily marked for [duplicated reads](#duplicated-reads) and [clipped bases](#clipped-bases).
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage of non duplicated reads, non clipped bases, non overlapping bases, primary alignments, achieving a mapping quality of 20 or greater is derived from [mosdepth v0.3.2](#mosdepth). It is further narrowed down to the non gap regions of GRCh38 assembly, autosomes only using [bedtools intersect](#bedtools-intersect). The median absolute deviation of the coverage is then calculated using [datamash](#datamash).
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources

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

### Autosomes non gap regions

Autosomes non gap regions refers to the selection of chromosome 1 to 22, excluding chromosome X, Y, M and alternative contigs. In addition, gap regions as defined by UCSC are excluded. See [NPM-sample-qc documentation](https://github.com/c-BIG/NPM-sample-qc/blob/master/resources/README.rst)

### GRCh38 assembly

GRCh38 assembly refers to [1000genome-dragen-3.7.6 reference](https://1000genomes-dragen-3.7.6.s3.amazonaws.com/references/fasta/hg38.fa)

### Overlapping bases

Overlapping bases refers to [mosdepth documentation](https://github.com/brentp/mosdepth), section "how it works"

## References

### DRAGEN

[https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform.html](https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform.html)

### Mosdepth

[https://github.com/brentp/mosdepth](https://github.com/brentp/mosdepth)

### Bedtools intersect

[https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html](https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html)

### Datamash

[https://www.gnu.org/software/datamash/](https://www.gnu.org/software/datamash/)

### Samtools stats

[http://www.htslib.org/doc/samtools-stats.html](http://www.htslib.org/doc/samtools-stats.html)
