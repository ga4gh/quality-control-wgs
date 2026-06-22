# Genome coverage uniformity
- **ID:** genome_coverage_uniformity
- **Description:** A measure of how evenly sequencing depth is distributed across the evaluated genome. Uniform coverage supports consistent variant detection, whereas non-uniform coverage may produce under-covered regions, false negatives, or biased copy-number estimates.
- **Implementation details:** Calculate coverage distribution across selected genomic bins or bases and summarize evenness using a defined statistic such as coverage quartiles. The implementation should define bin size, included genomic intervals, and alignment filters. 
- **Type:** Structured summary (eg. coverage quartiles)
- **Functionally equivalent implementations:**
  - mosdepth
  - bedtools genomecov
