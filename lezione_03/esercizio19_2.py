n: int = int(input("Inserisci un numero: "))

if n <= 0:
    print("Errore il numero è negativo!")
elif n % 2 == 0:
    sum = 0
    cont = 4
    while cont <= n:
        sum += cont
        cont += 4
    print(f"Somma dei numeri da 1 a {n} che sono divisibili per 4: {sum}")
else:
    prod = 1
    cont = 1
    while cont <= n:
        prod *= cont
        cont += 2
    print(f"Prodotto dei numeri dispari da 1 a {n}: {prod}")
        