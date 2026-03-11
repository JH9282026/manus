# Summarization Methods

Detailed guidance on summarization techniques.

---

## Extractive Summarization

### Method
Select and arrange the most important sentences from original text.

### Process
1. Score sentences by importance
2. Select top-scoring sentences
3. Arrange in logical order
4. Ensure coherence between selections

### Scoring Factors
- Position (first/last sentences weight higher)
- Keyword density
- Sentence length (moderate preferred)
- Named entity presence
- Numeric data presence

### Best For
- Legal documents (exact wording matters)
- Technical content (precision required)
- Scientific papers (accuracy critical)
- News articles (facts must be preserved)

---

## Abstractive Summarization

### Method
Generate new text that captures document essence through paraphrasing.

### Process
1. Understand document meaning
2. Identify key concepts
3. Generate novel sentences
4. Maintain factual accuracy

### Advantages
- More readable output
- Better compression
- Flexible tone adaptation
- Natural narrative flow

### Risks
- Potential for hallucination
- May lose precision
- Requires verification

### Best For
- Executive summaries
- Marketing content
- Educational materials
- Narrative documents

---

## Hybrid Approach

### Method
Combine extraction for accuracy with abstraction for readability.

### Process
1. Extract key sentences
2. Paraphrase for flow
3. Connect with transitions
4. Verify against source

### Best For
- General purpose summarization
- Business documents
- Research synthesis
- Multi-audience content

---

## Compression Ratios

| Source Length | Suggested Target |
|---------------|------------------|
| 500-1000 words | 100-200 (20%) |
| 1000-3000 words | 200-400 (15%) |
| 3000-10000 words | 300-700 (10%) |
| 10000+ words | 500-1000 (5%) |

---

## Quality Verification

### Accuracy Check
- Cross-reference claims against source
- Verify quotes and statistics
- Check named entities

### Completeness Check
- All main sections represented
- Key arguments captured
- Critical data included

### Readability Check
- Appropriate for audience
- Logical flow
- Clear language
