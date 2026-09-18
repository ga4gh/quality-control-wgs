# Read number
- **ID:** read_number
- **Description:** The total number of [high quality reads](terminologies.md#high-quality-reads) across short-red, continuous-long-read, discontiguous-long-read datasets, excluding supplementary and secondary alignments. Duplicate reads are included. For paired-end short-read and discontiguous long-read data, each read end is counted as an individual read rather than counting read pairs or inferred templates (e.g., proximity ligation molecules/templates). Read count should be interpreted alongside total base yield and read-length distributions, particularly for long-read datasets where read lengths vary substantially.

  - **Inferred Template Count (Discontiguous Long-Read)**
The total number of [high quality reads](terminologies.md#high-quality-reads) inferred physical templates (molecules) derived from discontiguous long-read sequencing (e.g., proximity-ligation or pore-C data). In this metric, all chimeric segments or paired/multiplexed read segments originating from the same physical molecule or concatemer are grouped and enumerated as a single inferred template, rather than counting individual alignment segments or read ends separately. Secondary and supplementary alignments are excluded from initiating new template counts. Duplicate templates are included unless otherwise specified? This metric reflects original input library molecule yield and should be evaluated alongside segment count and contact distribution.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, read counts are calculated by enumerating [high quality reads](terminologies.md#high-quality-reads) across short-read, contiguous-long-read, and discontiguous-long-read datasets. Alignments marked as secondary (0x100) and supplementary (0x800) are excluded using samtools (`samtools view -c -F 0x900`), while duplicate reads (0x400) are retained. For short paired-end and discontiguous datasets, each read end is counted as an individual read. For long-read datasets, total read counts, can be generated using (`NanoStat --no_supplementary`).

  - **Inferred Template Count (Discontiguous Long-Read)**
In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, inferred physical templates from discontiguous long-read datasets (e.g., TruPath, Pore-C or Hi-C concatemers) are determined by collapsing read alignments by molecule/read ID. Using samtools, secondary and supplementary alignments are excluded (-F 2304) to prevent duplicate segment tallying, and the primary QNAME identifiers (field 1) are deduplicated to produce the final physical template count.

Template-level metrics shall exclude singleton reads for which no containing template is defined.
Technology-specific implementation details (e.g., BX tags, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition.
- **Comments:**
use all the reads unmapped+primary alignment or primary alignments only?
excluding supplementary and secondary reads and duplicate reads are included.
  - **Count Inferred Template:**
```
# Count unique physical templates by extracting unique read IDs (QNAME)
# Excludes secondary and supplementary alignments (0x900 / 2304)
samtools view -F 2304 input_discontiguous.bam \
  | cut -f1 \
  | sort -u \
  | wc -l
```
  - **Count Read:**
```
# Option 1: Fast direct count via samtools
# Flag 2304 (0x900) excludes secondary (256) and supplementary (2048) records
samtools view -c -F 2304 input.bam
samtools stats 'raw total sequences'
samtools idxstats input.bam | awk '{mapped+=$3; unmapped+=$4} END {print "Total Primary Reads: " (mapped + unmapped)}'

# Option 2: Long-read text metrics via NanoStat (excludes supplementary, no plots generated)
NanoStat --bam input.bam \
  --no_supplementary \
  --threads 4 \
  > nanostats.txt

# Extract the high-quality read count from the NanoStat output
awk -F':' '/Number of reads/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' '
```
- **Type:** Integer (eg. 18452391)
- **Functionally equivalent implementations:**
  - [SeqFu `stats`](https://telatin.github.io/seqfu2/tools/stats.html), using the identical read set and reporting the sequence count
  - [samtools `view -c`](https://www.htslib.org/doc/samtools-view.html), with matching primary-record and read-inclusion filters when BAM or CRAM is used
  - [NanoPlot](https://github.com/wdecoster/NanoPlot), without downsampling, for contiguous-long-read data
  - [pycoQC](https://github.com/a-slide/pycoQC), using the complete declared ONT read set
- **Sequencing read type:** short-read | contiguous-long-read | discontiguous-long-read
- **Reference genome assembly:** N/A
- **Version:** 2.0
- **Sequencing technology:** Illumina | Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio) | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** N/A
- **Associated variant caller:** N/A
- **Associated basecaller:** N/A (Illumina short-read and proximity mapped reads) | Dorado/MinKNOW integrated Dorado (ONT) | SMRT Link/CCS (PacBio). Record the exact version and model where applicable.
