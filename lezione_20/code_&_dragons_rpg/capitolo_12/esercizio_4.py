class AnimalBase:
    def speak(self):
        pass

class Cat(AnimalBase):
    def speak(self):
        return "meow"

class Dog(AnimalBase):
    def speak(self):
        return "woof"