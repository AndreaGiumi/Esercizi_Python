class Vehicle:
    def __init__(self):
        self.speed = 0


class Car(Vehicle):

    def accelerate(self, delta: int):
         self.speed += delta