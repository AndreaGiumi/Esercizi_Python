def lunghezza(oggetto: str | list) -> int:

    '''
    Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro.
    In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!
    '''

    cont = 0

    for i in oggetto:
        cont += 1
    print(cont)


lunghezza([1,2,3])