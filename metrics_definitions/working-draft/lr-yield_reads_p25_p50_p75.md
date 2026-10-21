# Read length percentiles (P25, P50, P75)

- **ID:** `read_length_percentiles_p25_p50_p75`
- **Description:** 
   The read lengths, in base pairs, at the 25th percentile (P25), 50th percentile (median / P50), and 75th percentile (P75) of the read-length distribution derived from [high-quality reads](terminologies.md#high-quality-reads) across sequencing datasets.
   For every qualifying primary record, the full sequenced query length (including [soft-clipped bases](terminologies.md#clipped-bases), but excluding hard-clipped bases) is added to the cumulative yield for the respective quality threshold.
   
        - **Inclusions & Exclusions:**

            **Included:** 
            Mapped and unmapped primary records, duplicate reads, and [soft-clipped bases](terminologies.md#clipped-bases) (measured from the full sequenced query sequence length/(SEQ) length).\
            **Excluded:** Secondary alignments, supplementary alignments (to prevent multi-aligned segments from distorting the distribution), and hard-clipped bases.
            
            For paired-end and discontiguous sequencing data, each read end is evaluated as an individual read rather than aggregating read pairs or measuring inferred physical template spans.\
            These quartiles summarize read-length spread, library fragmentation, and tail skewness, particularly for long-read datasets where lengths vary substantially.

        **Inferred Template Length Percentiles (P25, P50, P75) (Discontiguous Long-Read)** (`inferred_template_length_percentiles_p25_p50_p75`)
         The lengths, in base pairs, at the 25th percentile (P25), 50th percentile (median / P50), and 75th percentile (P75) of the physical template length distribution derived from [high-quality reads](terminologies.md#high-quality-reads) in discontiguous long-read sequencing datasets.\
        &ensp;Grouping: Chimeric segments or paired/multiplexed read segments that originate from the same physical molecule or concatemer are grouped and evaluated as a single template unit rather than treating individual read ends separately.\
        &ensp;Length Determination: The length of each inferred template is measured by its genomic span (the distance between the outermost mapped coordinates of its constituent segments) or its total constituent base length, depending on the analytical implementation.
        - **Inclusions & Exclusions:**

            **Included:** 
            Duplicate templates (unless explicitly filtered out).\
            **Excluded:** Secondary and supplementary alignments from initiating new template length calculations.\
            These quartiles summarize the size distribution, fragmentation profile, and structural span of the original input library molecules, serving as a key indicator of proximity-ligation success and library integrity.

    - **Pre-Alignment Data:**
   The read lengths, in base pairs, at the 25th percentile (P25), median (P50), and 75th percentile (P75) of the read-length distribution derived from [high-quality reads](terminologies.md#high-quality-reads) across sequencing datasets.\
   For paired-end and discontiguous datasets, each read end is treated as an individual read rather than using read-pair or inferred template lengths.

- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, read-length percentiles are calculated from mapped and unmapped primary records in the declared input BAM/CRAM file that satisfy the sequencing-read-type-specific [high-quality reads](terminologies.md#high-quality-reads) criteria. Secondary (0x100) (and supplementary (0x800) alignements, and reads not passing platform/vendor quality controls (0x200) are excluded) alignments are excluded using samtools (-F 2304), while duplicate reads (0x400) are retained. Query lengths (SEQ length) are extracted, sorted, and evaluated at the rank indices for the 25th, 50th, and 75th percentiles. Only the query length (SEQ length) of the primary alignment is used for reads with supplementary alignments. For long-read datasets, this can also be extracted directly using (`NanoStat --no_supplementary`). If the total eligible read count is zero, N/A is reported for all quartiles. The same procedure applies to every sequencing read type.
- **Comments:**
```
# Option 1: Fast quartile extraction via samtools + awk
samtools view -F 2304 input.bam \
  | awk '{print length($10)}' \
  | sort -n \
  | awk ' {
      a[NR] = $1
    }
    END {
      if (NR == 0) {
        print "P25: N/A\nP50: N/A\nP75: N/A";
        exit;
      }
      p25_idx = int(NR * 0.25 + 0.5); if (p25_idx < 1) p25_idx = 1;
      p50_idx = int(NR * 0.50 + 0.5); if (p50_idx < 1) p50_idx = 1;
      p75_idx = int(NR * 0.75 + 0.5); if (p75_idx < 1) p75_idx = 1;

      printf "P25: %d\n", a[p25_idx];
      printf "P50: %d\n", a[p50_idx];
      printf "P75: %d\n", a[p75_idx];
    }'
# samtools view -F 2304 input.bam | awk '{print length($10)}' | datamash q1 1 median 1 q3 1

# Option 2: Long-read text extraction via NanoStat (no plots generated)
NanoStat --bam input.bam \
  --no_supplementary \
  --threads 4 \
  > nanostats.txt

# Extract quartiles from the NanoStat text summary table
p25=$(awk -F':' '/Read length quartile 25%/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' ')
p50=$(awk -F':' '/Median read length/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' ')
p75=$(awk -F':' '/Read length quartile 75%/ {gsub(/,/, "", $2); print $2}' nanostats.txt | tr -d ' ')

echo "P25: $p25"
echo "P50: $p50"
echo "P75: $p75"
```
- **Type:** Integer (bp), reported as three values: P25, P50, and P75
- **Functionally equivalent implementations:**
  - [NanoPlot](https://github.com/wdecoster/NanoPlot) without downsampling
  - [pycoQC](https://github.com/a-slide/pycoQC) using the complete read set
- **Sequencing read type:** contiguous-long-read
- **Reference genome assembly:** N/A
- **Version:** 2.0
- **Sequencing technology:** Oxford Nanopore Technologies (ONT) | Pacific Biosciences (PacBio)
- **Associated aligner:** N/A
- **Associated basecaller:** Dorado (ONT) | SMRT Link/CCS (PacBio); record the exact version and model.
