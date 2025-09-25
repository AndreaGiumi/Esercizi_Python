from forma import Forma
class Quadrato(Forma):
    '''
    Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
    Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
    Il metodo getArea() deve calcolare l'area del quadrato.
    Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore.
    Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

    '''
    __lato: float

    def __init__(self, lato: float):
        super().__init__()
        self.setNome("Quadrato")
        self.setLato(lato)

    def setLato(self, lato: float) -> None:
        if not lato or isinstance(lato, float):
            raise ValueError("Inserire un valore per il lato corretto!")
        else:
            self.__lato = lato

    def getLato(self) -> float:
        return self.__lato
    

    def getArea(self) -> float:
        area = self.getLato() * self.getLato()
        return area
    

    def render(self) -> None:
        print(f"Ecco un Quadrato di lato {self.getLato()}")
        for i in range(self.getLato()):
            if i == 0 or i == self.getLato() - 1:
                print("*" * self.getLato())
            else:
                print("*" + " " * (self.getLato() - 2) + "*")
        print(f"L'Area di questo Quadrato vale {self.getArea()}")

    

if __name__=="__main__":

    quadrato: Quadrato = Quadrato(5)

    print(quadrato.getNome())

    quadrato.render()

    