"""
Sezione 9 - Classi: basi (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 9.1 - Classe Libro
# Attributi: titolo, autore, pagine.
# Implementa __init__, __str__ (descrizione leggibile) e is_lungo()
# (True se ha più di 300 pagine). Crea 3 oggetti e stampali.
class Libro:
    def __init__(self, titolo: str, autore: str, pagine: int) -> None:
        # TODO
        pass

    def __str__(self) -> str:
        # TODO
        pass

    def is_lungo(self) -> bool:
        # TODO
        pass


# Esercizio 9.2 - Contatore con incapsulamento
# Attributo protetto _conteggio. Metodi: setZero(), add1(), sub1()
# (mai sotto zero), getConteggio().
class Contatore:
    _conteggio: int

    def __init__(self, conteggio: int = 0) -> None:
        self._conteggio = conteggio

    def setZero(self) -> None:
        # TODO
        pass

    def add1(self) -> None:
        # TODO
        pass

    def sub1(self) -> None:
        # TODO: non scendere sotto zero
        pass

    def getConteggio(self) -> int:
        # TODO
        pass


# Esercizio 9.3 - ContoBancario (difficile)
# Attributi protetti _titolare e _saldo.
#   - deposita(importo) e preleva(importo) con controlli di validità
#   - getter per saldo e titolare
#   - lista interna _movimenti che registra ogni operazione
#   - estratto_conto() che stampa tutti i movimenti
class ContoBancario:
    def __init__(self, titolare: str, saldo: float = 0) -> None:
        # TODO
        pass

    # TODO: deposita, preleva, getter, estratto_conto


if __name__ == "__main__":
    # TODO: crea gli oggetti e testa i metodi
    pass
