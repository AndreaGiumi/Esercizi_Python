"""
Sezione 11 - File e JSON (difficoltà: difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""

import json


# Esercizio 11.1 - Lettura e scrittura file di testo
# Scrivi su diario.txt tre righe (with open...), rileggi e stampa
# ogni riga numerata, poi aggiungi una riga in fondo (modalità "a").
def esercizio_11_1() -> None:
    # TODO
    pass


# Esercizio 11.2 - Contatore di parole
# Leggi un file di testo e stampa: numero di righe, numero di parole e
# la parola più frequente. Gestisci FileNotFoundError.
def esercizio_11_2(percorso: str) -> None:
    # TODO
    pass


# Esercizio 11.3 - Salvataggio oggetti in JSON (difficile)
# Riprendi la classe Libro (es. 9.1) e aggiungi:
#   - to_dict() che ritorna un dizionario con gli attributi
#   - salva_libreria(libri, percorso) con json.dump()
#   - carica_libreria(percorso) -> list con json.load() che ricostruisce i Libro
class Libro:
    def __init__(self, titolo: str, autore: str, pagine: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def to_dict(self) -> dict:
        # TODO
        pass


def salva_libreria(libri: list[Libro], percorso: str) -> None:
    # TODO
    pass


def carica_libreria(percorso: str) -> list[Libro]:
    # TODO
    pass


if __name__ == "__main__":
    esercizio_11_1()
    # esercizio_11_2("diario.txt")
