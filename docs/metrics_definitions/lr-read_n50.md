# Read N50

- **ID:** read_n50
- **Description:** The length-weighted median read length of eligible [high-quality reads](terminologies.md#high-quality-reads) in a sequencing dataset. It is defined as the read length $L$ such that reads of length $\ge L$, when sorted in descending order of length, contain at least 50% of the total sequenced base yield. The eligible-read population comprises mapped and unmapped primary records, excluding secondary and supplementary alignments while retaining duplicate reads. Read length is measured from the full sequenced query string (SEQ length, including soft-clipped bases but excluding hard-clipped bases). For paired-end short-read and discontiguous long-read datasets, each read end is evaluated as an individual read rather than aggregating read pairs or inferred physical template lengths. For short-read datasets, Read N50 reflects the read-length distribution after quality or adapter trimming. For contiguous long-read datasets, it serves as a key indicator of high-molecular-weight DNA integrity and library fragment size.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, Read N50 is computed across mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). Secondary (0x100) and supplementary (0x800) alignments are excluded using [samtools `view`](https://www.htslib.org/doc/samtools-view.html) (-F 2304), while duplicate reads (0x400) are retained. Query lengths (SEQ length) are sorted in descending order, and lengths are accumulated until the cumulative sum meets or exceeds 50% of the total sequenced base yield. For paired-end short-read or discontiguous long-read data, each mate is counted separately as an individual read. For long-read datasets, this can be extracted directly using (`NanoStat --no_supplementary`). When total base yield is zero, N/A is reported. The same procedure applies to every sequencing read type.
- **Comments:**
  - Also, applicable to raw sequencing data/before alignemnt/mapping.
  - Calculation must state whether adapter trimming, quality trimming, clipping, instrument filtering, or platform-specific pass/fail filtering was performed before the metric was calculated?
```
# Option 1: Universal calculation via samtools + awk
samtools view -F 2304 input.bam \
  | awk '{print length($10)}' \
  | sort -nr \
  | awk '
    {
      lens[NR] = $1
      total_bp += $1
    }
    END {
      if (total_bp == 0) { print "N/A"; exit }
      half_bp = total_bp / 2
      cum = 0
      for (i = 1; i <= NR; i++) {
        cum += lens[i]
        if (cum >= half_bp) {
          print lens[i]
          exit
        }
      }
    }'

# Option 2: Long-read extraction via NanoStat (no plots generated)
NanoStat --bam input.bam \
  --no_supplementary \
  --threads 4 \
  > nanostats.txt

# Extract N50 from NanoStat summary table
awk -F':' '/Read length N50/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' '
```
- **Type:** Integer, base pairs (eg. 150)
- **Functionally equivalent implementations:**
  - [SeqFu `stats`](https://telatin.github.io/seqfu2/tools/stats.html), using the identical read set and reporting N50
  - [seqkit `stats`]()
  - [samtools `stats`](https://www.htslib.org/doc/samtools-stats.html) read-length distribution with exact N50 post-processing, when BAM or CRAM contains the same read population and each read is counted once
  - [NanoPlot](https://github.com/wdecoster/NanoPlot), without downsampling, for contiguous-long-read data
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** N/A
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** N/A
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
