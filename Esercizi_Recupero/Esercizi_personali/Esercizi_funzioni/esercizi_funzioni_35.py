def conta_parole(lista: list[int]):
    dizionario = {}
    for el in lista:
        if el in dizionario:
            dizionario[el] += 1
        else:
            dizionario[el] = 1
    print(dizionario)

lista_char = ["Ciao", "Ciao mondo", "Ciao", "Cane", "Gatto", "Cane", "Cane", "Gatto"]

conta_parole(lista_char)