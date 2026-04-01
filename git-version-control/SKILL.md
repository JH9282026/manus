---
name: git-version-control
description: "Master Git version control for collaborative software development using branching strategies, merge workflows, and best practices. Implement GitFlow, GitHub Flow, trunk-based development, and feature branching. Use for: tracking code changes and history, collaborating with teams through pull requests, managing releases and hotfixes, resolving merge conflicts, maintaining clean commit history with rebasing, implementing CI/CD pipelines, code review workflows, and ensuring code quality through version control best practices."
---

# Git Version Control

Master distributed version control with Git for effective collaboration and code management.

## Overview

Git is a distributed version control system that tracks changes in source code during software development. It enables multiple developers to work together, maintains complete history, supports branching and merging, and provides powerful tools for collaboration and code review.

## Core Concepts

### Repository Structure

```bash
.git/                 # Git metadata and object database
  HEAD               # Points to current branch
  config             # Repository configuration
  objects/           # Git object database
  refs/              # References (branches, tags)
    heads/           # Local branches
    remotes/         # Remote branches
    tags/            # Tags
```

### The Three States

1. **Working Directory**: Modified files not yet staged
2. **Staging Area (Index)**: Files marked for next commit
3. **Repository**: Committed snapshots

```bash
# Working Directory → Staging Area
git add file.txt

# Staging Area → Repository
git commit -m "Add file"

# Check status
git status
```

## Essential Commands

### Repository Initialization

```bash
# Create new repository
git init

# Clone existing repository
git clone https://github.com/user/repo.git

# Clone with specific branch
git clone -b develop https://github.com/user/repo.git

# Shallow clone (faster, less history)
git clone --depth 1 https://github.com/user/repo.git
```

### Basic Workflow

```bash
# Check status
git status

# Add files to staging
git add file.txt
git add .                    # Add all changes
git add -p                   # Interactive staging

# Commit changes
git commit -m "Commit message"
git commit -am "Add and commit"  # Stage and commit tracked files

# View history
git log
git log --oneline --graph --all
git log --author="John"
git log --since="2 weeks ago"

# Show changes
git diff                     # Working directory vs staging
git diff --staged            # Staging vs last commit
git diff HEAD~1 HEAD         # Between commits
```

## Branching Strategies

### GitFlow

Comprehensive branching model for projects with scheduled releases.

```bash
# Main branches
main (production-ready code)
develop (integration branch)

# Supporting branches
feature/*    # New features
release/*    # Release preparation
hotfix/*     # Production fixes

# Feature branch workflow
git checkout develop
git checkout -b feature/user-auth
# ... work on feature ...
git checkout develop
git merge --no-ff feature/user-auth
git branch -d feature/user-auth

# Release branch
git checkout -b release/1.0.0 develop
# ... bug fixes, version bumps ...
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0
git checkout develop
git merge --no-ff release/1.0.0
git branch -d release/1.0.0

# Hotfix branch
git checkout -b hotfix/critical-bug main
# ... fix bug ...
git checkout main
git merge --no-ff hotfix/critical-bug
git tag -a v1.0.1
git checkout develop
git merge --no-ff hotfix/critical-bug
git branch -d hotfix/critical-bug
```

### GitHub Flow

Simpler workflow for continuous delivery.

```bash
# 1. Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/new-feature

# 2. Make changes and commit
git add .
git commit -m "Add new feature"

# 3. Push and create pull request
git push origin feature/new-feature

# 4. After review, merge to main
git checkout main
git merge feature/new-feature
git push origin main

# 5. Delete feature branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

### Trunk-Based Development

All developers commit to single main branch.

```bash
# Short-lived feature branches (< 1 day)
git checkout main
git pull origin main
git checkout -b feature/quick-fix

# ... make changes ...
git add .
git commit -m "Quick fix"

# Merge back quickly
git checkout main
git pull origin main
git merge feature/quick-fix
git push origin main
git branch -d feature/quick-fix
```

## Advanced Operations

### Rebasing

```bash
# Rebase current branch onto main
git checkout feature-branch
git rebase main

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Options in interactive rebase:
# pick   - use commit
# reword - use commit, edit message
# edit   - use commit, stop for amending
# squash - combine with previous commit
# fixup  - like squash, discard message
# drop   - remove commit

# Abort rebase
git rebase --abort

# Continue after resolving conflicts
git rebase --continue
```

### Cherry-Pick

```bash
# Apply specific commit to current branch
git cherry-pick abc123

# Cherry-pick multiple commits
git cherry-pick abc123 def456

# Cherry-pick without committing
git cherry-pick -n abc123
```

### Stashing

```bash
# Save current changes
git stash
git stash save "Work in progress"

# List stashes
git stash list

# Apply stash
git stash apply
git stash apply stash@{2}

# Apply and remove stash
git stash pop

# Create branch from stash
git stash branch new-branch stash@{0}

# Clear all stashes
git stash clear
```

### Reflog

```bash
# View reference log
git reflog

# Recover lost commits
git reflog
git checkout abc123

# Undo reset
git reset --hard HEAD@{1}
```

## Collaboration Workflows

### Pull Requests

```bash
# 1. Fork repository (on GitHub)

# 2. Clone your fork
git clone https://github.com/your-username/repo.git

# 3. Add upstream remote
git remote add upstream https://github.com/original-owner/repo.git

# 4. Create feature branch
git checkout -b feature/new-feature

# 5. Make changes and commit
git add .
git commit -m "Add new feature"

# 6. Push to your fork
git push origin feature/new-feature

# 7. Create pull request on GitHub

# 8. Keep branch updated
git fetch upstream
git rebase upstream/main

# 9. After merge, sync fork
git checkout main
git pull upstream main
git push origin main
```

### Code Review

```bash
# Fetch PR for local review
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Review changes
git diff main...pr-123

# Test locally
npm test

# Add review comments (on GitHub)
```

## Merge Strategies

### Fast-Forward Merge

```bash
# Default when possible
git merge feature-branch
```

### No-Fast-Forward Merge

```bash
# Always create merge commit
git merge --no-ff feature-branch
```

### Squash Merge

```bash
# Combine all commits into one
git merge --squash feature-branch
git commit -m "Feature: description"
```

### Rebase and Merge

```bash
# Rebase before merging
git checkout feature-branch
git rebase main
git checkout main
git merge feature-branch
```

## Conflict Resolution

```bash
# When conflicts occur
git merge feature-branch
# CONFLICT (content): Merge conflict in file.txt

# View conflicts
git status

# Edit conflicted files
# <<<<<<< HEAD
# Current branch content
# =======
# Incoming branch content
# >>>>>>> feature-branch

# After resolving
git add file.txt
git commit

# Abort merge
git merge --abort
```

## Best Practices

### Commit Messages

```bash
# Good commit message format
<type>(<scope>): <subject>

<body>

<footer>

# Types: feat, fix, docs, style, refactor, test, chore

# Example
feat(auth): add JWT authentication

Implement JWT-based authentication system with
refresh tokens and role-based access control.

Closes #123
```

### Branch Naming

```bash
# Convention
<type>/<description>

# Examples
feature/user-authentication
bugfix/login-error
hotfix/security-patch
release/v1.2.0
```

### Atomic Commits

```bash
# ❌ Bad - multiple unrelated changes
git commit -am "Fix bug, add feature, update docs"

# ✅ Good - single logical change
git commit -m "fix: resolve login timeout issue"
git commit -m "feat: add password reset functionality"
git commit -m "docs: update API documentation"
```

## Git Hooks

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/sh
npm run lint
npm test
```

### Commit-msg Hook

```bash
# .git/hooks/commit-msg
#!/bin/sh
commit_msg=$(cat $1)
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore):"; then
  echo "Invalid commit message format"
  exit 1
fi
```

### Using Husky

```bash
npm install --save-dev husky
npx husky install

# Add pre-commit hook
npx husky add .husky/pre-commit "npm test"
```

## Advanced Git

### Bisect (Find Bug Introduction)

```bash
# Start bisect
git bisect start
git bisect bad                 # Current commit is bad
git bisect good abc123         # Known good commit

# Git checks out middle commit
# Test and mark
git bisect good  # or git bisect bad

# Repeat until bug found
# Reset
git bisect reset
```

### Submodules

```bash
# Add submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Clone repository with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Update submodules
git submodule update --remote
```

## Using the Reference Files

### When to Read Each Reference

**`/references/workflow-strategies.md`** — Read when choosing branching strategy, implementing GitFlow/GitHub Flow, or establishing team workflows.

**`/references/advanced-commands.md`** — Read when performing complex operations like interactive rebase, cherry-pick, or bisect.

**`/references/collaboration-guide.md`** — Read when setting up pull request workflows, code review processes, or managing forks.

**`/references/troubleshooting.md`** — Read when resolving merge conflicts, recovering lost commits, or fixing repository issues.

## References

- [Advanced Git Techniques](references/advanced-git-techniques.md)
- [Branching Strategies](references/branching-strategies.md)
- [Collaboration Best Practices](references/collaboration-best-practices.md)
- [Git Fundamentals Workflows](references/git-fundamentals-workflows.md)
- [Troubleshooting Recovery](references/troubleshooting-recovery.md)
