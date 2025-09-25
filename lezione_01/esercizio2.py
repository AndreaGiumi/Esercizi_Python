max: int = int(input("Inserisci numero: "))
i: int = 1

while i < 4:
    n: int = int(input("Inserisci numeri: "))
    if n > max:
        max = n
    i += 1
    

print(f"Questo è il numero più grande: {max}")