def moltiplicatore(lista_num: list[int]) -> int:

    '''
    Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.
    '''
    molt = 1
    for i in lista_num:
        if i != 0:
            molt *= i
        print(molt)


lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]


moltiplicatore(lista_num)