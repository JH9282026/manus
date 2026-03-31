# Systematic Literature Review Methodology

## Introduction

Systematic literature reviews are rigorous, transparent, and reproducible methods for identifying, evaluating, and synthesizing existing research on a specific topic. Unlike traditional narrative reviews, systematic reviews follow explicit protocols to minimize bias and provide comprehensive coverage of available evidence.

## Systematic Review Process

### 1. Define Research Question

**PICO Framework** (for clinical/intervention studies)
- **P**opulation: Who is the study about?
- **I**ntervention: What is being tested or examined?
- **C**omparison: What is it being compared to?
- **O**utcome: What are the measured results?

**Alternative Frameworks**
- **SPIDER**: Sample, Phenomenon of Interest, Design, Evaluation, Research type
- **SPICE**: Setting, Perspective, Intervention, Comparison, Evaluation
- **PEO**: Population, Exposure, Outcome

**Research Question Characteristics**
- Specific and focused
- Answerable with available evidence
- Relevant to field or practice
- Feasible within time and resource constraints

### 2. Develop Protocol

**Protocol Components**
- Background and rationale
- Research objectives and questions
- Eligibility criteria (inclusion/exclusion)
- Search strategy and databases
- Study selection process
- Data extraction methods
- Quality assessment approach
- Synthesis and analysis plan
- Timeline and resources

**Protocol Registration**
- PROSPERO (health/social care)
- Open Science Framework (OSF)
- Provides transparency and prevents duplication
- Allows for protocol amendments with justification

### 3. Literature Search

**Database Selection**

*Multidisciplinary Databases*
- Web of Science
- Scopus
- Google Scholar
- Microsoft Academic

*Subject-Specific Databases*
- PubMed/MEDLINE (medicine, life sciences)
- IEEE Xplore (engineering, computer science)
- PsycINFO (psychology)
- ERIC (education)
- EconLit (economics)
- JSTOR (humanities, social sciences)

**Search Strategy Development**

*Keywords and Concepts*
- Identify key concepts from research question
- Generate synonyms and related terms
- Consider spelling variations and acronyms
- Use subject headings (MeSH, thesaurus terms)

*Boolean Operators*
- AND: Narrows search (both terms must be present)
- OR: Broadens search (either term can be present)
- NOT: Excludes terms

*Search Techniques*
- Truncation (*): Finds word variations (educat* = education, educational, educator)
- Wildcards (?): Replaces single character (wom?n = woman, women)
- Phrase searching: "climate change" (exact phrase)
- Proximity operators: NEAR, ADJ (terms within specified distance)

*Example Search String*
```
(("machine learning" OR "deep learning" OR "artificial intelligence") 
AND ("healthcare" OR "medical" OR "clinical") 
AND ("diagnosis" OR "prediction" OR "prognosis"))
```

**Search Documentation**
- Record all databases searched
- Document search strings for each database
- Note date of search and results count
- Save search history and results
- Enable reproducibility and transparency

**Grey Literature**
- Conference proceedings
- Dissertations and theses
- Government reports
- Technical reports
- Preprints (arXiv, bioRxiv, SSRN)
- Clinical trial registries

### 4. Study Selection

**Screening Process**

*Title and Abstract Screening*
- Initial screening based on titles and abstracts
- Apply inclusion/exclusion criteria
- Quick assessment of relevance
- Typically excludes 70-90% of records

*Full-Text Screening*
- Detailed review of full articles
- Apply complete eligibility criteria
- Document reasons for exclusion
- Resolve ambiguous cases

**Inclusion/Exclusion Criteria**

*Common Criteria*
- Publication date range
- Language restrictions
- Study design (RCT, observational, qualitative)
- Population characteristics
- Intervention or exposure type
- Outcome measures
- Publication status (peer-reviewed only vs. grey literature)

**Screening Tools**
- Covidence
- Rayyan
- DistillerSR
- EPPI-Reviewer
- Abstrackr

**Inter-Rater Reliability**
- Multiple reviewers screen independently
- Calculate agreement (Cohen's kappa, percent agreement)
- Resolve disagreements through discussion or third reviewer
- Typical threshold: Kappa > 0.60

### 5. Data Extraction

**Extraction Form Development**
- Pilot test on sample of studies
- Refine based on pilot results
- Ensure captures all relevant data
- Balance comprehensiveness with feasibility

**Data Elements**

*Study Characteristics*
- Authors, year, journal
- Study design and methodology
- Setting and context
- Sample size and characteristics
- Funding sources

*Intervention/Exposure Details*
- Description and components
- Dosage, duration, frequency
- Delivery method
- Comparison/control conditions

*Outcomes*
- Primary and secondary outcomes
- Measurement methods and tools
- Time points
- Results (means, SDs, effect sizes, p-values)

*Quality Indicators*
- Randomization method
- Blinding procedures
- Attrition rates
- Conflicts of interest

**Extraction Process**
- Dual extraction (two reviewers independently)
- Compare and resolve discrepancies
- Contact authors for missing data
- Document extraction decisions

### 6. Quality Assessment

**Risk of Bias Tools**

*Randomized Controlled Trials*
- Cochrane Risk of Bias Tool (RoB 2)
- Domains: Randomization, deviations, missing data, measurement, selection of reported results

*Observational Studies*
- Newcastle-Ottawa Scale (NOS)
- ROBINS-I (Risk Of Bias In Non-randomized Studies)
- Domains: Selection, comparability, outcome assessment

*Qualitative Studies*
- Critical Appraisal Skills Programme (CASP)
- Joanna Briggs Institute (JBI) Critical Appraisal Tools

**Quality Scoring**
- Rate each domain (low/high/unclear risk)
- Overall quality rating (high/moderate/low)
- Consider impact on results interpretation
- May inform sensitivity analyses

### 7. Data Synthesis

**Narrative Synthesis**
- Textual description of findings
- Organize by themes, outcomes, or study characteristics
- Identify patterns and relationships
- Discuss heterogeneity and inconsistencies
- Appropriate when meta-analysis not feasible

**Meta-Analysis**

*When Appropriate*
- Sufficient number of similar studies (typically ≥3)
- Comparable interventions and outcomes
- Quantitative data available
- Acceptable heterogeneity

*Effect Size Measures*
- Continuous outcomes: Mean difference, standardized mean difference (Cohen's d, Hedges' g)
- Binary outcomes: Risk ratio, odds ratio, risk difference
- Time-to-event: Hazard ratio

*Statistical Models*
- Fixed-effect model: Assumes single true effect
- Random-effects model: Assumes distribution of true effects
- Choice based on heterogeneity and assumptions

*Heterogeneity Assessment*
- I² statistic: Percentage of variation due to heterogeneity
  - 0-40%: Low heterogeneity
  - 30-60%: Moderate heterogeneity
  - 50-90%: Substantial heterogeneity
  - 75-100%: Considerable heterogeneity
- Q statistic and p-value
- Tau² (between-study variance)

*Forest Plots*
- Visual representation of meta-analysis results
- Shows individual study effects and confidence intervals
- Overall pooled effect with diamond
- Facilitates interpretation of heterogeneity

**Subgroup Analysis**
- Examine effects in subgroups (e.g., by age, intervention type)
- Test for subgroup differences
- Explore sources of heterogeneity
- Pre-specify in protocol to avoid data dredging

**Sensitivity Analysis**
- Assess robustness of findings
- Exclude low-quality studies
- Use different statistical models
- Examine impact of outliers
- Test assumptions

### 8. Reporting

**PRISMA Guidelines**
- Preferred Reporting Items for Systematic Reviews and Meta-Analyses
- 27-item checklist for transparent reporting
- Flow diagram showing study selection process
- Widely adopted standard

**PRISMA Flow Diagram**
```
Records identified through database searching (n=X)
↓
Records after duplicates removed (n=X)
↓
Records screened (n=X) → Records excluded (n=X)
↓
Full-text articles assessed (n=X) → Full-text excluded with reasons (n=X)
↓
Studies included in qualitative synthesis (n=X)
↓
Studies included in meta-analysis (n=X)
```

**Key Report Sections**
- Abstract (structured)
- Introduction (rationale, objectives)
- Methods (protocol, eligibility, search, selection, data extraction, quality assessment, synthesis)
- Results (study selection, characteristics, quality, synthesis)
- Discussion (summary, limitations, implications)
- Conclusions
- Funding and conflicts of interest

## Advanced Topics

### Network Meta-Analysis
- Compares multiple interventions simultaneously
- Uses direct and indirect evidence
- Ranks interventions by effectiveness
- Requires specialized software (e.g., WinBUGS, JAGS)

### Individual Patient Data (IPD) Meta-Analysis
- Uses raw data from individual studies
- More powerful than aggregate data meta-analysis
- Allows standardized analyses and subgroup exploration
- Requires collaboration with original study authors

### Meta-Regression
- Examines relationship between study characteristics and effect sizes
- Explores sources of heterogeneity
- Requires sufficient number of studies (typically ≥10)
- Can be univariate or multivariate

### Publication Bias Assessment

**Funnel Plots**
- Scatter plot of effect size vs. precision
- Asymmetry suggests publication bias
- Visual inspection and statistical tests (Egger's test)

**Trim and Fill Method**
- Estimates and adjusts for missing studies
- Provides adjusted effect size estimate

**Fail-Safe N**
- Number of null studies needed to nullify effect
- Large N suggests robust finding

## Software and Tools

**Reference Management**
- EndNote, Mendeley, Zotero
- Import search results
- Remove duplicates
- Organize and annotate

**Screening and Data Extraction**
- Covidence, Rayyan, DistillerSR
- Collaborative platforms
- Streamline screening and extraction
- Track progress and decisions

**Meta-Analysis**
- RevMan (Cochrane)
- Comprehensive Meta-Analysis (CMA)
- R packages (meta, metafor)
- Stata (metan, metareg)

**Quality Assessment**
- RoB 2 tool (Cochrane)
- ROBVIS (visualization)
- GRADEpro (evidence quality)

## Best Practices

1. **Pre-register protocol**: Enhances transparency and credibility
2. **Comprehensive search**: Multiple databases, grey literature, hand-searching
3. **Dual screening and extraction**: Reduces errors and bias
4. **Quality assessment**: Informs interpretation and recommendations
5. **Transparent reporting**: Follow PRISMA guidelines
6. **Acknowledge limitations**: Discuss search limitations, heterogeneity, bias
7. **Update regularly**: Systematic reviews become outdated; plan for updates

## Conclusion

Systematic literature reviews are the gold standard for synthesizing research evidence. By following rigorous, transparent methods, researchers can provide comprehensive, unbiased summaries of existing knowledge, identify research gaps, and inform policy and practice decisions.
