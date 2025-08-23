# main.py
from crud import create_task, get_tasks, update_task, delete_task

# Add tasks
create_task("Learn SQLAlchemy", "Understand how to use ORM")
create_task("Build project", "Make a Python + DB app")

# Get tasks
tasks = get_tasks()
print("Tasks:", tasks)

# Update task
update_task(1, done=True)

# Delete task
delete_task(2)
