# Literature Review Methodology

## PICO Framework

| Component | Definition | Example |
|-----------|-----------|---------|
| **P**opulation | Patient group or condition | Adults with Type 2 diabetes |
| **I**ntervention | Treatment or exposure | GLP-1 receptor agonists |
| **C**omparison | Alternative treatment | Insulin therapy |
| **O**utcome | Measurable result | HbA1c reduction, weight change |

---

## Search Strategy Design

### Database Search Components
1. **Population terms**: MeSH headings + free-text synonyms
2. **Intervention terms**: Drug names, procedure names, synonyms
3. **Boolean operators**: AND (between concepts), OR (within concepts)
4. **Filters**: Date range, language, study type, human subjects
5. **Wildcards**: Truncation (*) for word variations

### Search Example
```
("Type 2 Diabetes Mellitus"[MeSH] OR "type 2 diabet*"[tw])
AND
("GLP-1 receptor agonist*"[tw] OR "glucagon-like peptide"[tw] OR semaglutide[tw] OR liraglutide[tw])
AND
("HbA1c"[tw] OR "glycated hemoglobin"[tw] OR "weight"[tw])
```

### Search Documentation
- Record exact search strings for each database
- Document date of search
- Record number of results per database
- Save all results in reference manager

---

## Screening Process

### Title/Abstract Screening
- Apply inclusion/exclusion criteria
- Two independent reviewers (recommended)
- Track inter-rater reliability (Cohen's kappa >0.8)
- Resolve disagreements by consensus or third reviewer
- Document reasons for exclusion

### Inclusion/Exclusion Criteria Template
| Criterion | Include | Exclude |
|-----------|---------|---------|
| Population | Adults ≥18 with T2DM | Gestational diabetes, T1DM |
| Intervention | GLP-1 RA as monotherapy/add-on | GLP-1 in combination pills |
| Comparator | Any active comparator or placebo | No comparator |
| Outcome | HbA1c, weight, safety | Surrogate endpoints only |
| Study design | RCT, cohort ≥12 weeks | Case reports, reviews, <12 weeks |
| Language | English | Non-English |
| Date | 2010-present | Before 2010 |

### Full-Text Screening
- Apply detailed criteria to full articles
- Document specific exclusion reasons
- Create PRISMA flow diagram

---

## Data Extraction

### Standard Extraction Fields
- Study identification (authors, year, journal)
- Study design and setting
- Population characteristics (N, age, sex, baseline)
- Intervention details (dose, duration, delivery)
- Comparator details
- Outcomes (primary, secondary)
- Results (effect sizes, confidence intervals, p-values)
- Adverse events
- Risk of bias assessment
- Funding source and conflicts of interest

### PRISMA Flow Diagram
Document at each stage:
- Records identified from databases
- Duplicates removed
- Records screened (title/abstract)
- Records excluded (with reasons)
- Full-text articles assessed
- Full-text excluded (with reasons)
- Studies included in synthesis
