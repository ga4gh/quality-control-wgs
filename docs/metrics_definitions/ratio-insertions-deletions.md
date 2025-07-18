# Ratio: Insertions/Deletions

- **ID:** ratio_insertion_deletion
- **Description:** The ratio between number of short insertion and deletion (less than 50bp) in [VCF](References.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, calculate the ratio of insertions and deletion in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](References.md#samtools-view), (`bcftools view -H -v indels -f PASS....INS / bcftools view -H -v indels -f PASS....DEL`).
- **Type:** Float 2 decimal precision (eg. 1.13)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO vcfqc](References.md#icgc-argo)