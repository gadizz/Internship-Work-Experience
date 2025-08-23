from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup (SQLite file will be tasks.db in project folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Home route
@app.route('/')
def home():
    return render_template("home.html")

# Route to display tasks
@app.route('/tasks')
def show_tasks():
    tasks = Task.query.all()  # get all tasks from DB
    return render_template("tasks.html", tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
