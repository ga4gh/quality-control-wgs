# Ratio: Heterozygous/Homozygous (SNVs)

- **ID:** ratio_heterozygous_homzygous_snv
- **Description:** The ratio of sequence-resolved heterozygous SNV alternate calls to homozygous-alternate SNV calls observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Include only biallelic records with [high quality variants](terminologies.md#high-quality-variants). Multiallelic records must be split, and variants must be normalized (reference-based left-aligned) and atomized prior to calculation. The same definition and evaluation regions apply to short-read, contiguous-long-read, and discontiguous-long-read callsets.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, multiallelic records are split, and variants are atomized and normalized (reference-based left-aligned) against the matching reference FASTA using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -m -any -f reference.fa`). The callset is then restricted to autosomal non-gap intervals, selecting only biallelic SNVs with [high quality variants](terminologies.md#high-quality-variants) (`FILTER=PASS`). Heterozygous SNVs (`GT="het"`) and homozygous-alternate SNVs (`GT="AA"`) are counted separately, and the heterozygous-to-homozygous ratio is calculated by dividing the heterozygous count by the homozygous-alternate count. When the homozygous-alternate count is zero, N/A is reported rather than infinity. The same procedure is used for every sequencing read type.
- **Comments:** 
Homozygous-reference, missing, haploid, symbolic, and non-PASS calls are excluded.
This ratio is a broad QC indicator of sample consistency, coverage adequacy, contamination, ploidy assumptions, and variant-calling behaviour.
Record the bcftools version, reference assembly and FASTA checksum, evaluation-region checksum, selected sample, normalization command, filters, variant caller, and caller parameters.
- **Type:** Float, 2 decimal precision (eg. 1.64)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, selected-sample genotype, PASS-status, biallelic-SNV, denominator, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset, genotype definitions, and evaluation regions.
  - [hap.py](https://github.com/Illumina/hap.py), using the same normalized callset, genotype definitions, and evaluation regions.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.