"""
Sezione 6 - Ricorsione (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""

import time


# Esercizio 6.1 - Fattoriale
# Funzione ricorsiva. Ricorda il caso base!
def fattoriale(n: int) -> int:
    # TODO
    pass


# Esercizio 6.2 - Potenza ricorsiva
# Ricorsiva, senza usare **.
def potenza(base: int, esponente: int) -> int:
    # TODO
    pass


# Esercizio 6.3 - Fibonacci (difficile)
# Versione ricorsiva e versione iterativa. Confronta i tempi con
# time.time() per n = 30.
def fibonacci_ricorsivo(n: int) -> int:
    # TODO
    pass


def fibonacci_iterativo(n: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    print(fattoriale(5))
    print(potenza(2, 5))

    inizio = time.time()
    print(fibonacci_ricorsivo(30))
    print(f"Ricorsivo: {time.time() - inizio:.4f}s")

    inizio = time.time()
    print(fibonacci_iterativo(30))
    print(f"Iterativo: {time.time() - inizio:.4f}s")
