# Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
# classifichi i numeri in liste separate per numeri positivi e negativi

def convert2(lista_num: list[int|float]) ->dict[str, list[int|float]]:
    dict1: dict[str, list[str, int|int]] = {"positivi": [], "negativi": []}
    for elem in lista_num:
        if elem >= 0:
            dict1["positivi"].append(elem)
        else:
            dict1["negativi"].append(elem)
    return dict1

            


print(convert2([2, 5, 47, 4, 25, -98]))