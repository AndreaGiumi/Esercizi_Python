def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    return sorted(set(a) & set(b))  



if __name__=="__main__":

    lista_1 = [4, 4, 5, 8, 58, 2, 58]
    lista_2 = [4, 7, 5, 8, 38, 2, 54, 25, 11, 58]


    print(intersection_sorted(lista_1, lista_2))