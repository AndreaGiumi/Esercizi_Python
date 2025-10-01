def flatten_once(nested: list[list[int]]) -> list[int]:
    lista_appiattita = []
    if not nested:
        return  []
    else:
        for liste in nested:
            for i in liste:
                lista_appiattita.append(i)
        return lista_appiattita