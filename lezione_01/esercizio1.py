# print("Hello World")

import math
a = int(input("Inserisci valore ipotenusa: "))
b = int(input("Inserisci valore cateto: "))

if a > b:
 c = math.sqrt(a * a - b * b)
else:
    print("Errore")
print(f"{c:.2f}")









