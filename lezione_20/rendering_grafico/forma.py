from abc import ABC, abstractmethod
class Forma(ABC):

    '''
    Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma,
    come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma
    
    '''
    __nome: str
    def setNome(self, nome: str) -> None:
        if nome:
            self.__nome = nome
        else:
            print("Il nome non può essere una stringa vuota!")

    def getNome(self) -> str:
        return self.__nome
    
    @abstractmethod
    def getArea(self) -> None:
        pass

    
    def render(self) -> None:
        pass