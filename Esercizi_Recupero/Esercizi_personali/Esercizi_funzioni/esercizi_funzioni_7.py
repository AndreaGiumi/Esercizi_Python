def lenWord(lista_word: list[str]):
    '''
    Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga
    '''
    max_len: str = lista_word[0]
    for word in lista_word:
        if len(word) > len(max_len):
            max_len = word
    print(max_len)


lista_word: list[str] = ["Ciao", "Cane", "Porco Dio", "Madonna Troia", "Diocanebastardo"]

lenWord(lista_word)