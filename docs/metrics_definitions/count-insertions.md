# Count: Insertions

- **ID:** count_insertions
- **Description:** Total count of sequence-resolved short-insertion alternate alleles 1 to 49 bp in length observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Only [high quality variants](terminologies.md#high-quality-variants) are included. Multiallelic records must be split and normalized (reference based left-aligned) prior to counting. Symbolic and complex alleles lacking explicit sequence resolution are excluded. Applicable to short-read, contiguous long-read, and discontiguous long-read data.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, Normalize variants against the matching reference FASTA and split multiallelic records using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -f reference.fa -m -any`). Restrict the callset to autosomal non-gap intervals. Retain only (`FILTER=PASS`) records containing an alternate genotype (`GT="alt"`). Select indels and count records satisfying `ILEN>0 && ILEN<50`.
- **Type:** Integer (eg. 490511)
- **Functionally equivalent implementations:**
  - [NPM sample qc](References.md#npm-sample-qc), when the same normalization, size, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, size, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset, insertion-size limits, and filters.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.