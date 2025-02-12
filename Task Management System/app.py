import streamlit as st
from datetime import datetime

# Import your service classes (adjust the import paths if your folders are lowercase)
from Service.task_service import Task_Service
from Service.user_service import User_Service

# Initialize session state for our services if not already present
if 'task_service' not in st.session_state:
    st.session_state.task_service = Task_Service()

if 'user_service' not in st.session_state:
    st.session_state.user_service = User_Service()
    # Optionally add a user (if required)
    st.session_state.user_service.add_user(123, "vishwa", "vishwa02@gmail.com")

# Shortcut variables for easier access
task_service = st.session_state.task_service
user_service = st.session_state.user_service

st.title("Task Management System")

# --- Section: Create a Task ---
st.header("Create a Task")
with st.form("create_task_form"):
    task_id = st.number_input("Task ID", min_value=1, step=1, value=1)
    title = st.text_input("Task Title", value="New Task")
    description = st.text_area("Task Description", value="Describe the task here...")
    submit_task = st.form_submit_button("Create Task")

if submit_task:
    new_task = task_service.create_task(task_id, title, description)
    st.success(f"Task '{new_task.title}' created successfully!")

# --- Section: Pending Tasks and Complete Next Task ---
st.header("Pending Tasks and Complete Next Task")

# Display pending tasks from the task queue.
# (We assume pending tasks are stored in task_service.task_queue.items)
pending_tasks = []
for task in list(task_service.task_queue.items):
    pending_tasks.append({
        "Task ID": task.id,
        "Title": task.title,
        "Description": task.description
    })

if pending_tasks:
    st.subheader(f"Pending Tasks (Total: {len(pending_tasks)})")
    st.table(pending_tasks)
else:
    st.write("No pending tasks.")

# Button to complete the next pending task.
if st.button("Complete Next Task"):
    if not task_service.task_queue.is_empty():
        # Dequeue the next task
        task = task_service.task_queue.dequeue()
        # Set the completion timestamp
        task.completed_at = datetime.now()
        # Push it to the history stack
        task_service.task_history.push(task)
        st.info(
            f"Completed Task:\n"
            f"ID: {task.id}\n"
            f"Title: {task.title}\n"
            f"Description: {task.description}\n"
            f"Completed At: {task.completed_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
    else:
        st.warning("No tasks available to complete.")

# --- Section: Task History ---
st.header("Task History")
if task_service.task_history.is_empty():
    st.write("No tasks have been completed yet!")
else:
    # Get completed tasks. Since the history is a stack (LIFO), reverse the list to show the most recent first.
    completed_tasks = task_service.task_history.items[::-1]
    history_data = []
    for task in completed_tasks:
        completed_time = (
            task.completed_at.strftime("%Y-%m-%d %H:%M:%S")
            if hasattr(task, "completed_at")
            else "N/A"
        )
        history_data.append({
            "Task ID": task.id,
            "Title": task.title,
            "Description": task.description,
            "Completed At": completed_time
        })
    st.table(history_data)
