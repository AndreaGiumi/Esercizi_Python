def media(lista_num: int) -> float:
    '''
    Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.
    '''

    somma = 0

    for i in lista_num:
        somma += i
        media = somma / len(lista_num)
    print(f"{media:.2f}") 


lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]

media(lista_num)