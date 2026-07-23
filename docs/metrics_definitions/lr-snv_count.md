# SNV count
- **ID:** snv_count
- **Description:** The total number of single nucleotide variants identified relative to the reference genome. In human WGS, SNV count is used as a broad QC indicator for variant calling completeness and sample consistency.
- **Implementation details:** Count variant records classified as SNVs in the final variant call set after the selected filters are applied. The implementation should specify whether only PASS variants are counted, whether multi-allelic records are split, and whether counts are limited to autosomes, sex chromosomes, high-confidence regions, or the whole genome. For ONT and PacBio long-read data, SNV counts depend on depth, basecalling model, alignment, variant caller, filtering, and the reference genome build.
- **Type:** Integer (eg. 3650000)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfeval/vcfstats
  - hap.py
