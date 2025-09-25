


def specificLetter(list_word: list[str]):

    '''
    Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.

    '''

    letter: str = str(input("Specifica lettera: ")).upper()

    new_list: list[str] = []
    for word in list_word:
        if word[0] == letter:
            new_list.append(word)
    print(new_list)


list_word = ["Fragola", "Lupo", "Pallone", "Luna", "Sole", "Sale"]

specificLetter(list_word)