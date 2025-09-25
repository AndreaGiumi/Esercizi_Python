from forma import Forma

class Triangolo(Forma):

    '''
    Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità,
    si suppone che il triangolo in questione sia un triangolo rettangolo).
    Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
    Il metodo getArea() deve calcolare l'area del triangolo.
    Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore.
    Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
    
    '''

    __lato: float
    def __init__(self, lato: float):
        super().__init__()
        self.setNome("Triangolo")
        self.setLato(lato)


    
    def setLato(self, lato: float) -> None:
        if not lato or isinstance(lato, float):
            raise ValueError("Valore del lato non valido!")
        else:
            self.__lato = lato

    
    def getLato(self) -> float:
        return self.__lato
    

    def getArea(self) -> None:
        area = (self.getLato() * self.getLato()) // 2
        return area
    

    def render(self) -> None:
        print(f"Ecco un Triangolo avente base {self.getLato()} ed altezza {self.getLato()}!")
        for i in range(self.getLato()):
            if i == 0: 
                print("*")
            elif i == self.getLato() - 1:
                print("*" * (i + 1))
            else:
                print("*" + " " * (i - 1) + "*")
        print(f"L'Area di questo Triangolo vale {self.getArea()}")


if __name__=="__main__":

    triangolo1: Triangolo = Triangolo(4)

    triangolo1.render()