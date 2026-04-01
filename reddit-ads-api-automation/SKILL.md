---
description: "reddit-ads-api-automation skill"
---

# Manus Skill Format Template

Use this template in Abacus to generate skills that work with Manus out of the box. Copy the structure exactly — Manus is strict about the format.

---

## How Manus Skills Work

A skill is a directory containing a required `SKILL.md` file and optional reference files. Manus uses a three-level loading system:

1. **Metadata** (always loaded, ~100 words) — the YAML frontmatter in SKILL.md
2. **SKILL.md body** (loaded when skill triggers) — must be under 500 lines
3. **Reference files** (loaded on demand) — detailed content in `references/` subdirectory

The `description` field in the frontmatter is the **primary trigger mechanism**. Manus reads it to decide when to activate the skill. The body of SKILL.md only loads after the skill triggers.

---

## Directory Structure

```
skill-name/
├── SKILL.md              (REQUIRED — main skill file)
└── references/           (OPTIONAL — detailed content loaded on demand)
    ├── topic-one.md
    ├── topic-two.md
    └── topic-three.md
```

Other optional directories (only if needed):
- `scripts/` — executable Python or Bash scripts for repetitive tasks
- `templates/` — output assets like HTML templates, icons, fonts

**Do NOT include**: README.md, CHANGELOG.md, or other docs. Skills are for AI agents, not humans.

---

## SKILL.md Format

The file has two parts: YAML frontmatter and Markdown body.

### Part 1: YAML Frontmatter (REQUIRED)

```yaml
---
name: your-skill-name
description: Clear description of what the skill does AND when to use it. This is the trigger — Manus reads this to decide if the skill is relevant. Be comprehensive. Example format - "Do X, Y, and Z. Use for: scenario A, scenario B, scenario C."
---
```

**Rules for frontmatter:**
- `name` — lowercase, hyphenated, no spaces (e.g., `ad-creation`, `private-pilot-ground-school`)
- `description` — must include WHAT the skill does AND WHEN to use it. This is the most important field. Be thorough but concise. Think of it as the skill's elevator pitch that helps Manus match it to user requests.

### Part 2: Markdown Body (REQUIRED)

```markdown
# Skill Name

One-line summary of what this skill does.

## Overview

Brief overview paragraph. What does this skill provide? What can it do?

## [Core Section — e.g., Quick Start, Framework Selection, Process]

The main instructional content. Use tables for selection guides, comparisons, or specs.
Use imperative/infinitive form ("Use this when..." not "This is used when...").

### Subsection

Content here. Keep it actionable and concise.

## [Additional Sections as needed]

More content. Remember: only include information Manus doesn't already know.
Challenge every paragraph: "Does this justify its token cost?"

## Using the Reference Files

### When to Read Each Reference

**`/references/topic-one.md`** — Read when [specific trigger condition].

**`/references/topic-two.md`** — Read when [specific trigger condition].

This section tells Manus WHEN to load each reference file.
```

**Rules for the body:**
- Keep under 500 lines total
- Use imperative/infinitive form throughout
- Reference files with relative paths: `/references/filename.md`
- Include tables for comparisons, selection guides, specs
- Only add information Manus doesn't already have — it's already smart
- Move detailed/lengthy content to reference files, keep SKILL.md as the overview and navigation layer

---

## Reference Files Format

Each reference file is plain Markdown. No frontmatter needed. Just content.

```markdown
# Topic Name

Brief intro paragraph.

---

## Section One

Detailed content here. This is where the depth lives.
Can be longer than SKILL.md since it's only loaded when needed.

## Section Two

More detailed content.
```

**Rules for reference files:**
- Plain Markdown, no YAML frontmatter
- Can be longer than SKILL.md (they're loaded on demand)
- Each file should cover one coherent topic
- Don't duplicate content between SKILL.md and references
- SKILL.md summarizes; references go deep

---

## Complete Example: A Simple Skill

### Directory Structure
```
email-outreach/
├── SKILL.md
└── references/
    ├── cold-email-templates.md
    └── follow-up-sequences.md
```

### SKILL.md
```markdown
---
name: email-outreach
description: Create high-converting cold email campaigns and follow-up sequences for B2B outreach. Use for writing cold emails, designing drip sequences, crafting subject lines, personalizing outreach at scale, and optimizing reply rates.
---

# Email Outreach

Create effective cold email campaigns and automated follow-up sequences for B2B sales outreach.

## Overview

This skill provides frameworks, templates, and best practices for cold email outreach including initial contact emails, multi-touch follow-up sequences, subject line optimization, and personalization strategies.

## Quick Start: Email Type Selection

| Scenario | Template Type | Reference |
|----------|--------------|-----------|
| First contact, cold lead | Cold intro email | `/references/cold-email-templates.md` |
| No reply after 3 days | Follow-up sequence | `/references/follow-up-sequences.md` |
| Warm intro via referral | Warm referral email | `/references/cold-email-templates.md` |

## Core Principles

1. **Personalize the first line** — reference something specific about the recipient
2. **One CTA per email** — don't give multiple options
3. **Keep it short** — under 150 words for cold emails
4. **Subject lines matter** — test 5-10 variations

## Using the Reference Files

**`/references/cold-email-templates.md`** — Read when writing any initial outreach email or when you need proven templates to start from.

**`/references/follow-up-sequences.md`** — Read when designing multi-email sequences or when a prospect hasn't replied.
```

---

## Prompt for Abacus

Copy and paste this into Abacus when generating a skill:

```
Generate a Manus-compatible skill following this exact format:

1. Create a SKILL.md file with:
   - YAML frontmatter containing `name` (lowercase-hyphenated) and `description` (comprehensive — what it does AND when to use it)
   - Markdown body under 500 lines with overview, core instructional content, and a "Using the Reference Files" section
   - Use imperative/infinitive form throughout
   - Use tables for comparisons and selection guides
   - Only include information an advanced AI wouldn't already know
   - Reference detailed content with relative paths like `/references/filename.md`

2. Create reference files in a `references/` directory:
   - Plain Markdown, no frontmatter
   - One coherent topic per file
   - This is where detailed/lengthy content lives
   - Don't duplicate content from SKILL.md

3. Do NOT include README.md, CHANGELOG.md, or other auxiliary files.

4. The skill directory structure should be:
   skill-name/
   ├── SKILL.md
   └── references/
       ├── topic-one.md
       └── topic-two.md

The skill topic is: [DESCRIBE YOUR SKILL HERE]
```

---

## Deploying to Manus

Once Abacus generates the files:

1. Send me the SKILL.md and all reference files
2. I'll place them in `/home/ubuntu/skills/your-skill-name/`
3. I'll validate and activate the skill
4. It's ready to use immediately

Alternatively, if you have multiple skills, send them all and I'll batch deploy them.
