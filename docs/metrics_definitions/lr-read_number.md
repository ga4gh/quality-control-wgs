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
