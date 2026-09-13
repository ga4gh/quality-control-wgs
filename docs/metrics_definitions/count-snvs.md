# Count: SNVs

- **ID:** count_snvs
- **Description:** Total count of single nucleotide variant (SNV) alternate alleles observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Only [high quality variants](terminologies.md#high-quality-variants) are included. Multiallelic records must be split and normalized (reference based left-aligned) prior to counting. This metric applies across short-read, contiguous long-read, and discontiguous long-read callsets.

# the variant caller and its exact version and parameters must be reported because they can materially affect the result.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, variants are normalized against the matching reference FASTA and multiallelic records are split using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -f reference.fa -m -any`). The callset is then restricted to autosomal non-gap intervals, retaining only (`FILTER=PASS`) records with an alternate genotype (`GT="alt"`). SNVs are filtered and counted using (`bcftools view -H -v snps -f PASS -R autosomal_nongap.bed -i 'GT="alt"`).

- **Comments:**
```
bcftools norm -f reference.fa -m -any input.vcf.gz \
  | bcftools view -H \  
      -R autosomal_nongap.bed \
      -f PASS \
      -v snps \
      -i 'GT="alt"' \
  | wc -l
```
- **Type:** Integer (eg. 3906868)
- **Functionally equivalent implementations:**
  - [NPM sample qc](References.md#npm-sample-qc), when the same normalization, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset and filters.
  - [hap.py](https://github.com/Illumina/hap.py), using the same normalized callset and filters.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.