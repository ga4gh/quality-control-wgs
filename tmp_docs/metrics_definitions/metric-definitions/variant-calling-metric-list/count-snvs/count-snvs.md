# Count: SNVs

- **ID:** count_snvs
- **Description:** The number of variant of type SNVs in [VCF](#vcf-format), only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](#npm-sample-qc) reference implementation, calculate the number of variant of type SNVs in VCF, only in [autosomal regions](#autosomes-non-gap-regions), [high quality variants](#high-quality-variants) by [bcftools view](#samtools-view), (`bcftools view -H -v snps -f PASS`).
- **Type:** Integer (eg. 3906868)
- **Functionally equivalent implementations:**
  - [ARGO vcfqc](#argo)

