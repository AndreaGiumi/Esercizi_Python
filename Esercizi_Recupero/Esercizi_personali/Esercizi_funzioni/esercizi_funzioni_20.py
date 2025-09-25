def len_char_pro(lista_word: list[str]) -> list[int]:

    '''
    Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la
      lunghezza delle parole contenute in A.

    Questo esercizio può essere risolto anche usando una list comprehension.
    '''


    lista_B = [len(i) for i in lista_word]

    print(lista_word)
    print(lista_B)


lista_A = ["ciao", "Come va?", "Andrea"]

len_char_pro(lista_A)