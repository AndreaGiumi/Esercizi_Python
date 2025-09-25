def baricentro(v: list[int]):
    for i in range(len(v)):
        if sum(v[:i+1]) == sum(v[i+1:]):
            return i
    return None

def printResult(v: list[int]):
    if baricentro(v) == None:
        return f"Il baricentro del vettore v={v} non esiste!" 
    else:
        return f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={baricentro(v)}!"

def baricentroOttimizzato(v: list[int]):
    total = sum(v)
    somma_s = 0

    for i in range(len(v)):
        somma_r = total - somma_s
        if somma_s == somma_r:
            return i
        somma_s += v[i]
    return None
        

if __name__=="__main__":
    v1 = [1, 2, 3, 2, 5, 2, 1]
    v2 = [2, 0, -1, 4, 6, 3, -1]

    print(baricentro(v1))
    print(printResult(v1))
    print(baricentroOttimizzato(v1))
    print("-----------------------------------")
    print(baricentro(v2))
    print(printResult(v2))
    print(baricentroOttimizzato(v2))