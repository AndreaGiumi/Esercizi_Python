def Production(n: int):
    if n == 0:
        return 2
    else:
        return (n + 2) * Production(n - 1)



print(Production(7))