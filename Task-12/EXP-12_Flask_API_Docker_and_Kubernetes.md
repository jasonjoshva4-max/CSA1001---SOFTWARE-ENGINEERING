# EXP-12: Containerizing and Deploying a Flask REST API with Docker & Kubernetes

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 12  
**Tools Used:** Python 3.11, Flask, Docker, Kubernetes (kubectl, Minikube)

## 1. AIM
To develop a Python **Flask REST API**, containerize it with Docker, and orchestrate its deployment using **Kubernetes Deployment and Service manifests**.

## 2. CODE IMPLEMENTATION EXPLANATION
- `app.py`: Defines REST endpoints (`/`, `/api/tasks`, `/api/health`).
- `Dockerfile`: Sets up Python 3.11 lightweight environment, installs dependencies, and runs Gunicorn WSGI server.
- `k8s-deployment.yaml`:
  - **Deployment:** Configures 3 Pod replicas for high availability and automatic failover.
  - **Service (NodePort):** Exposes port 5000 externally on host port 30080.

## 3. EXAM COMMAND BREAKDOWN
- `docker build -t flask-api:v1 .`: Builds local container image.
- `kubectl apply -f k8s-deployment.yaml`: Deploys pods and services to Kubernetes cluster.
- `kubectl get pods`: Checks status of running pod instances.
- `kubectl get services`: Verifies service NodePort mapping.
- `kubectl scale deployment flask-api-deployment --replicas=5`: Dynamically scales pods up to 5.
