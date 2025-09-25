num: int = int(input("inserisci numero: "))

if num <= 0:
    print("Il numero deve essere positivo!")
    
elif num % 1 != 0:
    print("Il numero deve essere intero positivo!")
    num: int = int(input("inserisci numero: "))
else:
    cont = 0
    i = 0

    while i < 10:
        n: int = int(input("Inserisci 10 numeri: "))

        if n % num == 0:
            cont += 1
    
        i += 1

    print(f"Il numero di numeri divisibili per {num} è: {cont}")
