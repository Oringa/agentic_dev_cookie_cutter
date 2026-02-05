---
name: commit
description: Creates semantic commits following project conventions with smart staging rules.
---

# Commit Creation

## Quick Start

```bash
/commit
/commit "custom message"
```

## Workflow

Follow @.claude/agents/git-workflow.md for staging, then:

1. **Review changes** - `git status`, `git diff`, `git diff --staged`
2. **Stage intelligently** - Use staging rules from git-workflow
3. **Generate message** - Review `git log --oneline -10` for style
4. **Create commit** - Use HEREDOC format

## Commit Message Format

```
type(scope): brief description

Detailed explanation of WHY (not what)
- Key change 1
- Key change 2
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Guidelines:**
- Focus on WHY, not WHAT (what is in the diff)
- Match existing commit style in the repo

## Create Commit

```bash
git commit -m "$(cat <<'EOF'
type(scope): brief description

Detailed explanation
EOF
)"
```

Verify: `git log -1 --format='%B'`
