def counter_words(text:str) -> dict[str, int]:
    d: dict[str, int] = {}
    text: str = text.lower()
    for parola in text:
        if parola not in d:
            d[parola] = 1
        else:
            d[parola] += 1
    
    return d


text: str = "CCAiaco a tuttiiiiii"

d = counter_words(text)

for word in d:
    print(f"{word}: {d[word]}")


print(d)