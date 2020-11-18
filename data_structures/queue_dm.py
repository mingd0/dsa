class Queue: 
    
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item): 
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else: 
            self.rear += 1
        self.queue.append(item)
    
    def dequeue(self): 
        if self.is_empty():
            return
        value = self.queue[self.front]
        if self.front == self.rear: 
            self.front = -1
            self.rear = -1        
        else: 
            self.front += 1
        return value
        
    def is_empty(self):
        return (self.front == -1 and self.rear == -1)
    
    def peek(self):
        return self.queue[self.front]