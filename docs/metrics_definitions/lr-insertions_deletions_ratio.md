# Insertions / Deletions ratio
- **ID:** small_insertions_deletions_ratio
- **Description:** The ratio of small insertion variant calls to small deletion variant calls. This metric summarizes the relative balance between insertion and deletion calls and can indicate systematic bias in sequencing, alignment, or variant calling.
- **Implementation details:** Count insertion events and deletion events using a defined VCF parsing approach, then divide the insertion count by the deletion count. The implementation should define the included variant size range, whether PASS-only variants are used, and how complex variants are classified. In ONT workflows, this metric can be useful for monitoring indel error patterns, particularly in homopolymer or repeat contexts. PacBio HiFi datasets may show a different indel balance due to different error profiles.
- **Type:** Float (eg. 1.15)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfstats
