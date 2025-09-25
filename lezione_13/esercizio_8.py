def vowelsCounter(s:str):
    if s == "":
        return 0
    
    first_char = s[0].lower()

    if first_char in "aeiou":
        return 1 + vowelsCounter(s[1:])
    else:
        return vowelsCounter(s[1:])

print(vowelsCounter("Ciao"))