def recursiveFactorial(a:int):
    if a < 2:
        return 1
    else:
        return a * recursiveFactorial(a - 1)
    


print(recursiveFactorial(100))


