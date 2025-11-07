def filtra_e_mappa(prodotti: dict[str,float]) -> dict[str,float]:

    '''
    Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti
    che hanno un prezzo superiore a 20, ma scontati del 10%.
    '''
    sconto = 0
    new_diz = {}
    for k in prodotti:
        if prodotti[k] > 20:
            sconto = prodotti[k] - prodotti[k] * 0.1
            new_diz[k] = sconto
    return new_diz


if __name__=="__main__":
    prod = {"mele": 15, "pane" : 44, "carne" : 55}

    print(filtra_e_mappa(prod))