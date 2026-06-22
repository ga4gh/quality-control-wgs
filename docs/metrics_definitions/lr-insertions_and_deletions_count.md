# Insertions and Deletions count
- **ID:** small_insertions_deletions_count
- **Description:** The separate counts of small (less than 50bp) insertion and deletion events in the variant call set. This provides more detailed information than total indel count and helps identify systematic bias in long-read variant calling.
- **Implementation details:** Split indel variants into insertion and deletion categories based on the length difference between the reference and alternate allele, or based on the symbolic variant type for larger events. Count each category after applying the selected filters. The implementation should specify handling of complex variants, multi-allelic records, symbolic alleles, and overlapping alleles. For ONT and PacBio datasets, reporting insertion and deletion counts separately is useful for monitoring platform, chemistry, basecaller, aligner, and caller-specific bias.
- **Type:** Structured integer counts (eg. insertions: 520000; deletions: 270000)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfstats
