# Genome coverage uniformity

- **ID:** genome_coverage_uniformity
- **Description:** A sequencing-read-type-specific measure of how evenly usable sequencing depth is distributed across defined autosomal non-gap evaluation regions of the selected reference genome.
  - Short-read and discontiguous long-read datasets: Evaluated across the pooled per-base depth distribution within the target intervals, including zero-coverage positions. Report the 25th percentile (Q1), median (Q2), 75th percentile (Q3), interquartile range ($\text{IQR} = \text{Q3} - \text{Q1}$), and unscaled Median Absolute Deviation ($\text{MAD} = \text{median}(\vert{}d_i - \text{median}(d)\vert{})$). Coverage is derived exclusively from non-duplicate primary alignments of [high-quality reads](terminologies.md#high-quality-reads); unmapped (0x4), secondary (0x100), QC-failed (0x200), duplicate (0x400) records are excluded.(, and supplementary (0x800) records are excluded (-F 3844)?). Overlapping paired-end segments are counted only once per physical template. For discontiguous long reads, only directly sequenced and mapped segments contribute to coverage; inferred intervening template spans must not be counted as continuous coverage.
  - Contiguous long-read datasets: Evaluated by partitioning the autosomal non-gap evaluation intervals into non-overlapping, contiguous 10,000-bp windows (excluding edge windows shorter than 10,000 bp). Zero-coverage windows are retained. Across all window mean depths, report the 25th percentile (Q1), median (Q2), 75th percentile (Q3), interquartile range ($\text{IQR} = \text{Q3} - \text{Q1}$), and unscaled $\text{MAD} = \text{median}(\vert{}D_i - \text{median}(D)\vert{})$. Input reads are restricted to non-duplicate primary alignments of [high-quality reads](terminologies.md#high-quality-reads) meeting platform-specific quality thresholds using read-level tags (qs for ONT, rq for PacBio) without filtering on individual base qualities.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, coverage distributions are calculated strictly over the autosomal non-gap interval file using `mosdepth`. Input records are restricted to [high-quality reads](terminologies.md#high-quality-reads) by excluding unmapped, secondary, QC-failed, duplicate reads `--flag 1796`. For short-read and discontiguous long-read data, overlapping paired bases are resolved natively by `mosdepth` without double counting. Summary statistics (Q1, Median, Q3, IQR (Q3 - Q1), unscaled MAD) are computed directly from the discrete cumulative frequency distribution in `*.mosdepth.region.dist.txt`. For contiguous long-read data, window-level mean depths are generated across fixed 10,000-bp bins using `mosdepth`. Non-parametric summary statistics are computed across the window mean values (column 4 of `*.regions.bed.gz`). If the evaluation region contains zero valid intervals, N/A is reported for all metrics.

  - Record the tool versions, reference assembly, evaluation-region checksum, 10-kb-window checksum and treatment of partial windows for the contiguous-long-read profile, base- or per-read-quality profile, per-read quality threshold where applicable, aligner, and basecaller or consensus-caller version. Per-base MAD values for short-read and discontiguous-long-read data and 10-kb window summaries for contiguous-long-read data describe uniformity at different scales and must not be compared as numerically equivalent values.

- **Comments:**
  - short paired-end mosdepth default setting. For contiguous long-read use --fast-mode / -x though it's not check the overlapping physical pair-end reads, it massive number of small insertions and deletions compared to short reads. Evaluating every tiny CIGAR operation adds extreme computational overhead. Skipping internal CIGAR operations (treating the read as a continuous block from start to end) is standard practice for long-read coverage tracking. With and without '-x' yield virtually identical coverage profiles.
  - replace this line to implementation detaion details:? For short paired-end read and discontiguous-long-read data, overlapping paired bases are resolved natively by mosdepth without double counting; also exclude **supplementary alignments** (0x800), --flag 3844 is explicitly specified.
  - high quality reads - reads passing the sequencing instrument/vendor quality filter / instrument-filter-passing reads where such a filter exists; SAM flag 0x200 not set. For contiguous-long reads quality thresholds using read-level tags (qs for ONT, rq for PacBio).
  - if exclude supplementary (0x800) reads then   $1796 + 2048 = \mathbf{3844}$ (or $\mathbf{3852}$ also excluding 0x8 unmapped mate, though 0x4 covers the read itself).

```
# ------------------------------------------------------------------------------
# 1. Short-Read & Discontiguous Long-Read (Per-Base Metrics)
# ------------------------------------------------------------------------------
mosdepth \
  --threads 4 \
  --by autosomes_non_gap.bed \
  --thresholds 5,10,15 \
  --flag 3844 \
  --no-per-base \
  short_read_qc \
  input_short_read.bam

# Extract Mean Coverage
mean_cov=$(awk '$1 == "total_region" { print $4 }' short_read_qc.mosdepth.summary.txt)

# Extract Percentage >= 5x, 10x, 15x
read pct_5x pct_10x pct_15x < <(awk '
  $1 == "total" {
    total_bases = $2
    if (total_bases > 0) {
      printf "%.2f %.2f %.2f\n", ($4 / total_bases) * 100, ($5 / total_bases) * 100, ($6 / total_bases) * 100
    } else {
      print "0.00 0.00 0.00"
    }
  }' short_read_qc.thresholds.bed.gz)

# Compute Q1, Median, Q3, IQR, and unscaled MAD from region distribution
read q1 med q3 iqr mad < <(awk '
  $1 == "total" {
    depth = $2
    prop_gt = $3
    cum_gt[depth] = prop_gt
    if (depth > max_d) max_d = depth
  }
  END {
    if (max_d == "") {
      print "N/A N/A N/A N/A N/A"
      exit
    }

    # Reconstruct discrete frequency at each depth
    for (d = 0; d <= max_d; d++) {
      p_at_least = (d == 0) ? 1.0 : ((d - 1 in cum_gt) ? cum_gt[d - 1] : 0.0)
      p_gt = (d in cum_gt) ? cum_gt[d] : 0.0
      freq[d] = p_at_least - p_gt
    }

    # Cumulative distribution for quartiles
    cum = 0
    q1 = -1; med = -1; q3 = -1
    for (d = 0; d <= max_d; d++) {
      cum += freq[d]
      if (q1 == -1 && cum >= 0.25) q1 = d
      if (med == -1 && cum >= 0.50) med = d
      if (q3 == -1 && cum >= 0.75) { q3 = d; break }
    }
    iqr = q3 - q1

    # Absolute deviations around median
    for (d = 0; d <= max_d; d++) {
      dev = (d >= med) ? (d - med) : (med - d)
      dev_freq[dev] += freq[d]
      if (dev > max_dev) max_dev = dev
    }

    # Median of absolute deviations
    cum_dev = 0; mad = 0
    for (dev = 0; dev <= max_dev; dev++) {
      cum_dev += dev_freq[dev]
      if (cum_dev >= 0.50) { mad = dev; break }
    }

    print q1, med, q3, iqr, mad
  }' short_read_qc.mosdepth.region.dist.txt)

echo "Mean Coverage: $mean_cov"
echo "Coverage >= 5x: ${pct_5x}%"
echo "Coverage >= 10x: ${pct_10x}%"
echo "Coverage >= 15x: ${pct_15x}%"
echo "Per-Base Q1: $q1"
echo "Per-Base Median (Q2): $med"
echo "Per-Base Q3: $q3"
echo "Per-Base IQR: $iqr"
echo "Per-Base MAD (unscaled): $mad"

# ------------------------------------------------------------------------------
# 2. Contiguous Long-Read (10-kb Window Mean Metrics)
# ------------------------------------------------------------------------------
# Pre-filter: Windows must be strictly full-length 10,000 bp
bedtools makewindows \
  -b autosomes_non_gap.bed \
  -w 10000 \
  | awk '($3 - $2) == 10000' > autosomes_non_gap_10kb_windows.bed

mosdepth \
  -x \
  --threads 4 \
  --by autosomes_non_gap_10kb_windows.bed \
  --thresholds 5,10,15 \
  --flag 3844 \
  --no-per-base \
  long_read_10kb \
  input_long_read.bam

# Extract Mean Coverage and Thresholds
lr_mean_cov=$(awk '$1 == "total_region" { print $4 }' long_read_10kb.mosdepth.summary.txt)
read lr_pct_5x lr_pct_10x lr_pct_15x < <(awk '
  $1 == "total" {
    total_bases = $2
    if (total_bases > 0) {
      printf "%.2f %.2f %.2f\n", ($4 / total_bases) * 100, ($5 / total_bases) * 100, ($6 / total_bases) * 100
    } else {
      print "0.00 0.00 0.00"
    }
  }' long_read_10kb.thresholds.bed.gz)

# Compute Q1, Median, Q3, IQR, and unscaled MAD from 10-kb window means
zcat long_read_10kb.regions.bed.gz \
  | awk '{ print $4 }' \
  | sort -g \
  | awk '
    {
      w[NR] = $1
    }
    END {
      if (NR == 0) {
        print "Q1: N/A\nMedian: N/A\nQ3: N/A\nIQR: N/A\nMAD: N/A"
        exit
      }

      q1_i = int(NR * 0.25 + 0.5); if (q1_i < 1) q1_i = 1
      m_i  = int(NR * 0.50 + 0.5); if (m_i < 1)  m_i = 1
      q3_i = int(NR * 0.75 + 0.5); if (q3_i < 1) q3_i = 1

      q1  = w[q1_i]
      med = w[m_i]
      q3  = w[q3_i]
      iqr = q3 - q1

      for (i = 1; i <= NR; i++) {
        dev[i] = (w[i] >= med) ? (w[i] - med) : (med - w[i])
      }

      n = asort(dev)
      mad_i = int(n * 0.50 + 0.5); if (mad_i < 1) mad_i = 1
      mad = dev[mad_i]

      printf "Window Mean Q1: %.2f\n", q1
      printf "Window Mean Median: %.2f\n", med
      printf "Window Mean Q3: %.2f\n", q3
      printf "Window Mean IQR: %.2f\n", iqr
      printf "Window Mean MAD (unscaled): %.2f\n", mad
    }'
```
- **Type:** Sequencing-read-type-specific: Float for short-read and discontiguous-long-read per-base MAD (eg. 4.00) | Structured numeric summary for contiguous-long-read data (eg. Q1: 27.40; median: 30.10; Q3: 32.60; IQR: 5.20; MAD: 2.10)
- **Functionally equivalent implementations:**
  - [ICGC-ARGO dnaalnqc](References.md#icgc-argo) for the short-read or discontiguous-long-read profile when it reproduces the reference implementation's intervals and filtering.
  - [samtools depth](https://www.htslib.org/doc/samtools-depth.html), followed by an exact per-base MAD calculation that includes zero-coverage positions, for short-read or discontiguous-long-read data when the same evaluation intervals, base-quality threshold, mapping-quality threshold, duplicate policy, primary-alignment policy, and overlap policy are used.
  - [samtools depth](https://www.htslib.org/doc/samtools-depth.html) followed by the identical 10-kb aggregation for the contiguous-long-read profile after the same per-read quality and alignment filtering.
  - [bedtools genomecov](https://bedtools.readthedocs.io/en/latest/content/tools/genomecov.html) followed by the identical 10-kb aggregation, after reproducing the applicable sequencing-read-type-specific filtering and overlap policy.
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN mapper (Illumina short-read) | minimap2 (ONT) | pbmm2/minimap2 (PacBio) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** GATK Haplotypecaller v4.6.2.0, Mutect2, DRAGEN 3.8, DRAGEN v4.4.7, DeepVariant
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.