class Counter:
    def __init__(self, count: int = 0) -> None:
        self.count = count

    
    def inc(self) -> None:
        self.count += 1
        
    
    def value(self) -> int:
        return self.count