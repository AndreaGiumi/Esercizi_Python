parole:list[str] = ["cane", "gatto", "ratto", "elefante", "si"]


parole_4 = list(filter(lambda x: len(x) > 4, parole))


print(parole_4)