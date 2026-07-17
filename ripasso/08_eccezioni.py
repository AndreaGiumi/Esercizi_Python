"""
Sezione 8 - Eccezioni (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""

import math


# Esercizio 8.1 - Radice sicura
# Calcola la radice quadrata con math.sqrt() e gestisci con try/except
# il caso di numero negativo (ValueError), stampando l'errore.
def safe_sqrt(numero: float) -> None:
    # TODO
    pass


# Esercizio 8.2 - Input robusto
# Continua a chiedere un input finché l'utente non inserisce un intero
# valido, gestendo il ValueError.
def chiedi_intero(messaggio: str) -> int:
    # TODO
    pass


# Esercizio 8.3 - Eccezione personalizzata (difficile)
# Crea SaldoInsufficienteError. La funzione preleva() solleva l'eccezione
# con raise se l'importo supera il saldo. Gestiscila con
# try/except/else/finally e osserva quando viene eseguito ogni blocco.
class SaldoInsufficienteError(Exception):
    pass


def preleva(saldo: float, importo: float) -> float:
    # TODO: raise SaldoInsufficienteError se importo > saldo
    pass


if __name__ == "__main__":
    safe_sqrt(25)
    safe_sqrt(-25)
    # numero = chiedi_intero("Inserisci un intero: ")
    # print(numero)
