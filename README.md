# Python Project Template

A starter template for building Python projects with Claude. Designed for people who want to build software but prefer to let Claude handle the coding details.

## Getting Started

1. Copy this folder to your computer
2. Open Claude Code in the folder
3. Describe what you want to build

That's it. Claude reads the instructions in this template and follows a structured workflow automatically.

## What Happens When You Ask Claude to Build Something

You describe what you want:

```
"I want to track my daily expenses. I should be able to add expenses
with a description, amount, and category, and see monthly totals."
```

Claude then follows this workflow automatically:

```
1. CODER: Build
   - Writes the code
   - Writes tests for every feature
   - Runs linting, type checks, and tests
   - Stores any secrets in .env (never in code)

2. REVIEWER: Review (automatic)
   - Checks for bugs and security issues
   - Verifies tests exist and pass
   - Checks secrets use .env properly
   - If problems found → fixes and reviews again (max 3 cycles)

3. Done: Working, tested code
```

### Triggering Workflows Explicitly

You can trigger the workflows manually using slash commands:

| Command | What It Does |
|---------|--------------|
| `/coder [task]` | Build a feature following coding standards |
| `/reviewer` | Review the current code for issues |
| `/commit` | Create a semantic commit with smart staging rules |

Example: `/coder add a login page with email and password`

## What's in This Template

### Your Code

| Folder | Purpose |
|--------|---------|
| `src/myproject/` | Your Python code goes here |
| `tests/` | Tests that verify your code works |

### Instructions for Claude

| Location | What It Does |
|----------|--------------|
| `.claude/agents/CODER.md` | How to implement features properly |
| `.claude/agents/REVIEWER.md` | Checklist for reviewing code quality |
| `.claude/agents/WORKFLOW.md` | The build → review → fix loop |
| `.claude/agents/git-workflow.md` | Git staging rules and secret detection |
| `.claude/skills/coder/` | Slash command for coding |
| `.claude/skills/reviewer/` | Slash command for reviewing |
| `.claude/skills/commit/` | Slash command for commits |

These files guide Claude to write better code. You can edit them to change how Claude works.

### Quality Tools

These run automatically to catch problems:

| Tool | What It Does |
|------|--------------|
| **Ruff** | Finds common mistakes and style issues |
| **Pyright** | Checks that data types are used correctly |
| **pytest** | Runs tests to verify the code works |
| **gitleaks** | Prevents accidentally saving passwords or API keys |
| **pre-commit** | Runs all checks automatically on each commit |

You don't need to run these yourself—Claude handles them.

## Project Structure

```
your-project/
├── src/myproject/       # Your code
├── tests/               # Tests
├── .claude/
│   ├── agents/          # Workflow instructions
│   └── skills/          # Slash commands
├── CLAUDE.md            # Main instructions
├── pyproject.toml       # Python settings
└── .env.example         # Template for secrets
```

You can ask Claude to rename `myproject` to match your project's name.

## Keeping Secrets Safe

If your project needs API keys, passwords, or other secrets:

- Claude stores them in a `.env` file (never saved to git)
- See `.env.example` for the format
- The gitleaks tool warns you if you accidentally try to commit a secret

Just tell Claude what services you're using, and it will handle the configuration.

## Tips for Good Results

**Be specific about behavior.** Instead of "add authentication", try "add login with email and password, reject passwords shorter than 8 characters."

**Describe the why.** "I need to export data to CSV so I can open it in Excel" helps Claude make better choices.

**Build incrementally.** One feature at a time works better than asking for everything at once.

## Requirements

- Python 3.11 or newer
- Claude Code

## License

MIT
