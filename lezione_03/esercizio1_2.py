posti_max: int = int(input("Inserisci posti massimi: "))

posti_liberi = posti_max

while True:
    opzioni = input("Inserisci una tra le opzioni: ingresso, uscita, stato, esci: ")
    if opzioni == "ingresso":
        if posti_liberi > 0:
            posti_liberi -= 1
        else:
            print("Il parcheggio è pieno")
    elif opzioni == "uscita":
        if posti_liberi < posti_max:
            posti_liberi += 1
        else:
            print("Il parcheggio è già vuoto")
    elif opzioni == "stato":
        print(posti_liberi, posti_max - posti_liberi)
    elif opzioni == "esci":
        break
    else:
        print("Errore! Seleziona una tra le seguenti opzioni: ingresso, uscita, stato, esci: ")