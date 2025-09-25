'''
Esercizio 8

Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******


'''




lista_num = []
while len(lista_num) <= 4:
    numeri: int = int(input("Inserisci cinque numeri: "))
    if numeri < 0 or numeri > 30:
        print("Il numero deve essere compreso tra 1 e 30")
    else:
        lista_num.append(numeri)

for num in lista_num:
    ast = "*" * num
    print(ast)



