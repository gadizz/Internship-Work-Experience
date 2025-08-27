# crud.py
from database import SessionLocal
from models import Task

# Insert sample tasks
def create_task(title, description):
    session = SessionLocal()
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return new_task

# Retrieve all tasks
def get_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks

# Update task status
def update_task(task_id, done=True):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.done = done
        session.commit()
    session.close()

# Delete task
def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
