# Ratio: Heterozygous/Homozygous (SNVs)

- **ID:** ratio_heterozygous_homzygous_snv
- **Description:** The ratio of heterozygous and homozygous variant of type SNVs in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the ratio of heterozygous and homozygous variant of type SNVs in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](terminologies.md#samtools-view), (`bcftools view -H -v snps -f PASS -g het / bcftools view -H -v snps -f PASS -g hom`).
- **Type:** Float 2 decimal precision (eg. 1.64)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ARGO vcfqc](References.md#argo)
