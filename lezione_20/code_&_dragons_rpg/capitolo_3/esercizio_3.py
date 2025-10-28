def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    lista_diff = []
    
    for num in a:
        if num not in b:
            lista_diff.append(num)
    for numm in b:
        if numm not in a:
            lista_diff.append(numm)
    return sorted(lista_diff)


if __name__=="__main__":

    lista_num = [1, 87, 58, 4, 2, 8]
    lista_num2= [4, 6, 558, 0, 77, 2, 9]


    print(symdiff_sorted(lista_num, lista_num2))