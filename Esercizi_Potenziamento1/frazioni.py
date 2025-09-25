from typing import Self
class Frazioni:
    _numeratore: float
    _denominatore: float

    def __init__(self, num: int, den: int) -> None:
        self.set_numeratore(num)
        self.set_denominatore(den)

    def set_numeratore(self, num: int) -> None:
        if not isinstance(num, int):
            num = 13
        else:
            self._numeratore = num

    def set_denominatore(self, den: float) -> None:
        if not isinstance(den, int) or den == 0:
            den = 5
        else:
            self._denominatore = den

    def numeratore(self) -> int:
        return self._numeratore



    def denominatore(self) -> int:
        return self._denominatore


    def value(self) -> float:
        result = self.set_numeratore() / self.set_denominatore()
        return f"{result:.3f}"
    
    def __str__(self) -> str:
        return f"{self.set_numeratore()}/{self.set_denominatore()}"

def mcd(x: int, y: int)-> int:
    list_mcd = []
    
    for i in range(1, min(x,y) + 1):
        if x % i == 0 and y % i == 0:
            list_mcd.append(i)
    print(max(list_mcd))
    

def semplifica(l: list[Frazioni]) -> list[Frazioni]:
    '''
    Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, ovvero il più grande divisore comune tra numeratore e denominatore è 1.

Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
 
Nello specifico:

    se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.
    se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.
Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.
    '''
    fraz_sempl = []
    for i in l:
        num: int = int(i.numeratore())
        den: int = int(i.denominatore())
        div = mcd(num, den)
    if div == 1:
        fraz_sempl.append(i)
    if div > 1:
        n_numeratore = num // n_numeratore
        d_den = den // d_den
        fraz_sempl.append([i])
        # print(fraz_sempl)
    
    print(fraz_sempl)

    


    
    

if __name__ == "__main__":

    fraz_1: Frazioni = Frazioni(10,5)
    # fraz_2: Frazioni = Frazioni(10,5)
    # fraz_3: Frazioni = Frazioni(10,5)
    # fraz_4: Frazioni = Frazioni(10,5)
    # fraz_5: Frazioni = Frazioni(10,5)
    # fraz_6: Frazioni = Frazioni(10,5)

    semplifica(fraz_1)

