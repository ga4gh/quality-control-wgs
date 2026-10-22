# Median read quality

- **ID:** median_read_quality
- **Description:** 
    - **Pre-Alignment Data:**
   The median of the per-read quality scores across [high-quality reads](terminologies.md#high-quality-reads) in the raw dataset.\
   The per-read score is derived from base quality strings (such as FASTQ QUAL values) or platform-reported read-level quality metrics.\
   This is a read-level calibration metric, not a count of individual bases above a specific quality threshold. For paired-end and discontiguous datasets, each read end is treated as an individual read rather than using read-pair or inferred template lengths.
   
    - **Post-Alignment Data:**
   The median [Phred scaled](terminologies.md#phred-scale) quality score of eligible [high-quality reads](terminologies.md#high-quality-reads) across sequencing datasets.
   Per-read quality is derived from the mean base quality across the sequenced query string or obtained directly from platform-reported summary scores. The median is then calculated across all included reads.
        - **Inclusions & Exclusions:**
            **Included:** 
            Primary alignments, non-overlapping portions of supplementary alignments, unmapped records, [duplicate reads](terminologies.md#duplicated-reads), and [soft-clipped bases](terminologies.md#clipped-bases) measured from the full sequenced query sequence quality score (QUAL) of eligible [high-quality reads](terminologies.md#high-quality-reads). No minimum mapping quality threshold is imposed.\
            **Excluded:** Secondary alignments, supplementary alignments, hard-clipped bases, and reads failing platform or vendor quality controls.
            
            For paired-end and discontiguous sequencing data, each read end is evaluated as an individual read rather than aggregating read pairs or inferred physical templates.\
            This metric serves as a direct indicator of overall sequencing accuracy and basecall reliability across the run.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, median read quality is calculated across mapped and unmapped primary records per-read mean base quality in the declared input BAM/CRAM file. Alignments marked as secondary (0x100) (and supplementary (0x800)) are excluded using samtools (-F 2304), while duplicate reads (0x400) and soft-clipped bases are retained. Only the QUAL string or platform-reported mean basecall Q-score of the of the primary reads is used for reads with supplementary alignments. For contiguous and discontiguous long-read datasets, the median read quality score generated using (`NanoStat --no_supplementary`). For BAM/CRAM files containing platform-specific summary tags, the score can also be evaluated by parsing the per-read mean quality tag (e.g., qs for ONT or -10 * log10(1 - rq) for PacBio).  When the total eligible read count is zero, N/A is reported. The same procedure applies to every sequencing read type. 

Calculate the mean quality score for each read from FASTQ (QUAL) quality strings or use the read-level quality value reported by the platform/basecaller. Then take the median across all included reads.
- **Comments:**
ONT and PacBio quality scores are not assumed to be numerically interchangeable, so results must be benchmarked within technology, chemistry, and basecaller/model strata.
  - For ONT, a Dorado/MinKNOW sequencing summary may instead be supplied so the platform-provided per-read score is used. For PacBio HiFi, use FASTQ qualities or a validated conversion of the BAM `rq` predicted-accuracy tag and document the conversion. 
  - The implementation should define whether failed reads, unclassified reads, unmapped reads, or quality-filtered reads are included.
  - Record input type, quality-score definition, basecaller/consensus-caller model, pass/fail inclusion rule, and any prior filtering. Benchmark ONT and PacBio separately.\
See how platform-reported quality score per read assigned for the primary-supplmentary reads; whether the score is based on full sequences in the read or only the matching and the split segment get it's own mean score **(Inclusion: ! non-overlapping portions of supplementary alignments?)**.
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
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN aligner (Illumina short-read) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** Dorado (ONT) | SMRT Link/CCS (PacBio); record exact version and model.
