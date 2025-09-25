'''
Esercizio 1

Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola 
"fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.
'''

while True:
    parola: str = str(input("Inserisci parola: "))

    if parola == "fine":
        break
    else:
        if parola[0] == parola[-1]:
            print(f"La prima è l'ultima lettere della parola {parola} sono uguali.")
        else:
            print(f"La prima è l'ultima lettere della parola {parola} non sono uguali.")
