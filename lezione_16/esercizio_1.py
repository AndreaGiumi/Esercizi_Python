class Contatore:
    _conteggio: int

    def __init__(self, conteggio: int = 0) -> None:
        self._conteggio = conteggio


    def setZero(self) -> None:
        self._conteggio = 0


    def add1(self) -> None:
        self._conteggio += 1

    
    def sub1(self) -> None:
        if self._conteggio > 0:
            self._conteggio -= 1
        else:
            print("None è possibile eseguire la sottrazione")
    
    def get_val(self) -> int:
        return self._conteggio
    

    def mostra(self):
        print(f"Valore corrente del conteggio: {self._conteggio}")