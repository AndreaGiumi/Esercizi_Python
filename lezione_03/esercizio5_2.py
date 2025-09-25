n: int = int(input("Inserisci numero: "))
sum = 0
i = 1

if n % 1 == 0 and n > 0:
    while i <= n:
        sum = sum + i*i
        i += 1
    print( f"La somma è uguale a: {sum}")
else:
    print("Errore, n deve essere positivi!")
