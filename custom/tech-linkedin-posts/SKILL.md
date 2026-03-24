---
name: tech-linkedin-posts
description: Write LinkedIn posts about tech news, AI/ML tools, open-source repos, papers, and product launches. Produces scroll-stopping posts with short punchy sentences, specific numbers, and structured breakdowns. Supports three post formats — full breakdown, medium commentary, and meme/reaction.
---

# Tech LinkedIn Post Writer

Write LinkedIn posts that cover tech news — AI/ML tools, open-source repos, research papers, product launches, and industry developments. Posts should stop the scroll, inform quickly, and deliver honest analysis.

## Before Writing

Before writing any post, ask the user:

1. **What is the topic?** A repo, paper, product, or news item.
2. **What format?** Full breakdown, medium commentary, or meme/reaction. If the user doesn't specify, default to full breakdown.
3. **What's your take?** Ask the user if they have an opinion or angle they want to include. If they don't, form one yourself based on the facts.

If the user provides a link, read it first and extract the key facts before writing.

---

## The Three Post Formats

### Format 1: Full Breakdown (primary format, ~500-800 words)

This is the workhorse. Use it when there is enough substance to explain — a new tool, a paper with results, a product launch with real features.

**Structure:**

```
[HOOK — 1 provocative sentence]

[WHAT IT IS — 1-2 sentences naming the thing and what it does]

[HOW IT WORKS — 3-6 short sentences, one idea per line, plain language]

[BULLET LIST — 4-6 items with specific numbers/stats, using > prefix or → arrows]

[ANALYSIS — 2-4 sentences with YOUR honest take: who benefits, what the tradeoffs are, what's overhyped, what actually matters]

[CLOSING — 1-2 sentences that land the point or look forward]

[CTA — the user's preferred call-to-action, or omit if none provided]
```

**Example skeleton:**

```
[Hook that makes someone stop scrolling.]

[Name of tool/paper] does [core thing] for [who].

It works by [simple explanation].
[Another short sentence expanding on the mechanism.]
[One more sentence if needed.]

Key capabilities:
> [Specific stat or feature]
> [Specific stat or feature]
> [Specific stat or feature]
> [Specific stat or feature]

[Your honest take — who this actually helps, what the limitations are, or why it matters more than it looks.]

[Forward-looking sentence or call to action.]
```

### Format 2: Medium Commentary (~100-250 words)

Use when the news is interesting but doesn't need a full teardown. An opinion, a reaction to an announcement, a quick share with context.

**Structure:**

```
[HOOK — 1 sentence, same quality as a full post]

[CONTEXT — 2-4 sentences explaining what happened]

[YOUR TAKE — 1-3 sentences with analysis or opinion]

[CTA if applicable]
```

This format works best when the value is in the *perspective*, not the explanation. The reader already knows what happened — they want to know what it means.

### Format 3: Meme / Reaction (~1-2 sentences)

Use for humor, cultural moments, or shared developer experiences. These are short, punchy, and rely on the image or video doing the heavy lifting.

**Structure:**

```
[One killer sentence. Maybe two.]
```

No bullets. No CTA. No explanation. The post IS the joke or the observation. Pair with an image, meme, or short video clip.

Good meme/reaction posts tap into shared frustration, absurdity, or awe that developers already feel but haven't articulated.

---

## Writing Rules

### Sentence Style

- **Short sentences.** One idea per sentence. If a sentence has a comma, consider splitting it.
- **Declarative tone.** State facts. Don't hedge with "might", "could potentially", "it seems like". Say what the thing does.
- **Plain language.** Write so a smart person outside the specific subfield can follow. If you must use a technical term, explain it in the same sentence.
- **Line breaks between sentences.** Each sentence or short thought gets its own line. This is LinkedIn, not a paragraph essay. The vertical rhythm matters for mobile reading.

### Numbers and Specificity

Numbers are the credibility engine. Use them constantly:

- Bad: "The model is very fast"
- Good: "The model runs at 54,000 fps on an $8 chip"

- Bad: "It saves a lot of storage"
- Good: "97% less storage than traditional vector databases"

- Bad: "Several companies have been affected"
- Good: "75,200 jobs since January 2025"

Always prefer the specific number over the vague adjective. If the source doesn't provide numbers, say so honestly rather than inventing vague superlatives.

### Hooks

The hook is the single most important line. It must create a reason to stop scrolling.

**Hook patterns that work:**

| Pattern | Example |
|---|---|
| Counterintuitive claim | "Your WiFi router can now do full-body surveillance without cameras." |
| Direct address + surprise | "Every prompt you send makes Claude Code worse." |
| Scale shock | "AI just quietly eliminated 75,000 jobs." |
| Status quo challenge | "Stop uploading 40-page PDFs to Claude." |
| Absurdity that's real | "You laughed at AI-powered cows. They're worth $2 billion now." |

**Hook anti-patterns to avoid:**

- Starting with "I'm excited to share..." or "Great news..."
- Questions that the reader doesn't care about yet
- Generic statements like "AI is changing everything"
- Clickbait that the post can't deliver on

### Bullet Lists

Use `>` prefix (LinkedIn blockquote style) or `→` arrows for feature/stat lists. Keep each item to one line. Lead with the specific number or capability, not filler.

- Bad: `> The model has an impressive context window of 1M tokens`
- Good: `> 1M token context window`

- Bad: `> It offers support for multiple programming languages`
- Good: `> Supports Python, Rust, Go, TypeScript out of the box`

Aim for 4-6 bullet items per list. Fewer feels thin. More feels like a changelog.

### Numbered Lists

Use numbered lists (1. 2. 3.) when describing a sequence, a workflow, or ranked items. Use bullet lists (>) when listing features or stats with no inherent order.

---

## Analysis and Honesty

This is what separates a good tech post from a content mill.

### Always Include

- **Who this actually helps.** "If you're building multimodal RAG systems, this cuts your pipeline from 4 models to 1."
- **What the tradeoffs are.** "Mobile isn't supported yet, and rendering can take up to 30 seconds."
- **Scale and maturity.** Distinguish between a research paper, a weekend project with 12 GitHub stars, and a production tool used by thousands.

### Never Do

- **Don't oversell small repos as breakthroughs.** A repo with 30 stars and one contributor is interesting, not revolutionary. Frame it proportionally.
- **Don't use false urgency.** "Just dropped" means it came out today or yesterday. If it launched two weeks ago, say "recently released" or just state the date.
- **Don't hide limitations.** If the tool only works on Linux, or requires a 4090, or is alpha-quality, say so. Your audience respects honesty more than hype.
- **Don't present press-release summaries as analysis.** Listing features is description. Analysis is saying which features matter, which are table stakes, and what's missing.
- **Don't claim something is "insane" or "game-changing" without backing it up.** If you use strong language, the next sentence must justify it with evidence.

### The Honest Take Section

In every full breakdown post, include 2-4 sentences of genuine analysis after the bullet list. This section should answer at least one of:

- Why does this matter more (or less) than it looks?
- Who should actually use this, and who should wait?
- What's the real competitive landscape here?
- What problem does this NOT solve that people will assume it does?
- Is this genuinely novel, or is it a better package of existing ideas?

This is your voice. This is what makes people follow you instead of just reading release notes.

---

## Post Length Guidelines

| Format | Target Length | When to Use |
|---|---|---|
| Full breakdown | 500-800 words | New tools, papers, launches with substance |
| Medium commentary | 100-250 words | Opinions, quick reactions, news with obvious context |
| Meme/reaction | 1-2 sentences | Humor, cultural moments, shared experiences |

For full breakdowns, err toward the longer end of the range when the topic has real depth. A 500-word post that feels complete is better than a 400-word post that feels rushed, but an 800-word post that repeats itself is worse than both.

---

## Topic Selection Guidance

The best posts cover topics where at least one of these is true:

- **Developers can use it today.** Practical > theoretical.
- **It challenges a common assumption.** "Benchmarks are broken" > "New model scores well."
- **The numbers are surprising.** Either surprisingly good, surprisingly bad, or surprisingly cheap.
- **It signals a trend.** One tool is news. Three tools doing the same thing is a pattern worth naming.

Avoid posting about something just because it's new. New and uninteresting is worse than old and insightful.

---

## Media Pairing

Every post should include media. The format depends on the content:

| Content Type | Best Media |
|---|---|
| Tool / repo with UI | Screen recording or demo video |
| Paper with results | Chart, graph, or key figure from the paper |
| Product launch | Product screenshot or promotional image |
| Industry news / opinion | Relevant image, infographic, or data visualization |
| Meme / reaction | The meme image or short clip |

If you can't find good media, a clean screenshot of the repo's README or a key code snippet works.

---

## Checklist Before Publishing

Run through this before finalizing any post:

- [ ] Does the hook make someone stop scrolling?
- [ ] Are all claims backed by specific numbers or sources?
- [ ] Is there at least one sentence of honest analysis (not just feature listing)?
- [ ] Would you be comfortable if the tool's creator read this post? (no misrepresentation)
- [ ] Would you be comfortable if a skeptic read this post? (no overselling)
- [ ] Is every sentence earning its place, or is there filler?
- [ ] Does the post read well on a phone screen? (short lines, vertical rhythm)
