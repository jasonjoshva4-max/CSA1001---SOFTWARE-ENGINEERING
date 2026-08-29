# EXP-9: Open Source Collaboration using Git Fork and Pull Request Workflow

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 9  
**Platform Under Study:** GitHub & Git CLI

## 1. AIM
To master the **Fork and Pull Request (PR) workflow** on GitHub for open-source contributions.

## 2. STEP-BY-STEP COMMAND WORKFLOW
1. **Fork Repository:** Click **Fork** on GitHub target repo (`original-org/sample-project`).
2. **Clone Forked Repo:** `git clone https://github.com/your-username/sample-project.git` -> `cd sample-project`.
3. **Configure Upstream Remote:**
   - `git remote add upstream https://github.com/original-org/sample-project.git`
   - `git remote -v` (verify `origin` and `upstream`).
4. **Create Feature Branch:** `git checkout -b feature/add-profile`.
5. **Make & Commit Changes:** `git add .` -> `git commit -m "feat: add user profile page"`.
6. **Sync with Upstream:** `git fetch upstream` -> `git rebase upstream/main`.
7. **Push to Fork:** `git push origin feature/add-profile`.
8. **Create PR on GitHub:** Open GitHub -> Click **Compare & pull request** -> Select `base: main` and `head: feature/add-profile` -> Submit PR.

## 3. VERIFICATION
- Remote check (`git remote -v`) shows both `origin` and `upstream`.
- PR appears cleanly on main repository without conflicts.
