# Bases with ≥ N-fold coverage
- **ID:** bases_ge_n_fold_coverage
- **Description:** The number or proportion of bases in selected genomic regions covered by at least N sequencing reads. Typical thresholds include 5x, 10x, and 15x. This metric estimates the callable fraction of the genome at different depth thresholds.
- **Implementation details:** Compute per-base depth across the selected genome intervals and count bases where depth is greater than or equal to each requested threshold. Report the count and, preferably, the fraction relative to the total number of evaluated bases. The implementation should define whether depth is calculated over the whole genome, autosomes only, high-confidence regions, or another whitelist. It should also specify read filters such as mapping quality, supplementary alignments, and secondary alignments.
- **Type:** Integer or Float (eg. 2850000000 bases ≥ 10x; 0.955 fraction ≥ 10x)
- **Functionally equivalent implementations:**
  - mosdepth thresholds
  - samtools depth
  - bedtools genomecov
