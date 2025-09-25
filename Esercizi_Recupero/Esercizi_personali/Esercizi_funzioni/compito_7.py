'''
Esercizio 7

Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.
'''

lista_a: list[int] = [1, 2, 3]
lista_b: list[int] = [4, 5, 6]
lista_c: list[int] = []

d = len(lista_a)

for i in range(d):
    lista_c.append(lista_a[i] + lista_b[(d-1)-i])
print(lista_c)



