# creare una funzione che data una lista di numer interi disordinati, ritroni la medesima lista di interi in modo ordinato (senza l'utilizzo di sort(), min(), max()

def bubble_sort(l:list[int]) -> list[int]:
    for i in range(len(l) // 2):
        # il ciclo controlla se il primo numero della lista è maggiore del secondo, se si li scambia
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        if l[1] > l[2]:
            l[1], l[2] = l[2], l[1]


        




    return l

    





lista: list[int] = [3, 100, 98, 4, 5, 45]


print(bubble_sort(lista))