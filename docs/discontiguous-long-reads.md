## Discontiguous Long Reads

Several technologies perform discontiguous sequencing of long molecules.
Using [SAM](https://samtools.github.io/hts-specs/SAMv1.pdf) terminology, the _template_ long molecules are sequence by multiple short _reads_.
This results in sequencing data that has attributes of both short and long read sequencing technologies.
As such, quality control of such data is a combination of _template_ level metrics, and _read_ level metrics.
To account for this, discontiguous long read sequencing technologies must report both _template_ level metrics and _read_ level metrics.

The following general principles apply to discontiguous long read sequencing technologies metrics:

- When calculating the _template_ level long read metrics, all references to _read_ in the metric definition should be treated as _template_ reference.
- Length-based _template_ metrics should used the inferred _template_ length
  - Note that this length is technology-dependent, and may vary based on the secondary analysis pipeline used for template determination.
  - If no relevant technology-dependent alternative definition is available, then the _template_ length shall be defined as the genomic distance between the extrema of the first and last read for which the _reads_ sharing a common _template_ are concordantly mapped.
- Depth/coverage-based _template_ metrics should be computed from sequence depth, not physical coverage.
- Count-based _template_ metrics should be computed based on the _template_ count.
These metrics should be independent of the number of _reads_ per _template_.
- _template_ metrics that do not have a meaningful equivalent to the contiguous long read should not be reported.
- _Read_ level metrics should include all reads, regardless of whether a containing _template_ as identified for that _read_.
- _template_ level metrics should exclude singleton reads for which no containing _template_ is defined.

- A common set of variant-level metrics should be redundantly reported for both _template_ and _read_ level metrics outputs.
That is, the variant calling output from the discontiguous long read secondary analysis pipeline should be used for both metrics outputs.
The _read_-level variant calls should not be calculated based on a separate _template_-naive secondary analysis pipeline.
- For metrics calculation purposes, discontiguous phase blocks should be split into contiguous phase blocks and phasing metrics calculated based on the contiguous blocks.
The definition underestimates the phasing capability of discontiguous long read technologies but provides the closest match to 
- Metrics downstream of variant calling should also be common