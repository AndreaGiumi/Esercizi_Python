"""
Sezione 1 - Basi: variabili, input/output, condizioni (difficoltà: facile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 1.1 - Saluto personalizzato
# Chiedi nome ed età con input(). Stampa con una f-string:
# "Ciao Andrea, tra 10 anni avrai 38 anni!"
def esercizio_1_1() -> None:
    nome: str = input("Inserisci il tuo nome: ").title()
    eta: int = int(input("Inserisci la tua età: "))

    print(f"Ciao {nome + " Giumi"}, tra 10 anni avrai {eta + 10} anni")

# Esercizio 1.2 - Pari o dispari
# Chiedi un numero intero e stampa se è pari o dispari.
# Se il numero è 0, stampa un messaggio dedicato.
def esercizio_1_2() -> None:
    numero: int = int(input("Inserisci un numero intero: "))

    if numero == 0:
        print("Il numero che hai inserito è ZERO")
    elif numero % 2 == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")


# Esercizio 1.3 - Convertitore di voti
# Chiedi un voto da 0 a 100 e stampa la fascia (if/elif/else):
#   90-100 -> "Eccellente"
#   70-89  -> "Buono"
#   60-69  -> "Sufficiente"
#   < 60   -> "Insufficiente"
# Se il voto non è tra 0 e 100, stampa "Voto non valido".
def esercizio_1_3() -> None:
    voto: int = int(input("Inserisci un voto tra 0 e 100: "))

    if 90 <= voto <= 100:
        print("Eccellente")
    elif 70 <= voto <= 89:
        print("Buono")
    elif 60 <= voto <= 69:
        print("Sufficente")
    elif 0 <= voto <= 59:
        print("Insufficente")
    else:
        print("Voto non valido")


if __name__ == "__main__":
    esercizio_1_1()
    esercizio_1_2()
    esercizio_1_3()
