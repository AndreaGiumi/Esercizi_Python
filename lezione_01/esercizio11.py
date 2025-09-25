liberi = 20

while True:
    opzioni: str = input("Inserisci opzioni tra: prenota, libera, visualizza, esci:  ")
    if opzioni == "prenota":
        if liberi > 0:
            liberi -= 1
        else:
            print("Non ci sono posti disponibili.")
    elif opzioni == "libera":
        if liberi < 20:
            liberi += 1
            print("Tutti i posti sono già disponibili.")
    elif opzioni == "visualizza":
        print(liberi)
        print(20 - liberi)
    elif opzioni == "esci":
        break
    else:
        print("Errore, inserire una delle opzioni disponibii tra: prenota, libera, visuaizza, esci")

