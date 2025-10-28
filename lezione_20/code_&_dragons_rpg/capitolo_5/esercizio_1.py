def range_sum(n: int) -> int:
    if n <= 0:
        return 0
    
    somma = []    
    for i in range(n+1):
        somma.append(i)
    return sum(somma)


print(range_sum(3))