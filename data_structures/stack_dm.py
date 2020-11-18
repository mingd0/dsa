class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return
        value = self.stack[self.top]
        del self.stack[self.top]
        self.top -= 1
        return value
    
    def is_empty(self):
        return self.top == -1
    
    def peek(self): 
        return self.stack[self.top]
