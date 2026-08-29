# EXP-13: Continuous Integration & Continuous Delivery (CI/CD) Pipeline using Jenkins

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 13  
**Tools Used:** Jenkins Automation Server, Git, Docker, Declarative Jenkinsfile

## 1. AIM
To construct an automated **CI/CD Pipeline** using **Jenkins** that triggers on code commits, checks out code, runs automated tests, builds a Docker image, and simulates deployment.

## 2. THEORY & PIPELINE ARCHITECTURE
A Jenkinsfile defines the CI/CD workflow as code.

```
+---------------+      +-------------------+      +------------------+      +-------------------+
|  Code Commit  | ===> | Stage 1: Checkout | ===> |  Stage 2: Test   | ===> | Stage 3: Docker   | ===> Deploy
| (Git / GitHub)|      |  (Git Clone)      |      |  (PyTest/Lint)   |      |  (Build & Image)  |      Success
+---------------+      +-------------------+      +------------------+      +-------------------+
```

## 3. DECLARATIVE JENKINSFILE DIRECTIVE EXPLANATIONS FOR EXAMS
1. `pipeline { ... }`: Root wrapper for Declarative Pipeline syntax in Jenkins.
2. `agent any`: Specifies that the pipeline can run on any available Jenkins build executor/node.
3. `environment { ... }`: Defines global environment variables accessible across all stages.
4. `stages { ... }`: Container block holding all sequential pipeline stages.
5. `stage('Stage Name') { ... }`: Defines a distinct phase in the CI/CD lifecycle (e.g., Test, Build, Deploy).
6. `steps { ... }`: Actual shell commands (`sh`) or Jenkins steps executed inside the stage.
7. `post { success { ... } failure { ... } }`: Conditional actions based on build outcome.

## 4. STEP-BY-STEP JENKINS SETUP PROCEDURE
1. Start Jenkins server: `docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts`.
2. Access `http://localhost:8080` and log in with initial admin credentials.
3. Create a **Pipeline** job named `LMS-CI-CD-Pipeline`.
4. Configure SCM: Git, enter repository URL, set Script Path to `Jenkinsfile`.
5. Trigger build manually using **Build Now** or automatically via GitHub webhook.

---
*End of EXP-13*
