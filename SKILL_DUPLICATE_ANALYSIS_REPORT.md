# Skill Duplicate & Overlap Analysis Report

**Repository:** JH9282026/manus  
**Date:** April 1, 2026  
**Total Skills Analyzed:** 606  

---

## Executive Summary

After analyzing all 606 SKILL.md files across the repository, the findings are:

| Category | Count | Severity |
|----------|-------|----------|
| **True Duplicates** (must merge) | 2 pairs | 🔴 High |
| **Template/Placeholder Skills** (unfilled) | 9 skills | 🔴 High |
| **Stub Skills** (under-developed, <2500 bytes) | 66 skills | 🟡 Medium |
| **Overlapping Domain Groups** (intentional specialization) | 25+ groups | 🟢 Low |
| **Near-duplicate pairs** (base vs advanced/specific) | ~8 pairs | 🟡 Medium |

**Overall Assessment:** The repository is **well-organized with minimal true duplication**. Only 2 genuine duplicate pairs exist. The vast majority of similarly-named skills are **intentional specializations** (e.g., platform-specific ad skills, genre-specific photography skills) and should NOT be merged. However, 9 template placeholders and ~66 stub skills need attention.

---

## 🔴 Category 1: TRUE DUPLICATES (Must Merge — 2 Pairs)

These are skills that cover the exact same topic with only formatting differences in the directory name.

### 1.1 Competitive Analysis & Intelligence
| Attribute | Skill A | Skill B |
|-----------|---------|---------|
| **Directory** | `competitive-analysis-&-intelligence` | `competitive-analysis-intelligence` |
| **Title** | Competitive Analysis & Intelligence | Competitive Analysis & Intelligence |
| **File Size** | 28,428 bytes (full) | 3,650 bytes (stub) |
| **Status** | ✅ Complete | ⚠️ Minimal/stub |

**Recommendation:** **DELETE** `competitive-analysis-intelligence` (the stub). Keep `competitive-analysis-&-intelligence` as the canonical version. Alternatively, rename to remove the `&` character (which can cause filesystem issues) and keep the full content.

### 1.2 Video Analysis & Visual Intelligence
| Attribute | Skill A | Skill B |
|-----------|---------|---------|
| **Directory** | `video-analysis-&-visual-intelligence` | `video-analysis-visual-intelligence` |
| **Title** | Video Analysis & Visual Intelligence | Video Analysis Visual Intelligence |
| **File Size** | 18,250 bytes (full) | 1,640 bytes (stub) |
| **Status** | ✅ Complete | ⚠️ Minimal/stub |

**Recommendation:** **DELETE** `video-analysis-visual-intelligence` (the stub). Keep `video-analysis-&-visual-intelligence` as the canonical version.

---

## 🔴 Category 2: TEMPLATE/PLACEHOLDER SKILLS (9 Skills — Not Implemented)

These 9 skills were never filled in — they still contain the default "Manus Skill Format Template" content with no actual skill-specific information.

| # | Directory Name | Expected Topic |
|---|----------------|----------------|
| 1 | `el-toro-ip-targeting` | El Toro IP Targeting Advertising |
| 2 | `instagram-ads-integration` | Instagram Advertising Integration |
| 3 | `linkedin-ads-targeting-creatives` | LinkedIn Ads Targeting & Creatives |
| 4 | `meta-ads-campaign-api` | Meta Ads Campaign API |
| 5 | `meta-ads-targeting-audiences` | Meta Ads Targeting & Audiences |
| 6 | `reddit-ads-api-automation` | Reddit Ads API Automation |
| 7 | `tiktok-ads-api-management` | TikTok Ads API Management |
| 8 | `x-ads-analytics-optimization` | X (Twitter) Ads Analytics & Optimization |
| 9 | `youtube-ads-google-api` | YouTube Ads Google API |

**Recommendation:** Either **populate these with real content** or **remove them** from the repository. As-is, they add zero value and inflate the skill count.

---

## 🟡 Category 3: NEAR-DUPLICATE PAIRS (Potential Merges — ~8 Pairs)

These pairs have very similar names and overlapping scope. One is typically a superset or more specialized version of the other.

### 3.1 Base vs. Advanced/Specific Pairs

| Base Skill | Related Skill | Relationship | Recommendation |
|------------|---------------|--------------|----------------|
| `compositing` (1,166B stub) | `vfx-compositing` (1,600B stub) | VFX compositing IS compositing | **Merge** into `vfx-compositing`, delete stub |
| `lighting-techniques` (1,128B stub) | `video-lighting-techniques` (10,522B full) | Video lighting is a subset of lighting | **Keep separate** — lighting-techniques could cover photography lighting; populate it |
| `cloud-security` (1,317B stub) | `cloud-security-advanced` (9,191B full) | Base vs. advanced | **Keep separate** — populate base skill with fundamentals |
| `serverless-architecture` (1,379B stub) | `serverless-architecture-advanced` (9,838B full) | Base vs. advanced | **Keep separate** — populate base skill with fundamentals |
| `mobile-app-design` (11,671B full) | `native-mobile-app-design` (2,363B stub) | General vs. native-specific | **Keep separate** — native has distinct concerns (platform guidelines) |
| `audio-restoration` (3,625B) | `audio-restoration-cleanup` (13,957B) | Same concept | **Merge** — keep `audio-restoration-cleanup` (more complete), delete other |
| `foley-sound-design` (3,742B) | `foley-sound-effects` (14,240B) | Same concept | **Merge** — keep `foley-sound-effects` (more complete), delete other |
| `accessibility-wcag` (15,624B full) | `web-accessibility-wcag` (2,011B stub) | Overlapping | **Merge** — `accessibility-wcag` already covers web; delete stub |

---

## 🟢 Category 4: INTENTIONAL DOMAIN GROUPS (Not Duplicates — Keep Separate)

The following groups contain skills with similar names that are **intentionally specialized** and should remain as separate skills.

### 4.1 Ad Campaign Management (13 skills) ✅ Keep All
Platform-specific ad management skills — each covers a different advertising platform with unique APIs, features, and best practices.

- `ad-campaign-management` — Generic/cross-platform (the umbrella skill)
- `apple-search-ads-campaign-management`
- `linkedin-ads-campaign-management`
- `meta-ads-campaign-management`
- `nextdoor-ads-campaign-management`
- `outbrain-campaign-management`
- `pinterest-ads-campaign-management`
- `quora-ads-campaign-management`
- `snapchat-ads-campaign-management`
- `taboola-campaign-management`
- `trade-desk-campaign-management`
- `twitch-ads-campaign-management`
- `x-ads-campaign-management`

**Verdict:** Each platform has unique targeting, creative formats, bidding strategies, and APIs. The generic skill provides cross-platform fundamentals. **No merging needed.**

### 4.2 Ad API/Automation (10 skills) ✅ Keep All (fix 2 templates)
Platform-specific API integration skills. Note: 2 are still template placeholders.

### 4.3 Copywriting Skills (20 skills) ✅ Keep All
Each targets a different medium/format with distinct conventions (email vs. billboard vs. legal vs. chatbot copywriting are fundamentally different crafts).

### 4.4 Photography Skills (12 skills) ✅ Keep All
Genre-specific photography — each requires different equipment, techniques, and artistic approaches.

### 4.5 Game Development (8 skills) ✅ Keep All
Covers different platforms (2D, 3D, mobile, VR, Unity) and aspects (design, assets, monetization).

### 4.6 Cloud Fundamentals (6 skills) ✅ Keep All
Provider-specific (AWS, Azure, GCP) plus cross-cutting concerns (security, cost optimization).

### 4.7 SEO Skills (6 skills) ✅ Keep All
Different SEO specializations: local, on-page, off-page, technical, video, and copywriting-focused.

### 4.8 Research Analysis (7 skills) ✅ Keep All
Different research domains: clinical, economic, geopolitical, historical, market, policy, regulatory.

### 4.9 C-Suite Leadership (8 skills) ✅ Keep All
Role-specific leadership skills for different executive positions.

### 4.10 Visual Communication/Design (3 skills) ✅ Keep All
Different output formats: graphic design, reports, slides.

### 4.11 Audio/Sound (12 skills) ✅ Keep All (after merging duplicates in Category 3)
Different audio disciplines: mastering, production, restoration, foley, live sound, MIDI, sound design.

### 4.12 Podcast (5 skills) ✅ Keep All
Different podcast aspects: advertising, production, script writing, audio/Spotify, video podcasting.

### 4.13 Amazon Advertising (5 skills) ✅ Keep All
Different Amazon ad products: API, DSP, seller strategy, sponsored brands, sponsored products.

### 4.14 Google Ads (5 skills) ✅ Keep All
Different campaign types: API, display, Performance Max, search, shopping/video.

### 4.15 Content Strategy (3 skills) ✅ Keep All
Different scopes: general planning, geo-targeted/AI-optimized, global/multi-market.

### 4.16 Frontend Development (3 skills) ✅ Keep All
Framework-specific: Angular, React, Svelte.

### 4.17 Accessibility (6 skills) ✅ Keep All (after merging overlap in Category 3)
Different accessibility contexts: general review, WCAG compliance, a11y design, presentations, video.

### 4.18 Mobile App (5 skills) ✅ Keep All
Different aspects: architecture, design, monetization, security, native design.

---

## 🟡 Category 5: STUB SKILLS NEEDING CONTENT (66 Skills)

These 66 skills exist but have minimal content (<2,500 bytes) compared to well-developed skills (typically 9,000–28,000 bytes). They need to be populated with full content.

<details>
<summary>Click to expand full list of 66 stub skills</summary>

| # | Skill Directory | Size |
|---|----------------|------|
| 1 | customer-success | 751B |
| 2 | sales-automation | 768B |
| 3 | churn-prevention | 782B |
| 4 | sales-analytics | 783B |
| 5 | customer-retention | 791B |
| 6 | lead-generation-advanced | 800B |
| 7 | account-management | 805B |
| 8 | user-story-mapping | 817B |
| 9 | product-roadmapping | 818B |
| 10 | product-management | 826B |
| 11 | feature-prioritization | 827B |
| 12 | ecommerce-analytics | 845B |
| 13 | lighting-techniques | 1,136B |
| 14 | cinematography | 1,138B |
| 15 | camera-operation | 1,147B |
| 16 | compositing | 1,166B |
| 17 | video-editing-advanced | 1,177B |
| 18 | cloud-security | 1,317B |
| 19 | infrastructure-as-code | 1,353B |
| 20 | ci-cd-pipelines | 1,358B |
| 21 | cloud-cost-optimization | 1,363B |
| 22 | serverless-architecture | 1,379B |
| 23 | vfx-compositing | 1,600B |
| 24 | game-asset-creation | 1,618B |
| 25 | video-analysis-visual-intelligence | 1,640B |
| 26 | rendering-optimization | 1,674B |
| 27 | infographic-production-workflow | 1,736B |
| 28 | particle-systems | 1,761B |
| 29 | investor-relations | 1,809B |
| 30 | infographic-marketing-distribution | 1,810B |
| 31 | microsoft-ads-api-integration | 1,830B |
| 32 | procedural-generation | 1,837B |
| 33 | job-description-writing | 1,892B |
| 34 | outbrain-campaign-management | 1,990B |
| 35 | web-accessibility-wcag | 2,011B |
| 36 | ecommerce-web-design | 2,012B |
| 37 | spreadsheet-analysis-manipulation | 2,015B |
| 38 | report-generation-automation | 2,018B |
| 39 | tool-intelligence-router | 2,031B |
| 40 | motion-graphics-animation | 2,033B |
| 41 | interactive-infographics-web-visualization | 2,045B |
| 42 | report-design-visual-communication | 2,050B |
| 43 | web-animation-interactions | 2,070B |
| 44 | typography-type-design | 2,074B |
| 45 | healthcare-compliance-regulations | 2,080B |
| 46 | industry-specific-landing-pages | 2,083B |
| 47 | outbrain-api-integration | 2,116B |
| 48 | video-thumbnails-titles | 2,130B |
| 49 | trade-desk-api-integration | 2,145B |
| 50 | mobile-first-pwa | 2,160B |
| 51 | intellectual-property-strategy | 2,183B |
| 52 | landing-page-design-conversion | 2,183B |
| 53 | industry-specific-presentation-formats | 2,211B |
| 54 | taboola-campaign-management | 2,257B |
| 55 | microsoft-ads-audience-network | 2,316B |
| 56 | infographic-design-fundamentals | 2,347B |
| 57 | native-mobile-app-design | 2,363B |
| 58 | image-analysis-visual-intelligence | 2,381B |
| 59 | content-strategy-planning | 2,382B |
| 60 | seo-copywriting-optimization | 2,406B |
| 61 | historical-research-analysis | 2,427B |
| 62 | trade-desk-campaign-management | 2,433B |
| 63 | creative-writing-storytelling | 2,461B |
| 64 | marketing-campaign-strategy-planning | 2,483B |
| 65 | taboola-api-integration | 2,488B |
| 66 | healthcare-administration-management | 2,490B |

</details>

---

## Summary of Recommended Actions

### Immediate Actions (High Priority)
1. **Delete 2 duplicate stubs:**
   - Remove `competitive-analysis-intelligence` (keep `competitive-analysis-&-intelligence`)
   - Remove `video-analysis-visual-intelligence` (keep `video-analysis-&-visual-intelligence`)

2. **Fix or remove 9 template placeholders** that were never populated with content

3. **Merge 3 near-duplicate pairs:**
   - Merge `compositing` → `vfx-compositing`
   - Merge `audio-restoration` → `audio-restoration-cleanup`
   - Merge `foley-sound-design` → `foley-sound-effects`
   - Merge `web-accessibility-wcag` → `accessibility-wcag`

### Medium Priority
4. **Populate 66 stub skills** with full content matching the standard template (9,000–15,000 bytes)

### No Action Needed
5. **All domain-specific groups** (ad platforms, copywriting types, photography genres, etc.) are intentionally specialized and should remain separate.

---

## Final Verdict

**Is merging necessary?** Only minimally. Out of 606 skills:
- **2 true duplicates** (0.3%) need merging — these are clearly accidental from the `&` character in directory names
- **4 near-duplicates** (0.7%) should be merged for clarity
- **9 placeholders** (1.5%) need content or removal
- **66 stubs** (10.9%) need content development
- **525 skills** (86.6%) are well-developed and appropriately distinct

The repository demonstrates **good architectural discipline** — the vast majority of similar-sounding skills are intentional specializations for different platforms, formats, or domains. The overlap rate is remarkably low for a 606-skill repository.
