# Phase block NG50
- **ID:** phase_block_ng50
- **Description:** The phase block length L such that 50% of the expected genome size, or a defined target genome size, is contained in phase blocks of length greater than or equal to L. It is analogous to NG50 for assemblies, but applied to phased haplotype blocks rather than contigs. For long reads, this metric reflects haplotype continuity and is a key indicator of long-range phasing performance.
- **Implementation details:** Obtain phase block intervals from the phased VCF or phasing output, calculate the length of each phase block, sort blocks by length in descending order, and accumulate block lengths until 50% of the chosen target genome size is reached. The block length at this point is the Phase Block NG50. The implementation should define the target genome size, whether only autosomes are included, how gaps and unphased regions are handled, and whether phase-set IDs from the PS tag or external block definitions are used. For ONT and PacBio data, Phase Block NG50 is strongly influenced by read length, read depth, heterozygous variant density, mapping quality, and phasing algorithm.
- **Type:** Integer, base pairs (eg. 28500000)
- **Functionally equivalent implementations:**
  - WhatsHap stats
