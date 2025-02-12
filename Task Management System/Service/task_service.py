from models import Task,Queue,Stack,Graph

class Task_Service:
    def __init__(self):
        self.tasks = []
        self.task_queue = Queue()
        self.task_history = Stack()

    def create_task(self,id,title,description):
        task = Task(id,title,description)
        self.tasks.append(task)
        self.task_queue.enqueue(task)
        return task


    def complete_task():
        if not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            self.task_history.push(task)
            return task.id,task.title,task.description
        return None

    def get_task_history(self):
        return self.task_history
