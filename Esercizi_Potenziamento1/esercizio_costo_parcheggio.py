from typing import Any
def calculateCharges(ore: float) -> int:
    tariffa = 0
    if ore <= 3:
        tariffa = 2
    else:
        if ore > 3 and ore < 24:
            if ore % 1 != 0:
                ore = round(ore)
            tariffa = 2 +(ore - 3) * 0.5
        else:
            tariffa = 10
    print(tariffa)


clienti: list[Any] = [1.5, 4.0, 5.5, 24.0]
totale = 0

print(f"{'Car':<10} {'Hours':<10} {'Charge':<10}")


for i in range(len(clienti)):
    print(f"{i+1:<10} {clienti[i]:<10} {t:<.2f}")
    t = calculateCharges(clienti[i])

    totale += t

print(f"{'TOTAL':<10} {sum(clienti):<10} {totale:<.2f}")

    


