
sum = 0
i = 1
while i != 5:
    n: int = int(input("Inserisci numeri: "))
    if n > 0:
        sum += n
    i += 1
    
print(f"Questa è la somma: {sum}")