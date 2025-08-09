# Architectural Decision Record

_This document serves as a record of decisions made throughout the product development process. Each entry outlines a decision that has been formally approved by members of the WGS-QC workgroup. Together, these ADRs capture the institutional memory of key decisions and their underlying rationales. The aim is to preserve the context behind these choices and share this knowledge with the broader community._

## Contents

[TOC]

## 2025-05-27

### Decision

**Finalization of NPM-sample-qc release v0.13.4**

- Addressed precision inconsistencies in the cross-contamination rate matrix (from 2 to 4 decimal places)
- Resolved inclusion logic for multi-allelic sites in sample QC
- Fixed incorrect count inflation due to string length checks in metrics involving alternate alleles

**Alignment with Argo Repository**

- Verified functional equivalence between NPM and Argo pipelines, except for “percentage of reads properly paired”
- Agreed to update the functional equivalent implementation and clearly document exceptions in the metric definitions
- Decided to link the Argo reference implementation in the G4GH repository alongside NPM as part of the formal documentation set

**Approval Process for Product Release**

- Timeline and document preparation agreed:
- Finalize: Product submission form, REWS form, and Security form
- Select PRC members and initiate public feedback channels
- Public comment period: July 15 – August 15, 2025
- PRC meeting: To be held during the same window (July 15–August 15)
- Target release: October 29, 2025 (GA4GH Plenary Session)

**Metric Definition Improvements**

- Each metric matrix will now include its field type to eliminate ambiguity
- Plan to improve clarity between nominal, continuous, and derived metrics across pipelines

**Roadmap Additions**

Confirmed inclusion of the following deliverables in the roadmap:

- A Common Practice Resource Guide for adopters
- A Peer-reviewed Publication to increase visibility and adoption of the standard
- Committed to updating the roadmap document accordingly

### Rationale

- Ensures technical precision, consistency, and compatibility across platforms (NPM, Argo)
- Formalizes the approval and feedback process in accordance with GA4GH standards
- Supports adoption through documentation, tooling references, and academic publication
- Enhances transparency and interpretability of metrics by standardizing field definitions and formats

## 2025-04-22

### Decision

**Include Multi-Allelic Indels in QC Metrics**

- Update the NPM QC pipeline to count multi-allelic sites in indel metrics (insertion/deletion counts and ratios).
- Remove existing filters that exclude multi-allelic sites to ensure biological relevance and data fidelity.

**Define Somatic Variant Metrics**

- Specify required input files (e.g., VCF, BAM) for somatic mutation QC calculations.
- Collaborate with Argo to integrate their VCF QC pipeline as a reference implementation.
- Address tumor purity/ploidy dependencies in metric definitions.

**Expand Ecosystem Integration**

- Align with GA4GH Data Connect and Damasc for federated querying of QC metrics.
- Engage Nomad and EGA to promote adoption beyond GA4GH.
- Plan ISO TC 215 alignment post-version 1 release.

**Roadmap Prioritization**

- Version 1 (Short-Read WGS): Finalize multi-allelic and somatic updates.
- Version 2: Add long-read sequencing and advanced somatic QC.

### Rationale

**Multi-Allelic Indels**

- Biological Relevance: Excluding multi-allelic sites risks omitting true variants (e.g., complex indels in cancer/population genomics).
- Data Integrity: Metrics should reflect raw input without arbitrary filtering.
- Implementation Impact: Minimal pipeline adjustments needed (removes a filter, no computational overhead).

**Somatic Variants**

- Standardization Need: Somatic pipelines lack unified QC metrics (e.g., tumor-normal concordance, artifact detection).
- Argo’s Benchmark: Their VCF QC pipeline provides a validated starting point.
- Clarity: Explicit input requirements (e.g., "Tumor VCF + BAM") prevent ambiguity.

**Ecosystem Integration**

- Interoperability: Data Connect enables centralized QC metric querying across repositories.
- Adoption: Partnerships with Nomad/EGA ensure real-world utility.
- Regulatory Alignment: ISO TC 215 collaboration future-proofs the standard.

**Roadmap**

- Short-read focus (v1): Ensures deliverability while deferring complex long-read/somatic challenges to v2

## 2025-02-25

### Decision

**1. NPM Repository**

- Confirm that there are no open issues or pull requests.
- Issues #136 and #138 are closed, resolving the cross-contamination rate calculation and updating the README.
- Pull Requests #137 and #141 are merged, updating the Nextflow manifest version and adding license details to the README.
- Pull Request #144 is merged, correcting the cross-contamination metric name and updating unit test results.

**2. GA4GH Repository**

- Acknowledge pending issues:

  - issue #40 (printing median value) – pending.
  - issue #46 (copyright update) – pending.
  - issue #50 (update reference implementation and docstore links) – pending.

- Closed/linked issues:

  - issue #45 (linked to NPM #137) – resolved in NPM and merged to GA4GH release 13.2.
  - issue #55 closed, correcting cross-contamination metric name.

- Pending pull requests:
  - issue #56 awaiting Argo VCF QC implementation results.

**3. Argo Implementation**

- Accept Argo’s completion of the VCF QC reference implementation, with 100-sample symmetric results expected in early March for correlation with the NPM reference implementation.
- Note Argo’s ongoing work on somatic mutation, with updates expected early March.
- Accept external contribution for minor license file fixes.

**4. Product Approval and Security Forms**

- Complete and submit the Product Approval Submission Form and Security Form to the GA4GH committee.
- Prepare a Public Review Committee (PRC) with members from multiple categories.
- Publish a recorded product presentation for a 30-day public comment period before PRC review.

**5. GA4GH Connect Session**

- Present WGS QC roadmap and interoperability plans on April 4, 2025, 11:15 ET.
- Rename current document as **Version 1.0** and the forthcoming document as **Version 2.0**.
- Include updates in Roadmap v2: QC for long-read germline post-alignment, long-read germline post-variant calling, structural variation, and somatic mutation.

### Rationale

- Repository alignment: Closing, merging, and linking related issues ensures consistent metric naming, updated documentation, and maintained compatibility across NPM and GA4GH repositories.

- Reference implementation verification: Coordinating NPM and Argo results strengthens confidence in the specification’s reproducibility and accuracy.

- Compliance and transparency: Completing GA4GH product approval requirements, including security forms and a public review period, ensures the process meets governance standards.

- Forward planning: Versioning and roadmap updates maintain clarity on current vs. future scope, enabling structured evolution of the specification.

## 2025-01-21

### Decision

**1. Finalize Version 1.0 Release**

- Close remaining PRs: Merge PR #57 (cross-contamination rate fix) and update reference implementation links (Issue #50).
- Publish release notes: Document all changes (closed Issues #45, #55, #136, #138; merged PRs #137, #141, #144).

**2. Integrate Argo’s VCF QC Implementation**

- Include as a reference implementation after March testing completion.
- Add somatic mutation metrics (under development) to Version 2.0 roadmap.

**3. Prepare for GA4GH Product Approval**

- Complete submission and security forms for committee review.
- Form Public Review Committee (PRC) with cross-workstream members.
- Share recorded presentation for 30-day public comment (pre-PRC review).

**4. Plan Version 2.0 & Connect Session**

- Scope: Long-read QC (germline/somatic), structural variants, GA4GH ecosystem interoperability.
- April 4 Connect Session: Present roadmap and align with Data Connect/Damasc.

### Rationale

**1. Version 1.0 Readiness**

- Closed Issues/PRs: Critical fixes (e.g., cross-contamination precision, license updates) ensure stability.
- Argo’s Contribution: VCF QC implementation expands use cases beyond NPM’s pipeline.

**2. Product Approval**

- GA4GH Compliance: Formal review ensures alignment with federation standards.
- Transparency: Public comment period invites community feedback.

**3. Version 2.0 Priorities**

- Long-Read/Somatic Gaps: Address emerging sequencing technologies and cancer genomics needs.
- Ecosystem Integration: Data Connect/Damasc compatibility enhances adoption.

**4. Connect Session**

- Visibility: Showcases progress to GA4GH members and external stakeholders (e.g., EGA, Nomad)

## 2024-11-26

### Decision

**1. Separate QC Workflows by File Type**

- BAM/CRAM Workflow: Alignment/post-alignment QC (NPM-led).
- VCF Workflow: Variant calling QC (Argo-led).
- Rationale: Simplifies implementation, testing, and adoption for distinct pipeline stages.

**2. Close Pending Issues**

- Issue #41: Dockstore registration (close).
- Issue #48: README updates (close).
- Issue #44: Median value implementation (defer to Version 2.0).

**3. Align NPM/Argo Metrics**

- Resolve Issue #45 (decimal precision) via cross-validation with GATK.
- Action: Justin/Linda to finalize comments.

**4. Version 2.0 Scope**

- Somatic Workflow: Argo to lead (align with Issue #46).
- Long-Read QC: Seek public benchmarks (e.g., Platinum dataset).
- Single Metric Document: Unify definitions across workflows.

**5. GA4GH Approval Timeline**

- Target April–July 2025 for full approval.
- Next Steps: Complete submission documents (Thomas to guide).

### Rationale

**1. Workflow Separation**

- Modularity: Enables independent updates (e.g., VCF metrics without BAM changes).
- User Flexibility: Labs can adopt workflows relevant to their pipelines.
- Validation Efficiency: Simplifies benchmarking (e.g., GIAB for VCF, Platinum for long-reads).

**2. Version 2.0 Priorities**

- Somatic Focus: Addresses critical gap in cancer genomics.
- Long-Reads: Prepares for emerging technologies (ONT/PacBio).
- Unified Docs: Reduces redundancy and improves clarity.

**3. Approval Process**

- GA4GH Alignment: Ensures interoperability with Data Connect/Damasc.
- Community Review: Incorporates feedback via public comment period

## 2024-10-22

### Decision

**1. Diversify Benchmark Resources**

- Merge PR #42: Expand 100-sample benchmark to include diverse ethnicities.
- Action: Argo to run pipeline on updated sample list for cross-validation.

**2. Standardize Metric Precision**

- Decimal Consistency: Align NPM/Argo cross-contamination rates (avoid rounding to 0%).
- Documentation: Add precision requirements to metric definitions (GitHub Issue #TBD).

**3. VCF QC Implementation**

- Reference Pipeline: Argo’s VCF QC workflow is now production-ready for testing.
- Deprecate MultiQC: NPM v0.13 removes MultiQC dependency (simplifies outputs).

**4. Somatic/Long-Read Roadmap**

- Somatic QC: Collaborate with Dragen to align with GA4GH metrics.
- Long-Reads: Use Platinum dataset (bioRxiv 10.1101/2024.10.02.616333) as benchmark.

**5. GA4GH Ecosystem Integration**

- Data Connect: Engage leads to incorporate QC metrics into federated queries.
- Publication: Draft GA4GH best practices paper for QC standards.

### Rationale

**1. Benchmark Diversity**

- Representation Matters: Ethnic diversity reduces bias in QC thresholds.
- Validation: Parallel runs (NPM/Argo) ensure metric robustness across populations.

**2. Metric Precision**

- Clinical Relevance: Rounding contamination rates to 0% masks critical quality issues.
- Interoperability: Consistent precision enables cross-pipeline comparisons.

**3. VCF QC Readiness**

- User Need: Separate VCF workflow simplifies adoption for variant-focused labs.
- Maintenance: Removing MultiQC reduces dependency conflicts.

**4. Future-Proofing**

- Somatic/Dragen: Industry alignment accelerates adoption.
- Long-Reads: Platinum dataset provides gold-standard validation

## 2024-09-24

### Decision

**1. Two-Phase Implementation Approach**

- Phase 1 (v1): Finalize short-read WGS QC standard and achieve GA4GH production status
- Phase 2 (v2): Expand scope to:
    - Somatic mutation QC (Argo-led implementation)
    - Long-read sequencing QC / Structural variant calling QC

**2. Documentation Strategy**

- Maintain single unified metric definition document
- Add versioned appendices for new data types (somatic/long-read)

**3. Pipeline Architecture**

- Develop specialized QC pipelines for:
    - Short-read alignment (BAM/CRAM)
    - Variant calling (VCF)
    - Somatic mutation
    - Long-read data
- Preserve interoperability through shared JSON schema

**4. Ethnicity Considerations**

- Formalize ethnicity-specific benchmarking in v1.1 update
- Document expected metric ranges by population group

**5. Governance**

- Form working subgroups for:
    - Somatic QC (Argo chair)
    - Long-read QC (open chair)
- Monthly cross-group syncs to maintain alignment


### Rationale

**1. Progressive Standardization**

- Completing short-read standard first provides stable foundation
- Parallel development risks scope creep and delays

**2. Technical Pragmatism**

- Separate pipelines allow:
    - Technology-specific optimizations
    - Independent versioning
    - Gradual adoption
- Shared schema ensures interoperability

**3. Biological Realism**

- Ethnicity-specific ranges reflect true genetic diversity
- Prevents false quality flags in diverse cohorts

**4. Community Alignment**

- Argo's clinical genomics expertise suits somatic leadership
- Open chair encourages long-read community participation

## 2024-07-23

### Decision

**1. Update Post-Alignment QC Metrics Definitions**

- Refine functional equivalence for DRAGEN v3.7 and other aligners.
- Focus on "not hard-to-sequence" regions (ensure benchmark regions exclude problematic genomic areas).
- Clarify implementation requirements for:
    - Coverage depth uniformity
    - Mapping quality distribution
    - Insert size metrics

**2. Expand Benchmark Dataset Diversity**

- Add ethnically diverse samples to the 100-sample benchmark set.
- Prioritize inclusion of:
    - African, East Asian, South Asian, and admixed populations
    - Samples with varying GC content and complexity

**3. Resolve Pending Pull Requests**

- PR #21, #22, #31, #32, #33: Finalize reviews and merges.
- PR #22: Update comparison analysis between NPM and DRAGEN v3.7.

**4. Improve Visualization & Reporting**

- Enhance Jupyter notebooks for:
    - Super-population stratification
    - Side-by-side tool comparisons (NPM vs. DRAGEN)
- Standardize plots for GA4GH documentation.

**5. Collaborate with GA4GH DRS Group**

- Define standardized region sets for benchmarking (e.g., "not hard-to-sequence" BED files).
- Ensure compatibility with GA4GH Data Repository Service (DRS) for metric sharing.

### Rationale

**1. Metric Refinements**

- DRAGEN v3.7 Alignment: Ensures interoperability with industry-standard pipelines.
- "Not Hard-to-Sequence" Regions: Reduces false QC failures in problematic genomic areas (e.g., high homology regions).
- Functional Equivalence: Allows fair comparison across tools (e.g., NPM vs. DRAGEN).

**2. Diverse Benchmarking**

- Ethnic Representation: Prevents population-specific biases in QC thresholds.
- Genomic Diversity: Captures wider range of technical challenges (e.g., GC extremes).

**3. Visualization & Reporting**

- Population Stratification: Helps labs interpret metric ranges for their cohorts.
- Tool Comparisons: Identifies systematic differences between implementations.

**4. DRS Integration**

- Reproducibility: Standardized regions enable cross-study comparisons.
- FAIR Compliance: DRS enables federated querying of QC metrics

## 2024-06-25

### Decision

**1. Investigate Sample Stratification in QC Plots**

- Hypothesis Testing: Correlate the two observed sample clusters with 1KGP ethnicity data (super-populations).
- Action: Update Jupyter notebooks to color-code samples by ethnicity.

**2.DRAGEN v3.7.8 Functional Equivalence**

- Root Cause: NPM’s region exclusion vs. DRAGEN’s lack of equivalent metrics.
- Short-Term Fix:
    - Run DRAGEN with whitelist regions (if supported).
    - Document workarounds for missing metrics (e.g., coverage uniformity).
- Long-Term Proposal:
    - Request DRAGEN to adopt whitelist by default via Illumina collaboration.

**3. VCF QC Tool Standardization**

- Clarify Tools: Specify whether bcftools, GATK, or custom scripts are used for VCF QC.
- Add to Docs: Update README with tool versions and parameters.

**4.Plotting Improvements**

- Replot Correlation Charts:
    - Fix axis scaling (log where appropriate).
    - Add jitter to overlapping ratio points.
- Ethnicity Annotation: Label clusters if ethnicity-linked.

**5. Plenary Attendance Plan**

- Remote Participation: Prioritize key discussions for asynchronous input (Slack/email).
- Delegate Presentation: Assign on-site attendees (e.g., Justin, Nicolas) to represent the group.

### Rationale

**1. Ethnicity-Driven QC Variation**

- Biological Reality: Metric distributions often differ by ancestry (e.g., AFR vs. EUR).
- Mitigation: Annotate plots to prevent misinterpretation as technical artifacts.

**2. DRAGEN Compatibility**

- User Need: Labs using DRAGEN require comparable QC outputs.
- Advocacy: Pushing for whitelist adoption improves future interoperability.

**3. Visualization Clarity**

- Jitter: Resolves overplotting in ratio metrics (e.g., Ti/Tv).
- Log Scales: Reveals patterns in skewed distributions (e.g., depth).

**4. Remote Collaboration**

- Inclusivity: Ensures absent members can contribute to decisions

## 2024-05-28

### Decision

**1. Functional Equivalence Confirmed**

- AWS 1KGP DRAGEN vs. NPM QC:
    - 3 metrics initially discrepant due to partial BAM processing.
    - 64 samples reanalyzed; results now show 100% correlation for yield/alignment metrics.
- Action:
    - Fix BAM loading issue in pipeline (GitHub Issue #TBD).
    - Document DRAGEN-NPM benchmark protocol.

**2. Variant Calling QC Metrics**

- PR #31 Review: Finalize definitions for:
    - Transition/Transversion (Ti/Tv) ratios
    - Indel size distributions
    - Multiallelic site frequencies
- Action: All members review proposed metrics.

**3. ISO Standardization Alignment**

- Clarify Engagement:
    - TC 140 (NGS): Focus on wet-lab protocols.
    - Bioinformatics TC: Target for QC metric standards.
- Action: Draft GA4GH-ISO crosswalk document (Thomas/Linda).

**4. GA4GH Product Integration**

- DRS Collaboration: Ensure QC metrics are queryable via Data Repository Service.
- Roadmap: Add interoperability milestone for Q3 2024.

### Rationale

**1. Tool Validation**

- Reproducibility: Confirms NPM and DRAGEN outputs are comparable when processed fully.
- Transparency: Documents edge cases (partial BAM loads) for future debugging.

**2. VC Metric Standardization**

- Clinical Relevance: Ti/Tv ratios detect sequencing artifacts.
- Biological Insight: Indel distributions vary by disease context.

**3. ISO Harmonization**

- Regulatory Impact: Aligns GA4GH standards with international frameworks.
- Scope Clarity: Separates wet-lab (TC 140) from bioinformatics standards.

**4. Ecosystem Integration**

- FAIR Data: DRS enables federated QC metric access.

## 2024-03-26

### Decision

**1. Define Functional Equivalence Thresholds**

- High Agreement Metrics (✅):
    - Require <5% relative difference (e.g., mean coverage, properly paired reads).
- Disputed Metrics (❌):
    - % Reads Mapped: Investigate mapping algorithm differences.
    - Insert Size Std Dev: Exclude from cross-tool comparisons.
- Non-Equivalent Metrics:
    - Label clearly in reports (e.g., "DRAGEN lacks PCT_Autosome_15x").

**2. Address Cell Line vs. Primary Sample Bias**

- Annotate 1KGP Data: Flag immortalized cell line status in benchmarks.
- Supplement with Primary Samples: Use Ivo’s inter-lab comparison data where possible.

**3. Variant Calling QC Standardization**

- Core Metrics:
    - Ti/Tv ratio (tumor/normal concordance for somatic).
    - Indel size spectrum.
- Exclusions:
    - DRAGEN-specific metrics without NPM equivalents.

**4. Pipeline Improvements**

- DRAGEN Whitelisting: Test `--region` parameter for assembly gap exclusion.
- NPM Updates: Add warning for cell line artifacts.

### Rationale

**1. Threshold Clarity**

- 5% threshold balances biological variability with technical reproducibility.
- Explicit non-equivalence prevents false comparisons.

**2. Sample Type Transparency**

- Cell lines show +15% false positives vs. primary samples (per Ivo’s data).
- Annotations ensure appropriate interpretation.

**3. Variant QC Focus**

- Ti/Tv ratios detect PCR artifacts; indel sizes reveal alignment issues

## 2024-02-27

### Decision

**1. VCF-Centric QC Contributions**

- Open Collaboration: Invite all members to propose metric definitions via GitHub markdown.
- Linking Pipelines: Use `.gitmodules` to reference external QC implementations (e.g., Argo’s pipeline).

**2. Workflow Versioning**

- NPM v0.12: Now reflects Picard updates.
- Argo Pipeline: Pending PR for updates (MH to guide GitHub submodule process).

**3. Long-Read Terminology**

- Scope: Officially include long-read QC in Roadmap v2.
- Clarification: Define "long-read" as:
    - PacBio HiFi: ≥Q20, ≥10 kb reads.
    - Oxford Nanopore: ≥Q15, ultra-long reads.

**4. Registry Integration**

- Docstore Registration: Accelerate via GA4GH Tool Registry Service.
- Metadata Alignment: Sync with GA4GH Metadata Schema group.

### Rationale

**1. Transparent Contributions**

- GitHub markdown ensures traceability; .gitmodules enables modular pipeline reuse.

**2. Forward Compatibility**

- Submodule approach allows independent pipeline updates without breaking references.

**3. Technology Neutrality**

- Explicit long-read definitions prevent ambiguity in v2 planning.

**4. Ecosystem Alignment**

- Docstore/Data Registry integration enables federated QC queries

## 2024-01-30

### Decision

**1. Roadmap Document Updates**

- Adopt new table of contents structure (per Maxime's proposal)
- Rename "Expected Completion Date" → "Completed Date"
- Add checkboxes for tracking progress
- Mark completed items as we progress

**2. Milestone Adjustments**

**Schema Integration**

  - Connect with Experiment Metadata group
  - Engage DRS team

**Reference Tools**

  - PR #19 ready
  - Merge PR
  - Continue Argo improvements

**Metric Finalization**

  - Identify responsible parties
  - Schedule alignment meeting

**3. 2024 Priority Projects**

- Post-Variant Calling QC Metrics
    - Select 5-7 key metrics (Ti/Tv ratio, indel spectrum, etc.)
    - Formalize definitions in GitHub markdown
    - Implement in ≥2 workflows (NPM + Argo)
- Reference Implementations
    - Formalize Argo workflow as second independent implementation
    - Establish validation protocol
- GA4GH Integration
    - Experiment Metadata WG (primary)
    - DRS standard (secondary)

**4. Benchmarking Resources**

- Current: DRAGEN v3.7.6 dataset available
- Needed: Additional version comparisons
- Action: Nominate benchmark coordinator


### Rationale

**1. Transparent Tracking**

- Checkboxes and renamed dates improve accountability
- Clear documentation of completed work

**2. Accelerating Progress**

- Merging PR #19 unblocks dependent work
- Parallel development of Argo implementation saves time

**3. Strategic Focus**

- VCF metrics address urgent community needs
- Dual implementations ensure robustness
- Metadata/DRS integration enables FAIR QC data

**4. Resource Optimization**

- Leverage existing DRAGEN data while planning expansions
- Technical paper will attract collaborators

## 2023-11-28

### Decision

- WG agree for the reference implementation to use picard to compute coverage based metrics with the default parameters (exclude unmapped reads & BQ < 20)

- WG see the benefit of running the pipeline on 3202 samples from 1000Genome project in order to define the range of accepted values to define functional equivalence.

- ARGO pipeline will work on Dockstore registration

- Align ARGO and NPM before running 1000 Genome dataset

- Need to participate to Experiments Metadata Standard and invite a representative to our meeting

## 2023-10-24

### Decision
Is the current process sufficient to ensure implementations work as advertised!

Seems that with 100 samples tested we already see some divergence in the implementations. It might not need to go further.


## 2023-09-26


### Decision

**1. Scope Expansion for Metrics**  

- Primary Focus: Germline short-read WGS QC (current priority).
- Future Extensions:
    - Variant Types: SNPs + small indels (Phase 1) → Structural Variants (Phase 2).
    - Read-Level QC: Deferred (e.g., FASTQ-style metrics, vendor quality tags).

**2. Vendor Engagement**

- DRAGEN (Illumina):
    - Request alignment of DRAGEN 3.7.8+ with GA4GH metric definitions.
    - Collaborate on standardizing variant-level QC flags.
- Unified Output Format: Advocate for a consolidated file (JSON/CRAM-tag) for all metrics.

**3. NIH Metric Framework Integration**

- Adopt/adapt NIH’s germline QC metrics where applicable.
- SV-CNV Cross-Validation: Explore in Phase 2 (per DC’s suggestion).

**4. Working Group Priorities**

- Short-Term: Finalize SNP/small-indel VCF metrics (Q2 2024).
- Long-Term:
    - Structural variant QC (2025).
    - Vendor tag standardization (post-2024).

### Rationale

**1. Focus on Germline Short-Reads**

- Addresses immediate community needs (clinical/large-scale genomics).
- Provides foundation for future expansions.

**2. Vendor Collaboration**

- DRAGEN Ubiquity: Ensures broad adoption of standards.
- Unified Outputs: Simplifies integration for end users.

**3. NIH Alignment**

- Leverages existing NIH/CSER work to avoid duplication.
- SV-CNV sanity checks improve variant reliability.

**4. Phased Approach**

- Prevents scope creep while planning for SVs/long-reads

## 2023-08-22

### Decision

**1. VCF-Centric QC Metrics Framework**

- Scope: Focus on germline short variants (SNPs/indels <50bp) from standard callers (e.g., DeepVariant, GATK).
 
 **Core Metrics:**

|Metric              |Definition          |Filter     |
|                    |                    |           |
|Insertion Count     |PASS variants only  |Exclude SVs|
|Deletion Count      |PASS variants only  |Exclude SVs|
|Ti/Tv Ratio         |All variants        |-

- Filtering: Standardize on PASS-only for critical metrics (per Linda/Jukka consensus).

**2. Implementation & Validation**

- Reference Workflows:
    - NPM (Nextflow): Current benchmark.
    - Argo (GATK-based): To be formalized.
- Benchmarking:
    - Run on 10K samples (Oliver’s bad-quality WGS + 1KG).
    - Compare via Dockstore for reproducibility.

**3. PR #7 Merge**

- Approve major revision of metric definitions for:
    - BAM/CRAM QC (mature).
    - VCF QC (initial draft).

**4. Somatic/Long-Read Deferral**

- Postpone until germline metrics are stable.
- Exception: Basic Ti/Tv for tumor/normal pairs.

### Rationale

**1. Practical Focus**

- PASS-only filtering reflects clinical/lab standards.
- Size cutoff (<50bp) aligns with major variant callers.

**2. Scalable Validation**

- 10K samples stress-test metric robustness.
- Dockstore ensures workflow portability.

**3. Ecosystem Alignment**

- PR #7 harmonizes with NIH/CSER frameworks.
- Delaying SVs avoids dilution of effort.

## 2023-03-28

### Decision

**1. Metric Definition Updates**

- Adopt PR revisions to clarify:
    - Remove ambiguous booleans (e.g., "include duplicates?") → Replace with plain-language descriptions.
    - Standardize insert size reporting (mean + median absolute deviation).
    - Rename "% read map" (was "read mapping quality") for clarity.
- Implementation Details Section:
    - Add tool-specific parameters (e.g., `verifyBAMID2` for contamination).
    - Document functionally equivalent thresholds (e.g., 1000 Genomes benchmarks).

**2. Coverage Metrics**

- Retain 15x autosome coverage (vs. AoU’s 20x):
    - Balances clinical utility and sequencing economics.
- Evenness Calculation:
    - Standardize on median/mean coverage ratio (simple, reproducible).
    - Future: Evaluate dispersion-based methods for tumor samples.

**3. Contamination Rate**

- Include as optional metric:
    - Tools: `verifyBAMID2` (alignment) or `GATK` `CalculateContamination` (post-calling).
    - No universal threshold: Labs set own cutoffs (e.g., ≤1% for clinical).
    - Exclude ACMG panel coverage: Too project-specific.

**4. VCF-Centric Additions**

- Required: Ti/Tv ratio, indel spectrum.
- Optional: Cross-sample contamination (tumor/normal).

### Rationale

**1. Clarity vs. Flexibility**

- Plain-language definitions reduce implementation drift.
- Optional contamination accommodates diverse use cases (research vs. clinical).

*82. Coverage Practicality**

- 15x covers most germline needs; 20x adds marginal value.
- Median/mean ratio is robust for evenness (per ICGC experience).

**3. Ecosystem Alignment**

- AoU metrics inform but don’t dictate standards.
- Tumor-specific methods deferred to somatic roadmap.

## 2023-02-21

### Decision

**1. Repository Structure & Governance**

- Folder Organization:
    - `/roadmap`: High-level deliverables
    - `/definitions`: Metric specifications (one .md per metric)
    - `/implementations`: Reference workflows (Singapore NPM, Argo)
- Approval Process: Merge PRs after 72-hour review window.

**2. Metric Definition Standards**

- Template:
```
markdown
Copy
Download
```
```
### `ID`
`mean_autosome_coverage`  


### `Description`  
Mean coverage depth across autosomes, excluding assembly gaps.  


### `Implementation`  
- **Tools**: mosdepth (default), samtools  
- **Parameters**: `-Q 13`, `--region autosomes.bed`  
- **Validated Ranges**: 25–35x (WGS)  


### `Notes`  
Aligns with All of Us 20x threshold but uses 15x for broader utility. 
```


### Rationale

**1. Clarity & Reproducibility**

- Plain-English definitions prevent tool-specific assumptions.
- Dockstore integration enables cloud-scale validation.

**2. Biological Utility**

- Dual mapping metrics address distinct quality aspects.
- Whitelists ensure consistent autosomal coverage calculations.

**3. Ecosystem Alignment**

- AoU/ICGC cross-pollination avoids duplication.
- Modular structure accommodates future expansions (e.g., somatic)

## 2023-01-17

**NA**

## 2022-12-13

### Decision

**1. GitHub Governance**

  - Protected `main` branch: Require 2-3 reviews before merging (Maxime/Lindsay to configure)
  - Process documentation: Adopt conventions from other GA4GH Work Stream repos (Lindsay to draft)
  - Repository naming: Retain current name (`wgs-sample-qc`), clarify scope in README

**2. SC Proposal Preparation**

- Submit questionnaire by Jan 12, with slides to follow
- Key deliverables:
    - Standardized JSON schemas for 7 core metrics
    - Reference implementations (Singapore-NPM, AGHA)
    - Benchmarking protocol (GIAB + 10X Linked-Read datasets)

**3. Technical Scope**

- Exclude sample/tumor metadata: QC outputs will not include genetic or clinical data
- API development: Defer to later phase; focus on file-based JSON outputs initially

**4. Functional Equivalence**

- Use metrics to compare pipelines (e.g., via statistical thresholds)
- Adopt alignment statistics framework from `alignstats` as reference

### Rationale

- Controlled Collaboration: Protected branches ensure stability while allowing community input.
- Clear Boundaries: Separating QC metrics from sample metadata prevents misuse and simplifies adoption.
- SC Alignment: Explicit deliverables (JSON schemas, implementations) demonstrate production readiness.
- Interoperability: File-first approach ensures compatibility with existing workflows; API can be added later.

## 2022-09-13

### Decision

**1. Finalize Reference Implementations**

- Singapore-NPM: Complete DSL2 transition and local resource handling (Nicolas/Maxime)
- AGHA: Test and provide feedback on implementation (Sehrish)

**2. Standardize Benchmarking Data**

- Use GIAB Baid dataset (PCR-free/PCR-plus WGS/WES) as primary benchmark
- Supplement with AGHA’s 10X Linked-Read (poor-quality data)
- Host datasets on AWS Open Data/Google Cloud for accessibility (Oliver)

**3. Refine Metric Definitions**

- Revise descriptions for the 7 core metrics (Nicolas/Maxime)
- Align JSON schemas with GA4GH standards

**4. Adjust Roadmap**

- Move ontology development to a later milestone
- Add GA4GH Standards Interoperability as a near-term milestone
- Prioritize pipeline validation over theoretical standardization

### Rationale

**Practical Focus:**

Core metrics and implementations provide immediate value for cross-pipeline comparison.

**Data Diversity:**

Combining GIAB (gold standard) and problematic datasets (10X Linked-Read) ensures robust validation.

**Technical Scalability:**
- DSL2 improves workflow portability.
- Local resource handling reduces runtime dependencies.

**Roadmap Realism:**

Separating ontology work allows focus on production-ready 

## 2022-07-26

### Decision

**1. Prioritize 5 core metrics for initial standardization:**

- Mean autosomal coverage
- Mapping quality distribution
- Contamination estimate
- Insert size metrics
- Read depth distribution

**2. Maintain two implementation tracks:**

- Minimal implementation: Core 5 metrics only (for benchmarking/comparison)
- Extended implementation: Full metric set (for exploratory analysis)

**3. Improve workflow portability:**

- Resolve environment-specific hardcoding in Nextflow/Docker
- Implement versioned releases with changelog
- Adopt GA4GH tool registry (Dockstore) for sharing

**4. Curate test datasets:**

- Include both high-quality (1000 Genomes) and problematic samples
- AGHA to share failed runs (Azure/AWS)
- Explore ICGC blacklisted samples where possible

### Rationale

**1. Practical adoption:**

Core metrics address critical QC needs while remaining manageable
Dual implementation balances standardization with flexibility

**2. Technical robustness:**

Focused metrics simplify cross-tool comparison
Version control ensures reproducibility

**3. Validation requirements:**

Problematic samples are essential for testing metric sensitivity
Public/private dataset mix provides comprehensive coverage

## 2022-05-17

### Decision

**1. Defer large-scale ontology development and focus on:**

- Finalizing JSON schemas for key metrics (e.g., coverage, contamination)
- Publishing reference implementations (Nextflow/Docker workflows)
- Documenting minimum metadata requirements (e.g., refget IDs, tool versions)

**2. Adopt a hybrid approach for ontologies:**

- Use existing terms (e.g., GenEpiO) where possible.
- Define only critical new terms (e.g., "autosomal_depth_of_coverage").
- Link JSON fields to ontology IDs (e.g., `"metric_type"`: `"GENEPIO:XXXX"`).

**3. Curate benchmarking datasets:**

- Prioritize real-world problematic samples (AGHA to share failed runs).
- Supplement with ICGC/CINECA data where accessible.
- Avoid synthetic data (per Ivo’s feedback on biological realism).

**4. Align with GA4GH tooling:**

- Use Dockstore for workflow sharing.
- Adopt refget for reference standardization.

### Rationale

- Practical adoption: JSON schemas and workflows provide immediate value to labs.
- Resource efficiency: Ontology work is time-intensive; defer to post-implementation.
- Real-world validation: Problematic samples (not just GIAB) are critical for QC use cases.
- Interoperability: Hybrid JSON+ontology approach balances rigor and flexibility

## 2022-04-12

### Decision

Adopt OBO Foundry principles for ontology development:

- Reuse existing terms from GenEpiO where applicable
- Create new terms following best practices (precise labels, technical definitions)
- Maintain separation between concepts and implementation details

**2. Pilot with mean autosomal coverage:**

- Create 3 new terms (depth/breadth of autosome coverage)
- Reuse 2 existing GenEpiO terms
- ```Structure as:
Copy
Download```

```
sequencing metric
└── coverage metric
    ├── depth of autosome coverage (new)
    └── breadth of autosome coverage (new)
    }
``` 
**3.Standardize parameters:**

Use "reference genome accession" (refget-compliant)
Replace "BED file name" with "genomic region filter URI"
Rename "minimum mapping quality score" to "minimum mapping quality threshold"

**4. Implement layered specification:**

Ontology layer: Universal definitions (e.g., "depth of coverage")
Application profile: Required fields for implementations (JSON schema)
Guidance documentation: Tool-specific parameters (e.g., mosdepth settings)

### Rationale

**1. Interoperability:**

- OBO Foundry compliance ensures compatibility with existing biomedical ontologies
- GenEpiO provides established framework for genomic quality terms

**2. Precision:**

- Technical definitions disambiguate metrics (e.g., "autosomal" vs whole-genome)
- Parameter standardization prevents implementation drift (e.g., refget for references)

**3. Scalability:**

- Pilot approach validates methodology before expanding to other metrics
- Layered design accommodates both universal concepts and tool-specific needs

**4. FAIR compliance:**

- URIs for region filters enable reproducibility
- Versioned terms maintain backward compatibility

## 2022-03-08 

### Decision

**1. Adopt GENEPIO ontology as foundation for QC metric standardization, with initial focus on:**

- Mean autosomal coverage as pilot term
- Alignment with existing GENEPIO quality terms (e.g., GENEPIO_0000087)

**2. Develop layered implementation:**

- Reference ontology: Generic metric definitions (platform/algorithm-agnostic)
- Application profiles: JSON schemas specifying required fields for implementations
- Controlled vocabularies: For parameters (e.g., mapping quality thresholds)

**3. Curate reference datasets from:**

- Genome in a Bottle (GIAB) Ashkenazim Trio
- ILMN Dragen 1kGP AWS dataset
- CINECA synthetic data (supplemental)

**4. Establish governance model:**

- GENEPIO team maintains core ontology
- GA4GH community extends through application profiles
- Implementation feedback loop via GitHub

### Rationale

**1. Avoids duplication by building on established GENEPIO framework**

**2. Balances flexibility and rigor:**

- Ontology provides semantic backbone
- JSON profiles enable practical adoption

**3. Comprehensive validation:**
- GIAB data provides gold-standard references
- Multiple platforms reveal edge cases

**4. Sustainable maintenance:**

- Leverages existing GENEPIO infrastructure
- Clear separation between universal definitions and implementation-specific needs

## 2022-01-18

### Decision

**1. Expand proof-of-concept analysis to:**

- Include Genome in a Bottle trio datasets
- Compare Dragen vs. non-Dragen implementations (via CWL workflows)
- Analyze diagnostic vs. research pipeline differences (SickKids use case)

**2. Develop a QC metrics ontology with:**

- Standardized JSON schema (initially non-LD, transitionable to JSON-LD)
- Controlled vocabularies for key fields (reference, filters, warning flags)
- Alignment with GA4GH standards (refget for references, future BED file standards)

**3. Define implementation priorities:**

- Core utility tools for metric calculation (independent of alignment/variant calling)
- Warning/flagging system for outlier metrics
- Top-level metadata (pipeline version, reference checksums, UMI info if available)

**4. Engage GA4GH work streams to:**

- Formalize ontology with Melanie Courtot (EBI)
- Align with refget and file format teams

### Rationale

**Evidence-based standardization:**

- SickKids comparison showed pipeline differences are smaller than metric definition differences (e.g., coverage calculations).
- Expanding to public datasets (GIAB) ensures broader applicability.

**Interoperability:**

- Plain JSON allows immediate implementation while enabling future transition to JSON-LD.
- Refget checksums provide precise reference tracking without redundant metadata.

**Practical adoption:**

- Decoupled QC tools enable integration with diverse pipelines (Dragen/non-Dragen).
- Warning flags address real-world needs for outlier detection (e.g., diagnostic labs).

**Community alignment:**

- Leveraging GA4GH ontologies (DUO) ensures compatibility with existing standards.
- CWL workflows support reproducibility across platforms.

## 2021-11-30

### Decision

**1. Adopt an ontology-based approach** for metric standardization, leveraging Melanie Courtot's expertise from EBI and building on DUO ontology experience

**2. Structure implementation documentation with:**

- Clear reporting guidelines with examples
- Implementation-specific sections (organized as a table of contents for submitted tools/scripts)
- Controlled vocabulary section for standardized fields

**3. Implement reference standardization using:**

- Mandatory refget checksums for precise reference identification
- Optional human-readable reference descriptions

**4. Expand proof-of-concept with SickKids diagnostic vs genome center comparisons to identify:**

- Pipeline version differences
- Unexplained metric variations

**5. Separate metadata architecture:**

- Top-level metadata section for global properties
- Metric-specific fields (marked N/A when not applicable)

### Rationale

**Ontology benefits:**

Enables semantic interoperability across implementations
Leverages existing GA4GH expertise (DUO experience)
Provides structured framework for community contributions

**Implementation clarity:**

Multiple real-world examples (SickKids, PRECISE) demonstrate practical adaptation
Structured documentation supports diverse tool integration

**Reference standardization:**

Refget ensures precise reproducibility
Maintains flexibility for different genome builds
Complements ongoing GA4GH work on BED file standardization

**Evidence-based development:**

Diagnostic vs research pipeline comparisons reveal practical challenges
Guides refinement of controlled vocabulary

**Scalable architecture:**

Separated metadata accommodates both global and metric-specific needs
"N/A" convention maintains structure while allowing implementation flexibility

## 2021-10-26

### Decision

**1. Adopt JSON as the primary output format for QC metrics, structured as:**

- `sample_id`,
- `qc_metrics` (aligned with the minimal definitions document),
- `reference_metadata` (e.g., refget checksum, BED file path).

**2. Separate global BAM properties** (e.g., duplicate marking, UMI usage) from per-metric calculations, with:

- A header section documenting filters/assumptions (e.g., clipping, overlapping bases),
- Optional tool-specific annotations (e.g., `samtools` flags).

**3. Prioritize runtime efficiency:**

- Allow streaming computation (e.g., `samtools` `mpileup`),
- Avoid reprocessing BAMs when possible (leverage existing headers/tools like `mosdepth`).

**4. Benchmark implementations using NA12878, focusing on:**

- Coverage discrepancies (autosomes vs. full genome),
- Variant counting methods (SNPs/indels categorization),
- Contamination metric harmonization.

**5. Engage GA4GH Work Streams** (e.g., `VRS`, `refget`) to align with broader standards, but defer BAM header embedding due to impracticality.

### Rationale

**Interoperability:** 

JSON ensures machine-readability and tool-agnostic adoption.

**Transparency:** 

Global headers clarify assumptions (e.g., filters applied) without bloating per-metric outputs.

**Performance:** 

Streaming-compatible tools (e.g., `samtools`) enable scalable QC for large cohorts.

**Validation:** 

NA12878 comparisons expose definitional nuances (e.g., coverage thresholds, overlapping bases).

**Community Alignment:** 

Leveraging GA4GH standards (e.g., `refget`) future-proofs the framework, while avoiding premature BAM header modifications.

## 2021-09-14

### Decision

**1. Define a core set of QC metrics for germline WGS, covering:**

- Alignment (e.g., coverage, mapping quality),
- Variant calling (high-level metrics only),
- Sample contamination (with explicit type definitions),
- Yield & quality (e.g., read quality, duplication).

**2. Standardize metric definitions with:**

- Unique names/IDs,
- Clear descriptions (including assumptions like clipping or filters),
- Preferred open-source tools (avoiding proprietary solutions).

**3. Allow flexible implementations** but require documentation of methodology (e.g., reference regions, tool versions).

**4. Optimize for runtime**—avoid recomputing metrics when avoidable (e.g., reuse BAM/CRAM stats).

**5. Validate via GitHub collaboration**—test implementations on NA12878 and refine definitions iteratively.

### Rationale

**Comparability:** Ensures metrics are interpretable across pipelines.

**Practicality:** Prioritizes widely supported tools and efficient computations.

**Adaptability:** Definitions accommodate multiple technologies (e.g., short/long reads).

**Transparency:** Documenting tool-specific assumptions mitigates misinterpretation (e.g., rounding differences).

**Community-driven:** GitHub-based validation ensures real-world usability.

## 2021-08-10

### Decision

The group decided to define a foundational set of WGS QC metrics, focusing first on those that are:

- Technically feasible to obtain from aligned data (BAM/CRAM)
- Widely used and accepted across institutions
- Relevant for determining sample usability and data quality
- Able to be calculated independently of platform or variant calling pipeline (where possible)

**Initial Metric Categories and Examples**

|Category                     |Example Metrics (Proposed)|
|                             |                          |
|Coverage                     |Mean read depth, % of genome covered at ≥X (e.g., 20x), genome completeness, absolute/effective coverage|
|**Mappability**              |% mappable reads, % mapped, % aligned, cross-species contamination|
|**Library/Read Quality**.    |% duplication, median fragment length, insert size, ATCG dropout, uniformity of coverage|
|**Yield**                    |Total bases > Q30 (e.g., Gb > Q30), total reads                                |
|**Contamination**            |Estimated contamination (e.g., verifyBAMID, % mixed reads), noise proxy metrics|
|**Callable Regions**         |% callable bases (e.g., genome, OMIM, ClinVar), reference genome version and regions covered|
|**Technology-specific flags**|Low-quality base prevalence, read length bias, differences in Q-score distribution (e.g., Illumina vs PacBio)|

**Additional distinctions:**

**Metric format:** scalar (e.g., % mapped) vs. distributional (e.g., insert size histogram)

**Metric derivation:** Derived directly from aligned reads, with clear documentation of computational choices (e.g., read depth calculation approach)

**Standardization approach:** Each metric will be defined both in plain language and optionally mapped to a reference implementation (e.g., Nextflow module)

### Rationale

**1. Wide applicability:** The selected metrics are broadly relevant and feasible for institutions to report without needing extensive pipeline changes.

**2. Reproducibility:** Focusing on BAM/CRAM-level metrics avoids reliance on downstream tools that vary more widely (e.g., variant callers).

**3. Interoperability:** Enables initial comparison across institutions even with varied processing approaches.

**4. Incremental adoption:** Allows organizations to begin contributing metrics from their current pipelines and participate in convergence over time.

**5. Clarity:** A living document and GitHub repository will track metric definitions, including optional reference code.

## 2021-06-29

### Decision

**1: Start with a Minimal, Agreed-Upon Set of QC Metrics**

**2: Develop Clear Definitions for Each Metric**

**3: Separate File Format/Schema from QC Computation Pipeline**

**4: Use the GitHub Repository and a Shared Google Doc for Collaborative Metric Listing**

**5: Exclude Somatic Sequencing from Scope**

**6: Ensure QC Metric Definitions are Build-Agnostic Where Possible**

**7: Encourage Metrics to Be Accompanied by Contextual Information**

**8. Create a Mailing List for Ongoing Communication**


### Rationale

**1.**

- Initiatives have diverse pipelines and stages of QC implementation.
- A common denominator will enable cross-project communication and comparability without requiring changes to local pipelines.
- Enables tracking and understanding across systems with varied infrastructure maturity (e.g., ingest-only QC vs. end-of-project QC).

**2.**

- Different initiatives use the same metric names with differing meanings or computational methods.
- Ambiguity in metric definitions leads to miscommunication both within and across initiatives.
- Needed for interoperability and trust when sharing data or results.

**3.**

- Some participants only need a standardized way to share and store metrics (file format/schema).
- Others also want a pipeline to calculate them.
- Decoupling these allows flexibility: adoption of the schema without forcing a specific implementation.

**4.**

Facilitates asynchronous collaboration.
Enables commenting and harmonization of metric names, definitions, and formats.
Promotes transparency and traceability of decisions made.

**5.**

- Somatic sequencing introduces additional complexity.
- Current efforts focus on germline WGS; including somatic would dilute the effort and make consensus more difficult.

**6.**

- Some initiatives use different reference genomes.
- Metrics need to remain interpretable across builds for consistent reporting and downstream use.

**7.**

- Tool outputs can differ even for the “same” metric, depending on implementation details or assumptions.
- Making the computation method transparent helps others interpret the results accurately and decide on fitness for use.

**8.**

- Supports continuous engagement.
- Avoids fragmented updates and misaligned efforts between meetings.
