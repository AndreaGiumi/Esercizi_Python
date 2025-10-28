class AbsShape:
    def area(self):
        pass

class AbsCircle(AbsShape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.141592653589793 * self.r * self.r