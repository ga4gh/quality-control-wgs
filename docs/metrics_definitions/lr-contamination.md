# Contamination
- **ID:** contamination
- **Description:** The estimated proportion of sequencing data originating from non-target organisms, unrelated human samples, or other unintended DNA sources. Contamination can reduce variant calling accuracy, alter allele balance, inflate apparent yield, and create misleading QC signals.
- **Implementation details:** Estimate contamination using taxonomic classification, alignment to alternate references, k-mer based methods, or genotype/allele-balance based methods. The method should specify whether it detects non-human contamination, human cross-sample contamination, or both. For ONT and PacBio workflows, contamination assessment may be performed before alignment using reads or after alignment using variant/genotype patterns. The chosen method should be documented because different tools measure different contamination signals.
- **Type:** Float, fraction or percentage (eg. 0.006; 0.6%)
- **Functionally equivalent implementations:**
  - Kraken2
  - Centrifuge
  - VerifyBamID
