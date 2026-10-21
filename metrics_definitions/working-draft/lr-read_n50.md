# Read N50

- **ID:** read_n50
- **Description:** 
    - **Post-Alignment Data:**
   The length-weighted median read length of eligible [high-quality reads](terminologies.md#high-quality-reads) across short-read, contiguous long-read, and discontiguous long-read datasets. It is defined as the read length L such that reads of length ≥ L, when sorted in descending order, contain at least 50% of the total sequenced base yield.
        - **Inclusions & Exclusions:**

            **Included:** 
            Mapped and unmapped primary records, [duplicate reads](terminologies.md#duplicated-reads), and [soft-clipped bases](terminologies.md#clipped-bases) (measured from the full sequenced query string/SEQ length).\
            **Excluded:** Secondary alignments, supplementary alignments, and hard-clipped bases.\
            \
            For paired-end short-read and discontiguous long-read datasets, each read end is evaluated as an individual read rather than aggregating read pairs or inferred physical template lengths.\

        **Inferred Template N50 (Discontiguous Long-Read)(`inferred_template_n50`)**
         The length-weighted median length of inferred physical templates (molecules) derived from discontiguous long-read sequencing datasets. It is defined as the template length L such that templates of length ≥ L, when sorted in descending order of length, account for at least 50% of the total cumulative length of all inferred templates.\
        &ensp;Grouping: Relies on chimeric segments or paired/multiplexed read segments that originate from the same physical molecule or concatemer, grouped and evaluated as a single template unit rather than treating individual read ends or alignment segments separately.\

        > Length Determination: The length of each inferred template is typically measured by its genomic span (the distance between the outermost mapped coordinates of its constituent segments) or total constituent base length, depending on the specific analytical implementation.
        - **Inclusions & Exclusions:**

            **Included:** 
            Duplicate templates (unless explicitly filtered out).\
            **Excluded:** Secondary and supplementary alignments from initiating new template length calculations.\
            This metric evaluates the size distribution and structural integrity of the original input library molecules, serving as a key indicator of proximity-ligation efficiency and long-range capture success.

    - **Pre-Alignment Data:**
   The length-weighted median read length within the raw sequencing dataset, defined as the read length $L$ such that 50% of the total sequenced bases are contained in reads with length ≥ L.\
   For short-read and discontiguous long-read paired-end datasets, each read end is treated as an individual read rather than using read-pair or inferred template lengths.\
   \
   Short-Read Datasets: Reflects the read-length distribution after quality or adapter trimming.\
   Contiguous Long-Read Datasets: Serves as a key indicator of high-molecular-weight (HMW) DNA integrity and library fragment size.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, Read N50 is computed across mapped and unmapped primary records of sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads). Secondary (0x100) (and supplementary (0x800) alignements, and reads not passing platform/vendor quality controls (0x200) are excluded)) alignments are excluded using [samtools `view`](https://www.htslib.org/doc/samtools-view.html) (-F 2304), while duplicate reads (0x400) and soft-clipped bases are retained. Query lengths (SEQ length) are sorted in descending order, and lengths are accumulated until the cumulative sum meets or exceeds 50% of the total sequenced base yield. Only the query length (SEQ length) of the primary alignment is used for reads with supplementary alignments. For paired-end short-read or discontiguous long-read data, each mate is counted separately as an individual read. For long-read datasets, this can be extracted directly using (`NanoStat --no_supplementary`). When total base yield is zero, N/A is reported. The same procedure applies to every sequencing read type.

Use the read sequences present in the declared input dataset; Do not downsample. If a sample spans multiple files, combine all included read lengths or concatenate the files losslessly before calculation; never average per-file N50 values. For paired short-read or discontiguous-long-read data, include the eligible reads from both mates in one sample-level calculation and count each mate separately.
- **Comments:**
  - Applicable to raw sequencing data before alignemnt/mapping.
  - Calculation must state whether adapter trimming, quality trimming, hard clipping, instrument filtering, or platform-specific pass/fail filtering was performed before the metric was calculated?
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
