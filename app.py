from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task model
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    priority = db.Column(db.String(10), default="low")

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tasks', methods=['GET', 'POST'])
def tasks_view():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        
        # Check if the form is for adding a new task
        new_task = Task(title=title, description=description, priority=priority)
        db.session.add(new_task)
        db.session.commit()
        
        return redirect(url_for('tasks_view'))

    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("tasks.html", tasks=tasks)

@app.route('/add')
def add_task():
    return render_template("add_task.html")

# New routes for editing and deleting tasks
@app.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return "Task not found", 404

    if request.method == 'POST':
        task.title       = request.form['title']
        task.description = request.form['description']
        task.priority    = request.form['priority']
        task.done        = 'done' in request.form
        db.session.commit()
        return redirect(url_for('tasks_view'))

    return render_template("edit_task.html", task=task)

@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Retrieve the task to be deleted
    task = db.session.get(Task, task_id)
    if not task:
        return "Task not found", 404

    # Delete the task from the database
    db.session.delete(task)
    db.session.commit()
    
    return redirect(url_for('tasks_view'))

# New API endpoint for toggling task completion status
@app.route('/api/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task.done = not task.done
    db.session.commit()
    
    return jsonify({'done': task.done})

if __name__ == '__main__':
    # You will need to run `db.create_all()` in a separate shell to create the database initially
    # with `from app import db; db.create_all()`.
    app.run(debug=True)