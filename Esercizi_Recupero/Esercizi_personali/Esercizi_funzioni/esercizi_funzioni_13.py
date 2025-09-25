def max_lista(lista_n: list[int]) -> int:

    '''
    Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.
    '''

    max_lista_n = lista_n[0]

    for i in lista_n:
        if i > max_lista_n:
            max_lista_n = i
    print(max_lista_n)


lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]

max_lista(lista_num)