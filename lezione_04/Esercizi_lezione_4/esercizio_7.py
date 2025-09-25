def roman_conversion(n: int) -> str:
    conversion: dict[str, int] = {
        "M": 1000,
        "CM" : 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC" : 90,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,

    }

    c: str = ""
    
    for key, value in conversion.items():
        if n == 0:
            raise ValueError("Non esiste lo zero nei numeri romani")
        if n > 3999:
            raise ValueError("Questo numero non può essere rappresentato.")
        while n >= value:
                c += key
                n -= value
    return c






print(roman_conversion(456))
