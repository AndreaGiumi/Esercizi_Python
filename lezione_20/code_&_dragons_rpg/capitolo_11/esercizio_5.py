class Logger:
    def write(self):
        pass
    def records(self):
        pass
    

class MemoryLogger(Logger):
    def __init__(self):
    
        self.record = []
        
    def write(self, msg):
        self.record.append(msg)
    
    def records(self):
        return self.record