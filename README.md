# Agent Skills

A collection of custom and community skills for Claude Code and other AI agents.

## Install

### All skills (recommended for a fresh machine)

```bash
npx skills add <github-username>/agent-skills -g --all --full-depth
```

### Custom skills only

```bash
npx skills add <github-username>/agent-skills -g --skill generate-review-context review-implementation blendai-issue-tagging --full-depth
```

### Community skills only

```bash
npx skills add <github-username>/agent-skills -g --skill analytics-tracking content-strategy design-an-interface edit-article emil-design-engineering find-skills frontend-design git-guardrails-claude-code grill-me improve-codebase-architecture marketing-ideas migrate-to-shoehorn next-best-practices next-cache-components obsidian-vault prd-to-issues prd-to-plan remotion-best-practices request-refactor-plan scaffold-exercises setup-pre-commit shadcn supabase-postgres-best-practices tdd triage-issue ubiquitous-language ui-ux-pro-max vercel-composition-patterns web-design-guidelines write-a-prd write-a-skill writing-skills --full-depth
```

## Update

```bash
npx skills update -g
```

## Structure

- `custom/` — skills we authored
- `community/` — skills from other people that we use

## Notes

- Project-specific skills (like `gitnexus-*`) are not stored here. They live in their respective project repos under `.claude/skills/`.
- The `--full-depth` flag is required because skills are nested inside `custom/` and `community/` subdirectories.
# SKILLS
