# Heterozygous / Homozygous ratio (SNVs | Indels)
- **ID:** heterozygous_homozygous_ratio
- **Description:** The ratio of heterozygous variant calls to homozygous alternate variant calls. It may be reported separately for SNVs and indels. In human germline WGS, this metric is used as a QC indicator for sample consistency, coverage adequacy, contamination, and variant calling behavior.
- **Implementation details:** Classify genotyped variant calls as heterozygous or homozygous alternate using the GT field in the VCF, then divide the heterozygous count by the homozygous alternate count. The implementation should define whether missing, reference, multi-allelic, sex chromosome, and non-diploid calls are included. For autosomal human WGS, SNV Het/Hom ratios are often expected to be approximately 1.5-2.0, but the expected value depends on ancestry, relatedness, sample type, filtering, and region selection. Low values may indicate allelic dropout or low coverage; high values may indicate contamination or mixed samples.
- **Type:** Float (eg. 1.72)
- **Functionally equivalent implementations:**
  - bcftools stats
  - RTG Tools vcfstats
  - hap.py
