from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {"id": 1, "title": "Complete Software Engineering Lab Tasks", "status": "In Progress"},
    {"id": 2, "title": "Containerize Flask App with Docker", "status": "Pending"}
]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        new_id = len(todos) + 1
        todos.append({"id": new_id, "title": title, "status": "Pending"})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['status'] = "Completed"
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
