def istogramma(lista_num: list[int]) -> None:

    '''
    Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

    Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

    ***

    *******

    *********

    *****
    '''

    for num in lista_num:
        print("*" * num)


lista_num = [1, 3, 5, 6, 7, 8]


istogramma(lista_num)