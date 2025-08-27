from app import app, db, Task

# Add tasks inside the app context
with app.app_context():
    task1 = Task(title="Learn Flask", description="Learn about Flask and how to implement it", done=True)
    task2 = Task(title="Finish task", description="Finish the daily task of this project", done=True)
    task3 = Task(title="Debug database", description="Make sure code runs as expected", done=False)

    db.session.add_all([task1, task2, task3])
    db.session.commit()

print("Tasks added successfully!")
