def listaPari(lista_num: list[int]):

    '''
    Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.
    '''
    lista_pari: list[int] = []

    for num in lista_num:
        if num % 2 == 0:
            lista_pari.append(num)
    print(lista_pari)




lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]


listaPari(lista_num)
