'''
Esercizio 6

Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.
'''

n1: int = int(input("Inserisci primo numero: "))

n2: int = int(input("Inserisci secondo numero: "))

if n1 > n2:
    i = n1
    lim = n2
else:
    i = n2
    lim = n1

prdotto = lim

while i >= lim:
    prdotto *= i    
    i-= 1

print(prdotto)