# Count: Insertions

- **ID:** count_insertions
- **Description:** The number of variant of type indels categorized as short insertions (less than 50bp) in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the number of variant of type indels categorized as insertions in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](terminologies.md#samtools-view), (`bcftools view -H -v indels -f PASS....INS`).
- **Type:** Integer (eg. 490511)
- **Functionally equivalent implementations:**
     - [ARGO vcfqc](terminologies.md#argo)

