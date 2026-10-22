
The specification section outlines the key quality control (QC) metrics defined by the QC of WGS Workgroup, along with their detailed descriptions. In developing these definitions, we have identified common [terminologies, concepts](terminologies.md) and [references](References.md) relevant across multiple metrics. These shared elements form the basis for a controled vocabulary which we aim to map to existing ontology(ies) terms (See [Roadmap](../roadmap_v2.md)).

The initial scope of this work focuses on QC for germline whole-genome sequencing (WGS). 
QC can be assessed at various stages of WGS data processing and analysis pipeline (e.g., post-FASTQ generation, post-alignment, post-variant calling). For this first release, the emphasis is on metrics derived from BAM/CRAM and VCF files. While all current QC metrics address short-read based WGS, their definition are designed to be technology-agnostic and adaptable to other sequencing approaches.

# Metric definitions

See individual metric definions under [Post Alignment metrics](https://ga4gh.github.io/quality-control-wgs/metrics_definitions/) and [Post Variant calling metrics](https://ga4gh.github.io/quality-control-wgs/metrics_definitions/)

# Metric definition template

QC metrics adhere to this general template:

- Id (mandatory): Unique identifier assigned to the QC metric.
- Description (mandatory): Definition and intended interpretation of the QC metric.
- Implementation details (mandatory): Information describing the reference implementation used to compute the QC metric, including the computational method, software, and software version, and parameters where applicable.
- Data yype (mandatory): The QC metric shall be reported as either an integer or floating-point value. For floating-point values, the minimum reporting precision shall be specified.
- Functionally equivalent implementations (optional): Alternative software implementations, workflows, or analytical pipelines that have been demonstrated through benchmarking to produce results consistent with the reference implementation for this QC metric within an acceptable range of variation.
- Sequencing read type (mandatory): Applicable sequencing data type (e.g., short-read or long-read).
- Reference genome assembly (mandatory): Applicable reference genome assembly (e.g., GRCh37 or GRCh38).
- Version (mandatory): Version of the metric definition.
- Sequencing technology (optional): Applicable sequencing platform or technology (e.g., Illumina, Oxford Nanopore Technologies, PacBio, Ultima Genomics).
- Associated aligner (optional): Alignment software name and version applicable to the metric, where relevant.
(e.g., BWA-MEM, DRAGEN v3.8, DRAGEN v4.4.7, Minimap2..)
- Associated variant caller (optional): Variant calling software name and version applicable to the metric, where relevant. (e.g., GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant,..)
- Associated basecaller (optional): (Illumina RTA short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio)


