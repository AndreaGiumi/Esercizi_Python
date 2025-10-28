import random
def f(s) -> str:
    l=[]

    for _ in range(0,100000):
        l.append(random.randint(0,1000000))
    
    for x in l:
        if s in l:
            print("Trovato")
            break

f(32)