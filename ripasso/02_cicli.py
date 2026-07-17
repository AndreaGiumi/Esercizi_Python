"""
Sezione 2 - Cicli: while e for (difficoltà: facile / media)

Completa ogni esercizio dove trovi il commento # TODO.
"""

import random


# Esercizio 2.1 - Somma dei positivi
# Con un ciclo while, chiedi 5 numeri all'utente e somma SOLO quelli positivi.
# Alla fine stampa la somma.
def esercizio_2_1() -> None:
    somma: int = 0
    i: int = 0

    while i < 5:
        numero: int = int(input("Inserisci un numero: "))

        if numero > 0:
            somma += numero
        i += 1
    print(somma)



# Esercizio 2.2 - Tabellina
# Chiedi un numero e stampa la sua tabellina da 1 a 10 con for e range().
# Esempio di riga: "7 x 3 = 21"
def esercizio_2_2() -> None:
    numero: int = int(input("Che tabellina vuoi creare? "))

    for i in range(1, 11):
        print(f"{numero} x {i} =  {numero * i}")


# Esercizio 2.3 - Indovina il numero (media)
# Il programma pensa un numero segreto con random.randint(1, 50).
# L'utente ha 7 tentativi: stampa "Troppo alto" o "Troppo basso".
# Se finisce i tentativi, rivela il numero segreto.
def esercizio_2_3() -> None:
    segreto: int = random.randint(1, 50)
    indovinato: bool = False
    i: int = 0
    while i < 7 and not indovinato:
        num: int = int(input("Inserisci numero: "))

        if num > segreto:
            print("Troppo alto")
        elif num < segreto:
            print("Troppo basso")
        else:
            print("Indovinato è proprio lui!!!")
            indovinato = True
        i += 1

    if not indovinato:
        print(f"Tentativi finiti, il numero segreto era: {segreto}")


        
    

if __name__ == "__main__":
    # esercizio_2_1()
    # esercizio_2_2()
    esercizio_2_3()
