from models import Task,Queue,Stack,Graph

class Task_Service:
    def __init__(self):
        self.tasks = []
        self.task_queue = Queue()
        self.task_history = Stack()

    def create_task(self,id,title,description):
        task = Task(id,title,description)
        self.tasks.append(task)
        self.task_queue.put(task)
        return task


    def complete_task():
        if not self.task_queue.is_empty():
            task = 

    def get_task_history():
