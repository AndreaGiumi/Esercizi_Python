def lenWord(list_word: list[str]):

    '''
    Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola
    '''
    lista_lunghezze: list[int] = []

    for word in list_word:
        lista_lunghezze.append(len(word))
    print(lista_lunghezze)


lista_word: list[str] = ["Ciao", "Cane", "Porco Dio", "Madonna Troia", "Diocanebastardo"]


lenWord(lista_word)