def palidrom_word(lista_parole: list[str]) -> str:
    '''
    Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.
    '''
    lista_palindomi: list[str] = []
    for word in lista_parole:
        new_word = word.replace(" ", "").lower()
        if new_word == new_word[::-1]:
            lista_palindomi.append(new_word)
    print(lista_palindomi)

lista_word: list[str] = ["Anna", "I topi non avevano nipoti", "Porco Dio", "Madonna Troia", "Dio cane bastardo"]


palidrom_word(lista_word)