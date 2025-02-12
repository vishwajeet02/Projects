from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.poplefts()

    def is_empty(self):
        return len(self.items) == 0
