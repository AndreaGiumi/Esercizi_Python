soglia: int = int(input("Inserisci numero soglia: "))
i = 0

while i <= 7:
    n: int = int(input("Inserisci numero: "))
    if n > soglia:
        print(f"Numero maggiore del numero soglia: {n}")

        i += 1