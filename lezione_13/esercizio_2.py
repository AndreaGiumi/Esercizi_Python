
def compoundInterest(m:float, t:int) -> float:
#     if t == 0:
#         return m
    
#     return compoundInterest(m * 1.005, t - 1)





    if m < 0.00:
        print("Errore")
        return 0.00
    elif m == 0.00:
        return 0.00
    else:
        if t <= 0:
            return round(m,2)
        else:
            return round(1.005 * compoundInterest(m,t-1), 2)
    

m = 10000
t = 1

k = compoundInterest(m,t)

print(round(k))