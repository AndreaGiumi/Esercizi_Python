'''
Esercizio 4

Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

    Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
    Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).

'''
lista_num: list[float] = []
lista_num_int: list[int] = []


while True:

    numero: float = float(input("Inserisci un numero: "))


    if numero < 0:
        break
    else:
        lista_num.append(numero)

    if numero.is_integer():
        lista_num_int.append(numero)
        media: float = sum(lista_num_int) / len(lista_num_int)


    max_num: float = lista_num[0]
    min_num: float = lista_num[0]
    for num in lista_num:

        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
print(f"Il numero più grande è {max_num} e il numero più piccolo è {min_num}")

print(f"Media dei numeri interi: {media}")
    

    

    
    


