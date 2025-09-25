# Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
# restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
# con i prezzi aumentati del 10% e arrotondati a due cifre decimali.


def prod(dict1:dict[str, int|float]) ->dict[str, int|float]:
    dict2: dict[str, int|float] = {}
    for key, value in dict1.items():
        if value <= 50:
            dict2[key] = value + (value * 0.1)
        else:
            continue
    
    return dict2

        
