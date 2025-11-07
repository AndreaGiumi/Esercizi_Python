def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    '''
    Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
    ''' 

    for key in dizionario:
        if valore == dizionario[key]:
            return key
    return None