# Architectural Decision Record

*This document serves as a record of decisions made throughout the product development process. Each entry outlines a decision that has been formally approved by members of the WGS-QC workgroup. Together, these ADRs capture the institutional memory of key decisions and their underlying rationales. The aim is to preserve the context behind these choices and share this knowledge with the broader community.*


## Contents

[TOC]

## 2025-05-27:

### Decision

1. Finalization of NPM v0.13.4
- Addressed precision inconsistencies in the cross-contamination rate matrix (from 2 to 4 decimal places)
- Resolved inclusion logic for multi-allelic sites in sample QC
- Fixed incorrect count inflation due to string length checks in metrics involving alternate alleles

2. Alignment with Argo Repository
- Verified functional equivalence between NPM and Argo pipelines, except for “percentage of reads properly paired”
- Agreed to update the functional equivalent implementation and clearly document exceptions in the metric definitions
- Decided to link the Argo reference implementation in the G4GH repository alongside NPM as part of the formal documentation set

3. Approval Process for Product Release
- Timeline and document preparation agreed:
- Finalize: Product submission form, REWS form, and Security form
- Select PRC members and initiate public feedback channels
- Public comment period: July 15 – August 15, 2025
- PRC meeting: To be held during the same window (July 15–August 15)
- Target release: October 29, 2025 (GA4GH Plenary Session)

4. Metric Definition Improvements
- Each metric matrix will now include its field type to eliminate ambiguity
- Plan to improve clarity between nominal, continuous, and derived metrics across pipelines

5. Roadmap Additions
Confirmed inclusion of the following deliverables in the roadmap:
- A Common Practice Resource Guide for adopters
- A Peer-reviewed Publication to increase visibility and adoption of the standard
- Committed to updating the roadmap document accordingly

### Rationale
- Ensures technical precision, consistency, and compatibility across platforms (NPM, Argo)
- Formalizes the approval and feedback process in accordance with GA4GH standards
- Supports adoption through documentation, tooling references, and academic publication
- Enhances transparency and interpretability of metrics by standardizing field definitions and formats



## 2025-04-22:

### Decision

1. Include Multi-Allelic Indels in QC Metrics

- Update the NPM QC pipeline to count multi-allelic sites in indel metrics (insertion/deletion counts and ratios).
- Remove existing filters that exclude multi-allelic sites to ensure biological relevance and data fidelity.

2. Define Somatic Variant Metrics
- Specify required input files (e.g., VCF, BAM) for somatic mutation QC calculations.
- Collaborate with Argo to integrate their VCF QC pipeline as a reference implementation.
- Address tumor purity/ploidy dependencies in metric definitions.

3. Expand Ecosystem Integration
- Align with GA4GH Data Connect and Damasc for federated querying of QC metrics.
- Engage Nomad and EGA to promote adoption beyond GA4GH.
- Plan ISO TC 215 alignment post-version 1 release.

4. Roadmap Prioritization
- Version 1 (Short-Read WGS): Finalize multi-allelic and somatic updates.
- Version 2: Add long-read sequencing and advanced somatic QC.


### Rationale

1. Multi-Allelic Indels
- Biological Relevance: Excluding multi-allelic sites risks omitting true variants (e.g., complex indels in cancer/population genomics).
- Data Integrity: Metrics should reflect raw input without arbitrary filtering.
- Implementation Impact: Minimal pipeline adjustments needed (removes a filter, no computational overhead).

2. Somatic Variants
- Standardization Need: Somatic pipelines lack unified QC metrics (e.g., tumor-normal concordance, artifact detection).
- Argo’s Benchmark: Their VCF QC pipeline provides a validated starting point.
- Clarity: Explicit input requirements (e.g., "Tumor VCF + BAM") prevent ambiguity.

3. Ecosystem Integration
- Interoperability: Data Connect enables centralized QC metric querying across repositories.
- Adoption: Partnerships with Nomad/EGA ensure real-world utility.
- Regulatory Alignment: ISO TC 215 collaboration future-proofs the standard.

4. Roadmap
- Short-read focus (v1): Ensures deliverability while deferring complex long-read/somatic challenges to v2

