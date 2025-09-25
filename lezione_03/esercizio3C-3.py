oggetti: str = []

for i in range(3):
    oggetto:str = str(input("Inserisci oggetto: "))
    oggetti.append(oggetto.lower())
   
match oggetti:
    # case 1
    case ["uova", "pane", "latte"]:
        print("Prodotti alimentari")
    # case 2
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    # case 3
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    # case 4
    case["telefono", "computer", "tablet"]:
        print("Dispositivi elettrnici")
    # case default
    case _:
        print("Categoria sconosciuta")
