---
name: prompt-engineering
description: "Master prompt design and optimization for LLMs. Use for zero-shot prompting, few-shot learning, chain-of-thought reasoning, prompt templates, instruction tuning, and maximizing LLM performance."
---

# Prompt Engineering

Master the art and science of designing effective prompts for Large Language Models.

## Overview

Prompt engineering is the practice of crafting inputs to guide LLMs toward desired outputs. This skill covers techniques from basic prompting to advanced optimization strategies.

## Quick Reference

| Scenario | Recommended Approach | Reference File |
|----------|---------------------|----------------|
| Basic task instructions and formatting | Core prompting techniques | `/references/core-techniques.md` |
| Complex reasoning and multi-step tasks | Advanced prompting strategies | `/references/advanced-strategies.md` |
| Systematic prompt improvement | Optimization and testing methods | `/references/optimization.md` |

## Core Principles

1. **Clarity** - Be specific and unambiguous in instructions
2. **Context** - Provide relevant background information
3. **Structure** - Use consistent formatting and delimiters
4. **Examples** - Show desired behavior through demonstrations
5. **Iteration** - Test and refine prompts systematically

## Prompting Techniques

### Zero-Shot Prompting
Direct instruction without examples.

**When to Use:** Simple, well-defined tasks
**Example:** "Translate the following English text to French: [text]"

### Few-Shot Prompting
Provide examples of desired input-output pairs.

**When to Use:** Tasks requiring specific format or style
**Benefits:** Guides model behavior, improves consistency

### Chain-of-Thought (CoT)
Encourage step-by-step reasoning.

**Trigger:** "Let's think step by step"
**Use Cases:** Math problems, logical reasoning, complex analysis

### Instruction Following
Clear, imperative commands with role definition.

**Structure:**
- Role: "You are an expert [domain] assistant"
- Task: "Your task is to [specific action]"
- Constraints: "Follow these guidelines: [rules]"
- Output format: "Provide response as [format]"

## Prompt Structure

**Effective Template:**
```
[Role/Context]
[Task Description]
[Input Data]
[Output Format]
[Constraints/Guidelines]
```

**Delimiters:**
- Use triple quotes, XML tags, or markdown for clarity
- Separate instructions from data
- Prevent prompt injection

## Using the Reference Files

**`/references/core-techniques.md`** — Zero-shot, few-shot, chain-of-thought, instruction following, role prompting, and formatting best practices.

**`/references/advanced-strategies.md`** — ReAct, self-consistency, tree-of-thoughts, meta-prompting, prompt chaining, and complex reasoning techniques.

**`/references/optimization.md`** — Systematic testing, A/B testing, automated optimization, evaluation metrics, and iterative refinement.

## Best Practices

- Start simple, add complexity as needed
- Use clear, specific language
- Provide examples for complex tasks
- Test prompts with diverse inputs
- Use delimiters to separate sections
- Specify output format explicitly
- Include constraints and guidelines
- Iterate based on results

## Common Pitfalls to Avoid

- Vague or ambiguous instructions
- Mixing instructions with data
- Assuming model has current information
- Not specifying output format
- Overcomplicating simple tasks
- Ignoring model limitations
- Not testing edge cases
- Failing to iterate and improve
