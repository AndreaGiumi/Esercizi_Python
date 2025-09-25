nome: str = str(input("Inserisci il tuo nome: "))
gender: str = str(input("Digitare m per Maschio e f per Femmina: "))

match gender:
    # caso = m
    case "m":
        print(f"Nome: {nome} Gender: Maschio")
    # caso = f
    case "f":
        print(f"Nome: {nome} Gender: Femmina")
    # caso default
    case _:
        print(f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")




