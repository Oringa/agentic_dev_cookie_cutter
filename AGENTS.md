# AI Agent Instructions

> This file provides instructions for AI coding assistants working on this project.

## IMPORTANT: Default Workflow

**For ANY request to build, implement, or fix something, you MUST:**

1. **Follow `.claude/agents/CODER.md`** - Read and follow these instructions
2. **Write tests** - Every feature needs tests in `tests/`
3. **Run quality checks** - `ruff check . && ruff format . && pyright src/ && pytest`
4. **Self-review** - Follow `.claude/agents/REVIEWER.md` to review your own code
5. **Fix issues** - If review finds problems, fix them and review again (max 3 cycles)

Do not skip these steps. This workflow ensures quality code.

---

## Project Overview

This is a Python project. The source folder is `src/myproject` - rename it if the user requests a specific project name.

## Quick Start

```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
```

## Core Commands

| Task | Command |
|------|---------|
| Install dependencies | `pip install -e ".[dev]"` |
| Run linter | `ruff check .` |
| Auto-fix lint issues | `ruff check . --fix` |
| Run formatter | `ruff format .` |
| Type check | `pyright src` |
| Run tests | `pytest` |
| Run all checks | `pre-commit run --all-files` |

## Project Structure

```
myproject/
├── .claude/
│   ├── agents/           # Agent instructions
│   │   ├── CODER.md      # Coding workflow
│   │   ├── REVIEWER.md   # Review workflow
│   │   ├── WORKFLOW.md   # Full workflow loop
│   │   └── git-workflow.md # Git staging and secret detection
│   └── skills/           # Slash commands
│       ├── coder/        # /coder command
│       ├── reviewer/     # /reviewer command
│       └── commit/       # /commit command
├── src/
│   └── myproject/        # Source code (rename this)
│       └── __init__.py
├── tests/                # Test files
├── CLAUDE.md             # Symlink to AGENTS.md
├── pyproject.toml        # Python configuration
├── .pre-commit-config.yaml
└── README.md
```

## Code Style Guidelines

### General Principles
1. **Readability over cleverness** - Write code that's easy to understand
2. **Single responsibility** - Functions/classes should do one thing well
3. **Explicit over implicit** - Be clear about types, return values, side effects
4. **Test what matters** - Focus on behavior, not implementation details

### Python Style
- Follow PEP 8 (enforced by Ruff)
- Use type hints for all function signatures
- Docstrings for public functions/classes (Google style)
- Maximum line length: 88 characters
- Use `pathlib.Path` over `os.path`
- Prefer f-strings over `.format()` or `%`

```python
# Example
def calculate_total(items: list[Item], tax_rate: float = 0.1) -> Decimal:
    """Calculate total price including tax.

    Args:
        items: List of items to calculate.
        tax_rate: Tax rate as decimal (default: 10%).

    Returns:
        Total price including tax.
    """
    subtotal = sum(item.price for item in items)
    return subtotal * (1 + Decimal(str(tax_rate)))
```

## Testing

### Test Organization
- Mirror the `src/` structure in `tests/`
- Name test files with `test_` prefix
- Use descriptive test names that explain the expected behavior

### What to Test
- Public API of modules
- Edge cases and error conditions
- **Do not test** implementation details or private methods

```python
def test_calculate_total_with_empty_list():
    """Empty list should return zero."""
    assert calculate_total([]) == Decimal("0")

def test_calculate_total_applies_tax():
    """Tax should be applied to subtotal."""
    items = [Item(price=Decimal("100"))]
    assert calculate_total(items, tax_rate=0.2) == Decimal("120")
```

## Git Workflow

### Branch Naming
- `feature/` - New features
- `fix/` - Bug fixes
- `refactor/` - Code refactoring

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat(auth): add JWT token refresh endpoint
fix(api): handle null response from external service
```

## Agent Workflow

This project uses a CODER → REVIEWER workflow:

1. **CODER** (`.claude/agents/CODER.md`) - Implements features and fixes bugs
2. **REVIEWER** (`.claude/agents/REVIEWER.md`) - Reviews code for quality and security
3. **WORKFLOW** (`.claude/agents/WORKFLOW.md`) - Defines the iteration loop

### Slash Commands

| Command | What It Does |
|---------|--------------|
| `/coder [task]` | Build a feature following coding standards |
| `/reviewer` | Review the current code for issues |
| `/commit` | Create a semantic commit with smart staging |

## Secrets and Configuration

Store secrets in `.env` files, never in code.

```bash
# .env (never committed - in .gitignore)
DATABASE_URL=postgres://user:pass@localhost/db
API_KEY=sk-1234567890
```

```python
# In code - read from environment
import os

api_key = os.environ["API_KEY"]
# or with a default
debug = os.environ.get("DEBUG", "false") == "true"
```

Create `.env.example` with placeholder values to document required variables:

```bash
# .env.example (committed - shows what's needed)
DATABASE_URL=postgres://user:pass@localhost/db
API_KEY=your-api-key-here
```

## Boundaries

### Always Do
- Run lint and tests before committing
- Update tests when changing functionality
- Use the existing code patterns and conventions

### Ask First
- Adding new dependencies
- Changing public APIs
- Architectural changes

### Never Do
- Commit secrets, API keys, or credentials
- Disable security checks or linting rules
- Push directly to main branch
