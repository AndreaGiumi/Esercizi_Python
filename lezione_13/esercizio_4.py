def recursiveDigitCounter(n:int):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + recursiveDigitCounter(n//10)


        
    


print(recursiveDigitCounter(352524))