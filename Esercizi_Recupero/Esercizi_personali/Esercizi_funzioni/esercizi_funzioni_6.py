def maxLista(lista_num: list[int]):
    '''
    Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo
    
    '''

    max_num = lista_num[0]

    for num in lista_num:
        if num > max_num:
            max_num = num
    print(max_num)



lista_numeri: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 1052, 111, 44]



maxLista(lista_numeri)