---
name: code-commenting
description: Apply Marc's BlendAI code commenting style — file headers only when non-obvious, JSDoc on every exported function and type, numbered step comments in flows, `═══` section dividers in large files, NOTE blocks for important gotchas, why-not-what inline comments. Use whenever writing or editing TypeScript/TSX/JS code in this codebase, when the user asks to add or improve comments, when reviewing PRs for comment quality, or when scaffolding a new module/route/hook/service.
disable-model-invocation: true
---

# Code Commenting (BlendAI)

## Goal

Comments explain **why**, **what is non-obvious**, and **what future-me would miss**. The code itself explains **what**. Names + types do the heavy lifting; comments fill the gaps.

## Hard rules

1. **Never narrate obvious code.** No `// Import the module`, `// Loop over items`, `// Return result`. If the line is self-evident from its identifiers, no comment.
2. **Why over what.** A comment must add context the reader can't get from reading the code: policy, gotcha, invariant, trade-off, history, link.
3. **Em-dashes `—` not `--` or `:`** inside comments when joining clauses.
4. **TODOs uppercase, own line**: `// TODO: handle expired tokens`. Never inline mid-sentence.
5. **Improve as you go.** When editing a function, fix or add comments in the surrounding code if they're missing or stale. Don't leave a half-commented module.

---

## 1. File headers

Add a top-of-file JSDoc block **only when the file's purpose is non-obvious from its name + location**. Skip headers on routes, components, hooks, and types files with self-explanatory names.

Use a header when:

- The file is a shared cross-cutting module that callers from multiple transports/layers use (services, runners, contracts, shared types with discriminants).
- There's a subtle execution-path contract worth stating up front.
Format: short, declarative. 1 line of purpose + 1 short paragraph of context. No tags.

```ts
/**
 * Shared published Workflow v2 run starter.
 *
 * API, MCP, and web routes pass an already-authenticated caller here so the
 * load/apply/validate/authorize/create/start path stays identical.
 */
```

```ts
/**
 * Shared types for Workflow v2 run authentication and published run starts.
 *
 * These types keep API, MCP, and web callers on the same execution contract
 * while letting each transport format errors and responses differently.
 */
```

---

## 2. Function JSDoc

**Every exported function gets a JSDoc**, even if it's one line. Internal/private helpers don't need it unless the behavior is non-obvious.

- Keep it terse — one sentence is usually enough.
- Use multi-line only when there's a non-obvious invariant or auth/trust boundary worth flagging.
- No `@param` / `@returns` unless TypeScript types are insufficient (rare — they almost always are sufficient).

```ts
/** Starts a published workflow run using the shared Workflow v2 execution path. */
export async function startPublishedWorkflowRun({ ... }) { ... }
```

```ts
/**
 * GET /api/v1/runs/:runId
 *
 * Returns the status and output of a workflow run.
 * Auth via API key (Bearer bai_...) or session.
 */
export async function GET(...) { ... }
```

For internal helpers, prefer no JSDoc — let the name + types speak:

```ts
function mapLoadFailureStatus(code: StartPublishedWorkflowRunFailure['code']) { ... }
```

---

## 3. Type / interface JSDoc

**Every exported type / interface gets a JSDoc.** Even one line. This applies to everything in `lib/types/**` and any types exported from feature modules.

```ts
/** How a workflow run request was authenticated. */
export type WorkflowRunAuthMethod = 'session' | 'api-key' | 'blend-mcp'

/** Successful authentication for a workflow run, with optional transport metadata. */
export type WorkflowRunAuthSuccess = {
    ok: true
    user: User
    method: WorkflowRunAuthMethod
    /** Present when authenticated via a user API key. */
    apiKey?: { id: string }
    /** Present when authenticated via a Blend MCP token. */
    blendMcp?: { id: string; workflowIds: string[]; tokenHash: string }
}
```

Add per-field comments only on fields whose presence/absence, units, or semantics aren't obvious from the name + type. Discriminant fields (`ok: true | false`, `code: '...'`) and IDs don't need comments.

---

## 4. Section dividers (only large files)

Use `═══` dividers **only in large files** (roughly 300+ lines) that mix multiple distinct concerns — hooks, services, runners. Don't add them to small files, routes, or single-purpose modules.

Format: 111-wide line of `═`, ALL CAPS title, 111-wide line again.

```ts
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
// HOOKS
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

Typical section names: `HOOKS`, `STATE`, `EVENT HANDLING`, `EFFECTS`, `MESSAGE OPERATIONS`, `REQUEST HANDLING`, `BOOKMARKS`, `TITLE & CANCELLATION`, `RETURN`. Match the section name to what's in the block — don't force a taxonomy.

---

## 5. Numbered step comments

**Use these liberally** in any function that runs a sequence of distinct steps — routes, orchestrators, runners, multi-stage handlers. They make flow scannable and double as a table of contents.

Two acceptable formats:

**Boxed, for route handlers and top-level orchestrators:**

```ts
export async function GET(request: Request, { params }) {
    // --- 1. Authenticate + rate limit ---
    const auth = await authenticateApiCaller(request)
    if (auth instanceof Response) return auth

    // --- 2. Fetch run detail (scoped to caller's userId) ---
    const { data: result, error } = await tryCatchAsync(...)
}
```

**Plain numbered, for inline flows inside a function:**

```ts
// 1. Try dedicated key first (reliable), fall back to shared cache
const directKey = `conv:${idFromPath}`
...

// 2. When server data arrives, merge (DB wins if completed, else cache wins)
if (initialConversationPromise) { ... }

// 3. When stream ID arrives, resume if needed
if (initialStreamIdPromise) { ... }
```

Rules:

- Always include a short clause explaining **why** or **what's non-obvious** in parentheses or after a dash.
- Steps should match the actual code blocks below them — don't number aspirationally.
- If the function only has 2 trivial steps, skip numbering. Use when there are 3+ distinct phases or when readers benefit from the map.

---

## 6. Inline comments

Trigger an inline comment when **any** of these apply:

- **Why / policy** — non-obvious business rule, security trade-off, or product decision.
- **Subtle invariant or business rule** — something that must hold true and isn't enforced by types.
- **Complex logic** that takes more than ~5 seconds to grok from the code alone.
- **Gotcha** — framework quirk (React StrictMode, Next.js cache, Supabase RLS), race condition, ordering dependency.

Style: terse, declarative, em-dashes for joining clauses.

```ts
// 404 for not found OR different user (avoids leaking existence)
if (!result) return apiError('Run not found.', 404, 'not_found')
```

```ts
// Per-user cap is threshold-only: any positive remaining cap can authorize
// one more full request discount, even if that request overdraws the cap.
if (perUserCapRemaining !== null && perUserCapRemaining <= EPSILON) {
    return 0
}
```

```ts
// Dedup — skip events already applied (log only, no per-event spam)
if (event.sequenceId <= lastAppliedSequenceIdRef.current) return
```

```ts
// Preserve failed state if an error was already recorded
if (msgToUpdate.error?.errorType || msgToUpdate.info.status.status === 'failed') { ... }
```

```ts
// Resume tracking — seeded from localStorage cache on mount
const activeStreamIdRef = useRef<string | null>(initialStreamId ?? null)
```

Anti-pattern (do not write):

```ts
// Set the user ID
const userId = user.id

// Loop over discounts
for (const discount of discounts) { ... }

// Return the result
return result
```

---

## 7. NOTE blocks

Use `// NOTE:` for **anything important future-me might miss**. Anti-patterns, framework footguns, "don't do X here", historical context, why-this-isn't-where-you'd-expect.

Format: multi-line `//` comment, starts with `// NOTE:`, immediately before the code it warns about.

```ts
// NOTE: Cache sync is handled by the useEffect on [messages] — NOT here.
// Writing to localStorage inside a state updater is a React anti-pattern
// (StrictMode calls updaters twice, causing stale overwrites).
setMessages((prevMessages) => { ... })
```

Use NOTE liberally for:

- React/Next.js footguns (StrictMode, RSC boundaries, hydration, stale closures).
- Supabase RLS and auth-context gotchas.
- Ordering dependencies (this must run before X).
- "We tried Y, it broke because Z, so we do W."
- Cache invalidation rules.

---

## 8. TODO comments

Uppercase, own line, colon. Optional issue/owner reference.

```ts
// TODO: handle expired refresh tokens here, not just at first request
```

```ts
// TODO(marc): switch to streaming once Supabase ships v3 realtime
```

Never inline mid-sentence, never lowercase, never `FIXME`/`XXX`/`HACK` — use TODO or NOTE.

---

## 9. Improve-as-you-go

When editing a file:

- If surrounding logic is missing comments and is non-trivial, add them while you're there.
- If an existing comment is stale or wrong, fix it.
- If an exported function/type has no JSDoc, add one.
- Don't refactor unrelated code or rename anything — only add/fix comments.
- Don't bulk-comment uncommented files unless the user asks.

---

## 10. Style tics (do these)

- **Em-dash `—`** for joining clauses inside comments: `// Dedup — skip events already applied`. Not `--` and not `:` when a dash would read better.
- **Lowercase verbs to start comments** unless it's a sentence: `// preserve failed state...`, `// resume tracking — ...`. JSDoc summaries can start uppercase.
- **No trailing punctuation** on short inline comments. Full stops on JSDoc sentences only.
- **No box-drawing or ASCII art** other than the `═══` section dividers.
- **No emojis** in source comments. (Console logs are a separate decision.)
- **No author names, no dates, no changelogs** in comments — git history has that.

---

## Quick checklist before committing

- [ ] All exported functions have JSDoc (1 line is fine).
- [ ] All exported types have JSDoc.
- [ ] No `// what the code obviously does` narration.
- [ ] Why-comments wherever a non-obvious decision was made.
- [ ] NOTE blocks on every framework footgun / anti-pattern warning.
- [ ] Numbered steps in multi-phase routes/orchestrators.
- [ ] Section dividers only if the file is large and mixes concerns.
- [ ] TODOs uppercase, own line.
- [ ] Em-dashes, not `--`.
