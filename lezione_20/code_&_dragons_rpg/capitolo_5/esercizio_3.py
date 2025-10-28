def sum_multiples(limit: int) -> int:
    if limit <= 0:
        return 0
    somma = 0
    for i in range(limit):
        if i < limit and i % 3 == 0 or i % 5 == 0:
            somma += i
    return somma
