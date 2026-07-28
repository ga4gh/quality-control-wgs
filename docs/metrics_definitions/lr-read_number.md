# Read number
- **ID:** read_number
- **Description:** The total number of sequencing reads generated in a run or included in an analysis dataset. For long-read sequencing, read number alone is not sufficient to describe output because reads can vary widely in length. It should therefore be interpreted together with total base yield, read length distribution, and read quality.
- **Implementation details:** Count all reads in the input FASTQ/BAM according to the selected inclusion criteria. The metric should specify whether all reads, pass reads, mapped reads are included. For ONT data, read number may be influenced by pore activity, run duration, library loading, fragmentation, and basecalling/read filtering choices.
- **Type:** Integer (eg. 18452391)
- **Functionally equivalent implementations:**
  - seqkit stats
  - samtools view -c
  - NanoPlot
  - pycoQC

# comments
- **Description:** The total number of sequencing reads generated in a run or included in an analysis dataset. For long-read sequencing, read number alone is not sufficient to describe output because reads can vary widely in length. It should therefore be interpreted together with total base yield, read length distribution, and read quality.

The total number of [high quality reads](terminologies.md#high-quality-reads) from short paired-end sequencing, continuous long-read sequencing, synthetic long-read sequencing (read level), and synthetic long-read sequencing (template level), excluding supplementary and secondary reads. Duplicate reads are included.

- **Implementation details:** Count all reads in the input BAM/CRAM according to the selected inclusion criteria. The metric should specify whether all reads, pass reads, mapped reads are included. For ONT data, read number may be influenced by pore activity, run duration, library loading, fragmentation, and basecalling/read filtering choices.

In the [NPM-sample-QC](References.md#npm-sample-qc) reference implementation this metric is computed using [samtools stats](References.md#samtools-stats), reporting the total number of [high quality reads](terminologies.md#high-quality-reads) from short paired-end sequencing, continuous long-read sequencing, synthetic long-read sequencing (read level), and [samtools stats](References.md#samtools-stats) flag-xxxxx for synthetic long-read sequencing (template level), excluding supplementary and secondary reads. Duplicated reads are included and no mapping qualiy is applied.

For synthetic long-read sequencing (template level), total number of [high quality reads](terminologies.md#high-quality-reads) shall be computed and reported using [samtools stats](References.md#samtools-stats) flag-xxxxx. Template-level metrics shall exclude singleton reads for which no containing template is defined.

Technology-specific implementation details (e.g., BX tags, SAM template identifiers, or other platform-specific tags) should be documented only where they deviate from the general metric definition.
- **Sequencing read type:** short-read|long-read
- **Reference genome assembly:** GRCh37 | GRCh38
- **Version:** 2.0
- **Sequencing technology:**
- **Associated aligner:**
- **Associated basecaller:**
- **Associated variant caller:**