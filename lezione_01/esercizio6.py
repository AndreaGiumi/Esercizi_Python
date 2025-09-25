n: int = int(input("Inserire un numero: "))

if n > 0:
    fact = 1
    i = 1

    while i <= n:
        fact *= i
        i += 1
else:
    print("Non posso calcolare il fattoriale di un numero negativo")

print(f"Il fattoriale del numero è {fact}")