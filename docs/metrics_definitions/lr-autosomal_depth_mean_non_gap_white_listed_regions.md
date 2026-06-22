# Autosomal depth (mean), non-gap white listed regions
- **ID:** autosomal_depth_mean
- **Description:** The mean sequencing depth across autosomal regions, typically restricted to non-gap and high-confidence whitelisted regions of the reference genome. This metric estimates the effective WGS coverage available for variant calling and other downstream analyses.
- **Implementation details:** Calculate depth over selected autosomal reference intervals after alignment. Exclude regions such as assembly gaps, centromeres, telomeres, and other problematic regions if a whitelist is used. Sum the aligned bases or per-base depths across the selected intervals and divide by the effective region length. The method should specify mapping quality, base quality, supplementary alignment, and secondary alignment filters. For ONT and PacBio human WGS, autosomal mean depth is commonly used to assess whether the dataset is sufficient for SNV, indel, SV, CNV, methylation, and phasing analyses.
- **Type:** Float, fold coverage (eg. 32.4)
- **Functionally equivalent implementations:**
  - mosdepth
  - samtools depth
  - bedtools genomecov
