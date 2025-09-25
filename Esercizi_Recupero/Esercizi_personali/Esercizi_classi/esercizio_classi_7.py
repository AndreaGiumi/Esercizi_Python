from abc import ABC, abstractmethod
import math
class Forma(ABC):

    '''
    Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma.
    Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() in modo appropriato per ogni forma. 
    Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.
    '''
    @abstractmethod
    def area(self):
        pass


class Quadrato(Forma):
    __lato: float
    def __init__(self, lato: float) -> None:
        self.set_lato(lato)

    
    def set_lato(self, lato: float) -> None:
        self.__lato = lato
    
    def lato(self) -> float:
        return self.__lato
    

    def area(self) -> float:
        return self.__lato ** 2
    


class Cerchio(Forma):
    __raggio: float
    def __init__(self, raggio: float) -> None:
        self.set_raggio(raggio)

    def set_raggio(self, raggio: float) -> None:
        self.__raggio = raggio


    def raggio(self) -> float:
        return self.__raggio
    

    def area(self):
        raggio: float = math.pi * self.raggio() **2
        return f"{raggio:.2}"
    

if __name__=="__main__":

    quadrato = Quadrato(5)
    print(quadrato.area())

    cerchio = Cerchio(5)
    print(cerchio.area())