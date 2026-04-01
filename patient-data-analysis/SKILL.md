---
name: patient-data-analysis
description: "Patient Data Analysis is a sophisticated capability for extracting actionable insights from diverse patient health information sources, including electronic health records, claims databases, patient registries, wearable device data, and patient-reported outcomes."
---

# Patient Data Analysis

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

Patient Data Analysis is a sophisticated capability for extracting actionable insights from diverse patient health information sources, including electronic health records, claims databases, patient registries, wearable device data, and patient-reported outcomes. This skill employs advanced statistical methods, machine learning algorithms, and clinical informatics techniques to transform raw patient data into intelligence that improves care quality, operational efficiency, and health outcomes.

The core purpose of this skill extends across multiple healthcare domains. In clinical settings, it supports precision medicine initiatives by identifying patient subpopulations likely to respond to specific interventions. In population health management, it enables risk stratification and care gap identification. For healthcare operations, it provides workforce optimization, resource utilization analysis, and throughput improvement recommendations. In research contexts, it facilitates real-world evidence generation and pragmatic trial design.

This skill should be deployed when organizations need to analyze treatment effectiveness in real-world populations, identify high-risk patients for preventive interventions, evaluate quality metrics and outcomes, optimize clinical workflows based on utilization patterns, conduct pharmacovigilance surveillance, support value-based care contracting, or generate regulatory-grade real-world evidence. It is essential for accountable care organizations, integrated delivery networks, health plans, and life sciences companies leveraging real-world data.

The analytical framework adheres to data quality standards including the Kahn Framework for data quality assessment, employs validated phenotyping algorithms from eMERGE and PCORnet networks, and applies causal inference methodologies appropriate for observational data including propensity score methods and instrumental variable approaches.

## 2. Required Inputs/Parameters

**Data Source Specifications:**
- EHR system type and data model (Epic, Cerner, Meditech, FHIR-based)
- Claims database structure (medical, pharmacy, enrollment)
- Registry specifications and data dictionaries
- Patient-generated health data formats
- Laboratory and imaging data sources

**Patient Cohort Parameters:**
- Inclusion/exclusion criteria using clinical concepts
- Observation period specifications
- Index event definitions
- Minimum data completeness requirements
- Demographic and clinical characteristic requirements

**Analytical Parameters:**
- Primary outcomes of interest with operational definitions
- Covariates for adjustment
- Time-to-event specifications
- Subgroup analysis requirements
- Sensitivity analysis specifications

**Compliance and Privacy Parameters:**
- IRB approval documentation or waiver
- Data use agreement specifications
- Minimum necessary standard application
- De-identification requirements (Safe Harbor, Expert Determination)
- Audit logging requirements

## 3. Expected Outputs/Deliverables

**Cohort Characterization:**
- Baseline characteristics tables with standardized mean differences
- Attrition diagrams showing cohort flow
- Data quality assessment reports
- Phenotype validation metrics
- Cohort comparison analyses

**Outcome Analyses:**
- Unadjusted and adjusted outcome rates
- Kaplan-Meier survival estimates with log-rank tests
- Hazard ratios with 95% confidence intervals from Cox models
- Risk difference and relative risk estimates
- Number needed to treat/harm calculations

**Predictive Models:**
- Risk stratification models with discrimination metrics (C-statistic)
- Calibration plots and Hosmer-Lemeshow statistics
- Feature importance rankings
- Model validation results (internal, external, temporal)
- Clinical decision support tool specifications

**Population Health Reports:**
- Care gap analyses with patient lists
- Quality metric dashboards (HEDIS, CMS Stars)
- Utilization patterns and cost analyses
- High-risk patient identification
- Social determinants of health assessments

**Operational Analytics:**
- Throughput and efficiency metrics
- Resource utilization analyses
- Readmission pattern analyses
- Length of stay optimization recommendations
- Appointment scheduling optimization

## 4. Example Use Cases

**Use Case 1: Chronic Disease Risk Stratification**
A Medicare Advantage plan requires population-level risk stratification for diabetes management. The skill processes claims and EHR data for 150,000 members, develops a predictive model for diabetes complications, validates the model against historical outcomes, identifies high-risk members for intensive care management, and quantifies expected cost savings from intervention.

**Use Case 2: Surgical Outcomes Analysis**
A hospital system evaluates its total joint replacement program quality. The skill analyzes 5 years of surgical data, calculates risk-adjusted complication rates, benchmarks against national registries, identifies surgeon and facility factors associated with outcomes, and develops quality improvement recommendations addressing modifiable risk factors.

**Use Case 3: Real-World Evidence for Regulatory Submission**
A pharmaceutical company generates post-market evidence for a cardiovascular medication. The skill designs a retrospective cohort study using federated EHR data, applies propensity score matching to address confounding, conducts effectiveness analysis with FDA-specified endpoints, performs required sensitivity analyses, and produces a study report suitable for regulatory submission.

**Use Case 4: Readmission Reduction Program**
A health system under CMS penalties for excess readmissions implements a predictive analytics program. The skill develops a 30-day readmission risk model, integrates real-time scoring into clinical workflows, identifies patients requiring transitional care interventions, and creates monitoring dashboards to track program effectiveness.

**Use Case 5: Clinical Trial Feasibility**
A contract research organization assesses trial feasibility for a rare disease indication. The skill queries multiple EHR networks to identify potentially eligible patients, characterizes the patient population against protocol criteria, estimates enrollment projections by site, and identifies protocol modifications that would expand the eligible population.

## 5. Prerequisites or Dependencies

**Data Infrastructure:**
- Data warehouse or lakehouse environment
- ETL pipelines for data standardization
- Common data model implementation (OMOP CDM, PCORnet CDM, Sentinel)
- De-identification tools and processes
- Secure analytical environment (FedRAMP, HIPAA-compliant)

**Vocabulary and Standards:**
- Standardized vocabularies (ICD-10, SNOMED CT, RxNorm, LOINC, CPT)
- Mapping tables for source-to-standard concepts
- Phenotype libraries and validation documentation
- Quality measure specifications

**Analytical Tools:**
- Statistical software (R, Python, SAS)
- Machine learning frameworks (scikit-learn, TensorFlow, XGBoost)
- Visualization tools (Tableau, Power BI, R Shiny)
- Cohort building tools (Atlas, TriNetX, HealthVerity)

**Governance Requirements:**
- Data governance framework
- IRB protocols or exemption documentation
- Data use agreements
- Privacy impact assessments
- Audit logging and access controls

**Clinical Expertise:**
- Clinical subject matter expertise for phenotype validation
- Biostatistical consultation for complex analyses
- Health informatics support for data quality assessment
- Clinical operations input for workflow integration

## Using the Reference Files

- [./references/01-fundamentals-of-healthcare-analytics.md](./references/01-fundamentals-of-healthcare-analytics.md): 01 Fundamentals Of Healthcare Analytics
- [./references/01_healthcare_analytics_fundamentals.md](./references/01_healthcare_analytics_fundamentals.md): 01 Healthcare Analytics Fundamentals
- [./references/02-clinical-data-analysis-methods.md](./references/02-clinical-data-analysis-methods.md): 02 Clinical Data Analysis Methods
- [./references/02_clinical_data_analysis_methods.md](./references/02_clinical_data_analysis_methods.md): 02 Clinical Data Analysis Methods
- [./references/03-data-mining-and-predictive-analytics.md](./references/03-data-mining-and-predictive-analytics.md): 03 Data Mining And Predictive Analytics
- [./references/03_healthcare_data_tools_technologies.md](./references/03_healthcare_data_tools_technologies.md): 03 Healthcare Data Tools Technologies
- [./references/04-tools-and-technologies.md](./references/04-tools-and-technologies.md): 04 Tools And Technologies
- [./references/04_privacy_ethics_compliance.md](./references/04_privacy_ethics_compliance.md): 04 Privacy Ethics Compliance
- [./references/05-challenges-ethics-and-best-practices.md](./references/05-challenges-ethics-and-best-practices.md): 05 Challenges Ethics And Best Practices

## References

- [01 Fundamentals Of Healthcare Analytics](references/01-fundamentals-of-healthcare-analytics.md)
- [01 Healthcare Analytics Fundamentals](references/01_healthcare_analytics_fundamentals.md)
- [02 Clinical Data Analysis Methods](references/02-clinical-data-analysis-methods.md)
- [02 Clinical Data Analysis Methods](references/02_clinical_data_analysis_methods.md)
- [03 Data Mining And Predictive Analytics](references/03-data-mining-and-predictive-analytics.md)
- [03 Healthcare Data Tools Technologies](references/03_healthcare_data_tools_technologies.md)
- [04 Tools And Technologies](references/04-tools-and-technologies.md)
- [04 Privacy Ethics Compliance](references/04_privacy_ethics_compliance.md)
- [05 Challenges Ethics And Best Practices](references/05-challenges-ethics-and-best-practices.md)
