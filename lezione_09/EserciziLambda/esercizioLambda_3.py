lista_numeri:int = [5, 12, 17, 18, 24, 32]

evens:list[int] = list(filter(lambda x:x % 2 == 0, lista_numeri))


print(evens)    