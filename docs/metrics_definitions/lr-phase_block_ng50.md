# Phase block NG50

- **ID:** phase_block_ng50
- **Description:** The phase block length L such that phase blocks with length greater than or equal to L collectively account for at least 50% of the agreed target genome length. It is analogous to assembly NG50 but is applied to phased haplotype blocks rather than contigs. A phase block is defined by phased heterozygous variants belonging to the same phase set, and its length is the genomic distance between its leftmost and rightmost phased variants. The metric measures haplotype continuity and is applicable to short-read, contiguous-long-read, and discontiguous-long-read phased callsets.
- **Implementation details:** In the [WhatsHap v2.8](https://whatshap.readthedocs.io/en/latest/guide.html) reference implementation, run `whatshap stats --chr-lengths chromosome_lengths.tsv --tsv phase_stats.tsv phased.vcf.gz` and report `block_n50` for the `ALL` row. Despite the column name, WhatsHap defines this value as NG50 because the 50% threshold is relative to the chromosome lengths obtained from the VCF header or `--chr-lengths`, rather than to the sum of phase-block lengths. For short-read and discontiguous-long-read data, use the same agreed read-backed phasing policy. For discontiguous-long-read data, do not use a proximity-derived long-molecule or template span to create, join, or extend phase blocks; use only the eligible read evidence permitted by the short-read phasing method. In every sequencing type, derive block boundaries from the leftmost and rightmost phased variants in each phase set and do not substitute read, read-pair, template, or inferred-molecule boundaries. Use the agreed target assembly and chromosome set, record whether autosomes only are used, and use the same input variant set and phasing criteria when comparing technologies. Record the variant caller, phasing software, versions, and parameters. A value of `0` means that the summed phase-block lengths do not reach 50% of the target length; `nan` means that chromosome lengths were unavailable.

- **Working details..**

1.
**Description:** The phase block length $L$ such that phased haplotype blocks of length $\ge L$, sorted in descending order of length, collectively span at least 50% of the agreed reference or target genome size ($G$). It is analogous to assembly NG50, substituting contigs with phased haplotype blocks. A phase block is delineated by phased heterozygous variants assigned to the same phase set (PS tag in VCF), and its length is defined as the genomic distance (in base pairs) between its leftmost and rightmost phased variant coordinates. The metric measures long-range haplotype continuity across short-read, contiguous long-read, and discontiguous long-read phased callsets. For discontiguous long-read datasets (e.g., proximity-ligation or Pore-C), phase blocks must be derived strictly from variant phasing links rather than continuous linear physical template spans.

**Implementation details:** In the NPM-sample-QC reference implementation, phase block NG50 is computed using WhatsHap (whatshap stats) on the phased VCF file (phased.vcf.gz). Phased variants are evaluated per chromosome, and reference sequence lengths are explicitly declared via --chr-lengths (or parsed from VCF header ##contig lines) to establish the denominator $G$. In the generated TSV report, the block_n50 metric from the ALL row is reported; despite the column label, WhatsHap implements this calculation as NG50 because the 50% accumulation threshold is evaluated against the total reference chromosome length rather than the sum of assembled phase blocks. Block boundaries are strictly determined by the first and last phased variant coordinates within each PS phase set. A value of 0 indicates that the cumulative phase block span does not reach 50% of the target genome size, and N/A is reported if reference chromosome lengths are unavailable. The same reference chromosome set (typically autosomes chr1–22) and input variant filtering criteria must be used across all sequencing platforms.
```
# Prepare two-column chromosome lengths file: <chromosome>\t<length>
# (Can be derived directly from the reference FASTA index .fai)
cut -f1,2 reference.fasta.fai > chromosome_lengths.tsv

# Run WhatsHap stats with explicit chromosome lengths
whatshap stats \
  --chr-lengths chromosome_lengths.tsv \
  --tsv phase_stats.tsv \
  phased.vcf.gz

# Extract the genome-wide NG50 (reported as block_n50 under chromosome 'ALL')
awk -F'\t' '
  NR == 1 {
    for (i = 1; i <= NF; i++) {
      if ($i == "chromosome") chr_col = i;
      if ($i == "block_n50") n50_col = i;
    }
  }
  NR > 1 && $chr_col == "ALL" {
    val = $n50_col;
    if (val == "" || val == "nan") print "N/A";
    else print val;
  }
' phase_stats.tsv
```

2.
**Description:** The phase block length $L$ such that phased haplotype blocks of length $\ge L$, sorted in descending order of length, collectively span at least 50% of the agreed reference genome target size ($G$). It is analogous to assembly NG50, substituting contigs with phased haplotype blocks. A phase block is delineated by high-quality, phased heterozygous variants belonging to the same phase set (PS tag in the VCF), and its length is defined as the genomic distance (in base pairs) between the leftmost and rightmost phased variant coordinates in that set. Evaluation is restricted to high-quality (FILTER == "PASS"), non-reference heterozygous SNVs situated within autosomal reference regions (chr1–22), excluding sex chromosomes, unplaced contigs, and assembly gaps to avoid non-diploid distortion. Homozygous variants (0|0, 1|1) and unphased sites are excluded as they do not provide haplotype-linking information. The metric measures long-range haplotype continuity across short-read, contiguous long-read, and discontiguous long-read datasets. For discontiguous long-read datasets (e.g., proximity-ligation or Pore-C), phase blocks must be derived strictly from variant phasing links rather than continuous physical molecule spans.

**Implementation details:** In the NPM-sample-QC reference implementation, phase block NG50 is computed using WhatsHap (whatshap stats) on a pre-filtered, phased VCF. The input callset is normalized and filtered to retain only high-quality (FILTER == "PASS"), biallelic, heterozygous SNVs on autosomal chromosomes (chr1–22) (with adequate depth and quality support (FORMAT/DP >= 10 && FORMAT/GQ >= 20) recommend such threshold?). Reference sequence lengths are provided via --chr-lengths (derived from the reference FASTA .fai index restricted to autosomes) to establish the denominator $G$. In the generated TSV report, the block_n50 metric from the ALL row is reported; despite the column label, WhatsHap implements this calculation as NG50 because the 50% threshold is evaluated relative to the total declared autosomal chromosome length rather than the sum of assembled phase blocks. A value of 0 indicates that cumulative phase blocks do not reach 50% of the target autosomal genome size, and N/A is reported if chromosome lengths are missing or cannot be matched.

```
# 1. Extract autosomal reference chromosome lengths (chr1-chr22) from FASTA index
awk 'BEGIN {
  for (i = 1; i <= 22; i++) autosomes["chr" i] = 1
}
$1 in autosomes { print $1 "\t" $2 }' reference.fasta.fai > autosome_lengths.tsv

# 2. Filter input phased VCF to PASS, biallelic, heterozygous autosomal SNVs
bcftools view \
  -r chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr20,chr21,chr22 \
  -f PASS \
  -g het \
  -m2 -M2 \
  -v snps \
  -i 'FORMAT/DP >= 10 && FORMAT/GQ >= 20' \
  input_phased.vcf.gz \
  -Oz -o filtered_phased_snvs.vcf.gz

tabix -p vcf filtered_phased_snvs.vcf.gz

# 3. Compute phasing statistics using WhatsHap
whatshap stats \
  --chr-lengths autosome_lengths.tsv \
  --tsv phase_stats.tsv \
  filtered_phased_snvs.vcf.gz

# 4. Extract Phase Block NG50 (reported as block_n50 under the ALL row)
awk -F'\t' '
  NR == 1 {
    for (i = 1; i <= NF; i++) {
      if ($i == "chromosome") chr_col = i;
      if ($i == "block_n50") n50_col = i;
    }
  }
  NR > 1 && $chr_col == "ALL" {
    val = $n50_col;
    if (val == "" || val == "nan") print "N/A";
    else print val;
  }
' phase_stats.tsv
```
3.
**Description:** The phase block length $L$ such that phased haplotype blocks of length $\ge L$, sorted in descending order of length, collectively span at least 50% of the agreed reference genome target size ($G$). It is analogous to assembly NG50, substituting contigs with phased haplotype blocks. A phase block is delineated by high-quality, phased heterozygous variants belonging to the same phase set (PS tag in the VCF), and its length is defined as the genomic distance (in base pairs) between the leftmost and rightmost phased variant coordinates in that set. Evaluation is strictly restricted to high-quality (FILTER == "PASS"), non-reference heterozygous SNVs situated within autosomal non-gap reference intervals (chr1–22), excluding sex chromosomes, unplaced contigs, and assembly gap regions (e.g., centromeric/telomeric N tracts). Homozygous variants (0|0, 1|1) and unphased sites are excluded as they do not provide haplotype-linking information. For discontiguous long-read datasets (e.g., proximity-ligation or Pore-C), phase blocks must be derived strictly from variant phasing links rather than continuous physical molecule spans.

**Implementation details:** In the NPM-sample-QC reference implementation, phase block NG50 is computed using WhatsHap (whatshap stats) on a pre-filtered, phased VCF. Target regions are defined by an autosomal non-gap interval BED file (derived by subtracting reference N-regions or assembly gap tracks from autosomes chr1–22). The input callset is filtered to retain only high-quality (FILTER == "PASS"), biallelic, heterozygous SNVs intersecting these intervals (with sufficient depth and quality (FORMAT/DP >= 10 && FORMAT/GQ >= 20) recommend such threshold?). Per-chromosome non-gap base totals are calculated from the BED intervals and supplied to WhatsHap via --chr-lengths to establish the target denominator $G$. In the generated TSV report, the block_n50 metric from the ALL row is reported. A value of 0 indicates that cumulative phase blocks do not reach 50% of the target autosomal non-gap size, and N/A is reported if target lengths are missing or cannot be matched.

To strictly enforce non-gap autosomal intervals (e.g., excluding centromeres, telomeres, and unsequenced N gaps), the interval definition must be applied in two places:

`- Variant filtering (bcftools view -T): Restricts variant evaluation to callable non-gap regions so spurious edge calls are excluded.

  - Denominator calculation ($G$): The length supplied to WhatsHap's --chr-lengths should reflect the effective non-gap base count per chromosome, rather than the raw chromosome coordinate span from the .fai file. If the full coordinate span is used, multi-megabase centromeric assembly gaps will artificially deflate the NG50 metric.
```
# 1. Generate autosomal non-gap intervals and calculate effective chromosome lengths (G)
#    Assume 'autosomes_non_gap.bed' contains non-gap callable intervals for chr1-22
awk '{ lens[$1] += ($3 - $2) } END { for (c in lens) print c "\t" lens[c] }' \
  autosomes_non_gap.bed \
  | sort -k1,1V > autosome_non_gap_lengths.tsv

# 2. Filter input phased VCF to PASS, biallelic, heterozygous SNVs within non-gap autosomes
bcftools view \
  -T autosomes_non_gap.bed \
  -f PASS \
  -g het \
  -m2 -M2 \
  -v snps \
  -i 'FORMAT/DP >= 10 && FORMAT/GQ >= 20' \
  input_phased.vcf.gz \
  -Oz -o filtered_phased_snvs.vcf.gz

tabix -p vcf filtered_phased_snvs.vcf.gz

OR
# 1. Normalize and split multiallelics while preserving phase tags
# 2. Filter strictly for PASS, heterozygous biallelic SNVs within autosomal non-gap BED
bcftools norm -m -any --keep-phased -f reference.fasta input_phased.vcf.gz -Ou \
  | bcftools view \
      -T autosomes_non_gap.bed \
      -f PASS \
      -g het \
      -m2 -M2 \
      -v snps \
      -i 'FORMAT/DP >= 10 && FORMAT/GQ >= 20' \
      -Oz -o filtered_phased_snvs.vcf.gz

tabix -p vcf filtered_phased_snvs.vcf.gz

# 3. Compute phasing statistics using WhatsHap with non-gap lengths
whatshap stats \
  --chr-lengths autosome_non_gap_lengths.tsv \
  --tsv phase_stats.tsv \
  filtered_phased_snvs.vcf.gz

# 4. Extract Phase Block NG50 (reported as block_n50 under the ALL row)
awk -F'\t' '
  NR == 1 {
    for (i = 1; i <= NF; i++) {
      if ($i == "chromosome") chr_col = i;
      if ($i == "block_n50") n50_col = i;
    }
  }
  NR > 1 && $chr_col == "ALL" {
    val = $n50_col;
    if (val == "" || val == "nan") print "N/A";
    else print val;
  }
' phase_stats.tsv


```
- **Type:** Integer, base pairs (eg. 28500000) or N/A when chromosome lengths are unavailable
- **Functionally equivalent implementations:**
  - None currently nominated; candidate implementations require benchmarking against the reference implementation using the same phased variant set, phase-block definitions, chromosome lengths, and chromosome set.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38 (matching chromosome lengths required)
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.