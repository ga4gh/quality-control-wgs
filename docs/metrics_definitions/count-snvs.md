# Count: SNVs

- **ID:** count_snvs
- **Description:** The number of variant of type SNVs in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the number of variant of type SNVs in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](terminologies.md#samtools-view), (`bcftools view -H -v snps -f PASS`).
- **Type:** Integer (eg. 3906868)
- **Functionally equivalent implementations:**
     - [ARGO vcfqc](terminologies.md#argo)

