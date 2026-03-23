---
name: generate-review-context
description: Generate a structured review context document for code implemented by another AI agent. Produces scope, files created, files modified, architecture summary, and review notes. Use when preparing for a code review of work done by another agent, when user says "generate review context", "prepare review", "document what was implemented", or wants to hand off implementation for review.
---

# Generate Review Context

Produce a structured Markdown review context document that gives a reviewing agent (or human) everything they need to assess an implementation without re-discovering it from scratch.

## When to Use

- An AI agent just finished implementing a feature and you need to document what was done.
- You want to hand off implementation work to a reviewer (human or AI).
- You want a snapshot of what changed before requesting a code review.

## Inputs

The user provides one or more of:
- A description of what was implemented
- The relevant design doc, PRD, or spec
- A git diff or list of changed files
- Verbal context about the work

If the user doesn't provide enough context, ask for:
1. What was the goal of the implementation?
2. Where is the design doc or spec?
3. Which files were created or modified?

## Process

1. **Identify the scope** — read the design doc/spec and the implementation to understand what was built vs what was planned.
2. **Inventory files** — separate into files created and files modified, with a one-line reason for each.
3. **Map the architecture** — describe the current architecture as implemented, not as planned.
4. **Flag review notes** — call out specific files or areas that need careful review attention.
5. **List what's not implemented** — things from the spec that were deferred or skipped.

## Output Format

Produce a single Markdown document with these sections in this exact order:

```markdown
## Review Context for [Feature Name]

### Scope
- 2-3 sentences on what this work implements.
- State what is real vs placeholder.
- State the boundary of the review (only these files, not unrelated changes).

### What Was Implemented
- Bullet list of the major deliverables, described functionally (not file-by-file).

### Files Created
For each new file:
- `path/to/file.ts`
  Reason: one-line explanation of why this file was created.

Group related files together (e.g., all layout components, all type files).

### Files Modified
For each modified file:
- `path/to/file.ts`
  Reason: one-line explanation of what changed and why.

### Current Architecture
- Describe the actual data flow and component relationships as implemented.
- Use a numbered list or short paragraphs, not a diagram.
- Focus on: where data enters, how it flows, where it renders.

### Relevant Docs
For each doc:
- `path/to/doc.md`
  How it should work: one-line on what this doc defines and whether it's the source of truth or outdated.

### Not Implemented Yet
- Bullet list of things from the spec/plan that were explicitly deferred.

### Review Notes
- Bullet list of specific areas that need careful review attention.
- Include file paths and line numbers when possible.
- Flag things like: potentially unused files, custom implementations that may be fragile, SQL that may not match debug output, scroll/layout fixes that need browser testing.
```

## Rules

- **Be factual, not promotional.** Don't say "elegantly implemented" — say what it does.
- **Include file paths.** Every claim should be traceable to a file.
- **Separate what exists from what's planned.** Never mix implemented features with future plans.
- **Flag uncertainty.** If you're not sure whether something works correctly, say so explicitly in the review notes.
- **Don't review the code yourself.** This skill generates the context document only. The actual review is a separate step.
- **Keep it scannable.** A reviewer should be able to read the full context in under 3 minutes.
