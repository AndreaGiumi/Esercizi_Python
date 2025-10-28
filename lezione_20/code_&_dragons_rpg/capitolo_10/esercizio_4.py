class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Error")
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0