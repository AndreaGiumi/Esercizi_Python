

def reverseString(word: str):
    '''
    Scrivi una funzione che prende una stringa e restituisce la stringa invertita.

    '''
    new_word: str = ""
    indice = len(word) - 1


    while indice >= 0:
        new_word += word[indice]
        indice -= 1
    print(new_word.lower())


reverseString("LLLO")