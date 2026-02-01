---
name: reviewer
description: Review code for quality, security, and correctness. Checks for bugs, security issues, and test coverage.
allowed-tools: Read, Grep, Glob, Bash
argument-hint: [optional: specific files to review]
---

# REVIEWER Workflow

Review the current code changes.

Follow the instructions in @.claude/agents/REVIEWER.md

Output format:
- Status: APPROVED or CHANGES_REQUESTED
- Issues found (Critical / Major / Minor)
- Required changes if any
