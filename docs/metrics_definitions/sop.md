# Standard Operating Procedure (SOP)
![My PDF](SOP_GA4GH_WGSQC_Standards_V2.pdf){ type=application/pdf style="width:100%;height:800px" }

# Standard Operating Procedure (SOP)
### Title
**SOP for Creating New and Updating Existing QC Metric Definitions for WGS-QC Standards v2.0**
###Version
• SOP Version: 1.0

• Maintained by: GA4GH WGS-QC Workgroup
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. Purpose
The purpose of this SOP is to define a clear, standardized process for GA4GH WGS-QC workgroup members and subject-matter experts to contribute to the development of **WGS-QC Standards v2.0.** This includes: 

- Creating **new QC metric definitions** for short-read and long-read WGS 

- Updating or amending **existing QC metric definitions from v1.0**

- Differentiating QC metrics by **sequencing data type (short-read vs long-read)**

This SOP supports the **roadmap v2** activities and ensures consistency, traceability, and reviewability of QC metric definitions prior to publication.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 2. Scope
This SOP applies to: All contributors to the GA4GH WGS-QC Standards GitHub repository 

- Development of QC metrics for:
    - Short-read WGS 
    - Long-read WGS (ONT, PacBio, Constellation) 
- Metric definition work contributing to WGS-QC Standards v2.0

Out of scope: 

- Tool benchmarking or performance evaluation 
- Dataset-specific QC thresholds
-------------------------------------------------------------------------------------------------------------------------------------------------------------

 
### 3. References

- [GA4GH WGS-QC GitHub Repository (v1.0):](https://github.com/ga4gh/quality-control-wgs)

- [Metric Definition Template (current):](https://ga4gh.github.io/quality-control-wgs/metrics_definitions/)

- [Published specifications (gh-pages):](https://github.com/ga4gh/quality-control-wgs/tree/gh-pages)
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 4. Roles and Responsibilities

#### 4.1 Contributors

- Propose new QC metrics or updates to existing metrics
- Author metric definitions using the agreed template
- Submit changes via GitHub pull requests

#### 4.2 Reviewers (WGS-QC Workgroup)

- Review metric definitions for clarity, correctness, and alignment with consensus
- Provide feedback and request revisions where required
- Approve and merge contributions

#### 4.3 Maintainers

- Manage branches and releases
- Publish approved metric definitions to gh-pages

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 5. Overview of Contribution Workflow

1.	Clone the GA4GH WGS-QC repository
2.	Create a new feature branch
3.	Create or update QC metric definition files `(.md)`
4.	Commit and push changes
5.	Create a pull request (PR)
6.	Review, revise, and merge into `develop-definition-v2`
7.	Publish approved metrics to `gh-pages`

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 6. Metric Definition Requirements (v2.0)
Each QC metric definition **must** follow the latest workgroup-consensus template and be authored as a **Markdown (.md)** file.

#### 6.1 Mandatory and Optional Fields
Each metric definition must include the following sections:

- **ID (mandatory):** Unique metric identifier (e.g., `yield_bp_q30`)
- **Description (mandatory):** Clear description of what the metric measures
- **Implementation details (mandatory):** How the metric is calculated or derived
- **Type (mandatory):** Whether the metric value is an integer or float. For float values, the minimal required decimal precision must be defined to ensure consistent reporting across workflows.
- **Functionally equivalent implementation (optional):** Alternative implementations/tools
- **Data type (mandatory):** `short-read | long-read`
- **Assembly (mandatory):** `GRCh37 | GRCh38`
- **Version (mandatory):** `1.0 | 2.0`
- **Sequencing platform / Technology (optional):** `Illumina` | `Constellation` | `ONT` | `PacBio`
- **Associated aligner (optional):** Free text or controlled list (e.g., `BWA-MEM, DRAGEN, Minimap2..`)
- **Associated variant caller (optional):** Free text or controlled list (e.g., `GATK, DRAGEN, DeepVariant..`)
#### 6.2 Versioning Guidance
- Existing v1.0 metrics that are **amended or extended** for v2.0 must:
    - Clearly state `Version: 2.0`
    - Document changes or clarifications in the implementation details
- New metrics introduced in Roadmap v2 must be labelled as Version: 2.0

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 7. GitHub Contribution Procedure
#### 7.1 Clone Repository
```
git clone https://github.com/ga4gh/quality-control-wgs.git
cd quality-control-wgs
```
#### 7.2 Create Feature Branch
```
Create a new branch for your contribution:
git checkout -b feature/<short-description>
```
Example:
```
git checkout -b feature/long-read-coverage-metric
```
#### 7.3 Navigate to Metric Definitions Directory
```
cd docs/metrics_definitions
```
#### 7.4 Create or Update Metric Definition
- Create a new `.md` file using the metric definition template, **or**
- Amend/update an existing metric definition to:
    - Correct errors
    - Improve clarity
    - Differentiate short-read vs long-read sequencing
File naming should be descriptive and consistent with existing metrics.
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------

### 8. Commit and Push Changes
Stage and commit your changes:

```
git add <file(s)>
git commit -m "Add/update QC metric definition for <metric name>"
```

Push your feature branch to origin:

```
git push origin feature/<short-description>
```
 
### 9. Pull Request (PR) Process

1.	Create a Pull Request (PR) from your feature branch
2.	Target branch: `develop-definition-v2`
3.	Provide a clear PR description including:
    - Purpose of the metric
    - Whether it is new or an update to v1.0
    - Any sequencing-type-specific considerations
    - Links to or references for any relevant GitHub issues, pull requests, or discussion threads

-------------------------------------------------------------------------------------------------------------------------------------------------------------

### 9.1 Recommended Pull Request (PR) Description Template
```
## Summary 
Brief description of the QC metric being added or updated. 
 
## Metric Scope 
- Metric name / ID: 
- New metric or update to existing v1.0 metric: 
- Data type: short-read | long-read 
 
## Rationale 
Explain why this metric is required or why changes are proposed. 
 
## Implementation Notes 
Key implementation details, assumptions, or sequencing-technology-specific 
considerations. 
 
## Related Discussions 
- GitHub issue(s): <link> 
- Pull request(s): <link> 
- Workgroup discussion / meeting notes (if applicable): <link>
```

Contributors are encouraged to use the following template when creating a pull request:9.2 Review and Approval

- PRs will be reviewed by WGS-QC workgroup members
- Contributors may be asked to revise content based on feedback
- Once approved, PRs will be merged into `develop-definition-v2` branch

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 10. Publication
- Approved metric definitions will be published via the `gh-pages` branch
- Published content represents the **official WGS-QC v2.0 product specification**

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 11. Change Management
- All changes must be tracked via GitHub commits and PRs
- Major updates or breaking changes should be discussed during workgroup meetings

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
### 12. Contact
For questions or clarification, please contact the GA4GH WGS-QC workgroup via the GitHub repository or scheduled workgroup meetings.

------------------------------------------------------------------------------------------------------------------------------------------------------------- 

### List of Potential Long-read QC Metrics
The following non-exhaustive list represents candidate QC metrics for consideration as part of the WGS-QC v2.0 roadmap. These metrics are provided to guide discussion, prioritization, and contribution by the workgroup and domain experts.

```
Read and Coverage-level Metrics::

Read N50
Yield (bp) 
Yield (reads ≥ N bp): 0, 10,000, 50,000, 100,000 
Read number ?
Reads mapped 
Reads mapped (%) 
Median read quality / Mean read quality 
Median read length / Mean read length 
Autosomal depth (mean), non-gap white listed regions 
Bases with ≥ N-fold coverage (e.g. 5X / 10X / 15X) 
Genome coverage uniformity 
Contamination

Variant-level Metrics::

SNV count 
Indel count (short indels | long indels) 
Heterozygous / Homozygous ratio (SNVs | Indels) 
Transition / Transversion (Ti/Tv) rate

```

