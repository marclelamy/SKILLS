---
name: git-commit-markdown
description: Write git add, commit, and push commands as a copyable Markdown code block. Does NOT execute any commands. Use when user wants to commit, push, save changes, or says "commit this", "push this", "write the git commands", or "prepare a commit".
---

# Git Commit Markdown

Write git commands as a Markdown code block for the user to copy, paste, and run themselves. **Never execute git commands.**

## Process

1. Track which files you created, modified, or deleted during this conversation
2. Write a short commit message based on what was done
3. Output the commands as a single fenced code block

## Rules

- **No git commands**: Never run `git status`, `git diff`, or any git command. Multiple agents may be working in parallel, so git state is unreliable. Only reference files you personally touched in this conversation
- **git add**: List only the specific files you modified, created, or deleted. Never use `git add .` or `git add -A`
- **git commit**: Message must be one line. Use a second line only if absolutely necessary. No conventional-commit prefixes unless the repo already uses them
- **git push**: Include `git push` (or `git push -u origin <branch>` if the branch has no upstream)
- **Output format**: One fenced ```bash block containing all commands, ready to copy and run
- **Do not execute**: Only write the commands. Never run them

## Output Example

```bash
git add src/components/Button.tsx src/utils/helpers.ts
git commit -m "Fix button click handler and update helper imports"
git push
```
