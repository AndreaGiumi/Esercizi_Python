def conta_dispari(lista_num: list[int]):
    lista_div = []
    for num in lista_num:
        if num % 3 == 0:
            lista_div.append(num)
    print(lista_div)


conta_dispari([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])