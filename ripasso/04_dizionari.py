"""
Sezione 4 - Dizionari (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 4.1 - Classifica pari/dispari
# Funzione che prende una lista di numeri e ritorna un dizionario con
# le chiavi "pari" e "dispari", ognuna con la lista dei numeri corrispondenti.
def classifica_numeri(lista: list[int]) -> dict[str, list[int]]:
    # TODO
    pass


# Esercizio 4.2 - Conta lettere
# Data una frase, costruisci un dizionario che conta quante volte compare
# ogni lettera (ignora gli spazi). Stampa la lettera più frequente.
def conta_lettere(frase: str) -> dict[str, int]:
    # TODO
    pass


# Esercizio 4.3 - Rubrica telefonica (difficile)
# Rubrica come dizionario {nome: telefono} con menu testuale in un while:
#   1. Aggiungi contatto   2. Cerca contatto   3. Elimina contatto
#   4. Mostra tutti        5. Esci
# Gestisci contatto già esistente o inesistente.
def rubrica() -> None:
    contatti: dict[str, str] = {}
    # TODO: ciclo del menu
    pass


if __name__ == "__main__":
    print(classifica_numeri([1, 2, 3, 4, 5, 6]))
    print(conta_lettere("programmazione"))
    rubrica()
