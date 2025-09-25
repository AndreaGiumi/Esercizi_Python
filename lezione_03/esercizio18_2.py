n: int = int(input("Inserisci lunghezza serie: "))

i = 0
sum = 0
media = 0
sum_pari = 0
sum_dispari = 0

while i < n:
    x: int = int(input("Inserisci numero: "))
    sum += x
    i += 1
    media = sum / i
    if x % 2 == 0 and x > media:
        sum_pari += x
    else:
        sum_dispari += x
print(f"Questa è la somma dei numeri pari o maggiori della media: {sum_pari}\nQuesta è la somma di numeri dispari o minori della media: {sum_dispari}")

if sum_pari > sum_dispari:
    print(f"{sum_pari} è maggiore!")
elif sum_dispari > sum_pari:
    print(f"{sum_dispari} è maggiore!")
else:
    print("Le somme sono uguali!")









