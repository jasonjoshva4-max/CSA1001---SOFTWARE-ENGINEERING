# EXP-14: Continuous Deployment (CD) Workflow using GitHub Actions

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 14  
**Tools Used:** GitHub Actions, YAML Workflow Syntax, Docker Hub

## 1. AIM
To create an automated **GitHub Actions Workflow** that triggers on git pushes to the `main` branch, lints code, runs tests, builds a Docker image, and publishes it to Docker Hub.

## 2. LINE-BY-LINE WORKFLOW EXPLANATION FOR EXAMS
- `name:` Human-readable title of the workflow displayed in GitHub Actions UI.
- `on: push: branches: ["main"]`: Event trigger: execution starts automatically whenever code is pushed to `main`.
- `jobs:` Groups together all jobs that run in the workflow.
- `runs-on: ubuntu-latest`: Specifies the virtual machine runner environment provided by GitHub.
- `steps:` Array of sequential tasks executed within a job.
- `uses: actions/checkout@v4`: Pre-built official action that downloads repo code onto the runner.
- `${{ secrets.DOCKER_USERNAME }}`: Securely retrieves encrypted credentials stored in GitHub Repository Secrets.

## 3. CONFIGURING REPOSITORY SECRETS
1. Go to GitHub Repo -> **Settings > Secrets and variables > Actions**.
2. Add `DOCKER_USERNAME` and `DOCKER_PASSWORD`.
3. Push changes to `main` branch to trigger automated pipeline execution.

---
*End of EXP-14*
