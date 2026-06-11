# Agent Skills

A collection of custom and community skills for Claude Code and other AI agents.

## Install

### All skills (recommended for a fresh machine)

```bash
npx skills add marclelamy/SKILLS --all --full-depth
```

### Custom skills only

```bash
npx skills add marclelamy/SKILLS -g --skill generate-review-context review-implementation blendai-issue-tagging --full-depth
```

### Community skills only

```bash
npx skills add marclelamy/SKILLS -g --skill analytics-tracking content-strategy design-an-interface edit-article emil-design-engineering find-skills frontend-design git-guardrails-claude-code grill-me improve-codebase-architecture marketing-ideas migrate-to-shoehorn next-best-practices next-cache-components obsidian-vault prd-to-issues prd-to-plan remotion-best-practices request-refactor-plan scaffold-exercises setup-pre-commit shadcn supabase-postgres-best-practices tdd triage-issue ubiquitous-language ui-ux-pro-max vercel-composition-patterns web-design-guidelines write-a-prd write-a-skill writing-skills brutalist-skill minimalist-skill output-skill redesign-skill soft-skill stitch-skill taste-skill --full-depth
```

## Update

```bash
npx skills update -g
```

## Sync vendored upstream skills (diff / pull)

Some folders under `community/` are copies of third-party repos. To **compare only what you already have** against GitHub and optionally overwrite local copies, use the manifest-driven script:

```bash
./scripts/sync-upstream-skills.sh --list
./scripts/sync-upstream-skills.sh                    # dry-run (rsync -n, no writes)
./scripts/sync-upstream-skills.sh --source matt-pocock
./scripts/sync-upstream-skills.sh --apply            # actually pull changes
```

Configuration lives in [`scripts/upstream-sources.json`](scripts/upstream-sources.json). Each entry sets `github` (`owner/repo`), `branch`, `local_dir` (where your copy lives), and `upstream_skills_path` (use `""` when each skill is a folder at the repo root—e.g. [mattpocock/skills](https://github.com/mattpocock/skills)—or `skills` when skills live under that subfolder—e.g. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)). The script only syncs **immediate subdirectories** of `local_dir` that contain a `SKILL.md`, plus any `extra_files` you list.

**Different layouts:** GitHub does not expose one API for “diff arbitrary folder trees” across repos. The practical pattern is a **shallow clone** of upstream, then **directory sync** (`rsync`) from the path you configure. The manifest is the adapter (flat root vs `skills/` vs other monorepos). **Anthropic**-style trees under `community/anthropic/` may need a custom `upstream_skills_path` per skill or manual sync until you map each folder to a stable upstream path ([claude-plugins-official](https://github.com/anthropics/claude-plugins-official) is a different shape than a flat skills repo).

`--apply` uses `rsync --delete`. Commit or branch first if you need to keep local edits.

## Structure

- `custom/` — skills we authored
- `community/` — skills from other people that we use
- `community/matt-pocock/` — [mattpocock/skills](https://github.com/mattpocock/skills) (flat layout on GitHub)
- `community/leonxlnx/` — [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (`skills/*` on GitHub; includes `llms.txt` at the creator folder root)
- `community/anthropic/` — Anthropic-related vendored skills (sync rules TBD; see [claude-plugins-official](https://github.com/anthropics/claude-plugins-official))

## Notes

- Project-specific skills (like `gitnexus-*`) are not stored here. They live in their respective project repos under `.claude/skills/`.
- The `--full-depth` flag is required because skills are nested inside `custom/` and `community/` subdirectories.