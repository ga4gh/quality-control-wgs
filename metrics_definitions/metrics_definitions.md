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

## Terminology & References

1. **ALT contigs** refers to [GATK technical Documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360035890951-Human-genome-reference-builds-GRCh38-or-hg38-b37-hg19#:~:text=GRCh38%2Fhg38%20is%20the%20assembly,extent%20we%20see%20with%20GRCh38.), section 2: "Features of GRCh38/hg38", GRCh38 ALT contigs

2. **Base quality score** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4: “The alignment section: mandatory fields”, “QUAL: ASCII of base QUALity”

3. **bedtools intersect** refers to [bedtools 2.30.0 documentation](https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html), Section "intersect"

4. **clipped bases** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2: ”Terminologies and Concepts”, “Linear alignment“ & section 1.4 “The alignment section: mandatory fields”, “CIGAR: CIGAR string”

5. **datamash** refers to [datamach documentation](https://www.gnu.org/software/datamash/)

6. **duplicated reads** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4: “The alignment section: mandatory fields”, “FLAG: Combination of bitwise FLAGs”

7. **GRCh38 assembly** refers to [1000genome-dragen-3.7.6 reference](https://1000genomes-dragen-3.7.6.s3.amazonaws.com/references/fasta/hg38.fa)

8. **High quality reads** refers to sequencing instrument filter. For Illumina sequencer, leverages internal quality filtering procedure called [chastity filter](https://gatk.broadinstitute.org/hc/en-us/articles/360035890991-PF-reads-Illumina-chastity-filter). Reads that pass this filter are called "PF" for "pass-filter"

9. **Mapping quality** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.4 “The alignment section: mandatory fields”, “MAPQ: MAPping Quality”

10. **Mosdepth** refers to [mosdepth documentation](https://github.com/brentp/mosdepth)

11. **Non gap regions** refers to [NPM-sample-qc documentation](https://github.com/c-BIG/NPM-sample-qc/blob/master/resources/README.rst)

12. **Overlapping bases** refers to [mosdepth documentation](https://github.com/brentp/mosdepth), section "how it works

13. **PHRED scale** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2
”Terminologies and Concepts”, “Phred scale“

14. **Picard CollectQualityYieldMetrics** refers to [GATK documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360040507031-CollectQualityYieldMetrics-Picard-), section "CollectQualityYieldMetrics (Picard)" & [GATK specifications](https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectQualityYieldMetrics.QualityYieldMetrics)

15. **Picard CollectInsertSizeMetrics** refers to [GATK documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360037055772-CollectInsertSizeMetrics-Picard-), section "CollectInsertSizeMetrics (Picard)" & [GATK specifications](https://broadinstitute.github.io/picard/picard-metric-definitions.html#InsertSizeMetrics)

16. **Primary alignments** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2 ”Terminologies and Concepts”, “Multiple mapping“ & section 1.4 “The alignment section: mandatory fields”, “FLAG: Combination of bitwise FLAGs”

17. **Secondary alignments** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.2 ”Terminologies and Concepts”, “Multiple mapping“ & section 1.4 “The alignment section: mandatory fields”, “FLAG: Combination of bitwise FLAGs”

18. **UMI** refers to [SAM Format Specification v1](https://samtools.github.io/hts-specs/SAMv1.pdf), section 1.3.1 "Defined sub-sort terms”, “umi“

19. **Window-size** refers to [mosdepth documentation](https://github.com/brentp/mosdepth)

## Metric list

### Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** The number of bases in high quality reads<sup>8</sup> primary alignments<sup>16</sup>, short paired-end sequencing alignments, achieving a base quality score<sup>2</sup>(PHRED scale<sup>13</sup>) of 30 or higher. Duplicated reads<sup>6</sup> and clipped bases<sup>4</sup> are included & no minimum mapping quality<sup>6</sup> is imposed.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using GATK Picard’s CollectQualityYieldMetric<sup>14</sup>, reporting the PF_Q30_BASES field. Only high quality bases and primary alignment are considered. No filter of duplicate reads, clipped bases or mapping qualiy is applied.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] DRAGEN v3.7.6. Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`

### Mean autosome coverage

- **ID:** mean_autosome_coverage
- **Description:** The mean sequencing coverage derived from primary<sup>16</sup> short paired-end sequencing alignments of non duplicated reads<sup>6</sup>, non clipped bases<sup>4</sup> achieving a mapping quality<sup>9</sup> of 20 or greater in non gap regions<sup>11</sup> within GRCh38<sup>7</sup> primary assembly autosomes only. Alignments on heterochromosomes, mitochondrial DNA or alt contigs<sup>1</sup> assemblies<sup>17</sup> are excluded. Overlapping bases<sup>12</sup> are only counted once. Because only non duplicated reads & non clipped bases are taken into consideration, it is critcal that the (BAM/CRAM) alignment files be readily marked for duplicate<sup>3</sup> and clipped<sup>4</sup>
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed as the mean value of 1,000bp window-size<sup>19</sup> coverage for properly aligned primary reads, non duplicated reads, non clipped bases and non overlapping bases mapped on non gap regions of automoses achieving a mapping quality<sup>9</sup> of 20 or greater by mosdepth v0.3.2<sup>10</sup> and custom script using bedtools intersect<sup>3</sup> and datamash<sup>5</sup>.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources

### Percent autosomes covered ≥ 15 X

- **ID:** pct_autosomes_15x
- **Description:** The percentage of bases in primary<sup>16</sup> short paired-end sequencing alignments of non duplicated reads<sup>6</sup>, non clipped bases<sup>4</sup> and non overlapping bases<sup>9</sup> achieving a mapping quality<sup>9</sup> of 20 or greater that attained at least 15X sequence coverage in non gap region<sup>11</sup> within GRCh38<sup>7</sup> primary assembly autosomes only. Alignments on heterochromosomes, mitochondrial DNA or alt contigs<sup>1</sup> assemblies<sup>17</sup> are excluded. Overlapping bases<sup>12</sup> are only counted once. Because only non duplicated reads & non clipped bases are taken into consideration, it is critcal that the (BAM/CRAM) alignment files be readily marked for duplicate<sup>3</sup> and clipped<sup>4</sup>
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage of non duplicated reads, non clipped bases, non overlapping bases, primary short paired-end sequencing alignments, achieving a mapping quality of 20 or greater is derived from mosdepth v0.3.2<sup>10</sup>. It is further narrowed to the non gap region within GRCh38 primary assembly autosomes only using bedtools intersect<sup>8</sup> were accounted to calculate the percentage of bases attained more than 15X coverage over the autosomes by custom script using datamash<sup>5</sup>.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources

### Percent read mapped

- **ID:** pct_reads_mapped
- **Description:** The percentage of primary reads<sup>16</sup>, paired or single, that are mappable to the REF sequence with MAPQ<sup>9</sup> > 0 after alignment.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using samtools stats. The percentage of primary reads mapped to GRCh38<sup>7</sup> with MAPQ > 0 includes duplicated reads.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - samtools stats (reads_mapped / sequences)
  - [Candidate] DRAGEN v3.7.6. Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Mapped reads`

### Properly paired read

- **ID:** pct_reads_properly_paired
- **Description:** The percentage of mappable properly paired primary<sup>16</sup> non duplicated<sup>6</sup> reads to the REF sequence with MAPQ<sup>9</sup> > 0 after alignment.
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed using samtools stats. The percentage of properly paired primary reads mapped to GRCh38<sup>7</sup> with MAPQ > 0 includes duplicated reads.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] DRAGEN v3.7.6. Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Properly paired reads`

### Mean insert size

- **ID:** mean_insert_size
- **Description:** The average absolute template length for paired and non duplicated mapped reads<sup>6</sup>
- **Implementation details:** In the NPM-sample-QC reference implementation it is computed from the paired and non duplicated mapped reads using GATK Picard’s CollectInsertSizeMetrics<sup>15</sup>.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
  - [Candidate] DRAGEN v3.7.6. Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Insert length: mean`

### Genome coverage uniformity

- **ID:** autosome_coverage_uniformity
- **Description:** The percentage of bases with more or less than 25% coverage difference from the mean autosome coverage
- **Implementation details:** In the NPM-sample-QC reference implementation, the genome-wide sequencing coverage of non duplicated reads, non clipped bases, non overlapping bases, primary short paired-end sequencing alignments, achieving a mapping quality of 20 or greater is derived from mosdepth v0.3.2<sup>10</sup>. It is further narrowed to the non gap region within GRCh38 primary assembly autosomes only using bedtools intersect<sup>8</sup> were accounted to calculate the median absolute deviation of the coverage over the autosomes by custom script using datamash<sup>5</sup>.
- **Functionally equivalent implementations:** Are considered functionally equivalent alternative implementations producing values within 1% of those reported by the reference implementation when computing the metric for data in the benchmark_resources
