
# Bases ≥ Q30

- **ID:** yield_bp_q30
- **Description:** 
    - **Post-Alignment Data:**
   The total number of bases with a [base quality score](terminologies.md#base-quality-score) of 30 or greater ([Phred scale](terminologies.md#phred-scale)) derived from primary alignments, non-overlapping portions of supplementary alignments, and unmapped records of [high quality reads](terminologies.md#high-quality-reads) in the dataset.

    - **Inclusions & Exclusions:**
     **Included:** Non-overlapping bases from primary and supplementary alignments, unmapped records, [duplicate reads](terminologies.md#duplicated-reads), and [clipped bases](terminologies.md#clipped-bases). No minimum [mapping quality](terminologies.md#mapping-quality) threshold is imposed. (Note: It is critical that alignment files have duplicate reads properly marked).

     **Excluded:** Secondary alignments and reads failing platform or vendor quality controls.

    - **Pre-Alignment Data:**
    The total number of bases with a base quality score of 30 or greater (Phred scale) derived from high-quality reads within the raw sequencing dataset.

    For discontiguous long-read sequencing, only physically sequenced (observed) bases are counted; the unsequenced span of the inferred proximity molecule or template does not contribute to this metric.
    
- **Implementation details:** In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation, this metric is computed using [samtools stats](terminologies.md#samtools-stats), coupled with a custom parser that sums bases with [base quality score](terminologies.md#base-quality-score) 30 or greater from the First Fragment Quality (FFQ) and Last Fragment Quality (LFQ) tables. This implementation is identical for short-read and discontiguous-long-read data: evaluation is restricted to primary alignments and unmapped reads from [high quality reads](terminologies.md#high-quality-reads) (filtering out 0x100, (0x200)), while secondary alignments are excluded. [Duplicate reads](terminologies.md#duplicated-reads) are retained, [clipped bases](terminologies.md#clipped-bases) are included, and no [mapping quality](terminologies.md#mapping-quality) filter is applied. For discontiguous-long-read data, records are processed identically to short reads, counting only observed sequenced bases and excluding the unsequenced span intervals between read ends.

**Pre-Alignment Data:**
The count of high-quality bases ($Q \ge 30$) for unaligned data is computed directly from the declared unaligned BAM or CRAM file containing sequencing-read-type-specific high-quality reads. Reads failing platform or vendor quality checks (SAM flag 0x200) are excluded.
Metric evaluation: Evaluated across the raw Phred quality array (QUAL field) of each eligible primary record. Each base quality score represents the error probability on the Phred scale ($Q = -10 \log_{10} P_{\text{error}}$).
Base accumulator: For every byte in the record's QUAL array where $\text{value} \ge 30$, the high-quality base accumulator increments by one.
Missing quality handling: In accordance with the SAM specification, if a record stores an unassigned quality field (represented by * or a missing quality buffer), its bases cannot be evaluated and do not increment the count.
The final metric is reported as the raw integer sum of all passing bases across the library. When the total sequenced length is zero, N/A is reported. This procedure is applied independently to each sequencing read type.
- **Comments:** 
    - open to both `single-end (SE)` and `paired-end (PE)`, accounting **Ultima single-end (SE) sequencing**?
    - high quality reads - reads passing the sequencing instrument/vendor quality filter / instrument-filter-passing reads where such a filter exists; SAM flag 0x200 not set.
    - If this metric is also applicable to discontiguous-long-read sequencing at the template level, the computation method shall be specified.
    - Technology-specific implementation details (e.g., **BX tags**, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition/Implementaion.

```
    samtools stats -F 0x300 in.bam > in.stats 
    // exclude secondary 0x100 / 256 while preserving all unmapped, mapped, duplicate reads, and soft-clipped bases. To exclude vendor quality check (QC-failed 0x200 / 512) use -F 768.
    awk '$1 ~ /^[FL]FQ$/ { for (i = 33; i <= NF; i++) sum += $i } END { print "Total >=Q30 bases (PE):", sum }' stats.txt

OR

    Python (Pysam) custom script
    import pysam

    bam_file = "input.bam"
    bq_cutoff = 30  # Your target BQ score

    total_bases_passing = 0

    with pysam.AlignmentFile(bam_file, "rb") as samfile:
        for read in samfile:
            # EXCLUDE: Secondary alignments (Flag 0x100)
            if read.is_secondary:
                continue
                
            # EXCLUDE: Vendor/QC-failed reads (Flag 0x200)
            if read.is_qcfail:
                continue
            
            # INCLUDED: 
            # - Supplementary alignments (0x800)
            # - Duplicate reads (0x400)
            # - Unmapped reads (0x4)

            # read.query_qualities provides BQ scores for all bases in the sequence,
            # which naturally includes soft-clipped segments.
            if read.query_qualities:
                total_bases_passing += sum(1 for q in read.query_qualities if q >= bq_cutoff)

    print(f"Total bases (excluding secondary & QC-fail) with BQ >= {bq_cutoff}: {total_bases_passing}")

OR
Mapped reads:

    # 1. Get a list of all chromosomes/contigs from the BAM header
    # 2. Use xargs to process them in parallel across 8 cores
    # 3. Stream the regions, filter flags, and sum base qualities using a fast Awk array
    samtools view -H input.bam | grep "^@SQ" | cut -f2 | sed 's/SN://' | \ xargs -I {} -n 1 -P 8 sh -c '
    samtools view -F 768 input.bam "{}" | awk -v cutoff=30 \
    "BEGIN {FS=\"\t\"} 
    {
        # Split the QUAL string (11th field) into individual characters
        n = split(\$11, chars, \"\");
        for (i = 1; i <= n; i++) {
        # Convert Phred character to numeric BQ score (ASCII - 33)
        if (ord[chars[i]] == 0) ord[chars[i]] = id = index(\"!\\\"#\$%&'\''()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_~\`abcdefghijklmnopqrstuvwxyz{|}~\", chars[i]) - 1;
        if (ord[chars[i]] >= cutoff) count++;
        }
    } 
    END {print count}"
    ' | awk '{sum+=$1} END {print "Total bases >= 30: " sum}'


and Unmpped reads:

    samtools view -f 4 -F 768 input.bam | awk -v cutoff=30 \
    'BEGIN {FS="\t"} {
    n = split($11, chars, "");
    for (i = 1; i <= n; i++) {
        if (ord[chars[i]] == 0) ord[chars[i]] = index("!\"#$%&'\''()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~", chars[i]) - 1;
        if (ord[chars[i]] >= cutoff) count++;
    }
    } END {print count}'

OR 
Unaligned data:

    samtools stats -F 0x200 unaligned.bam > unaligned.stats
    awk '/^FFQ|^LFQ/ && $2 >= 30 {sum += $3} END {print sum}' unaligned.stats
```

- **Type:** Integer (eg. 102984371235)
- **Functionally equivalent implementations:**
    - [ICGC-ARGO dnaalnqc](References.md#icgc-argo)
    - [DRAGEN v3.7.6](References.md#dragen). Extracted from [sample-id].mapping_metrics.csv, key name: `MAPPING/ALIGNING SUMMARY,,Q30 bases`
- **Sequencing read type:** short-read | discontiguous-long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:** Illumina | Illumina TruPath Genome (proximity mapped reads; formerly Constellation)
- **Associated aligner:** BWA-MEM/BWA-MEM2 or DRAGEN aligner (Illumina short-read) | DRAGEN TruPath pipeline (Illumina proximity mapped reads). Record the exact version and parameters.
- **Associated variant caller:** N/A
- **Associated basecaller:** 
