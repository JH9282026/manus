---
name: patent-research-prior-art-analysis
description: "Patent Research & Prior Art Analysis is a specialized intellectual property research skill that systematically searches, analyzes, and interprets patent documentation and related prior art to inform innovation strategy, patentability assessments, and freedom-to-operate evaluations."
---

---
name: Patent Research & Prior Art Analysis
description: Conducts comprehensive patent landscape analysis and prior art searches to assess patentability, identify freedom-to-operate risks, and support intellectual property strategy decisions.
---

# Patent Research & Prior Art Analysis


## Overview

This section provides an overview of the skill.

## Skill Description and Purpose

Patent Research & Prior Art Analysis is a specialized intellectual property research skill that systematically searches, analyzes, and interprets patent documentation and related prior art to inform innovation strategy, patentability assessments, and freedom-to-operate evaluations. This skill enables organizations to navigate the complex patent landscape, protect their innovations, and avoid infringement risks.

The primary purpose of this skill is to provide evidence-based intellectual property intelligence that supports critical business decisions. Whether assessing the novelty of an invention before filing a patent application, evaluating infringement risks before product launch, or understanding competitive patent portfolios, this skill delivers structured analysis that informs strategic choices.

This skill should be deployed in several scenarios: before initiating patent prosecution to assess patentability and identify potential obstacles; before product launch to evaluate freedom-to-operate risks; during M&A due diligence to assess IP assets; when developing R&D strategy to identify white spaces; and when monitoring competitor IP activity for strategic intelligence.

The analysis framework encompasses patent literature (granted patents and published applications across jurisdictions), non-patent literature (academic papers, conference proceedings, technical standards, product documentation), and commercial prior art (existing products, marketing materials, trade show demonstrations). By examining this comprehensive prior art landscape, the skill provides thorough assessments that meet professional standards.

It is critical to note that while this skill provides valuable preliminary research and analysis, it does not constitute legal advice. Final patent strategy decisions should involve consultation with qualified patent attorneys or agents who can provide legally privileged opinions.

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `research_type` | String | Type of analysis ("patentability", "freedom_to_operate", "landscape", "invalidity") | Yes |
| `subject_technology` | Object | Technical description of the invention or product | Yes |
| `jurisdictions` | Array[String] | Geographic scope for analysis (e.g., ["US", "EP", "CN", "JP"]) | Yes |
| `technical_field` | String | Technology domain and classification codes | Yes |

### Subject Technology Specification

```yaml
subject_technology:
  title: "Descriptive title of invention/product"
  
  technical_description:
    problem_statement: "Technical problem being solved"
    solution_summary: "High-level description of the solution"
    detailed_description: "Comprehensive technical explanation"
    novel_features: ["List of potentially novel elements"]
    
  technical_specifications:
    components: ["Key technical components"]
    materials: ["Relevant materials if applicable"]
    processes: ["Key process steps if applicable"]
    parameters: ["Critical parameters and ranges"]
    
  context:
    field_of_invention: "Technology classification"
    related_technologies: ["Adjacent technology areas"]
    known_prior_art: ["References already known"]
```

### Search Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `date_range` | Object | {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"} | Yes |
| `patent_classifications` | Array[String] | CPC, IPC, or USPC codes to search | No |
| `assignee_focus` | Array[String] | Specific companies or inventors to emphasize | No |
| `language_requirements` | Array[String] | Languages for non-English patent analysis | No |
| `non_patent_literature` | Boolean | Include academic and technical literature | No |

### Research Type Specifications

**Patentability Search**
- Focus: Novelty and non-obviousness assessment
- Scope: Prior art predating invention date
- Depth: Comprehensive within relevant classifications

**Freedom-to-Operate (FTO) Analysis**
- Focus: Active patents that may be infringed
- Scope: Currently enforceable patents in target jurisdictions
- Depth: Claim-level analysis for relevant patents

**Patent Landscape Analysis**
- Focus: Overall patent activity in technology space
- Scope: Comprehensive patent portfolio mapping
- Depth: Statistical and strategic analysis

**Invalidity Search**
- Focus: Prior art to challenge specific patent claims
- Scope: Prior art predating target patent priority date
- Depth: Exhaustive search targeting specific claim elements

## Expected Outputs/Deliverables

### Core Deliverables

**1. Prior Art Search Report**

*Executive Summary*
- Research objectives and scope
- Key findings synopsis
- Critical references identified
- Strategic recommendations

*Methodology Section*
- Search strategy documentation
- Databases and sources searched
- Search queries and classifications
- Date parameters and limitations

*Prior Art Analysis*
For each relevant reference:
- Bibliographic information (number, title, assignee, dates)
- Abstract and key figure
- Relevance assessment to subject technology
- Specific teachings that relate to invention
- Element-by-element comparison (for patentability/invalidity)
- Claim mapping (for FTO analysis)
- Risk level assessment (High/Medium/Low)

**2. Claim Charts (For FTO/Invalidity)**

| Claim Element | Prior Art Reference | Relevant Disclosure | Analysis |
|--------------|--------------------|--------------------|----------|
| Preamble | US Patent X | Paragraph [0045] | Direct teaching of... |
| Element 1a | Publication Y | Figure 3, col. 4 | Shows substantially similar... |
| Element 1b | Product Z documentation | Page 12 | Demonstrates commercial use of... |

**3. Patent Landscape Map (For Landscape Analysis)**

*Quantitative Analysis*
- Patent filing trends over time
- Geographic distribution of filings
- Top assignee rankings
- Technology classification breakdown
- Citation network analysis

*Strategic Analysis*
- White space identification
- Technology trajectory assessment
- Competitive positioning map
- Collaboration network visualization
- Licensing opportunity identification

**4. Risk Assessment Matrix**

| Reference | Relevance | Risk Level | Claim Coverage | Recommendations |
|-----------|-----------|------------|----------------|-----------------|
| US10,XXX,XXX | High | Critical | Claims 1, 3, 7 | Design around required |
| EP3,XXX,XXX | Medium | Moderate | Claim 12 only | Monitor; low coverage |
| CN1XX,XXX,XXX | Low | Minimal | None directly | No action needed |

**5. Strategic Recommendations**

- Patentability assessment with confidence level
- Recommended claim scope strategies
- Design-around opportunities identified
- Licensing considerations
- Further investigation recommendations
- Timeline and priority recommendations

### Output Formats

| Deliverable | Format | Specifications |
|-------------|--------|----------------|
| Search Report | PDF/Markdown | 30-100 pages depending on scope |
| Claim Charts | Excel/PDF | Detailed element mapping |
| Reference Database | Structured data | All analyzed references |
| Landscape Visualizations | PNG/Interactive | Charts, maps, networks |
| Executive Presentation | PPTX/PDF | 10-20 slide summary |

### Quality Standards

- Search comprehensiveness: Coverage of major patent databases (USPTO, EPO, WIPO, CN, JP, KR)
- Non-patent literature: Academic databases, IEEE, technical standards
- Date accuracy: Proper priority date handling
- Translation quality: Machine translation with key passage human review
- Relevance precision: Focus on materially relevant references
- Classification completeness: Full CPC/IPC coverage for technology area
- Documentation: Reproducible search methodology

## Example Use Cases

### Use Case 1: Pre-Filing Patentability Assessment

**Scenario**: Technology company developed novel machine learning algorithm for predictive maintenance and needs to assess patentability before investing in patent prosecution.

**Subject Technology**: Neural network architecture combining time-series analysis with anomaly detection for industrial equipment failure prediction

**Analysis Scope**: Comprehensive prior art search in US, EP, CN, JP covering patent and non-patent literature from relevant period

**Deliverables**: Prior art search report identifying closest references, novelty assessment for each claim element, recommended claim scope, and prosecution strategy recommendations

### Use Case 2: Freedom-to-Operate for Product Launch

**Scenario**: Medical device company preparing to launch new surgical instrument needs FTO clearance for US and European markets.

**Subject Technology**: Detailed product specifications including mechanical design, electronics, software functionality, and manufacturing processes

**Analysis Scope**: Active patents from major competitors and NPEs in US and EP that could cover product features, with claim-level analysis

**Deliverables**: FTO report with identified risk patents, claim charts for high-risk references, risk matrix with prioritization, design-around recommendations, and licensing target identification

### Use Case 3: Competitive Patent Landscape

**Scenario**: R&D organization planning 5-year research strategy needs to understand patent landscape in quantum computing to identify opportunities and avoid crowded spaces.

**Subject Technology**: Quantum computing hardware, error correction, and algorithm optimization

**Analysis Scope**: Comprehensive landscape of quantum computing patents across all major offices, including filing trends, assignee analysis, and technology clustering

**Deliverables**: Landscape report with filing trend analysis, competitive positioning maps, white space identification, technology trajectory assessment, and strategic recommendations for R&D focus areas

### Use Case 4: Patent Invalidity Research

**Scenario**: Company facing patent infringement assertion needs prior art to challenge validity of asserted patent claims.

**Subject Technology**: Accused product features mapped to asserted patent claims

**Analysis Scope**: Exhaustive search for prior art predating target patent priority date, including international patents, academic literature, standards, and commercial products

**Deliverables**: Invalidity search report with strongest prior art references, detailed claim charts mapping prior art to each claim element, anticipation and obviousness arguments, and litigation support documentation

## Prerequisites or Dependencies

### Required Capabilities

| Capability | Purpose | Criticality |
|------------|---------|-------------|
| Patent database access | Primary search capability | Essential |
| Document retrieval | Full patent document access | Essential |
| Technical analysis | Claim interpretation | Essential |
| Foreign language processing | Non-English patent analysis | Important |
| Classification expertise | Effective search strategy | Essential |

### Database Access Requirements

**Essential Patent Databases**
- USPTO (PatFT, AppFT, PTAB documents)
- EPO (Espacenet, European Patent Register)
- WIPO (PatentScope)
- Google Patents (cross-jurisdictional)
- China CNIPA
- Japan JPO

**Non-Patent Literature Sources**
- IEEE Xplore
- ACM Digital Library
- Google Scholar
- arXiv
- Technical standards bodies (ISO, IEEE standards)
- Company technical documentation

### Technical Prerequisites

- Understanding of patent claim interpretation
- Familiarity with patent classification systems (CPC, IPC, USPC)
- Knowledge of patent prosecution procedures
- Ability to read and analyze technical specifications
- Boolean search query construction skills
- Prior art date determination expertise

### Jurisdictional Knowledge

- US patent law basics (novelty, non-obviousness, written description)
- EPO patent requirements (European Patent Convention)
- PCT filing and national phase procedures
- Major jurisdiction differences (US first-to-file, grace periods)
- Patent term and maintenance requirements

### Limitations and Disclaimers

- This skill provides research and analysis, not legal opinions
- FTO conclusions require attorney review for privileged status
- Claim interpretation may differ from court/office interpretation
- Non-English patents subject to translation limitations
- Unpublished applications not accessible in search
- Commercial prior art may be difficult to date definitively
- Final patentability determined by patent office examination

## Using the Reference Files

- [01 Fundamentals Of Prior Art Analysis](./references/01-fundamentals-of-prior-art-analysis.md): 01 Fundamentals Of Prior Art Analysis
- [01 Prior Art Search Fundamentals](./references/01_prior_art_search_fundamentals.md): 01 Prior Art Search Fundamentals
- [02 Search Strategies And Methodologies](./references/02-search-strategies-and-methodologies.md): 02 Search Strategies And Methodologies
- [02 Search Methodologies Techniques](./references/02_search_methodologies_techniques.md): 02 Search Methodologies Techniques
- [03 Databases And Research Tools](./references/03-databases-and-research-tools.md): 03 Databases And Research Tools
- [03 Patent Databases Resources](./references/03_patent_databases_resources.md): 03 Patent Databases Resources
- [04 Invalidity Analysis And Patent Challenges](./references/04-invalidity-analysis-and-patent-challenges.md): 04 Invalidity Analysis And Patent Challenges
- [04 Analysis Documentation Reporting](./references/04_analysis_documentation_reporting.md): 04 Analysis Documentation Reporting
- [05 Legal Framework And Best Practices](./references/05-legal-framework-and-best-practices.md): 05 Legal Framework And Best Practices
