from ride import Ride

class RollerCoaster(Ride):
    def __init__(self, id: str, name: str, min_height_cm: int, inversions: int):
        super().__init__(id, name, min_height_cm)
        self.setInversions(inversions)
    
    def setInversions(self, inversions: int) -> None:
        if isinstance(inversions, int ) and inversions >= 1:
            self.inversions = inversions
        else:
            raise ValueError("Errore, inserire un valore più grande!")
    
    def category(self):
        return "roller_coaster"

    def base_wait(self):
        return 15
    
    def info(self):
        return {
            "id" : self.id,
            "nome" : self.name,
            "altezza minima" : self.min_height_cm,
            "categoria" : self.category(),
            "inversioni" : self.inversions,
            "attesa minima" : self.base_wait()
        }