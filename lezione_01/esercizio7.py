pari = 0
dispari = 0 
i = 1
while i <= 10:
    n: int = int(input("Inserire numeri: "))

    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    i += 1
    
print(f"Conto dei numeri pari: {pari}")
print(f"Conto dei numeri dispari: {dispari}")

