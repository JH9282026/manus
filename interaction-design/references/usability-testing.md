# Usability Testing

Comprehensive guide to planning, conducting, and analyzing usability tests for interaction design validation.

---

## Usability Testing Fundamentals

### What is Usability Testing?

Usability testing is a research method where representative users attempt to complete tasks with a product while observers watch, listen, and take notes. The goal is to identify usability problems, collect qualitative and quantitative data, and determine user satisfaction.

### Why Usability Testing Matters

**Cost savings:**
- Fixing issues during design: $1
- Fixing during development: $10
- Fixing after release: $100

**Effectiveness:**
- 5 users reveal 85% of usability issues
- Iterative testing (3 rounds of 5 users) more effective than one round of 15 users

**Validation:**
- Confirms or refutes design assumptions
- Provides evidence for design decisions
- Identifies unexpected user behaviors

---

## Types of Usability Testing

### Moderated vs. Unmoderated

| Aspect | Moderated | Unmoderated |
|--------|-----------|-------------|
| **Facilitator present** | Yes | No |
| **Flexibility** | High (can probe deeper) | Low (fixed script) |
| **Cost** | Higher (facilitator time) | Lower (automated) |
| **Participant pool** | Smaller (scheduling constraints) | Larger (on-demand) |
| **Insights depth** | Deeper (can ask follow-ups) | Shallower (no clarification) |
| **Best for** | Complex tasks, early-stage research | Simple tasks, large sample sizes |

### Remote vs. In-Person

| Aspect | Remote | In-Person |
|--------|--------|----------|
| **Geographic reach** | Global | Local |
| **Natural environment** | Yes (user's context) | No (lab setting) |
| **Technical issues** | More common (connectivity, screen sharing) | Fewer |
| **Body language observation** | Limited (depends on video quality) | Full |
| **Cost** | Lower (no travel/facility) | Higher |
| **Best for** | Distributed users, web/mobile apps | Physical products, accessibility testing |

### Formative vs. Summative

**Formative testing** — During design process to improve product
- Goal: Identify and fix usability issues
- Timing: Early and throughout design
- Sample size: Small (5-8 users per iteration)
- Methods: Think-aloud, task-based testing

**Summative testing** — After design to measure performance
- Goal: Measure usability against benchmarks
- Timing: Before launch or after major release
- Sample size: Larger (20+ users for statistical significance)
- Methods: Task completion rates, time-on-task, satisfaction surveys

---

## Planning Usability Tests

### 1. Define Research Goals

**Good research questions:**
- Can users successfully complete checkout?
- Do users understand the difference between "Save" and "Publish"?
- Can users find the settings menu?
- How long does it take users to create their first project?

**Poor research questions:**
- Do users like the design? (Too vague, subjective)
- Is the product usable? (Too broad)
- What do users think about the color scheme? (Not behavioral)

### 2. Identify Target Users

**Create participant criteria:**

**Demographics:**
- Age range
- Geographic location
- Language
- Education level

**Behavioral:**
- Frequency of similar product use
- Technical proficiency
- Domain expertise

**Contextual:**
- Device ownership (smartphone, tablet, desktop)
- Internet connection quality
- Accessibility needs

**Example criteria:**
- Age 25-45
- Uses project management software at least weekly
- Works in team of 5+ people
- Comfortable with web applications
- Not a UX designer (avoid expert bias)

### 3. Recruit Participants

**Recruitment sources:**

**Internal:**
- Customer database (existing users)
- Email lists
- In-app recruitment (banner or modal)

**External:**
- User research platforms (UserTesting, Respondent, User Interviews)
- Social media (LinkedIn, Twitter, Facebook groups)
- Craigslist or local classifieds
- Professional recruiters (expensive but effective)

**Screening:**
- Create screening questionnaire (5-10 questions)
- Filter for target criteria
- Avoid leading questions that reveal "correct" answers
- Over-recruit by 20% (account for no-shows)

**Incentives:**
- Cash ($50-150 for 1-hour session, varies by market)
- Gift cards (Amazon, Visa)
- Product discounts or free subscriptions
- Donation to charity (if participant prefers)

### 4. Create Test Plan

**Test plan components:**

**1. Introduction (5 minutes)**
- Welcome and thank participant
- Explain purpose (testing product, not participant)
- Review consent form and recording permission
- Encourage thinking aloud
- Answer questions

**2. Background questions (5 minutes)**
- Confirm participant criteria
- Understand context and experience
- Build rapport

**3. Tasks (30-40 minutes)**
- 5-8 tasks (more tasks = less depth per task)
- Realistic scenarios (not "Click the button")
- Clear success criteria

**4. Post-task questions (5 minutes)**
- Satisfaction rating (1-5 or 1-7 scale)
- Difficulty rating
- Open-ended feedback

**5. Debrief (5 minutes)**
- Overall impressions
- Comparison to alternatives
- Feature requests
- Thank participant and provide incentive

**Total time: 60 minutes** (standard session length)

### 5. Write Effective Tasks

**Task writing principles:**

**Good task:**
"You need to change your password because you think your account may have been compromised. Show me how you would do that."

**Why it's good:**
- Provides realistic context (why user would do this)
- Doesn't reveal solution (doesn't say "Go to Settings")
- Clear success criteria (password changed)

**Poor task:**
"Click on Settings, then Security, then Change Password."

**Why it's poor:**
- No context (why would user do this?)
- Reveals exact steps (not testing navigation)
- Not realistic (users don't follow instructions, they have goals)

**Task structure:**
1. **Context** — Why is the user doing this?
2. **Goal** — What does the user want to accomplish?
3. **Success criteria** — How will you know they succeeded?

**Example tasks:**

**E-commerce:**
"You're looking for a birthday gift for your friend who loves cooking. Find a gift under $50 and add it to your cart."

**Project management:**
"Your team just finished the design phase of the project. Update the project status to reflect this milestone."

**Banking app:**
"You need to pay your rent ($1,200) to your landlord, John Smith. Show me how you would do that."

---

## Conducting Usability Tests

### Facilitator Role

**Do:**
- Remain neutral (don't help or hint)
- Encourage thinking aloud ("What are you thinking?")
- Probe for understanding ("Why did you click that?")
- Observe body language and facial expressions
- Take notes on behaviors, not just comments

**Don't:**
- Lead participant ("Don't you think this button is confusing?")
- Defend the design ("That's actually supposed to...")
- Interrupt during task (wait for natural pauses)
- Answer questions (reflect back: "What would you do if I weren't here?")

### Think-Aloud Protocol

**Purpose:** Understand user's thought process in real-time.

**Instructions to participant:**
"As you use the product, please think aloud — say what you're looking at, what you're trying to do, and what you're thinking. Imagine I'm sitting next to you and you're showing me how to use it."

**Encouraging think-aloud:**
- "What are you looking for?"
- "What are you thinking?"
- "What do you expect to happen?"
- "Why did you choose that option?"

**Challenges:**
- Some users naturally quiet (need more prompting)
- Thinking aloud can slow down tasks (affects time metrics)
- Users may censor thoughts ("I shouldn't say that")

**Alternative: Retrospective think-aloud**
- User completes task silently
- Replay recording and ask user to explain their thinking
- More accurate time metrics, but less immediate insights

### Handling Common Situations

**Participant is stuck:**
- Wait 30-60 seconds (users often figure it out)
- Ask: "What are you looking for?" or "What would you do if I weren't here?"
- If still stuck after 2-3 minutes, provide hint or move to next task
- Note: Task failure is valuable data, not a problem

**Participant asks for help:**
- Reflect question back: "What do you think you should do?"
- If they insist: "I can't help right now, but what would you try?"
- Last resort: "Let's move on to the next task"

**Participant criticizes design harshly:**
- Stay neutral: "Thank you for that feedback"
- Probe deeper: "Can you tell me more about that?"
- Don't defend: Resist urge to explain design rationale

**Participant goes off-task:**
- Gently redirect: "That's interesting. Let's get back to [task]."
- Note the distraction (may indicate confusing UI)

**Technical issues:**
- Have backup plan (different device, different prototype)
- If unfixable, reschedule participant (still pay incentive)
- Document issue for future sessions

### Note-Taking and Recording

**What to record:**
- Screen recording (required)
- Participant video (helpful for facial expressions)
- Audio (backup if video fails)
- Facilitator notes (observations, quotes, timestamps)

**Note-taking template:**

```
Participant: P01
Date: 2026-03-16
Task: Change password

Observations:
- [00:05] Looked at top-right corner first (expected account menu)
- [00:15] Clicked profile picture, found Settings
- [00:30] Scanned Settings page, paused at "Security"
- [00:45] "I'm looking for something about passwords..."
- [01:00] Clicked Security, immediately found Change Password
- [01:15] Task completed successfully

Quotes:
- "I expected this to be in my profile somewhere"
- "Security makes sense for passwords"

Issues:
- None

Success: Yes
Time: 1:15
Difficulty (1-5): 2
```

**Tools:**
- **Screen recording:** Zoom, Loom, QuickTime (Mac), OBS (free)
- **Note-taking:** Google Docs, Notion, Dovetail, EnjoyHQ
- **Participant management:** Calendly, User Interviews, Respondent

---

## Analyzing Usability Test Results

### Quantitative Analysis

**Key metrics:**

**1. Task success rate**
- Formula: (Successful completions / Total attempts) × 100
- Example: 8 out of 10 users completed checkout = 80% success rate
- Benchmark: >80% is good, <70% needs improvement

**2. Time on task**
- Measure: Seconds from task start to completion
- Calculate: Mean and median (median less affected by outliers)
- Compare: Against benchmark or previous version

**3. Error rate**
- Count: Number of errors per task
- Types: Navigation errors, input errors, interpretation errors
- Severity: Critical (prevents completion) vs. minor (slows down)

**4. Satisfaction ratings**
- Scale: 1-5 or 1-7 ("How easy was this task?")
- Calculate: Mean score per task
- Benchmark: >4 on 5-point scale is good

**Statistical significance:**
- Need 20+ participants for reliable quantitative data
- For small samples (5-8), focus on qualitative insights
- Use quantitative data to identify trends, not prove significance

### Qualitative Analysis

**Thematic analysis:**

1. **Review notes and recordings** — Watch all sessions, take detailed notes
2. **Identify patterns** — What issues appeared multiple times?
3. **Group by theme** — Navigation issues, labeling confusion, missing features
4. **Prioritize by severity and frequency** — High severity + high frequency = top priority

**Severity rating:**

| Severity | Definition | Example | Priority |
|----------|------------|---------|----------|
| **Critical** | Prevents task completion | Can't find checkout button | P0 (fix immediately) |
| **Serious** | Causes significant delay or frustration | Confusing form labels, multiple errors | P1 (fix before launch) |
| **Moderate** | Causes minor delay or confusion | Unclear icon, non-optimal path | P2 (fix if time allows) |
| **Minor** | Cosmetic or rare issue | Typo, slight visual misalignment | P3 (backlog) |

**Frequency rating:**

- **High** — 4+ out of 5 users experienced issue
- **Medium** — 2-3 out of 5 users
- **Low** — 1 out of 5 users

**Prioritization matrix:**

| Frequency \ Severity | Critical | Serious | Moderate | Minor |
|---------------------|----------|---------|----------|-------|
| **High** | P0 | P0 | P1 | P2 |
| **Medium** | P0 | P1 | P2 | P3 |
| **Low** | P1 | P2 | P3 | P3 |

### Creating Actionable Insights

**Poor insight:**
"Users found the interface confusing."

**Why it's poor:**
- Too vague (what specifically was confusing?)
- No context (which users? which tasks?)
- No recommendation (what should we do?)

**Good insight:**
"4 out of 5 users couldn't find the 'Export' button because it was hidden in the overflow menu. Users expected it in the main toolbar next to 'Save' and 'Share'. Recommendation: Move 'Export' to main toolbar."

**Why it's good:**
- Specific issue (Export button location)
- Quantified (4 out of 5 users)
- Explains why (user expectation)
- Actionable recommendation (move to toolbar)

**Insight template:**

```
Issue: [What went wrong?]
Evidence: [How many users? What did they do/say?]
Impact: [How does this affect users?]
Root cause: [Why did this happen?]
Recommendation: [What should we change?]
Priority: [P0/P1/P2/P3]
```

---

## Reporting Usability Test Results

### Report Structure

**1. Executive Summary (1 page)**
- Key findings (top 3-5 issues)
- Overall success rate and satisfaction
- High-priority recommendations

**2. Methodology (1 page)**
- Participant criteria and recruitment
- Number of participants
- Test format (remote/in-person, moderated/unmoderated)
- Tasks tested

**3. Findings (5-10 pages)**
- Issue-by-issue breakdown
- Evidence (quotes, screenshots, video clips)
- Severity and frequency ratings
- Recommendations

**4. Appendix**
- Full task list
- Participant demographics
- Raw data (task success rates, time on task)
- Detailed notes (if needed)

### Presentation Tips

**For stakeholders:**
- Lead with impact ("3 out of 5 users couldn't complete checkout")
- Use video clips (more compelling than text)
- Focus on top priorities (don't overwhelm with every issue)
- Provide clear recommendations (not just problems)

**For designers/developers:**
- Include detailed evidence (screenshots, quotes, timestamps)
- Explain user mental models (why they expected X)
- Suggest specific design changes
- Prioritize issues clearly

**For executives:**
- Focus on business impact ("20% of users abandoned checkout")
- Quantify when possible (success rates, time savings)
- Tie to business goals (conversion, retention, satisfaction)
- Keep it brief (executive summary only)

---

## Continuous Usability Testing

### Integrating Testing into Workflow

**Sprint-based testing:**
- Test at end of each sprint (every 2 weeks)
- 3-5 users per sprint
- Focus on new features or changes
- Quick turnaround (report within 2-3 days)

**Milestone testing:**
- Test at major milestones (end of design phase, before launch)
- 8-10 users
- Comprehensive task coverage
- Detailed report with prioritized recommendations

**Continuous testing:**
- Always-on unmoderated testing (UserTesting, Maze)
- Automated metrics (task success, time, clicks)
- Weekly or monthly review of results
- Supplement with periodic moderated sessions

### Building a Testing Culture

**Make testing visible:**
- Share video clips in team meetings
- Post findings in shared Slack channel
- Create highlight reels of key issues

**Involve the team:**
- Invite designers/developers to observe sessions
- Rotate note-taking responsibilities
- Collaborative analysis workshops

**Celebrate impact:**
- Track before/after metrics ("Success rate improved from 60% to 90%")
- Share user testimonials ("This is so much easier now!")
- Recognize team members who act on findings

---

## Usability Testing Tools

### Moderated Testing Platforms

**Zoom / Google Meet**
- Purpose: Video conferencing for remote moderated tests
- Cost: Free to $20/month
- Features: Screen sharing, recording, breakout rooms

**Lookback**
- Purpose: Specialized user research platform
- Cost: $99-399/month
- Features: Live observation, timestamped notes, highlight reels

**UserZoom**
- Purpose: Enterprise research platform
- Cost: Custom pricing (expensive)
- Features: Moderated and unmoderated testing, panel recruitment, analytics

### Unmoderated Testing Platforms

**UserTesting**
- Purpose: On-demand user testing
- Cost: $49-99 per video (or subscription)
- Features: Large participant panel, quick turnaround, video recordings

**Maze**
- Purpose: Rapid prototype testing
- Cost: Free to $99/month
- Features: Integrates with Figma, quantitative metrics, heatmaps

**UsabilityHub**
- Purpose: Quick tests (5-second test, first-click test)
- Cost: Free to $99/month
- Features: Fast results, large panel, simple tests

### Analysis Tools

**Dovetail**
- Purpose: Research repository and analysis
- Cost: $29-99/user/month
- Features: Transcription, tagging, insights, collaboration

**EnjoyHQ**
- Purpose: Research repository
- Cost: $100-200/month
- Features: Centralized research storage, tagging, search

**Notion / Airtable**
- Purpose: General-purpose database for research tracking
- Cost: Free to $20/user/month
- Features: Flexible structure, collaboration, templates

---

## Advanced Usability Testing Techniques

### A/B Testing

Compare two design variations to see which performs better.

**When to use:**
- Optimizing specific elements (button color, CTA text)
- Validating design decisions with data
- Large user base (need statistical significance)

**Process:**
1. Create two versions (A and B)
2. Randomly assign users to each version
3. Measure key metric (conversion, task success, time)
4. Determine which version performs better

**Limitations:**
- Doesn't explain why one version is better
- Requires large sample size (hundreds to thousands of users)
- Only tests one variable at a time

### Eye Tracking

Track where users look on screen to understand attention patterns.

**When to use:**
- Understanding visual hierarchy
- Identifying overlooked elements
- Optimizing layouts and information architecture

**Equipment:**
- Hardware eye trackers (Tobii, EyeLink) — expensive, very accurate
- Webcam-based (Sticky, RealEye) — affordable, less accurate

**Insights:**
- Heatmaps (where users looked most)
- Gaze plots (order of visual attention)
- Time to first fixation (how quickly users notice element)

**Limitations:**
- Expensive equipment and setup
- Small sample sizes (5-10 users)
- Looking ≠ understanding (users may look at something but not comprehend it)

### Card Sorting

Understand how users categorize and organize information.

**When to use:**
- Designing navigation structure
- Organizing content
- Creating taxonomies

**Types:**
- **Open card sort** — Users create their own categories
- **Closed card sort** — Users sort into predefined categories
- **Hybrid** — Combination of open and closed

**Process:**
1. Write content items on cards (physical or digital)
2. Ask users to group related items
3. Ask users to name each group
4. Analyze patterns across users

**Tools:**
- OptimalSort (online card sorting)
- Miro or FigJam (virtual sticky notes)
- Physical index cards (in-person)

### Tree Testing

Test navigation structure without visual design.

**When to use:**
- Validating information architecture
- Testing navigation labels
- Before visual design (isolate structure from aesthetics)

**Process:**
1. Create text-only hierarchy (no visual design)
2. Give users tasks ("Where would you find X?")
3. Users navigate through text menu
4. Measure success rate and path taken

**Tools:**
- Treejack (Optimal Workshop)
- UsabilityHub
- Simple HTML page with nested lists

---

Usability testing is not a one-time activity but an ongoing practice. Test early, test often, and act on findings to create products that truly meet user needs.
