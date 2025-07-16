# Count: Deletions

- **ID:** count_deletions
- **Description:** The number of variant type indels categorized as short deletions (less than 50bp) in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the number of variant of type indels categorized as deletions in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](terminologies.md#samtools-view), (`bcftools view -H -v indels -f PASS....DEL`).
- **Type:** Integer (eg. 444892)
- **Functionally equivalent implementations:**
    - [ARGO vcfqc](terminologies.md#argo)

