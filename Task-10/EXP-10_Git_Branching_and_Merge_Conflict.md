# EXP-10: Git Branching Strategies and Resolving Merge Conflicts

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 10  
**Tool Used:** Git CLI

## 1. AIM
To demonstrate Git branching techniques, trigger a **merge conflict** between two parallel branches modifying the same file lines, and resolve the conflict manually.

## 2. STEP-BY-STEP EXPERIMENTAL STEPS
```bash
# 1. Initialize Repo
mkdir git-conflict-demo && cd git-conflict-demo && git init
Set-Content -Path "app.txt" -Value "Line 1: System Init`nLine 2: Default Config"
git add app.txt && git commit -m "Initial commit"

# 2. Branch feature-A
git checkout -b feature-A
Set-Content -Path "app.txt" -Value "Line 1: System Init`nLine 2: Config by Feature A (Auth added)"
git add app.txt && git commit -m "feat: Auth in Feature A"

# 3. Main branch modification
git checkout main
Set-Content -Path "app.txt" -Value "Line 1: System Init`nLine 2: Config by Main (OAuth2 added)"
git add app.txt && git commit -m "feat: OAuth2 in Main"

# 4. Trigger Conflict
git merge feature-A
```

## 3. CONFLICT RESOLUTION
1. Open `app.txt` with markers:
   ```text
   <<<<<<< HEAD
   Line 2: Config by Main (OAuth2 added)
   =======
   Line 2: Config by Feature A (Auth added)
   >>>>>>> feature-A
   ```
2. Edit to resolve: `Line 2: Config updated (Auth + OAuth2 added)`.
3. Finalize: `git add app.txt` -> `git commit -m "fix: resolve conflict between main and feature-A"`.
4. Verify tree: `git log --graph --oneline --all`.
