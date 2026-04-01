---
name: machine-translation-post-editing
description: "Perform professional machine translation post-editing (MTPE) to refine MT output for accuracy, fluency, and cultural appropriateness. Use for: light post-editing (LPE) of internal documents, full post-editing (FPE) of customer-facing content, quality assessment of neural MT systems, optimizing MTPE workflows with CAT tools, implementing ISO 18587 standards, training MT engines with feedback, managing translation memory and termbases, evaluating post-editing effort, and ensuring consistency across multilingual projects."
---

# Machine Translation Post-Editing

Refine machine-translated content through professional post-editing to achieve publication-ready quality while maintaining efficiency.

## Overview

Machine Translation Post-Editing (MTPE) combines the speed of automated translation with human linguistic expertise. This skill covers the complete MTPE workflow from source text optimization through quality assurance, including light and full post-editing approaches, CAT tool integration, quality estimation, and adherence to international standards like ISO 18587.

## Post-Editing Types and Selection

| Content Type | Editing Level | Target Quality | Speed Gain | Use Cases |
|--------------|---------------|----------------|------------|------------|
| Internal documentation | Light (LPE) | Comprehensible | 2-3x faster than human translation | Technical docs, internal communications, knowledge bases |
| Customer-facing content | Full (FPE) | Publication-ready | 15-30% faster than human translation | Marketing materials, legal documents, medical content, educational materials |
| User-generated content | Light (LPE) | Understandable | 2-3x faster | Community forums, reviews, social media |
| Brand communications | Full (FPE) | Native-like fluency | 15-30% faster | Website copy, product descriptions, press releases |
| Technical specifications | Full (FPE) | Precise accuracy | 15-30% faster | Engineering docs, regulatory filings, safety information |

**Light Post-Editing (LPE)** focuses on correcting errors that impede comprehension—grammatical mistakes, spelling errors, obvious mistranslations. The goal is rapid comprehensibility without extensive stylistic refinement.

**Full Post-Editing (FPE)** aims for quality comparable to human translation, addressing accuracy, style, tone, cultural appropriateness, and readability. Includes sentence restructuring, terminology optimization, and stylistic improvements.

## MTPE Workflow Framework

### 1. Pre-Editing and Source Optimization

Prepare source text before MT processing:

- **Simplify syntax**: Limit sentences to ~20 words for optimal MT performance
- **Standardize terminology**: Use consistent terms throughout source content
- **Remove ambiguity**: Spell out dates, clarify pronouns, avoid idioms
- **Clean formatting**: Ensure consistent structure and remove unnecessary markup
- **Quality check**: Proofread source text to eliminate errors that MT will propagate

### 2. MT Engine Selection and Customization

- **Language pair optimization**: Select engines trained on your language combination
- **Domain specialization**: Use industry-specific MT engines (legal, medical, technical)
- **Custom training**: Feed high-quality translation memories and glossaries to the engine
- **Quality estimation**: Test multiple engines and compare output quality before committing
- **Avoid generic engines**: Google Translate and similar tools lack domain specialization

### 3. Initial Quality Assessment

Before deep editing:

- **Skim the output**: Identify major errors, inconsistencies, or problematic sections
- **Assess MT quality**: Determine if post-editing is viable or if retranslation is needed
- **Prioritize segments**: Focus effort on high-value or high-visibility content
- **Check terminology**: Verify that key terms are translated correctly
- **Identify patterns**: Note recurring errors to address systematically

### 4. Post-Editing Execution

**Accuracy corrections:**
- Fix mistranslations and factual errors
- Verify numbers, dates, names, and technical terms
- Ensure meaning aligns with source content
- Validate against approved terminology

**Fluency improvements:**
- Smooth awkward phrasing and unnatural constructions
- Improve sentence flow and readability
- Adjust word order for target language conventions
- Eliminate redundancy and verbosity

**Style and tone adaptation (FPE only):**
- Match brand voice and communication style
- Adapt register (formal/informal) to context
- Localize cultural references and idioms
- Ensure consistency in voice and perspective

### 5. Quality Assurance and Validation

- **Linguistic QA**: Proofread for grammar, spelling, punctuation
- **Technical QA**: Verify formatting, tags, placeholders, variables
- **Terminology consistency**: Check against glossaries and style guides
- **Comparative review**: Spot-check against source for accuracy
- **Automated QA tools**: Run checks for common errors (double spaces, missing punctuation)

## CAT Tool Integration

### Essential CAT Features for MTPE

| Feature | Purpose | Benefit |
|---------|---------|----------|
| Translation Memory (TM) | Store and reuse previous translations | Ensures consistency, reduces repetitive work |
| Termbases/Glossaries | Manage approved terminology | Maintains terminology consistency across projects |
| Quality Estimation (QE) | Predict MT output quality | Prioritizes editing effort, identifies problematic segments |
| Automated QA checks | Detect formatting and linguistic errors | Catches common mistakes before delivery |
| Segment filtering | Sort by quality score or edit distance | Focuses attention on segments needing most work |
| Concordance search | Find term usage in context | Ensures consistent translation of recurring phrases |

### Recommended CAT Tools for MTPE

- **Trados Studio**: Industry standard with robust QE integration and MT support
- **MemoQ**: Strong terminology management and QA features
- **Phrase (formerly Memsource)**: Cloud-based with excellent MT integration
- **Smartling**: Translation management system with built-in MT and QE
- **XTM Cloud**: Comprehensive TMS with workflow automation

### Quality Estimation (QE) in Practice

QE predicts MT quality without human reference translations:

- **Word-level QE**: Flags potentially incorrect words
- **Sentence-level QE**: Scores entire sentences for quality
- **Document-level QE**: Determines if content is suitable for post-editing

Use QE to:
- Decide between post-editing and retranslation
- Estimate post-editing time and effort
- Allocate translator resources efficiently
- Validate translator quality assessments

## Quality Standards and Metrics

### ISO 18587 Standard

International standard for full human post-editing of MT output:

- **Competence requirements**: Post-editors must have translation expertise, subject matter knowledge, and CAT tool proficiency
- **Process requirements**: Define specifications, use appropriate MT engines, implement QA procedures
- **Output requirements**: Final translation must meet same quality standards as human translation

### Quality Evaluation Frameworks

**Multidimensional Quality Metrics (MQM):**
- Accuracy (terminology, mistranslation, omission, addition)
- Fluency (grammar, spelling, punctuation, inconsistency)
- Style (register, awkward phrasing)
- Locale convention (date format, currency, units)

**Edit Distance Metrics:**
- **TER (Translation Edit Rate)**: Measures number of edits needed
- **HTER (Human-Targeted TER)**: Edits required to achieve acceptable quality
- Lower scores indicate better MT quality and less post-editing effort

### Key Performance Indicators (KPIs)

Track MTPE effectiveness:

| KPI | Measurement | Target |
|-----|-------------|--------|
| Post-editing speed | Words per hour | 2-3x human translation (LPE), 1.2-1.5x (FPE) |
| Edit distance | % of segments requiring changes | <30% for good MT quality |
| Quality scores | MQM error rate | <5 errors per 1000 words (FPE) |
| Cost savings | % reduction vs. human translation | 30-50% for LPE, 15-30% for FPE |
| Turnaround time | Days to completion | 40-60% faster than human translation |

## Best Practices for Post-Editors

### Efficiency Guidelines

1. **Don't over-edit**: For LPE, resist the urge to perfect style—focus on comprehension
2. **Recognize good MT**: If a segment is correct, move on quickly
3. **Know when to retranslate**: If editing takes longer than translating from scratch, start over
4. **Use keyboard shortcuts**: Master CAT tool shortcuts to minimize mouse usage
5. **Batch similar content**: Process similar segments together for consistency

### Quality Guidelines

1. **Maintain source fidelity**: Don't add or omit information
2. **Preserve formatting**: Keep tags, variables, and placeholders intact
3. **Follow style guides**: Adhere to client-specific terminology and conventions
4. **Consider context**: Review surrounding segments for coherence
5. **Document decisions**: Note terminology choices and style decisions for future reference

### Common MT Errors to Watch For

- **False friends**: Words that look similar but have different meanings
- **Gender and number agreement**: Especially in Romance languages
- **Pronoun ambiguity**: MT often struggles with pronoun reference
- **Idioms and metaphors**: Usually translated literally
- **Cultural references**: May not translate appropriately
- **Technical terminology**: Generic MT often mistranslates specialized terms
- **Negation errors**: "Not" may be dropped or misplaced
- **Word order**: May follow source language structure inappropriately

## Continuous Improvement

### Feedback Loops

- **Post-editor feedback**: Collect insights on recurring MT errors
- **Client feedback**: Incorporate quality concerns into guidelines
- **MT engine retraining**: Use post-edited content to improve MT quality
- **Glossary updates**: Add new terms discovered during post-editing
- **Process refinement**: Adjust workflows based on efficiency metrics

### MT Engine Optimization

- **Custom training data**: Feed high-quality TMs to the MT engine
- **Domain adaptation**: Train on industry-specific corpora
- **Terminology injection**: Ensure glossary terms are prioritized
- **Quality monitoring**: Track MT quality over time and retrain as needed
- **A/B testing**: Compare different MT engines or configurations

## Using the Reference Files

### When to Read Each Reference

**`/references/mtpe-fundamentals.md`** — Read when you need comprehensive understanding of MTPE principles, the evolution from rule-based to neural MT, cognitive aspects of post-editing, or detailed explanations of light vs. full post-editing approaches.

**`/references/mt-systems-quality.md`** — Read when selecting or evaluating MT engines, understanding neural MT architectures, implementing quality estimation systems, or comparing different MT technologies (statistical, neural, hybrid).

**`/references/post-editing-workflow.md`** — Read when designing MTPE workflows, training post-editors, implementing ISO 18587 standards, optimizing productivity, or troubleshooting workflow bottlenecks.

**`/references/tools-best-practices.md`** — Read when selecting CAT tools for MTPE, configuring translation memories and termbases, implementing automated QA processes, or establishing team-wide best practices and guidelines.

## References

- [Mt Systems Quality](references/mt-systems-quality.md)
- [Mtpe Fundamentals](references/mtpe-fundamentals.md)
- [Post Editing Workflow](references/post-editing-workflow.md)
- [Tools Best Practices](references/tools-best-practices.md)
