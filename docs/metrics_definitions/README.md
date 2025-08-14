
The specification section outlines the key quality control (QC) metrics defined by the QC of WGS Workgroup, along with their detailed descriptions. In developing these definitions, we have identified common [terminologies and concepts](terminologies.md) relevant across multiple metrics. These shared elements form the basis for a controled vocabulary which we aim to map to existing ontology(ies) terms (See [Roadmap](roadmap_v2.md)).

The initial scope of this work focuses on QC for germline whole-genome sequencing (WGS). 
QC can be assessed at various stages of WGS data processing and analysis pipeline (e.g., post-FASTQ generation, post-alignment, post-variant calling). For this first release, the emphasis is on metrics derived from BAM/CRAM and VCF files. While all current QC metrics address short-read based WGS, their definition are designed to be technology-agnostic and adaptable to other sequencing approaches.

# Metric definitions

See individual metric definions under [Post Alignment metrics](https://ga4gh.github.io/quality-control-wgs/metrics_definitions/) and [Post Variant calling metrics](https://ga4gh.github.io/quality-control-wgs/metrics_definitions/)

# Metric definition template

QC metrics adhere to this general template:

- Id (mandatory): Metric identifier
- Description (mandatory): Metric description.
- Implementation details (mandatory): Tool and version used to calculate the metric & insights into the metric implementation, where possible.
- Type (mandatory): whether a metric is an integer or float, and for float values, to define the minimal required decimal precision to ensure consistent reporting across workflows.
- Functionally equivalent implementations (optional): A description of what constitute a valid alternative implementation producing values within an acceptable range of variation when compared to value(s) reported by the reference implementation when computing the metric i.e Validated equivalent implementations. We welcome the inclusion of candidate equivalent implementations.


