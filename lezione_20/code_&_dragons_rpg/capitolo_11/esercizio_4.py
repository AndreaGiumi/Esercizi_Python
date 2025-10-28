class Employee:
    def __init__(self, name):
        self.name = name
        

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.team = []
    
    def add_member(self, name):
        self.team.append(name)