# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dizionario = {}
    pari = []
    dispari = []

    for num in lista:
        if num % 2 == 0:
            pari.append(num)
        else:
            dispari.append(num)
    dizionario["pari"] = pari
    dizionario["dispari"] = dispari

    return dizionario