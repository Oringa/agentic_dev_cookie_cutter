---
name: git-workflow
description: Git staging, branch verification, and change review. Shared logic for /commit skill.
tools: Read, Bash, Glob, Grep
---

## Review Changes

Run in parallel:
```bash
git status
git diff              # unstaged
git diff --staged     # staged
```

Identify: staged files, unstaged tracked files, untracked files.

## Staging Rules

- NEVER use `git add --all` or `git add .`
- Use `git add -u` to stage tracked files only
- For untracked files: ASK user for each file whether to stage
- Skip files that likely contain secrets

## Secret Detection

Warn and skip staging for files matching:
- `.env*`, `*.env`
- `credentials*`, `secrets*`
- `*_key*`, `*_token*`, `*_secret*`

If user explicitly requests to stage secrets, warn them clearly.

## Branch Verification

1. Confirm on feature branch (not main/master)
2. Branch naming: `feature/`, `fix/`, `chore/` prefixes
3. If on main, ask user to create/switch to feature branch
