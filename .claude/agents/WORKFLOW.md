# Agent Loop Workflow

This document describes the iterative workflow between CODER and REVIEWER agents for implementing and reviewing code changes.

## Overview

The agent loop creates a feedback cycle that improves code quality through structured review. Code is implemented by the CODER agent and reviewed by the REVIEWER agent until it meets quality standards.

## Workflow Diagram

```
┌─────────────────┐
│     START       │
│  (Issue/Task)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     CODER       │
│   Implement     │
│   Solution      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Quality Gates  │
│  (Lint/Test)    │
└────────┬────────┘
         │
    Pass │ Fail ──► Fix & Retry
         │
         ▼
┌─────────────────┐     CHANGES_REQUESTED
│    REVIEWER     │◄─────────────────────┐
│    Review       │                      │
│    Code         │                      │
└────────┬────────┘                      │
         │                               │
         ▼                               │
    ┌────────────┐                       │
    │  Decision  │                       │
    └─────┬──────┘                       │
          │                              │
    APPROVED                             │
          │              ┌───────────────┴───────────────┐
          │              │           CODER               │
          │              │      Address Feedback         │
          │              └───────────────────────────────┘
          ▼
┌─────────────────┐
│      DONE       │
│   Complete!     │
└─────────────────┘
```

## Step-by-Step Process

### Phase 1: Task Assignment

1. **Human** describes a task or feature
2. Task is assigned to **CODER** agent
3. CODER reads task requirements

### Phase 2: Implementation (CODER)

1. CODER reads `.claude/agents/CODER.md` for instructions
2. CODER explores codebase to understand context
3. CODER plans the implementation approach
4. CODER implements the solution:
   - Writes/modifies code
   - Adds/updates tests
5. CODER runs quality gates:
   ```bash
   ruff check .
   ruff format --check .
   mypy src/
   pytest
   ```
6. CODER provides implementation summary
7. CODER signals: **"Ready for Review"**

### Phase 3: Review (REVIEWER)

1. REVIEWER reads `.claude/agents/REVIEWER.md` for instructions
2. REVIEWER examines all changed files
3. REVIEWER runs quality checks independently
4. REVIEWER applies review checklist:
   - Code Quality
   - Security
   - Testing
   - Performance
5. REVIEWER outputs review in standard format:
   - **APPROVED** → Done
   - **CHANGES_REQUESTED** → Return to CODER

### Phase 4: Iteration Loop

When changes are requested:

1. REVIEWER provides specific, actionable feedback
2. CODER reads feedback carefully
3. CODER addresses each issue:
   - Critical issues: Must fix
   - Major issues: Should fix
   - Minor issues: Fix or note for later
4. CODER re-runs quality gates
5. CODER provides updated summary
6. CODER signals: **"Ready for Re-review"**
7. REVIEWER reviews again (go to Phase 3)

### Phase 5: Completion

When APPROVED:

1. Changes are committed
2. Task is complete

## Commands Reference

### CODER Commands
```bash
# Setup
pip install -e ".[dev]"

# Development cycle
ruff check .              # Lint
ruff format .             # Format
mypy src/                 # Type check
pytest                    # Test
pre-commit run --all-files  # All checks

# Git workflow
git checkout -b feature/task-name
git add <files>
git commit -m "feat: description"
```

### REVIEWER Commands
```bash
# View changes
git diff main...HEAD
git diff main...HEAD --name-only

# Run quality checks
ruff check .
mypy src/
pytest -v

# Check specific file
git show HEAD:path/to/file.py
```

## Iteration Limits

To prevent infinite loops:

| Cycle | Action |
|-------|--------|
| 1 | Normal review and feedback |
| 2 | Focus on remaining critical/major issues |
| 3 | Final review - must resolve or escalate |
| 4+ | **Escalate to human** |

### Escalation Triggers
- 3 review cycles without approval
- Security vulnerability disagreement
- Architectural concerns
- Scope creep detected

## Communication Format

### CODER → REVIEWER Handoff
```markdown
## Ready for Review

**Changes**: [brief summary]

Files Changed:
- `file1.py` - [what changed]
- `file2.py` - [what changed]

Tests:
- Added: `test_feature.py`
- All passing: YES

Notes:
- [Any context for reviewer]
```

### REVIEWER → CODER Feedback
```markdown
## Review: CHANGES_REQUESTED

### Required Changes
1. [ ] [Specific change with file:line reference]
2. [ ] [Specific change with file:line reference]

### Details
[Issue explanation and fix suggestions]
```

### CODER → REVIEWER (After Fixes)
```markdown
## Ready for Re-review

**Addressed**:
1. ✅ [Issue 1] - Fixed in [file:line]
2. ✅ [Issue 2] - Fixed in [file:line]

**Notes**:
- [Any context about the fixes]
```

## Quality Gates

These must pass before REVIEWER begins review:

| Gate | Command | Blocking |
|------|---------|----------|
| Lint | `ruff check .` | Yes |
| Format | `ruff format --check .` | Yes |
| Types | `mypy src/` | Yes |
| Tests | `pytest` | Yes |
| Secrets | `gitleaks detect` | Yes |

## Best Practices

### For CODER
1. Run all quality gates before requesting review
2. Provide clear summaries
3. Self-review changes before handoff
4. Address all critical issues promptly
5. Ask for clarification if feedback is unclear

### For REVIEWER
1. Be specific with feedback (file:line references)
2. Explain why something is an issue
3. Suggest fixes, don't just point out problems
4. Acknowledge good work
5. Prioritize feedback (critical > major > minor)

### For Both
1. Keep changes focused and small when possible
2. Communicate clearly
3. Follow the iteration limits
4. Escalate when stuck
