# Task Management System

## Introduction

Welcome to the **Task Management System** project! This is a simple and powerful tool designed to help users create, manage, and track their tasks. Built using Python and Streamlit, the system allows users to add tasks, complete them in order, and view their task history. The project demonstrates basic data structures like Queues and Stacks, while offering a clean and user-friendly UI.

Whether you’re a beginner learning about data structures or an experienced developer looking for a project to contribute to, this repository provides a great learning platform.

## Features

- **Task Creation**: Add new tasks with a title, description, and ID.
- **Task Completion**: Complete tasks in the order they are created and move them to a completed task history.
- **Task History**: View a list of all completed tasks, including the time and date they were completed.
- **Data Structures**: Implements Queue (for pending tasks) and Stack (for completed tasks) to manage tasks.
- **Streamlit UI**: A simple, interactive user interface to manage tasks efficiently.

## Installation

Follow these steps to install and set up the project locally.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python (version 3.7 or higher)
- Streamlit (for the UI)
- Required Python libraries

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/task-management-system.git
    cd task-management-system
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    streamlit run app.py
    ```

After running the command, your web browser should open with the Task Management System interface.

## Usage

Once the app is up and running:

- **Create Tasks**: Fill in the task details (ID, title, and description) and click "Create Task".
- **Complete Tasks**: Click the button to complete the next task, which will move it from the queue to the history.
- **View History**: See the list of completed tasks along with their details and completion time.

You can modify the code in `task_service.py` and `app.py` to suit your needs or enhance functionality. The app uses Streamlit, so it’s easy to make UI improvements.

## Contributing

We welcome contributions to this project! To get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request to the main branch.

### Guidelines

- Please make sure your code is well-commented and easy to understand.
- Follow PEP 8 guidelines for Python code style.
- Add tests if applicable.
- Ensure that your feature works correctly and doesn’t break any existing functionality.

## Contact Information

If you have any questions or suggestions, feel free to reach out!

- **Email**: vishwajeet25200012@gmail.com

---

Thank you for checking out the **Task Management System**! We hope it helps you learn about task management systems and data structures while providing a useful tool for personal or collaborative projects.
