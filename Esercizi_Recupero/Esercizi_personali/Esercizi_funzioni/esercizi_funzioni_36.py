def conta_pari(lista: list[int]):
    count = 0

    for num in lista:
        if num % 2 == 0:
            count += 1
    return count

print(conta_pari([2, 4 ,6 ,7, 8 ,87, 88, 65, 55, 44]))