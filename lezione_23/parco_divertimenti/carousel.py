from ride import Ride
class Carousel(Ride):
    def __init__(self, id: str, name: str, min_height_cm: int, animals: list[str]):
        super().__init__(id, name, min_height_cm)

        self.animals = animals
    
    def category(self):
        return "family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        return {
            "id" : self.id,
            "nome" : self.name,
            "altezza minima" : self.min_height_cm,
            "categoria" : self.category(),
            "animali" : self.animals,
            "attesa minima" : self.base_wait()
        }