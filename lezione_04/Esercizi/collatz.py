
# def f(n: int):
#     if n % 2 == 0:
#         return n / 2
#     else:
#         return (3 * n) + 1
    

# def collotz(c: int):
#     coll = f(c)
#     while True:

#         if coll == 1:
#             break
        
#         r = f(c)

#     return r
        

# print(collotz(6))

# import matplotlib.pyplot as plt

def collatz(n:float) ->list[float]:
    numeri:list = [n]

    while n!= 1:

        if n % 2 == 0:

            n  = n / 2

        else:

            n = (3 * n) + 1

        numeri.append(n)
    
    return numeri


print(collatz(5))