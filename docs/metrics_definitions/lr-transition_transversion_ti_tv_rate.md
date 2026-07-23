# Transition / Transversion (Ti/Tv) rate
- **ID:** titv_ratio
- **Description:** The ratio of transition SNVs to transversion SNVs. Transitions are A↔G and C↔T substitutions; transversions are all other single-base substitutions. Ti/Tv is a widely used variant-callset QC metric because true human germline SNVs have a characteristic enrichment for transitions. For long reads, it is recommended to restrict this estimation to a specific whitelist of consistently diploid regions to prevent confounding true allelic variation from paralogous variation (variants between copies of copy number variable loci) which often features lower Ti/Tv due to distinct evolutionary mechanisms.
- **Implementation details:** Count SNVs classified as transitions and SNVs classified as transversions in the filtered call set, then divide the transition count by the transversion count. The implementation should specify whether only PASS variants are used and whether counts are restricted to autosomes, high-confidence regions, or the whole genome. For ONT human WGS not restricted to whitelisted diploid regions, Ti/Tv values may be lower than the commonly cited short-read WGS expectation of ~2.0–2.1 (see above), and should therefore be interpreted relative to the platform, caller, chemistry, and filtering strategy used.
- **Type:** Float (eg. 1.8)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfstats
  - hap.py (note that even when a high-confidence set for false positive comparison is passed to hap.py as “-f”, this is not used for Ti/Tv calculation – rather a whitelist must be explicitly specified via “--location” or similar)
