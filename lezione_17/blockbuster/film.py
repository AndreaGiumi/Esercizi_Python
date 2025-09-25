from __future__ import annotations
class Film:

    '''
    ### CLASSE: Film
    In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int)
    ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
    
    - Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale. 
    
    '''

    __id: int
    __titolo: str

    def __init__(self, id: int, titolo: str) -> None:
        self.setID(id)
        self.setTitolo(titolo)

    
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id
    
    def setTitolo(self, titolo: str) -> None:
        self.__titolo = titolo

    def getTitolo(self) -> str:
        return self.__titolo
    
    def isEqual(self, otherFilm: Film) -> bool:
        if otherFilm.getID() == self.getID():
            return True
        return False
        
if __name__=="__main__":
    film1: Film = Film(27, "Redivivo")
    film2: Film = Film(257, "La vita è bella")


    print(film2.isEqual(film1))

    print(film1.getTitolo(), film1.getID())