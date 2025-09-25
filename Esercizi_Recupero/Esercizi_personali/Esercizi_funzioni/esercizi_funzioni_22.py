def convertitore(num: float) -> float:
    '''
    Scrivi una funzione che, dato in ingresso un valore espresso in metri,
    mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?
    '''

    conv = {}
    if num > 0:
        conv["pollici"]= num * 39.37008
        conv["miglia"] = num / 1609.344
        conv["piedi"] = num * 3.280840
        conv["iarde"]=  num * 1.093613
    print(f"{num} metri corrispondono a:")
    for key, value in conv.items():
        print(f"{key}: {value}")

convertitore(41)
