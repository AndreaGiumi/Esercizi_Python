def lista_tuple(lista_num: list[int]):
    lista_elem = []
    for num in range(len(lista_num)):
        lista_elem.append((lista_num[num], num))
    print(lista_elem)


lista_num = [3, 43, 22, 13, 54, 64, 3]


lista_tuple(lista_num)