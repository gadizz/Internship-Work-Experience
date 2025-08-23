from flask import Flask, render_template, request, redirect, url_for
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    priority = db.Column(db.String(10), default="low")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tasks', methods=['GET', 'POST'])
def tasks_view():
    if request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']
        new_task = Task(title=title, priority=priority)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks_view'))

    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)

@app.route('/add')
def add_task():
    return render_template("add_task.html")

if __name__ == '__main__':
    app.run(debug=True)
