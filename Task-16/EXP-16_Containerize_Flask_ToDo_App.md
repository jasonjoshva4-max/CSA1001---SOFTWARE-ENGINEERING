# EXP-16: Containerizing a Full-Stack Flask To-Do Web Application using Docker

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 16  
**Tools Used:** Python 3.11, Flask, HTML5/CSS3, Gunicorn, Docker Engine

## 1. AIM
To build a functional **Flask To-Do Web Application** with interactive UI, write a production-ready **Dockerfile**, containerize the application, and test container execution.

## 2. CODE STRUCTURE EXPLANATION FOR EXAMS
- `app.py`: Flask application routes for listing, adding, completing, and deleting tasks.
- `templates/index.html`: Responsive frontend HTML template.
- `Dockerfile`: Multi-stage Python build with Gunicorn WSGI server.

## 3. BUILD & RUN COMMANDS
- `docker build -t flask-todo-app:v1 .`
- `docker run -d -p 5000:5000 --name todo-app-container flask-todo-app:v1`
- Open browser at `http://localhost:5000`.

---
*End of EXP-16*
