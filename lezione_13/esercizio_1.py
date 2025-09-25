def recursivePower(a:int, b:int):
    if b == 0:
        return 1
    else:
        return int(a * recursivePower(a, b - 1))


print(recursivePower(3,4))
print(recursivePower(4,3))
print(recursivePower(2,5))
print(recursivePower(5,2))
