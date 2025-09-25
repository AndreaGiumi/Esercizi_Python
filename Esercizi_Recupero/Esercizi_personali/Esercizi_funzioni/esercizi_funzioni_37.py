def conta_char(parola: str, char: str):
    count = 0
    for i in parola:
        if i == char:
            count += 1
    print(count)



conta_char("Ciaaaaaaaaaao", "a")