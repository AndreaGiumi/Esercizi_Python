def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    '''
    Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
    Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
    '''

    diz = {}
    for inner_tuple, valore_tupla in tuples:
        if inner_tuple not in diz:
            diz[inner_tuple] = [valore_tupla]
        else:
            diz[inner_tuple].append(valore_tupla)

    return diz


print(lista_a_dizionario([("dio", 25), ("ei", 1), ("ei", 27)]))




