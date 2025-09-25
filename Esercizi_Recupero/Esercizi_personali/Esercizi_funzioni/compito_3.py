'''
Esercizio 3

Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output.
 Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.
'''


parola: str = str(input("Inserisci parola: "))

new_parola = ""

for char in parola:
    new_parola = char + new_parola
    
print(new_parola)