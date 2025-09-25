mammiferi: str = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili: str = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: str = ["aquila", "pappagallo", "gufo", "falco"]
pesci: str = ["squalo", "trota", "salmone", "carpa"]

animale: str = str(input("Digita il nome di un animale: "))

anitype: str

match animale:
    # case 1
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria mammiferi!")
        anitype = "mammifero"
    # case 2
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria rettili!")
        anitype = "rettile"
    # case 3
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria uccelli!")
        anitype = "uccello"
    # case 3
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria pesci!")
        anitype = "pesce"
    # case default
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")