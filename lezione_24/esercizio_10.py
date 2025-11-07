def frequency_dict(elements: list) -> dict:
    '''
    Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
    '''
    new_diz = {}
    for item in elements:
        if item not in new_diz:
            new_diz[item] = 1
        else:
            new_diz[item] += 1
    return new_diz