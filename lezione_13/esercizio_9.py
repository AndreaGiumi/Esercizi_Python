def vowelRemover(s:str):
    if s == "":
        return ""
    
    first_char = s[0].lower()

    if first_char not in "aeiou":
        return first_char + vowelRemover(s[1:])
    else:
        return vowelRemover(s[1:])
    

print(vowelRemover("sesso"))