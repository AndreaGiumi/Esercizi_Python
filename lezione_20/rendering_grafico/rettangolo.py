from forma import Forma
class Rettangolo(Forma):

    '''
    
    Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
    Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
    Il metodo getArea() deve calcolare l'area del rettangolo.
    Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore.
    Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
    '''
    __base: float
    __altezza: float

    def __init__(self, base: float, altezza: float):
        super().__init__()
        self.setNome("Rettangolo")
        self.setBase(base)
        self.setAltezza(altezza)



    def setBase(self, base: float) -> None:
        if not base or isinstance(base, float):
            raise ValueError("Valore della base non valido!")
        else:
            self.__base = base

    def getBase(self) -> float:
        return self.__base
    
    def setAltezza(self, altezza: float) -> None:
        if not altezza or isinstance(altezza, float):
            raise ValueError("Valore altezza non valido!")
        else:
            self.__altezza = altezza

    def getAltezza(self) -> float:
        return self.__altezza
    

    def getArea(self):
        area =   self.getBase()* self.getAltezza()
        return area


    def render(self):
        print(f"Ecco un Rettangolo avente base {self.getBase()} e altezza {self.getAltezza()}")

        for i in range(self.getBase()):
            for j in range(self.getAltezza()):
                if i == 0 or i == self.getBase() - 1:
                    print("*", end=" ")
                elif j == 0 or j == self.getAltezza() - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("\n", end="")
        print(f"L'Area di questo Rettangolo vale {self.getArea()}")

if __name__=="__main__":

    rettangolo1: Rettangolo = Rettangolo(4, 8)
    rettangolo1.render()
