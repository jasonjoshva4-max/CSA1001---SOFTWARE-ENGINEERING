# EXP-11: Containerizing a Static Website using Docker and Nginx

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 11  
**Tools Used:** Docker Engine, Nginx, HTML5/CSS3

## 1. AIM
To build and containerize a static HTML website using Docker and Nginx, expose port 8080, and verify container operation.

## 2. EXAM COMMAND BREAKDOWN
- `docker build -t static-web-app:v1 .`
  - `docker build`: Builds Docker image from Dockerfile.
  - `-t static-web-app:v1`: Tags image name and version.
  - `.`: Specifies current directory as build context.
- `docker run -d -p 8080:80 --name my-static-container static-web-app:v1`
  - `-d`: Detached mode (runs in background).
  - `-p 8080:80`: Maps host port 8080 to container port 80.
  - `--name my-static-container`: Names the running container.
- `docker ps`: Lists running containers.
- `docker stop my-static-container`: Stops container execution.
- `docker rm my-static-container`: Removes container.
