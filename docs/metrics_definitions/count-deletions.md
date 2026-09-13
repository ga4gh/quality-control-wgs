# Count: Deletions

- **ID:** count_deletions
- **Description:** Total count of sequence-resolved short-deletion alternate alleles 1 to 49 bp in length observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Only [high quality variants](terminologies.md#high-quality-variants) are included. Multiallelic records must be split and normalized (reference based left-aligned) prior to counting. Symbolic and complex alleles lacking explicit sequence resolution are excluded. This metric applies across short-read, contiguous long-read, and discontiguous long-read callsets.

#because variant caller choice, version, and parameterization substantially influence deletion yields, these provenance details must be reported alongside the metric 'OR' Variant caller name, exact version, and invocation parameters must be reported, as caller heuristics materially impact indel counts 'OR' the variant caller and its exact version and parameters must be reported because they can materially affect the result.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, variants are normalized against the matching reference FASTA and split across multiallelic records using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -f reference.fa -m -any`). The callset is then restricted to autosomal non-gap intervals, retaining only (`FILTER=PASS`) records with an alternate genotype (`GT="alt"`). Finally, indels are filtered to count records satisfying `ILEN<0 && ILEN>-50`.

#Record the bcftools version, reference assembly and FASTA checksum, evaluation-region checksum, normalization command, filters, variant caller, and caller parameters. The same procedure is used for every sequencing read type.

- **Comments:** 
    - non-gap regions 'excluding centromeric/telomeric assembly gaps'
    - symbolic records (e.g., <DEL>) and complex unphased replacements are omitted.
    - PASS variant has successfully met all quality and filtering criteria defined by the variant caller.
```
bcftools norm -f reference.fa -m -any input.vcf.gz \
  | bcftools view -s "$SAMPLE" -R autosomal_nongap.bed -f PASS -i 'GT="alt"' \
  | bcftools filter -i 'TYPE="indel" && ILEN < 0 && ILEN > -50' \
  | grep -v '^#' \
  | wc -l
  ```
- **Type:** Integer (eg. 444892)
- **Functionally equivalent implementations:**
  - [NPM sample qc](References.md#npm-sample-qc), when the same normalization, size, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, size, sample-genotype, PASS-status, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset, deletion-size limits, and filters.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
