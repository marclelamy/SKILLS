---
name: code-commenting
description: Code commenting conventions for TypeScript/React projects. Use when adding comments to new files, reviewing uncommented code, or when user asks to document/comment code. Covers file headers, type annotations, function docs, inline comments, and what NOT to comment.
---

# Code Commenting

Concise, layered commenting that explains *why* and *what role* code plays — never restates what the code already says.

## File-level header

Every new file gets a `/** */` block at the top, **before imports**. Two to four lines max.

**Pattern:**
```ts
/**
 * Short name or role of this file.
 *
 * One or two sentences of context: what it does, where it fits,
 * and any non-obvious constraints or scope limits.
 */
```

**Good — concise, adds context:**
```ts
/**
 * Reducer for node result state transitions.
 *
 * Pure function — takes the current result state and an action, returns the
 * next state. Used by `useWorkflowV2NodeTest` to update result state as
 * stream events arrive during a test run.
 */
```

**Good — flags temporary / MVP scope:**
```ts
/**
 * Creates the default in-memory document for the workflow v2 MVP.
 *
 * Returns a single `llm` node with default config — no persistence yet.
 * This will be replaced by a real load-from-database path in a future slice.
 */
```

**Bad — too verbose, repeats what imports say:**
```ts
/**
 * This file contains the createInitialWorkflowV2Document function.
 * It imports WorkflowV2Document from the types directory and
 * workflowV2LlmNodeDefinition from the definitions directory.
 * It creates a document with nodes and edges arrays...
 */
```

### When to use a longer header

If a file has a catalog of variants (actions, event types, enum values), list them in the header so readers can scan without scrolling:

```ts
/**
 * Reducer for node result state transitions.
 *
 * Actions:
 *   node-start      — Appends a new "running" result entry
 *   node-status     — Updates the latest entry's status
 *   node-sync-parts — Replaces the latest entry's parts array (used for streaming)
 *   node-completed  — Marks the latest entry as completed
 *   node-failed     — Marks the latest entry as failed with an error
 */
```

### `'use client'` files

Place the header **after** the directive, before imports:

```ts
'use client'

/**
 * Single-node test execution hook for workflow v2.
 * ...
 */

import { useCallback } from 'react'
```

---

## Type & schema comments

### Simple / self-documenting — single-line `/** */`

```ts
/** Lifecycle status of a single node execution: pending → running → completed | failed. */
export const workflowV2NodeResultStatusSchema = z.enum([...])
```

```ts
/** A directed edge connecting one node's output handle to another node's input handle. */
export const workflowV2DocumentEdgeSchema = z.object({...})
```

### Complex / non-obvious — multi-line `/** */`

Use when the schema's role isn't clear from its name, or when it has runtime behavior worth calling out:

```ts
/**
 * Resolved inputs the node received at execution time, keyed by target handle.
 * Empty for single-node test runs; populated during multi-node workflow execution.
 */
export const workflowV2InputGroupsSchema = z.record(...)
```

```ts
/**
 * Per-node result state: an append-only results array plus an optional pointer
 * to which result is "active" (defaults to latest when undefined).
 */
export const workflowV2NodeResultStateSchema = z.object({...})
```

### When NOT to comment a type/schema

- If the name fully explains it (e.g. `workflowV2NodeErrorSchema` with `message`, `code` fields)
- Inferred type exports — group them under a single section comment instead:

```ts
/**
 * Inferred types from Zod schemas.
 */
export type WorkflowV2NodeResultStatus = z.infer<typeof workflowV2NodeResultStatusSchema>
export type WorkflowV2NodeError = z.infer<typeof workflowV2NodeErrorSchema>
```

### Never do `@property` lists for types

If the fields are named well, don't restate them:

```ts
// BAD — redundant
/**
 * @property modelId      — The model to use for generation
 * @property prompt        — The user prompt sent to the model
 * @property systemPrompt  — Optional system-level instructions
 * @property temperature   — Sampling temperature
 */
export const configSchema = z.object({
    modelId: z.string().min(1),
    prompt: z.string(),
    ...
})

// GOOD — one-liner is enough
/** User-editable config fields for an `llm` node. */
export const configSchema = z.object({...})
```

---

## Function & helper comments

### Exported functions — single-line `/** */`

```ts
/** Looks up a node definition by type. Throws if the type is not registered. */
export function getWorkflowV2NodeDefinition(nodeType: WorkflowV2NodeType) {...}
```

### Private helpers — single-line `/** */`

```ts
/** Immutably updates the most recent result entry in the state. */
function patchLatestResult(state, updater) {...}
```

```ts
/** Maps result status → badge color variant. */
function getStatusBadgeVariant(status: string | null) {...}
```

```ts
/** Extracts a displayable string from any Part type for the result preview. */
function formatResultPart(part: Part) {...}
```

### Small utility constructors

```ts
/** Helper to build a structured node error from message + optional metadata. */
function createNodeError(message: string, errorType?: string, code?: number) {...}
```

---

## Inline comments (`//`)

Use sparingly — only when the *why* or *what happens next* isn't obvious from reading the code.

### Good uses

**Before a key callback or hook wiring:**
```ts
// Dispatches a result action for a node and keeps the ref in sync with React state.
const applyNodeAction = useCallback(...)

// Wires into the shared SSE generation endpoint and maps stream events to result actions.
const { makeRequest, isStreaming } = useAIRequest(...)

// Validates config, builds a RequestV2, and kicks off the stream for a single node.
const runNodeTest = useCallback(async (nodeId: string) => {...})
```

**Before a derived computation:**
```ts
// Derive model dropdown options from the global models list; fall back to guest default.
const textModelOptions = useMemo(...)

// Map document nodes → React Flow nodes, attaching result state and handlers as data.
const nodes = useMemo(...)
```

### Bad uses — don't comment the obvious

```ts
// BAD
// Set the state
setState(newValue)

// Check if node exists
if (!node) return

// Return the results
return { nodeResultStateById, runNodeTest }
```

---

## Constants & module-level values

Only comment if the purpose isn't obvious:

```ts
// No comment needed — name says it all
const EMPTY_NODE_RESULT_STATE: WorkflowV2NodeResultState = { results: [] }

// Comment needed — explains a non-obvious registration
/** Register custom node types — React Flow uses this to resolve `type: 'workflowV2Node'`. */
const nodeTypes: NodeTypes = { workflowV2Node: WorkflowV2Node }
```

---

## React component files

1. **File header** — what the component renders, any scope limits
2. **Helper functions above the component** — one-line `/** */` each
3. **Key `useMemo` / `useCallback` blocks** — inline `//` comment
4. **JSX** — no comments unless there's a non-obvious workaround

```ts
/**
 * Workflow v2 node component — rendered by React Flow for each node on the canvas.
 *
 * Currently hardcoded for the `llm` node type. Will be generalized when
 * additional node types are added.
 */

/** Maps result status → badge color variant. */
function getStatusBadgeVariant(status: string | null) {...}

/** Joins all parts of the active result into a single string for display. */
function getResultText(resultState: WorkflowV2NodeResultState) {...}

export function WorkflowV2Node({ data }: NodeProps<WorkflowV2FlowNode>) {...}
```

---

## Summary checklist

| Layer | Format | When |
|---|---|---|
| File header | `/** */` multi-line | Every new file |
| Schema / type | `/** */` single or multi | When name alone isn't enough |
| Inferred type group | `/** Inferred types... */` | Group of `z.infer` exports |
| Exported function | `/** */` single-line | Always |
| Private helper | `/** */` single-line | When purpose isn't obvious from name |
| Inline callback/memo | `//` single-line | Before key wiring points |
| Constants | `/** */` single-line | Only if non-obvious |
| JSX | None | Unless there's a workaround |

**Golden rule:** If removing the comment would make a reader pause and re-read the code to understand its role, keep the comment. If the code already says the same thing, delete it.
