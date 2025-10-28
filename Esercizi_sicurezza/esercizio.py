def s2n(s: str):
    base = 1
    n = 0
    for c in s:
        n = n + base * ord(c)

        base *= 256
    return n



print(s2n("Ciao"))