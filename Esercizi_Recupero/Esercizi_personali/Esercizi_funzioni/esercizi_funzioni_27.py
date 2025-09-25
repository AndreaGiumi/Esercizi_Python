from typing import Any
def no_a_capo():
    # Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. '
    # 'Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.
    qualcosa: any = input("Inserisci qualcosa: ")

    while qualcosa != "":

        print(qualcosa, end=" ")
        qualcosa: any = input("Inserisci qualcosa: ")




no_a_capo()