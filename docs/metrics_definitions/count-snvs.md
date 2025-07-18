# Count: SNVs

- **ID:** count_snvs
- **Description:** The number of variant of type SNVs in [VCF](References.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, calculate the number of variant of type SNVs in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](References.md#samtools-view), (`bcftools view -H -v snps -f PASS`).
- **Type:** Integer (eg. 3906868)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO vcfqc](References.md#icgc-argo)