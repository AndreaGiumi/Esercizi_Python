def binary_search(lista: list[int], x: int ):
    i,j = 0, len(lista)
    mid = len(lista)// 2

    if lista[mid] == x:
        print(True)
    elif lista[mid] > x:
        j = mid 
        binary_search(lista[i:j], x)
    else:
        i = mid + 1
        binary_search(lista[i:j], x)


lista_1 = [2, 3, 14, 15, 25, 47, 58]



binary_search(lista_1, 7)