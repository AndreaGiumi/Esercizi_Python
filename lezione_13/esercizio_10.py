def charDuplicator(s:str):

    if s == "":
        return ""
    
    first_char = s[0].lower()

    return first_char * 2 + charDuplicator(s[1:])

print(charDuplicator("Vino"))
