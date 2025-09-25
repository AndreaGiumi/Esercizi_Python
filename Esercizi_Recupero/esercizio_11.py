import string
def count_unique_words(text:str):
    
    dict_n = {}
    x = []
    parola = ""
    for c in text.lower():
        if c.isalpha():
            parola += c
        else:
            x.append(parola)
            parola = ""

    x = list(filter(None, x))
    
    for i in x:
        if i not in dict_n:
            dict_n[i] = 1
        else:
            dict_n[i] += 1


    print(dict_n) 



count_unique_words("Originally formulated for several-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.")
