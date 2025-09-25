'''
Esercizio 2

Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.
'''

frase: str = str(input("Inserisci una frase: "))

cont = 0
for char in frase:
    if char == " ":
        cont += 1
print(f"Il numero di spazi nella frase {frase} sono: {cont}")