# Indel count
- **ID:** small_indel_count
- **Description:** The total number of insertion and deletion variants less than 50 bp in length identified relative to the reference genome. Indels may be reported separately as insertion and deletion events. Long-read sequencing improves detection of indels in repetitive, low-complexity, and structurally challenging genomic regions.
- **Implementation details:** Count insertion and deletion alleles in the final VCF after selected filters. Count insertion and deletion alleles ≤50 bp in the final VCF after selected filters. The implementation should specify how complex variants are handled, whether multi-allelic records are split, and whether only PASS calls are included.
- **Type:** Integer or structured counts (eg. 790000 total; 520000 insertions; 270000 deletions)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfstats
  - hap.py
