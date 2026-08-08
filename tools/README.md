# Blewbury Beer Festival Developer Tools

Developer utilities are exposed through one CLI:

```bash
python3 tools/cli.py --help
```

Available commands:

```text
docs
import-wordpress
optimise-images
release
audit
refactor-homepage
```

Examples:

```bash
python3 tools/cli.py docs
python3 tools/cli.py docs --check
python3 tools/cli.py audit
python3 tools/cli.py release
python3 tools/cli.py refactor-homepage
python3 tools/cli.py refactor-homepage --check
```

## Design principle

Use Python tooling for multi-file generation and transformations.

Keep shell commands small and use them mainly for Git, package management and build operations.

Avoid large shell heredoc scripts.
