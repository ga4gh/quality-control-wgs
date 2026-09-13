# Ratio: Insertions/Deletions

- **ID:** ratio_insertion_deletion
- **Description:** Ratio of sequence-resolved short-insertion alternate alleles to short-deletion alternate alleles (1 to 49 bp in length) observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Only biallelic [high quality variants](terminologies.md#high-quality-variants) are included. Multiallelic records must be split, and variants must be normalized (reference-based left-aligned) and atomized prior to calculation. Symbolic alleles such as `<INS>` and `<DEL>` and complex alleles that cannot be decomposed into sequence-explicit insertions or deletions are excluded from this reference calculation. The same definition and evaluation regions apply to short-read, contiguous-long-read, and discontiguous-long-read callsets.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, multiallelic records are split, and variants are atomized and normalized (reference-based left-aligned) against the matching reference FASTA using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -m -any -f reference.fa`). The callset is then restricted to autosomal non-gap intervals, retaining only (`FILTER=PASS`) records with an alternate genotype (`GT="alt"`). Sequence-resolved short insertions (`ILEN>0 && ILEN<50`) and short deletions (`ILEN<0 && ILEN>-50`) are counted separately, and the insertion-to-deletion ratio is calculated by dividing the insertion count by the deletion count. when the deletion count is zero, N/A is reported rather than infinity.The same procedure is used for every sequencing read type.
- **Comments:** 
Record the bcftools version, reference assembly and FASTA checksum, evaluation-region checksum, selected sample, normalization and atomization command, filters, variant caller, and caller parameters.
```
# Normalize and filter sample variants
bcftools norm -f reference.fa -m -any input.vcf.gz \
  | bcftools view -s "$SAMPLE" -R autosomal_nongap.bed -f PASS -i 'GT="alt"' > filtered_sample.vcf

# Count short insertions (1 to 49 bp)
n_ins=$(bcftools filter -i 'TYPE="indel" && ILEN > 0 && ILEN < 50' filtered_sample.vcf \
  | grep -v '^#' \
  | wc -l)

# Count short deletions (1 to 49 bp)
n_del=$(bcftools filter -i 'TYPE="indel" && ILEN < 0 && ILEN > -50' filtered_sample.vcf \
  | grep -v '^#' \
  | wc -l)

# Compute insertion-to-deletion ratio
awk -v ins="$n_ins" -v del="$n_del" 'BEGIN { if (del > 0) printf "%.4f\n", ins / del; else print "NA" }'
```
- **Type:** Float, 2 decimal precision (eg. 1.13)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, atomization, size, sample-genotype, PASS-status, symbolic-allele, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset, indel-size limits, symbolic-allele policy, and evaluation regions.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.