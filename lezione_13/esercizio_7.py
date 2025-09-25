def Production3(n:int):
    if n == 1:
        return 1
    else:
        return (n**3) * Production3(n-1)

print(Production3(5))