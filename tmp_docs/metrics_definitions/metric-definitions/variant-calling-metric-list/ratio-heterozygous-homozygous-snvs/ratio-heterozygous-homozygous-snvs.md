# Ratio: Heterozygous/Homozygous (SNVs)

- **ID:** ratio_heterozygous_homzygous_snv
- **Description:** The ratio of heterozygous and homozygous variant of type SNVs in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the ratio of heterozygous and homozygous variant of type SNVs in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v snps -f PASS -g het / bcftools view -H -v snps -f PASS -g hom`).
- **Type:** Float 2 decimal precision (eg. 1.64)
- **Functionally equivalent implementations:**
  - [ARGO vcfqc](#argo)

