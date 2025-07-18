# Ratio: Heterozygous/Homozygous (indels)

- **ID:** ratio_heterozygous_homzygous_indel
- **Description:** The ratio of heterozygous and homozygous variant of type indels in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the ratio of heterozygous and homozygous variant of type indels in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants) by [bcftools view](terminologies.md#samtools-view), (`bcftools view -H -v indels -f PASS -g het / bcftools view -H -v indels -f PASS -g hom`).
- **Type:** Float 2 decimal precision (eg. 2.02)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ICGC-ARGO vcfqc](References.md#icgc-argo)