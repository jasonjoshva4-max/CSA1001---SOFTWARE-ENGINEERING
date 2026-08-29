from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Setup Docker", "status": "Completed"},
    {"id": 2, "title": "Deploy to Kubernetes", "status": "In Progress"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Flask API on Kubernetes!", "status": "Healthy"})

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "count": len(tasks)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
