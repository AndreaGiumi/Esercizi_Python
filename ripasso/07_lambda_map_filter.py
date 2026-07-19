"""
Sezione 7 - Lambda, map, filter e RegEx (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""

import re


# Esercizio 7.1 - Lambda base
# Con map() e una lambda: i quadrati.
# Con filter() e una lambda: solo i multipli di 3.
def esercizio_7_1() -> None:
    numeri: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quadrati: list[int] = list(map(lambda x : x ** 2, numeri))
    multipli: list[int] = list(filter(lambda x : x % 3 == 0, quadrati))
    print(quadrati)
    print(multipli)



# Esercizio 7.2 - Ordinamento personalizzato
# Usa sorted() con key=lambda per ordinare:
#   - per voto crescente
#   - per nome in ordine alfabetico
def esercizio_7_2() -> None:
    studenti: list[tuple[str, int]] = [("Anna", 28), ("Luca", 30), ("Marco", 25)]
    # new_stud: list[tuple[str, int]] = list(sorted(lambda:x))


# Esercizio 7.3 - RegEx (difficile)
# Con il modulo re:
#   - verifica se una stringa è un'email valida (testo@testo.dominio)
#   - estrai tutti i numeri da "Ho comprato 3 mele e 12 arance a 5 euro"
def email_valida(email: str) -> bool:
    # TODO
    pass


def estrai_numeri(frase: str) -> list[str]:
    # TODO
    pass


if __name__ == "__main__":
    esercizio_7_1()
    esercizio_7_2()
    print(email_valida("andrea@example.com"))
    print(estrai_numeri("Ho comprato 3 mele e 12 arance a 5 euro"))
