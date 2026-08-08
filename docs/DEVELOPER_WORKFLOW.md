# Developer Workflow

## Principle

Prefer repeatable tooling over manual file editing.

## Conventions

Use:

- Git for version control
- Python for multi-file generation or transformation
- small shell commands for Git and build operations
- one logical change per commit

Avoid:

- large heredoc shell scripts
- manual repetitive edits
- untracked one-off transformations

## Standard Change Flow

1. Check repository status.
2. Run or create a repeatable tool.
3. Review the diff.
4. Build the site.
5. Commit one logical change.

## Tooling

Project utilities live in `tools/`.

Scripts should be safe to re-run, create missing directories, overwrite only files they own, print what they changed, and fail clearly if something unexpected happens.
