def sum_above_threshold(numbers: list[int], threshold: int = 20) -> int:
    '''
    Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
    '''
    somma = 0
    for i in numbers:
        if i > threshold:
            somma += i
    return somma