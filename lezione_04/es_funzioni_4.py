def check_each(lista:list[int]):
    for i in lista:
        if i > 5:
            print(f"{i} è maggiore di 5")
        elif i < 5:
            print(f"{i} è minore di 5")
        else:
            print(f"{i} è uguale a 5")



ciao:list = [1, 2, 34, 56, 7, 5]

check_each(ciao)