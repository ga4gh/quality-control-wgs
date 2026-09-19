# Median read quality

- **ID:** median_read_quality
- **Description:** The median [Phred scaled](terminologies.md#phred-scale) quality score of eligible [high quality reads](terminologies.md#high-quality-reads) across short-read, contiguous long-read, and discontiguous long-read datasets. The eligible-read population comprises (only primary alignments?) mapped and unmapped primary records, excluding secondary and supplementary alignments to prevent multi-aligned segments from being counted multiple times. Duplicate reads are retained. For short-read data, the per-read quality is derived from the mean base quality across the sequenced query string. For contiguous long-read data, platform-standard tags are used where available, such as the Dorado or MinKNOW qs tag (mean basecall Q-score) for ONT, or the rq tag (predicted read accuracy converted to Phred scale) for PacBio. For paired-end short-read and discontiguous long-read data, each read end is evaluated as an individual read rather than aggregating read pairs or inferred physical templates. This metric serves as a direct indicator of sequencing accuracy and basecall reliability across the run.
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, median read quality is calculated across mapped and unmapped primary records in the declared input BAM/CRAM file. Alignments marked as secondary (0x100) and supplementary (0x800) are excluded using samtools (-F 2304), while duplicate reads (0x400) are retained. For contiguous and discontiguous long-read datasets, the median read quality score generated using (`NanoStat --no_supplementary`). For BAM/CRAM files containing platform-specific summary tags, the score can also be evaluated by parsing the per-read mean quality tag (e.g., qs for ONT or -10 * log10(1 - rq) for PacBio). When the total eligible read count is zero, N/A is reported. The same procedure applies to every sequencing read type.
- **Comments:**
  - The median of the per-read quality scores across reads in the dataset. The per-read score must be the score reported by the platform/basecaller or the explicitly documented score derived from the read's base qualities. This is a read-level calibration metric, not a count of individual bases above a Q threshold. ONT and PacBio quality scores are not assumed to be numerically interchangeable, so results must be benchmarked within technology, chemistry, and basecaller/model strata.
  - For ONT, a Dorado/MinKNOW sequencing summary may instead be supplied so the platform-provided per-read score is used. For PacBio HiFi, use FASTQ qualities or a validated conversion of the BAM `rq` predicted-accuracy tag and document the conversion. 
  - Calculate the mean quality score for each read from FASTQ quality strings or use the read-level quality value reported by the basecaller. Then take the median across all included reads. The implementation should define whether failed reads, unclassified reads, unmapped reads, or quality-filtered reads are included.
  - Record input type, quality-score definition, basecaller/consensus-caller model, pass/fail inclusion rule, and any prior filtering. Benchmark ONT and PacBio separately.
```
# Option 1: Direct long-read text extraction via NanoStat (excludes supplementary, no plots generated)
NanoStat --bam input.bam \
  --no_supplementary \
  --threads 4 \
  > nanostats.txt

# Extract median read quality
awk -F':' '/Median read quality/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' '

# Option 2: Direct tag extraction via samtools for ONT BAMs (using the Dorado/MinKNOW 'qs' tag)
samtools view -F 2304 input.bam \
  | grep -o 'qs:f:[^[:space:]]*' \
  | cut -d':' -f3 \
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
- **Type:** Float, Phred-scaled quality score (eg. 16.8)
- **Functionally equivalent implementations:**
  - [Dorado summary v2.1.0](https://github.com/nanoporetech/dorado) followed by the median of `mean_qscore_template` for ONT BAM/CRAM
  - [pycoQC](https://github.com/a-slide/pycoQC) using the same complete ONT read set and inclusion rules
- **Sequencing read type:** contiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCH38
- **Version:** 2.0
- **Sequencing technology:** Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio)
- **Associated aligner:** N/A
- **Associated variant caller:** N/A
- **Associated basecaller:** Dorado (ONT) | SMRT Link/CCS (PacBio); record exact version and model.
