from abc import ABC, abstractmethod
import math

class Shape(ABC):
    _area: float
    _perimeter:float
    @abstractmethod
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, raggio: float) -> None:
        super().__init__()
        self.raggio = raggio

        
    def area(self) ->float:
        form_area = math.pi * (self.raggio **2)
        print(f"Questa è l'area del cerchio: {form_area:.2f}")


    def perimeter(self) -> float:
        form_perimetro = 2*self.raggio*math.pi
        print(f"Questa è la circonferenza del cerchio: {form_perimetro:.2f}")
    


class Rectangle(Shape):
    def __init__(self, b: float, h: float) ->None:
        super().__init__()
        self.b = b
        self.h = h

    def area(self) ->None:
        calc_area = self.b * self.h
        print(f"Questa è l'area del rettangolo: {calc_area:.2f}")


    def perimeter(self) -> None:
       calc_per = (2*self.b) + (2*self.h)
       print(f"Questo è il perimetro del rettangolo: {calc_per:.2f}")



c:Circle = Circle(14.24)

c.area()
c.perimeter()


r:Rectangle = Rectangle(4.5,21.2)



r.area()
r.perimeter()


    
