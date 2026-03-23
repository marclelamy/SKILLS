---
name: blendai-issue-tagging
description: Use when creating issues, tasks, or bugs in Notion for BlendAI. Assigns Domain tags (what product areas) and Layer tags (where in stack).
---

# BlendAI Issue Tagging

## Overview

Every issue gets **two types of tags** in Notion:
1. **Domain** - Which product area(s) (Chat, Billing, Workflow Builder, etc.)
2. **Layer** - Where in the technical stack (UI/UX, API/Backend, Database, etc.)

**Multiple tags allowed** - Assign all that apply based on task scope.

## Quick Reference

### Domains (25)

| Domain | Scope |
|--------|-------|
| **Chat** | Prompt area, messages, comparison mode, voice chat, chat UX |
| **Memory** | Memory extraction, follow-ups, saved context, recall |
| **Personalization** | User profile, preferences, custom behavior, adaptive AI |
| **Projects** | Project-scoped workspaces, attached context |
| **Knowledge Base** | Stored files, indexed content, persistent retrieval |
| **AI Models** | Model catalog, providers, model pricing, capabilities |
| **Routing** | Auto model selection, dispatchers, tool selection logic |
| **Search** | Web search, deep research, retrieval, query generation |
| **Workflow Builder** | Canvas, nodes, handles, templates, editor |
| **Workflow Execution** | Runs, queues, resumable jobs, streaming state |
| **Workflow Sharing** | Publish, marketplace, fork, revenue sharing |
| **Smart Notes** | Bookmark product, note UI, note retrieval |
| **Capture** | Share sheet, WhatsApp, OCR, transcription, ingestion |
| **Billing** | Credits, charges, Stripe mechanics |
| **Pricing** | Plans, tiers, feature gating, pricing page logic |
| **Monetization** | Discounts, affiliate, payouts, profit-share |
| **Accounts** | User lifecycle, onboarding, roles |
| **Auth** | Login, signup, permissions, access control |
| **Settings** | User preferences, app configuration |
| **Support** | Support chat, support tickets, founder messaging |
| **Feedback** | Feature requests, voting, changelog asks |
| **Analytics** | Dashboards, metrics, reporting |
| **Internal Ops** | Admin tools, maintenance surfaces, internal workflows |
| **Growth Site** | Landing page, marketing site, conversion pages |
| **Content** | Blog, outreach, SEO pages, marketing content ops |

### Layers (5)

| Layer | Scope |
|-------|-------|
| **UI/UX** | Components, styling, interactions, accessibility, responsive design |
| **API/Backend** | Endpoints, business logic, validation, middleware, server code |
| **Database** | Schema, migrations, queries, indexes, data modeling |
| **Integrations** | External APIs, webhooks, third-party services, OAuth |
| **Reliability** | Performance, caching, error handling, monitoring, scaling |

## Tagging Rules

1. **Assign all relevant Domains** - Tag every product area the issue touches
2. **Assign all relevant Layers** - Tag every technical layer involved
3. **Use Notion tags column** - Add as tags (e.g., `Chat`, `Memory`, `UI/UX`, `Database`)

## Examples

| Issue | Domains | Layers |
|-------|---------|--------|
| "Chat input loses focus on mobile" | Chat | UI/UX |
| "Chat memory not persisting across sessions" | Chat, Memory | API/Backend, Database |
| "Stripe webhook not updating credits" | Billing | Integrations, API/Backend |
| "Full-stack workflow marketplace MVP" | Workflow Sharing, Monetization | UI/UX, API/Backend, Database |
| "Model selection dropdown slow + API timeout" | AI Models, Routing | UI/UX, API/Backend, Reliability |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Tagging only one Domain when multiple apply | Read scope carefully - tag all affected areas |
| Confusing Routing vs AI Models | Routing = selection logic; AI Models = catalog/pricing |
| Confusing Billing vs Pricing vs Monetization | Billing = Stripe/charges; Pricing = tiers/gates; Monetization = affiliate/payouts |
| Missing Reliability on perf issues | Any performance/scaling work needs Reliability tag |
