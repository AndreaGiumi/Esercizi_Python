"""
Sezione 5 - Funzioni (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 5.1 - Calcolatrice
# Quattro funzioni con parametri tipizzati. La divisione gestisce
# il divisore uguale a zero. Poi un menu che chiede operazione e numeri.
def somma(a: float, b: float) -> float:
    # TODO
    pass


def sottrazione(a: float, b: float) -> float:
    # TODO
    pass


def moltiplicazione(a: float, b: float) -> float:
    # TODO
    pass


def divisione(a: float, b: float) -> float | None:
    # TODO: gestisci b == 0
    pass


def menu_calcolatrice() -> None:
    # TODO
    pass


# Esercizio 5.2 - Validatore password
# Ritorna True solo se la password: >= 8 caratteri, almeno una maiuscola,
# almeno un numero.
def valida_password(password: str) -> bool:
    # TODO
    pass


# Esercizio 5.3 - Funzioni con valori di default (difficile)
# Applica prima lo sconto (in %) e poi aggiunge l'IVA.
# Testala con 1, 2 e 3 argomenti, anche con keyword arguments.
def calcola_prezzo(prezzo_base: float, sconto: float = 0, iva: float = 22) -> float:
    # TODO
    pass


if __name__ == "__main__":
    menu_calcolatrice()
    print(valida_password("Password1"))
    print(calcola_prezzo(100))
    print(calcola_prezzo(100, sconto=10))
    print(calcola_prezzo(100, sconto=10, iva=4))
