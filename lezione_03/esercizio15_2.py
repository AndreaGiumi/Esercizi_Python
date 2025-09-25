num: int = int(input("Inserisci numero: "))

if num > 0 and num <= 100:
        sum = 0
        i = 1
        while i <= num:
            if i % 2 == 0:
                sum += i
            i += 1
        print(f"La somma dei numeri pari da 1 a {num} è: {sum}")
elif num <= 0:
    sum = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            sum += i
        i += 1    

    print(f"La somma dei numeri dispari da 1 a abs{num} è: abs{sum}")











