# Template Placeholder Skills Report

**Repository:** JH9282026/manus  
**Date:** April 1, 2026  
**Total Skills in Repository:** 606  
**Template Placeholders Identified:** 9  

---

## What Is a "Template Placeholder"?

A **template placeholder** is a SKILL.md file that was never filled in with actual skill content. Instead of containing real instructional material about its topic, it contains a **verbatim copy of the Manus Skill Format Template** — the same document used to teach people how to *create* skills.

Think of it like finding a blank form in a filing cabinet. The form has instructions on how to fill it out ("Write your name here", "Describe your experience here"), but nobody ever actually filled it in. These 9 skills look like real skills from the outside (they have proper directory names and even reference files), but when Manus loads them, it gets instructions on *how to write a skill* instead of actual knowledge about the topic.

---

## Why This Matters

| Problem | Impact |
|---------|--------|
| **Zero skill value** | When triggered, Manus loads template instructions instead of topic expertise |
| **Wasted tokens** | Each placeholder is ~7,000 bytes of template text that provides no useful information |
| **Misleading skill count** | Inflates the 606-skill count by 9 (1.5%) with non-functional entries |
| **False triggers** | The generic description `"skill-name skill"` may cause incorrect skill matching |
| **Confusing reference files** | Some have reference files with real-ish content, creating an inconsistent state |

---

## The 9 Template Placeholder Skills

All 9 are in the **digital advertising / ads platform** domain:

| # | Skill Directory | Generic Description Used | File Size | Reference Files |
|---|-----------------|-------------------------|-----------|-----------------|
| 1 | `el-toro-ip-targeting` | `"el-toro-ip-targeting skill"` | 6,995 B | 5 files |
| 2 | `instagram-ads-integration` | `"instagram-ads-integration skill"` | 7,000 B | 11 files |
| 3 | `linkedin-ads-targeting-creatives` | `"linkedin-ads-targeting-creatives skill"` | 7,007 B | 11 files |
| 4 | `meta-ads-campaign-api` | `"meta-ads-campaign-api skill"` | 6,996 B | 10 files |
| 5 | `meta-ads-targeting-audiences` | `"meta-ads-targeting-audiences skill"` | 7,003 B | 11 files |
| 6 | `reddit-ads-api-automation` | `"reddit-ads-api-automation skill"` | 7,000 B | 6 files |
| 7 | `tiktok-ads-api-management` | `"tiktok-ads-api-management skill"` | 7,000 B | 4 files |
| 8 | `x-ads-analytics-optimization` | `"x-ads-analytics-optimization skill"` | 7,003 B | 7 files |
| 9 | `youtube-ads-google-api` | `"youtube-ads-google-api skill"` | 6,997 B | 7 files |

---

## How to Identify a Template Placeholder

There are three dead giveaways that distinguish a template placeholder from a real skill:

### 1. The Title Is "Manus Skill Format Template"

Every placeholder's body starts with:

```markdown
# Manus Skill Format Template

Use this template in Abacus to generate skills that work with Manus out of the box.
```

A **real skill** starts with its actual topic name:

```markdown
# Google Ads Search Campaigns

Create high-performing search advertising campaigns on Google Search Network...
```

### 2. The Description Is Just the Skill Name + "skill"

Every placeholder's YAML frontmatter has a generic, useless description:

```yaml
---
description: "meta-ads-campaign-api skill"
---
```

A **real skill** has a rich, trigger-worthy description:

```yaml
---
name: google-ads-search-campaigns
description: "Create and optimize Google Ads Search campaigns including Responsive Search Ads,
Dynamic Search Ads, and Call-Only Ads. Use for keyword research and targeting, ad copy creation
with multiple headlines and descriptions, bid strategy selection..."
---
```

### 3. The Body Contains Template Instructions, Not Skill Knowledge

The entire body of every placeholder contains sections like:
- "How Manus Skills Work" (explains the skill system itself)
- "Directory Structure" (shows the `skill-name/` folder layout)
- "SKILL.md Format" (explains YAML frontmatter and markdown body rules)
- "Complete Example: A Simple Skill" (the email-outreach example)
- "Prompt for Abacus" (copy-paste instructions for generating skills)
- "Deploying to Manus" (how to activate skills)

**None of this is actual skill content.** It's the instruction manual for creating skills.

---

## What a Properly Filled-In Skill Looks Like

Here's a side-by-side comparison using the advertising domain:

### ❌ Template Placeholder (`meta-ads-campaign-api/SKILL.md`)

```yaml
---
description: "meta-ads-campaign-api skill"
---
```
```markdown
# Manus Skill Format Template

Use this template in Abacus to generate skills that work with Manus out of the box...

## How Manus Skills Work
[... 200 lines of template instructions ...]

## Prompt for Abacus
[... instructions for skill generation ...]
```

**What Manus gets:** Instructions on how to create skills. Zero knowledge about Meta Ads.

### ✅ Complete Skill (`google-ads-search-campaigns/SKILL.md`)

```yaml
---
name: google-ads-search-campaigns
description: "Create and optimize Google Ads Search campaigns including Responsive Search Ads,
Dynamic Search Ads, and Call-Only Ads. Use for keyword research and targeting..."
---
```
```markdown
# Google Ads Search Campaigns

Create high-performing search advertising campaigns on Google Search Network...

## Campaign Type Selection
| Business Goal | Campaign Type | Bidding Strategy | Best For |
|...|...|...|...|

## Responsive Search Ads (RSA) Structure
### Asset Requirements
- Headlines: 3-15 unique headlines (max 30 characters each)
[... actual actionable knowledge ...]
```

**What Manus gets:** Actionable campaign creation knowledge, comparison tables, API details.

---

## Reference File Status

An interesting complication: some placeholders have reference files that contain *partially real* content, while others have generic boilerplate references.

| Skill | Ref Files | Reference Quality |
|-------|-----------|-------------------|
| `el-toro-ip-targeting` | 5 | ⚠️ Generic boilerplate — uses filler phrases like "This comprehensive reference guide covers..." |
| `instagram-ads-integration` | 11 | ✅ Appear to have real content (OAuth, API docs) |
| `linkedin-ads-targeting-creatives` | 11 | Needs review |
| `meta-ads-campaign-api` | 10 | Needs review |
| `meta-ads-targeting-audiences` | 11 | Needs review |
| `reddit-ads-api-automation` | 6 | Needs review |
| `tiktok-ads-api-management` | 4 | Needs review |
| `x-ads-analytics-optimization` | 7 | Needs review |
| `youtube-ads-google-api` | 7 | Needs review |

Even where reference files exist with real content, the **SKILL.md itself is broken** — it can't route Manus to those reference files because it contains template instructions instead of a "Using the Reference Files" section pointing to the actual files.

---

## Recommendations

### Option A: Populate with Real Content (Recommended)
These are all valuable advertising platform skills. Replace each SKILL.md with proper content:

1. **Replace the YAML frontmatter** with a real `name` and comprehensive `description`
2. **Replace the body** with actual platform-specific knowledge (API details, campaign setup workflows, targeting options, best practices)
3. **Add a "Using the Reference Files" section** that points to the existing reference files
4. **Review existing reference files** — keep the real ones, replace the boilerplate ones

### Option B: Delete Entirely
If the skills aren't needed, remove the 9 directories to:
- Clean up the repository
- Stop inflating the skill count
- Prevent false triggering

### Option C: Regenerate Using the Template
Use the Abacus prompt in Template.md to regenerate proper skill content for each of the 9 topics, then replace the current placeholder files.

---

## Summary

| Metric | Value |
|--------|-------|
| Total placeholders | 9 |
| All in same domain? | Yes — digital advertising platforms |
| Content type | Verbatim copy of Template.md |
| Any unique content? | No — only the description field differs (contains skill name) |
| Reference files present? | Yes (4-11 files each), quality varies |
| Severity | 🔴 High — these skills are non-functional |
| Recommended action | Populate with real content or delete |

---

*Report generated April 1, 2026 from analysis of `/home/ubuntu/github_repos/manus`*
