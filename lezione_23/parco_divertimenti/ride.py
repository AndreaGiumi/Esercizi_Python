from abc import ABC, abstractmethod
class Ride(ABC):
    def __init__(self, id: str, name: str, min_height_cm: int) -> None:
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self):
        pass


    @abstractmethod
    def base_wait(self):
        pass

    def info(self):
        return {
            "id" : self.id,
            "nome" : self.name,
            "altezza minima" : self.min_height_cm,
            "categoria" : self.category()
        }
    
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return self.base_wait() * crowd_factor
       

