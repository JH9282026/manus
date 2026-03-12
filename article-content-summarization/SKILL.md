---
name: "article-content-summarization"
description: "Transform lengthy documents into concise, well-structured summaries. Use for: article summarization, research paper abstracts, executive summaries, book chapter digests, meeting transcript summaries, legal document simplification, multi-source synthesis, extractive summarization, abstractive summarization, and key insight extraction."
---

# Article & Content Summarization

Condense large bodies of text into structured key points, executive summaries, and actionable insights.

## Overview

Transform lengthy, complex documents into concise summaries that preserve essential information while dramatically reducing reading time. Apply extractive, abstractive, or hybrid techniques based on content requirements.

## Summarization Techniques

| Technique | Method | Best For |
|-----------|--------|----------|
| Extractive | Select important sentences | Legal, technical, scientific |
| Abstractive | Generate new paraphrased text | Readability, narratives |
| Hybrid | Combine both approaches | General purpose |

## Summary Types

| Type | Length | Structure |
|------|--------|----------|
| Executive | 200-300 words | Flowing paragraphs |
| Bullet Points | Variable | Hierarchical lists |
| One-Sentence | 15-30 words | Single statement |
| Multi-Level | Short/Medium/Long | Progressive disclosure |
| Structured | By section | Mirrors original |

## Output Components

### Header Section
- Document title and source
- Original word count and reading time
- Summary word count and compression ratio
- Technique used

### Core Summary
Formatted per summary type selection.

### Extracted Elements (Optional)
- Key themes (3-7)
- Named entities (people, orgs, dates)
- Important quotes
- Statistical highlights
- Conclusions and recommendations

## Audience Adaptation

| Audience | Vocabulary | Detail Level |
|----------|------------|-------------|
| General Public | Plain language | Overview |
| Expert | Technical terms | Deep |
| Executive | Business focus | Strategic |
| Student | Educational | Explanatory |
| Researcher | Academic | Comprehensive |

## Quality Standards

| Criterion | Standard |
|-----------|----------|
| Accuracy | Zero hallucinations |
| Completeness | All key points captured |
| Clarity | Appropriate reading level |
| Conciseness | No redundancy |
| Coherence | Logical flow |

## Content Types Supported

- Research papers
- Business reports
- News articles
- Legal documents
- Technical documentation
- Book chapters
- Meeting transcripts
- Email threads
- Presentations

## Processing Parameters

| Parameter | Options |
|-----------|--------|
| Target length | Short/Medium/Long or word count |
| Compression ratio | 5-50% of original |
| Focus areas | Methodology, results, conclusions |
| Extract quotes | Yes/No |
| Preserve citations | Yes/No |
| Simplify language | Yes/No |

## Using the Reference Files

### `/references/summarization-methods.md`
Read when selecting and applying extractive, abstractive, or hybrid techniques.

### `/references/multi-document-synthesis.md`
Read when synthesizing or comparing multiple source documents.

## Reference Files

This skill includes the following detailed reference materials:

- [Academic Summaries](references/academic-summaries.md)
- [Article Summaries](references/article-summaries.md)
- [Executive Summaries](references/executive-summaries.md)
- [Multi Document Synthesis](references/multi-document-synthesis.md)
- [Multi Source](references/multi-source.md)
- [Specialized Summaries](references/specialized-summaries.md)
- [Summarization Methods](references/summarization-methods.md)
