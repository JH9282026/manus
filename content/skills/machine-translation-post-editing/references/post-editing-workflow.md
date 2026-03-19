# Post-Editing Workflow Design

Comprehensive guide to designing, implementing, and optimizing MTPE workflows for translation teams and organizations.

---

## Workflow Architecture

### Basic MTPE Workflow

```
1. Source content preparation
   ↓
2. Pre-editing (optional)
   ↓
3. Machine translation
   ↓
4. Quality estimation (optional)
   ↓
5. Post-editing
   ↓
6. Quality assurance
   ↓
7. Delivery
```

### Advanced MTPE Workflow with Routing

```
1. Source content preparation
   ↓
2. Content analysis and segmentation
   ↓
3. TM matching and leverage analysis
   ↓
4. MT for non-matched segments
   ↓
5. Quality estimation
   ↓
6. Intelligent routing:
   - High QE score → Light post-editing
   - Medium QE score → Full post-editing
   - Low QE score → Human translation from scratch
   ↓
7. Post-editing/translation
   ↓
8. Linguistic QA
   ↓
9. Technical QA
   ↓
10. Client review (optional)
   ↓
11. Delivery and feedback collection
   ↓
12. MT engine retraining (periodic)
```

## Pre-Translation Phase

### Source Content Analysis

**Content profiling**:
- Identify content type (technical, marketing, legal, etc.)
- Assess complexity and domain specificity
- Determine target audience and quality requirements
- Estimate volume and repetition rate

**Suitability assessment**:
- Is MT appropriate for this content?
- What quality level is required (LPE vs. FPE)?
- Are there legal or confidentiality constraints?
- What is the expected ROI of MTPE vs. human translation?

**Decision criteria**:

| Factor | MT Suitable | MT Not Suitable |
|--------|-------------|------------------|
| Content type | Technical, informational | Creative, marketing transcreation |
| Quality requirement | Comprehensible, accurate | Perfect, brand-critical |
| Volume | High (>10,000 words) | Low (<1,000 words) |
| Repetition | High repetition | Unique, varied content |
| Deadline | Urgent | Flexible |
| Budget | Cost-sensitive | Quality-prioritized |
| Legal risk | Low | High (contracts, regulatory) |

### Source Text Optimization (Pre-Editing)

Improve MT quality by optimizing source content:

**Simplification**:
- Break long sentences (>25 words) into shorter ones
- Use active voice instead of passive
- Avoid complex nested clauses
- Replace ambiguous pronouns with explicit nouns

**Standardization**:
- Use consistent terminology throughout
- Standardize date and number formats
- Apply consistent capitalization and punctuation
- Remove or standardize abbreviations

**Clarification**:
- Spell out acronyms on first use
- Avoid idioms and colloquialisms
- Clarify ambiguous references
- Add context where needed

**Formatting**:
- Clean up inconsistent formatting
- Remove unnecessary markup
- Ensure proper tagging of non-translatable elements
- Validate file structure

**Quality check**:
- Proofread source text for errors
- Verify factual accuracy
- Ensure completeness
- Check for placeholder text or comments

**ROI consideration**: Pre-editing adds upfront cost but can significantly reduce post-editing effort. Most beneficial for:
- High-volume content that will be translated into multiple languages
- Content that will be reused or updated frequently
- Projects where source quality is known to be poor

### Translation Memory Leverage

**TM matching process**:
1. Segment source content
2. Search TM for matches
3. Categorize segments:
   - 100% matches: Reuse without MT
   - 95-99% fuzzy matches: May benefit from MT or human editing
   - <95% matches: Send to MT
   - No match: Send to MT

**Hybrid approach**:
- Use TM for high matches (>85%)
- Use MT for low matches (<85%)
- Combine TM and MT suggestions for fuzzy matches
- Post-editor chooses best option

**TM maintenance**:
- Regularly update TM with post-edited content
- Clean up outdated or incorrect entries
- Align TM with current terminology and style
- Segment and align legacy translations

## MT Processing Phase

### MT Engine Configuration

**Engine selection**:
- Choose engine optimized for language pair
- Select domain-specific engine if available
- Consider custom-trained engine for high-volume clients

**Customization**:
- Upload client glossaries and termbases
- Provide style guides and reference materials
- Fine-tune engine on client-specific TM
- Configure terminology enforcement

**Quality settings**:
- Balance speed vs. quality (beam search width)
- Configure output length constraints
- Set formality level if supported
- Enable/disable specific features (transliteration, etc.)

### Batch Processing

**Segmentation**:
- Ensure consistent segmentation rules across TM and MT
- Preserve formatting and tags
- Handle special characters and entities
- Maintain segment IDs for tracking

**Processing**:
- Batch translate all segments
- Handle errors and timeouts gracefully
- Log processing statistics
- Preserve metadata and context

**Quality estimation**:
- Run QE model on MT output
- Assign quality scores to each segment
- Flag potentially problematic segments
- Generate QE report for project manager

## Post-Editing Phase

### Task Assignment and Routing

**Post-editor selection**:
- Match post-editors to content domain
- Consider language pair expertise
- Balance workload across team
- Account for post-editor speed and quality history

**Segment routing based on QE**:
- High quality (QE >80): Assign to LPE queue
- Medium quality (QE 50-80): Assign to FPE queue
- Low quality (QE <50): Assign to human translation queue

**Workload management**:
- Distribute segments evenly
- Provide time estimates based on QE scores
- Allow post-editors to flag problematic content
- Enable collaboration for difficult segments

### Post-Editing Environment Setup

**CAT tool configuration**:
- Display source, MT output, and TM matches side-by-side
- Show QE scores and confidence indicators
- Enable keyboard shortcuts for common actions
- Configure auto-propagation of corrections
- Set up QA checks to run automatically

**Reference materials**:
- Provide access to glossaries and termbases
- Link to style guides and client instructions
- Make previous translations searchable
- Provide context (surrounding segments, screenshots, etc.)

**Guidelines and instructions**:
- Clearly specify editing level (LPE vs. FPE)
- Define quality expectations
- Provide examples of acceptable edits
- Clarify handling of specific issues (formatting, terminology, etc.)
- Set productivity targets if applicable

### Post-Editing Execution

**Efficient post-editing techniques**:

1. **Quick assessment**: Skim segment to determine if MT is usable
2. **Accept or reject**: If MT is good, accept quickly; if unusable, retranslate from scratch
3. **Focused editing**: Correct specific errors without over-editing
4. **Keyboard-centric**: Minimize mouse usage with shortcuts
5. **Batch similar segments**: Process repetitive content together for consistency
6. **Use auto-propagation**: Apply corrections to identical segments automatically
7. **Leverage concordance**: Search for term usage in TM for consistency
8. **Flag issues**: Mark segments needing review or clarification

**Common editing patterns**:

**Accuracy corrections**:
- Fix mistranslations and false friends
- Correct numbers, dates, and proper nouns
- Verify technical terminology
- Ensure completeness (no omissions or additions)

**Fluency improvements**:
- Adjust word order for naturalness
- Fix agreement errors (gender, number, case)
- Correct verb tenses and aspects
- Smooth awkward phrasing

**Style adjustments (FPE)**:
- Adapt register and formality
- Localize cultural references
- Replace literal translations with idiomatic expressions
- Ensure consistency in tone and voice

**Technical corrections**:
- Preserve tags and formatting
- Maintain placeholders and variables
- Ensure proper encoding of special characters
- Verify link and reference integrity

### Productivity Monitoring

**Metrics to track**:
- Words per hour by post-editor
- Time per segment by QE score range
- Edit distance (% of MT output changed)
- Segments accepted without editing
- Segments retranslated from scratch

**Analysis**:
- Identify productivity bottlenecks
- Correlate QE scores with actual post-editing effort
- Compare post-editor performance
- Detect content types that slow down post-editing

**Optimization**:
- Provide additional training for struggling post-editors
- Adjust QE thresholds for routing
- Refine MT engine based on common errors
- Update guidelines based on observed issues

## Quality Assurance Phase

### Linguistic QA

**Proofreading**:
- Review for grammar, spelling, punctuation errors
- Check terminology consistency
- Verify style guide compliance
- Ensure natural fluency

**Comparative review**:
- Spot-check against source for accuracy
- Verify completeness (no omissions or additions)
- Check that meaning is preserved
- Validate cultural appropriateness

**Consistency check**:
- Ensure consistent translation of repeated terms
- Verify consistent style and tone throughout
- Check for contradictions or discrepancies
- Validate proper nouns and brand names

### Technical QA

**Automated checks**:
- Tag and placeholder verification
- Number and date format consistency
- Spelling and grammar check
- Terminology compliance
- Length restrictions (for UI strings)
- Forbidden terms or patterns

**Manual checks**:
- Formatting preservation
- Link and cross-reference integrity
- Special character rendering
- File structure and metadata
- Encoding and character set

**Context validation**:
- Review in actual context (website, software, document)
- Check layout and text fit
- Verify functionality (clickable links, etc.)
- Test on target platform if applicable

### Quality Scoring

**Sampling approach**:
- Review representative sample (5-10% of content)
- Stratify by content type, post-editor, QE score
- Use MQM or similar framework for error annotation
- Calculate quality score based on error severity

**Full review approach**:
- Review 100% of content for critical projects
- Use automated QA tools to flag potential issues
- Human reviewer validates flagged segments
- More expensive but ensures highest quality

**Acceptance criteria**:
- Define quality thresholds (e.g., <5 major errors per 1000 words)
- Specify acceptable error types and severity
- Establish process for handling failed QA
- Document quality standards in SLA

## Post-Delivery Phase

### Feedback Collection

**Client feedback**:
- Request structured feedback on quality
- Identify specific issues or concerns
- Understand client expectations and preferences
- Incorporate feedback into future projects

**Post-editor feedback**:
- Collect insights on MT quality and common errors
- Identify workflow pain points
- Gather suggestions for improvement
- Recognize and address training needs

**End-user feedback**:
- Monitor user comments and complaints
- Track support tickets related to translation
- Analyze user engagement metrics
- Identify content that may need revision

### Continuous Improvement

**MT engine optimization**:
- Retrain engine with post-edited content
- Update terminology and style preferences
- Fine-tune for identified error patterns
- Benchmark quality improvements over time

**Workflow refinement**:
- Adjust QE thresholds based on actual effort
- Optimize routing and assignment logic
- Streamline CAT tool configuration
- Automate repetitive tasks

**Team development**:
- Provide targeted training based on performance data
- Share best practices among post-editors
- Calibrate quality standards through group reviews
- Recognize and reward high performers

**Process documentation**:
- Update guidelines based on lessons learned
- Document solutions to recurring issues
- Maintain knowledge base of best practices
- Version control for process changes

### Performance Analytics

**KPI dashboard**:
- Overall productivity (words per hour)
- Quality scores by project and post-editor
- Cost savings vs. human translation
- Turnaround time improvements
- Client satisfaction ratings

**Trend analysis**:
- Track metrics over time
- Identify seasonal patterns
- Correlate changes with process improvements
- Forecast capacity and resource needs

**Benchmarking**:
- Compare performance across language pairs
- Benchmark against industry standards
- Evaluate ROI of MTPE vs. alternatives
- Assess competitiveness of pricing and quality

---

## Summary

A well-designed MTPE workflow integrates source optimization, intelligent MT processing, efficient post-editing, rigorous quality assurance, and continuous improvement. Success depends on clear guidelines, appropriate technology, skilled post-editors, and data-driven optimization. By systematically analyzing performance and incorporating feedback, organizations can maximize the quality and efficiency benefits of MTPE while maintaining professional standards and client satisfaction.
