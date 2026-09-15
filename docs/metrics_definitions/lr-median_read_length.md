# Median read length
- **ID:** median_read_length
- **Description:** The median length, in base pairs, of eligible [high quality reads](terminologies.md#high-quality-reads) across short-read, contiguous long-read, and discontiguous long-read datasets. Secondary and supplementary alignments are excluded to prevent multialigned segments from skewing the distribution, while duplicate reads are retained. Read length is determined from the full sequenced query sequence including soft-clipped bases. For paired-end short-read and discontiguous long-read data, each read end is evaluated as an individual read rather than aggregating read pairs or measuring inferred physical template spans. This metric reflects sequencing run performance and fragmentation dynamics, and it should be interpreted alongside the total base yield, and read count.

**Median Inferred Template Span (Discontiguous Long-Read):**
The median genomic span, in base pairs, of [high quality reads](terminologies.md#high-quality-reads) inferred physical templates (molecules) derived from discontiguous long-read sequencing (e.g., proximity-ligation or Pore-C data). In this metric, all chimeric segments or multiplexed read alignments belonging to the same physical molecule or concatemer are grouped, and the span is measured across the outermost reference mapping coordinates for each template, rather than measuring individual alignment segment lengths. Secondary and supplementary alignments are excluded from initiating new templates. Duplicate templates are included unless otherwise specified?. This metric reflects the physical fragment size or contact distribution captured by the proximity library.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, median read length is calculated from [high quality reads](terminologies.md#high-quality-reads) (primary alignments?) primary records including unmapped reads in the declared input BAM/CRAM file. Secondary (0x100) and supplementary (0x800) alignments are excluded using samtools (-F 2304), while duplicate reads (0x400) are retained. The query sequence length of each eligible read (SEQ length, which accounts for soft clips but excludes hard clips) is extracted, sorted, and the median is computed. For long-read datasets, this can also be extracted directly using (`NanoStat --no_supplementary`). When the total read count is zero, N/A is reported. The same procedure applies to every sequencing read type.

**Median Inferred Template Span (Discontiguous Long-Read)**
In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, the median template span for discontiguous long-read datasets (e.g., Pore-C or Hi-C concatemers) is computed by grouping [high quality reads](terminologies.md#high-quality-reads) primary and supplementary alignment segments by template identifier (QNAME). Secondary alignments (0x100) and unmapped reads (0x4) are excluded. For intra-chromosomal alignments belonging to the same template, the outermost genomic span is determined as (max_end - min_start + 1). The resulting template spans are sorted and the median is calculated. Inter-chromosomal contacts are excluded from linear template span calculations, and N/A is reported if no multi-alignment intra-chromosomal templates exist.
- **Comments:**
  - if only primary alignments, update the samtools filter to exclude unmapped reads by adding 0x4 (flag 2308 / 0x904).
```
  # Option 1: Fast direct extraction and median calculation via samtools + awk
samtools view -F 2304 input.bam \
  | awk '{print length($10)}' \
  | sort -n \
  | awk ' {
      a[NR] = $1
    }
    END {
      if (NR == 0) { print "N/A"; exit }
      if (NR % 2 == 1) {
        print a[(NR + 1) / 2]
      } else {
        print (a[NR / 2] + a[(NR / 2) + 1]) / 2
      }
    }'

# Option 2: Long-read text extraction via NanoStat (no plots generated)
NanoStat --bam input.bam \
  --no_supplementary \
  --threads 4 \
  > nanostats.txt

# Extract median read length
awk -F':' '/Median read length/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' '
```
**Template Span:**
```
# Filter to mapped, non-secondary segments, group by QNAME and chromosome, and compute linear genomic spans
samtools view -F 260 input_discontiguous.bam \
  | awk '{
      # Calculate end position from POS and CIGAR reference consumption
      qname = $1; rname = $3; pos = $4; cigar = $6;
      end = pos;
      while (match(cigar, /[0-9]+[MIDNX=]/)) {
        val = substr(cigar, RSTART, RLENGTH - 1);
        op = substr(cigar, RSTART + RLENGTH - 1, 1);
        if (op ~ /[MDNX=]/) end += val;
        cigar = substr(cigar, RSTART + RLENGTH);
      }
      key = qname "\t" rname;
      if (!(key in min) || pos < min[key]) min[key] = pos;
      if (!(key in max) || end > max[key]) max[key] = end;
    }
    END {
      for (k in min) {
        span = max[k] - min[k] + 1;
        if (span > 0) print span;
      }
    }' \
  | sort -n \
  | awk ' {
      a[NR] = $1
    }
    END {
      if (NR == 0) { print "N/A"; exit }
      if (NR % 2 == 1) {
        print a[(NR + 1) / 2]
      } else {
        print (a[NR / 2] + a[(NR / 2) + 1]) / 2
      }
    }'
```
- **Type:** Integer, base pairs (eg. 7800)
- **Functionally equivalent implementations:**
  - [NanoPlot](https://github.com/wdecoster/NanoPlot) without downsampling
  - [pycoQC](https://github.com/a-slide/pycoQC) using the complete read set
  - [samtools stats](https://www.htslib.org/doc/samtools-stats.html) read-length distribution with exact median post-processing
- **Sequencing read type:** contiguous-long-read
- **Reference genome assembly:** GRCh37 |GRCh38
- **Version:** 2.0
- **Sequencing technology:** Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio)
- **Associated aligner:** N/A
- **Associated variant caller:** N/A
- **Associated basecaller:** Dorado (ONT) | SMRT Link/CCS (PacBio); record exact version and model.
