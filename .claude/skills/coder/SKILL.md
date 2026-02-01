---
name: coder
description: Implement a feature or fix following project coding standards. Writes code, tests, runs quality checks, then automatically reviews.
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
argument-hint: [description of what to build]
---

# CODER Workflow

Implement the requested feature: $ARGUMENTS

Follow the instructions in @.claude/agents/CODER.md

After implementation:
1. Run quality checks: `ruff check . && ruff format . && mypy src/ && pytest`
2. Provide an implementation summary
3. **Automatically review**: Follow @.claude/agents/REVIEWER.md to review your code
4. If issues found, fix them and review again (max 3 cycles)
