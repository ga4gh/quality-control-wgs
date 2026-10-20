# Ratio: Heterozygous/Homozygous (indels)

- **ID:** ratio_heterozygous_homozygous_indel
- **Description:** The ratio of sequence-resolved heterozygous short-indel alternate calls to homozygous-alternate short-indel calls (1 to 49 bp in length) observed in the [autosomal non-gap regions](terminologies.md#autosomes-non-gap-regions). Only biallelic [high-quality variants](terminologies.md#high-quality-variants) are included. Multiallelic records must be split, and variants must be normalized (reference-based left-aligned) and atomized prior to calculation.  Homozygous-reference, missing, haploid, symbolic, and non-PASS calls are excluded, as are complex alleles that cannot be decomposed into sequence-explicit insertions or deletions. The same definition and evaluation regions apply to short-read, contiguous-long-read, and discontiguous-long-read callsets. This ratio is a broad QC indicator of sample consistency, coverage adequacy, contamination, ploidy assumptions, and variant-calling behaviour.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, multiallelic records are split, and variants are atomized and normalized (reference-based left-aligned) against the matching reference FASTA using [bcftools](https://www.htslib.org/doc/bcftools.html) (`bcftools norm -m -any -f reference.fa`). The callset is then restricted to autosomal non-gap intervals, selecting passing (`FILTER=PASS`), biallelic, sequence-resolved short indels satisfying `ABS(ILEN)>0 && ABS(ILEN)<50`. Heterozygous indels (`GT="het"`) and homozygous-alternate indels (`GT="AA"`) are counted separately, and the heterozygous-to-homozygous ratio is calculated by dividing the heterozygous count by the homozygous-alternate count. When the homozygous-alternate count is zero, N/A is reported rather than infinity. The same procedure is used for every sequencing read type.
- **Comments:**
```
# Normalize, atomize, split multiallelic records, and filter to passing autosomal biallelic indels (1 to 49 bp)
bcftools norm -f reference.fa -a -m -any input.vcf.gz \
  | bcftools view -R autosomal_nongap.bed -f PASS -v indels -m 2 -M 2 \
  | bcftools filter -i 'abs(ILEN) > 0 && abs(ILEN) < 50' > filtered_indels.vcf

# Count heterozygous short indels
n_het=$(bcftools view -H -i 'GT="het"' filtered_indels.vcf | wc -l)

# Count homozygous-alternate short indels (excluding homozygous-reference)
n_hom_alt=$(bcftools view -H -i 'GT="AA"' filtered_indels.vcf | wc -l)

# Compute heterozygous-to-homozygous ratio
awk -v het="$n_het" -v hom="$n_hom_alt" 'BEGIN {
  if (hom > 0) printf "%.4f\n", het / hom;
  else print "N/A"
}'
```
- **Type:** Float, 2 decimal precision (eg. 2.02)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO vcfqc](References.md#icgc-argo), when the same normalization, atomization, indel-size, selected-sample genotype, PASS-status, symbolic-allele, denominator, and evaluation-region rules are applied.
  - [RTG Tools vcfstats](https://github.com/RealTimeGenomics/rtg-tools), using the same normalized callset, indel-size limits, genotype definitions, symbolic-allele policy, and evaluation regions.
  - [hap.py](https://github.com/Illumina/hap.py), using the same normalized callset, indel-size limits, genotype definitions, symbolic-allele policy, and evaluation regions.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
