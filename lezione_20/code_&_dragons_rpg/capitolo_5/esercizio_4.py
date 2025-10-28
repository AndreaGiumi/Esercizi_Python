def primes_up_to(n: int) -> list[int]:
    primes = []
    for x in range(2, n+1):
        for d in range(2, int(x**0.5) + 1):
            if x % d == 0:
                break
        else:  
            primes.append(x)
    return sorted(primes)