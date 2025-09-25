# Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
# dato valore intero definito threshold.


def tresh(lista: list[int], threshold) -> int:
    prod = 1
    for elem in lista:
        if elem < threshold:
            prod *= elem
    return prod


print(tresh([25, 2, 4, 14, 8, 12, 25], 14))




# def fattoriale(n: int) -> int:
#     if n == 1:
#         return 1 
#     return n*fattoriale(n-1)
    


# print(fattoriale(5))