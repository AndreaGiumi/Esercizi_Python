def chunk(lst: list[int], size: int) -> list[list[int]]:
    carovana: list[list[int]] = []

    if size < 0:
        return []

    if not lst:
        return []
    else:
        squadra: list[int] = []

        
    for i in lst:
        squadra.append(i)
        if len(squadra) == size:
            carovana.append(squadra)
            squadra: list[int] = []
        
    if squadra:
            carovana.append(squadra)
    return carovana

    

if __name__=="__main__":

    plotone: list[int] = [1, 2, 3, 52, 14, 147, 58, 4, 26, 258, 874, 6985 ,458, 5658, 55, 22, 14, 77, 88, 99 ,63]


    print(chunk(plotone, 4))