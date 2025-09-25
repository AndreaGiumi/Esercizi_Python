def sommalista(lista_num: list[int]) -> int:

    '''
    Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

    Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.
    '''
    somma = 0
    for num in lista_num:
        somma += num
    print(somma)



lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]


sommalista(lista_num)