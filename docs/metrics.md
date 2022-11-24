# Metric definitions
In this document, the WGS of QC workgroup intends to identify a set of key QC metrics and spell out their detailed definitions. Whilst doing so, we expect to encounter recurrent information fields that apply to many metrics. Those can then be used as the basis for standardised guidelines for reporting QC metrics.

## General notes
- The document is just a first draft to capture conversations from our regular meetings. It provides some templated sections as a guide, but those may not be exhaustive. As such, feel free to make as many changes as needed; we can always recover previous versions of the document using the file history.
- In terms of scope, the workgroup has agreed to focus on germline WGS QC first. While all of the workgroup participants are working with short-read data at the moment, we wish to make the definitions general enough to be applicable to other technologies as well. The workgroup also acknowledges that there are multiple stages in the analysis pipeline at which one may want to perform QC (e.g. post-FASTQ generation, post-alignment, post-variant calling). For the first iteration of the guidelines, the workgroup has agreed to focus on metrics that can be obtained from a BAM/CRAM file. Thus, metrics such as contamination or variant counts remain out of scope at the moment.

## Controlled vocabulary
This section lists several example metrics in an attempt to capture which fields would be required to accurately describe how each metric has been calculated. When defining each metric, we attempt to align to the following general template:
- Id (mandatory): metric_id
- Description (mandatory): Metric description.
- Source (mandatory): Tool and version used to calculate the metric.
- Implementation details (optional, depending on metric): Standardised insights into the metric implementation, where possible.

**Example metric: Bases ≥ Q30**
- Id: yield_bp_q30
- Description: The number of bases with BQ ≥ 30.
- Source: DRAGEN 3.7.6
- Implementation details:

| Field | Description | Format | Value in Example Implementation |
| ----- | ----------- | ------ | ------------------------------- |
| MIN_BQ | Minimum base quality | Integer | 30 |
| MIN_MQ | Minimum mapping quality | Integer | 0 |
| DUP | Are reads marked as duplicates included? | Boolean | FALSE |
| CLP | Are clipped bases (hard and soft clipped) included? | Boolean | FALSE |
| OLP | Are overlapping bases included? | Boolean | FALSE |
| UMI | Are unique Molecular Identifier used to collapse reads? | Boolean | FALSE |
| SEC | Are secondary alignments included? | Boolean | FALSE |


**Example metric: Mean autosome coverage**
- Id: mean_autosome_coverage
- Description: The mean coverage in autosomes.
- Source: in-house tool based on mosdepth v0.3.2
- Implementation details:

| Field | Description | Format | Value in Example Implementation |
| ----- | ----------- | ------ | ------------------------------- |
| REF | Genomic reference build | String | GRCh38 |
| BED | Genomic filtering regions | String | Homo_sapiens_assembly38.autosomes.bed |
| MIN_BQ | Minimum base quality | Integer | 0 |
| MIN_MQ | Minimum mapping quality | Integer | 20 |
| DUP | Are duplicates included | Boolean | FALSE |
| CLP | Are clipped bases (hard and soft clipped) included? | Boolean | FALSE |
| OLP | Are overlapping bases included? | Boolean | FALSE |
| UMI | Are unique Molecular Identifier used to collapse reads? | Boolean | FALSE |
| SEC | Are secondary alignments included? | Boolean | FALSE |

**Example metric: Percent autosomes covered ≥ 15 X**
- Id: pct_autosomes_15x
- Description: The percentage of bases that attained at least 15X sequence coverage in autosomes.
- Source: in-house tool based on mosdepth v0.3.2 
- Implementation details: same as mean_autosome_coverage.

**Example metric: Genome coverage uniformity**
- Id: autosome_coverage_uniformity
- Description: The percentage of bases with more or less than 25% coverage difference from the mean autosome coverage
- Source: in-house tool based on mosdepth v0.3.2 calculating (PCT < 0.75 * mean_autosome_coverage) + (PCT > 1.25 * mean_autosome_coverage) 
- Implementation details: same as mean_autosome_coverage.

**Example metric: Read mapping quality**
- Id (mandatory): read_mapping_quality
- Description (mandatory): The percentage of reads mappable to the REF sequence with MAPQ>0
- Source (mandatory): Via samtools (reads_mapped_percent)
- Implementation details: same as mean_autosome_coverage.

**Example metric: Discordant read pairs**
- Id (mandatory): discordant_read_pairs
- Description (mandatory): The percentage of properly paired reads after alignment
- Source (mandatory): Via samtools (reads_properly_paired_percent)
- Implementation details: same as mean_autosome_coverage.

**Example metric: Mean insert size**
- Id (mandatory): mean_insert_size
- Description (mandatory): A tuple of mean insert size for paired and mapped reads followed by the insert size standard deviation for the average template length distribution
- Source (mandatory): Via samtools (Insert_size_average and insert_size_standard_deviation)
- Implementation details: same as mean_autosome_coverage.

## Example implementations
*calculate_coverage.py*

A mosdepth wrapper to calculate average coverage and genome completeness metrics.
Documentation: [https://bit.ly/3EcgZXN](https://bit.ly/3EcgZXN]
