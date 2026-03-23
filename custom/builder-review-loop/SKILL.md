---
name: builder-review-loop
description: Use when one agent is implementing code and another agent must review the resulting changes, compare the summary against the actual files, decide whether to fix now or move on, and write the next tightly scoped prompt with context handoff guidance.
---

# Builder Review Loop

Use a two-agent workflow:
- The builder agent implements the requested slice.
- The reviewer agent reads the real files, not just the summary, and helps the user decide whether to fix, defer, revert, or proceed.
- The human owns scope and final decisions.

## Core Rules

- Treat the builder summary as a claim, not proof. Read the touched files.
- Findings come first. Prioritize bugs, regressions, scope drift, and contract breaks over style.
- Separate `must fix now` from `can defer`.
- Keep prompts narrow: one bug fix or one feature slice at a time.
- Do not silently reopen product or architecture decisions that the user already made.
- Prefer a fresh conversation when context is bloated and the next agent can reconstruct state from the code.

## Review Workflow

1. Read the builder summary and exact files changed.
2. Read the touched files plus the nearest neighboring files needed to verify the claims.
3. Classify findings:
   - `High`: wrong behavior, data loss, broken contract, serious regression.
   - `Medium`: incomplete slice, UX mismatch, race condition, unsafe assumption.
   - `Low`: cleanup, naming, minor debt, acceptable temporary duplication.
4. Answer the user’s direct questions plainly:
   - Is the change good enough to keep?
   - Fix now or move on?
   - Is something missing?
   - Was something included that should not be here?
   - Fresh conversation or existing one?
5. If there are no blocking findings, say so explicitly and name the next slice.

## Review Rubric

Check these in order:

- Does the code actually do what the summary claims?
- Did the builder stay within the requested scope?
- Does it match the locked contracts, master plan, and latest user decisions?
- Is there hidden hardcoding or architecture drift?
- Are UI truth and runtime truth reading from the same source of truth?
- Can the change lose, overwrite, or fabricate user state?
- Is the remaining debt acceptable for the current phase?

## Decision Rules

- `Fix now` if the issue causes incorrect behavior, lost state, misleading UX, invalid persistence, or contract breakage.
- `Defer` if the issue is real but isolated, understood, and does not poison the next slice.
- `Revert` only if the direction is wrong, scope exploded, or the change makes the architecture harder to recover.
- `Proceed` when the slice is coherent and only minor follow-up debt remains.

## Prompt Writing Rules

Every next-step prompt should include:

- The current goal in one sentence
- The context about the feature or bugfix 
- Exact files to read first
- The specific bug or missing behavior
- Clear constraints on what not to touch
- Acceptance criteria
- Required verification
- Expected final response shape

Do not write vague prompts like:
- "make it cleaner"
- "make it more dynamic"
- "improve the architecture"

## Handoff Rule

Use a fresh conversation when:
- The context window is crowded
- A new feature slice is starting
- Several review rounds have already happened
- The next agent can recover truth from the code and current files

Reuse the same conversation when:
- The follow-up is tiny and local
- The same bug is being fixed
- The recent reasoning still matters more than the code state

## Default Response Shape

Use this structure:

1. `Findings`
2. `Answer`
3. `Next step`
4. `Prompt`
5. `Fresh vs existing conversation`

## Prompt Template

```text
We are continuing a phased implementation. This task is intentionally narrow.

Read these files first:
- ...
- ...

Current issue:
- ...

What to change:
- ...

Constraints:
- Do not ...
- Keep ...
- Stay within ...

Acceptance criteria:
- ...
- ...

Verification:
- Run ...
- Report exact files changed
- Explain the root cause and why the fix works