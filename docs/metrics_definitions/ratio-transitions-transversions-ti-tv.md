# Ratio: Transitions/Transversions (ti/tv)

- **ID:** ratio_transitions_transversions_snv
- **Description:** The ratio of transitions and transversions of bi-allelic SNVs in [VCF](terminologies.md#vcf-format), only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality variants](terminologies.md#high-quality-variants).
- **Implementation details:** In the [NPM-sample-QC](terminologies.md#npm-sample-qc) reference implementation, calculate the ratio of transitions and transversions of bi-allelic SNVs in VCF, only in [autosomal regions](terminologies.md#autosomes-non-gap-regions), [high quality-variants](terminologies.md#high-quality-variants) by `bcftools stats`, (`bcftools stats -f PASS ... TSTV`).
- **Type:** Float 2 decimal precision (eg. 1.12)
- **Functionally equivalent implementations:**
    - [NPM sample qc](References.md#npm-sample-qc)
    - [ARGO vcfqc](References.md#argo)
