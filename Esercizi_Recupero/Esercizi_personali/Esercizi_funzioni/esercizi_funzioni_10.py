def max_of_list(lista_num: list[int]) -> list[int]:

    '''
    Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.
    '''

    list_max: list[int] = []

    goal: int = int(input("Inserisci numero soglia: "))

    for i in lista_num:
        if i > goal:
            list_max.append(i)
    print(list_max)


lista_num: list[int] = [24, 1, 5, 88, 47, 63, 22, 2, 95, 102, 111, 44]

max_of_list(lista_num)