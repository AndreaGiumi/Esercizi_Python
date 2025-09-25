punteggio = 0

while punteggio < 100:
    d1: int = int(input("Numero uscito dal dado 1:  "))
    d2: int = int(input("Numero uscito dal dado 2:  "))

    if d1 > 0 or d1 <= 6 or d2 > 0 or d2 <= 6:
        sum = d1 + d2
        print(f"Lancio dadi: D1 = {d1}, D2 = {d2}, Somma = {sum}")

        if d1 % 2 == 0 and d2 % 2 == 0 and sum > 8:
            punteggio = 100
            print("Vittoria!")
        elif d1 == 6 or d2 == 6 or sum == 7:
            punteggio += 10
            print(f"Incremento punteggio di 10. Punteggio attuale: {punteggio}")
            
        else:
            punteggio = 0
            print("Sconfitta!")
