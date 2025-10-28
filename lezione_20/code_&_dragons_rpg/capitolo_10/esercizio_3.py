from typing import Any
class Rectangle:

    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        area = self.w * self.h
        return area
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area() == other.area()
            
    

    def perimeter(self) -> float:
        perimeter = (self.w + self.h) * 2
        return perimeter