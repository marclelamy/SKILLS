---
name: feature-to-posts
description: >
  Generate 3-5 social media post variations (LinkedIn, Twitter/X, Reddit) from a feature description.
  Each post uses a different angle and perspective while keeping an authentic solo-founder voice.
  Use this skill when the user says things like "I just built this feature", "write posts about this",
  "help me announce this", "create social content for this feature", "I need posts for this",
  "market this feature", or describes a feature and wants help promoting it on social media.
  Also triggers when the user mentions writing posts, creating announcements, or generating content
  about something they shipped, launched, or are building.
---

# Feature to Posts

Turn a feature description into 3-5 ready-to-post social media variations. Each post takes a different angle and is tailored to a specific platform (LinkedIn, Twitter/X, or Reddit), but the voice stays the same everywhere: authentic, direct, solo-founder energy.

## Before Writing

### Step 1: Understand the feature

Ask the user:

1. **What did you build?** Get the feature name, what it does, and why it matters.
2. **Who is it for?** Who benefits most from this feature?
3. **What's the story?** Was there a problem that led to this? A moment of insight? A user request?

If the user provides a link, demo, or screenshot — read it first and extract key details.

### Step 2: Load context

Read the user's marketing folder to understand their product positioning, voice, and strategy:

- Read `/Users/marclamy/Documents/Code/BlendAI/z-notes/marketing/PLAN.md` for overall strategy and positioning
- Read `/Users/marclamy/Documents/Code/BlendAI/z-notes/marketing/advices/main.md` for content creation principles
- Read `/Users/marclamy/Documents/Code/BlendAI/z-notes/marketing/advices/golden rules.md` for hook and video structure patterns

Skim these quickly — you're looking for voice, positioning, and any relevant content pillars. Don't read every file.

### Step 3: Load related skills

Before generating posts, check if these skills are available and load the ones that are relevant:

- **tech-linkedin-posts** — Use its writing rules, hook patterns, and analysis framework. This skill has the most detailed guidance on post structure, so lean on it heavily for LinkedIn posts.
- **content-strategy** — Use for understanding which content type fits (searchable vs shareable, buyer stage, topic clusters). Helpful for framing the angle.
- **marketing-ideas** — Skim for relevant tactics or angles that could inspire a post's framing (e.g., building in public, product-led growth, community-driven).

You don't need to run these skills end-to-end. Read their SKILL.md files for guidance and apply what's relevant.

---

## Generating Posts

Create **3-5 post variations**. Each one must use a **different angle** and target a **different platform**.

### The Five Angles

Pick 3-5 from these perspectives. Not every post needs every angle — choose what fits the feature:

**1. Builder Journey** — "Here's what I learned building this"
Share the behind-the-scenes. What was hard? What surprised you? What did you almost do differently? This angle works because people follow builders, not products.

**2. Problem-Solution** — "You know that annoying thing? I fixed it"
Lead with the pain. Describe the frustration your users feel, then reveal the feature as the answer. Works best when the problem is widely relatable.

**3. Educational** — "Here's how to do X with this"
Teach something. Show a use case, a workflow, a before/after. The feature is the vehicle, but the value is the knowledge. This angle builds trust.

**4. Honest Take** — "This isn't perfect, but here's why it matters"
Be upfront about limitations, tradeoffs, or what's still missing. Counterintuitively, honesty builds more credibility than hype. Acknowledge what's not there yet while explaining why what IS there matters.

**5. Big Picture** — "This is where things are heading"
Zoom out. Connect the feature to a larger trend, a shift in how people work, or a vision for the future. This positions you as someone who thinks beyond the immediate.

### Platform Adaptation

The voice stays the same across platforms — authentic, direct, no corporate speak. But the format adapts:

**LinkedIn**
- Longer form (300-600 words)
- Line breaks between sentences for mobile readability
- Can include bullet lists with `>` or `→`
- Hook in the first line is critical (it's the "see more" cutoff)
- End with a question or soft CTA to drive comments

**Twitter/X**
- Tight and punchy (under 280 chars for single tweet, or 3-5 tweet thread)
- For threads: hook tweet → key points → honest take → CTA
- No fluff. Every word earns its spot
- Can be more casual, use abbreviations

**Reddit**
- Conversational and community-first
- Lead with value or a genuine question, not self-promotion
- Acknowledge the community ("I've been lurking here for months...")
- Share what you learned, not just what you built
- Be ready for skepticism — address it preemptively
- Subreddit-aware: suggest which subreddit fits (r/SideProject, r/startups, r/artificial, etc.)

---

## Voice Guidelines

These are non-negotiable regardless of platform:

- **Be yourself.** Same person on LinkedIn as on Reddit. No corporate mask.
- **Solo founder energy.** You're building this yourself. That's your superpower — lean into it.
- **Specific over vague.** Use real numbers, real timelines, real stories. "I spent 3 weeks on this" beats "after extensive development."
- **Vulnerable when real.** Admitting something was hard or that you're not sure about something builds trust. Don't manufacture vulnerability — just don't hide it.
- **No hype words without backup.** If you say "game-changing," the next sentence better explain why. Otherwise, just describe what it does and let people decide.
- **Short sentences.** One idea per sentence. If it has a comma, consider splitting it.

---

## Output Format

For each post, output:

```
### Post [N]: [Angle] — [Platform]

[The actual post text, ready to copy-paste]

**Why this angle:** [1 sentence explaining why this framing works for this feature]
**Suggested media:** [What image, screenshot, video, or GIF would pair well]
```

After all posts, add:

```
### Quick Comparison

| # | Platform | Angle | Hook | Length |
|---|----------|-------|------|--------|
| 1 | LinkedIn | Builder Journey | "..." | ~400 words |
| 2 | Twitter/X | Problem-Solution | "..." | 5-tweet thread |
| ... | ... | ... | ... | ... |
```

This table helps the user quickly scan and pick which ones to use.

---

## Final Check

Before delivering, verify each post against:

- [ ] Does the hook stop the scroll?
- [ ] Is there at least one specific number, timeline, or concrete detail?
- [ ] Would you post this yourself without editing? (if not, edit it)
- [ ] Does it sound like a real person, not a marketing bot?
- [ ] Is it adapted to the platform's conventions?
- [ ] Could someone who doesn't know your product still get value from this?
