voto: int = int(input("Inserisci voto: "))

match voto:
    # case 10
    case 10:
        print("Eccellente!")
    # case 9-8
    case 9|8:
        print("Molto buono!")
    # case 7-6
    case 7|6:
        print("Sufficiente!")
    # case 5-4
    case 5|4:
        print("Insufficiente!")
    # case 1-3
    case 3|2|1:
        print("Gravemente insufficiente!")
    # case default
    case _:
        print("Voto non valido!")