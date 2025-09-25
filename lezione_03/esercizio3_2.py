nomeCorso = input("Inserisci nome del corso a cui vuoi partecipare: ")
max_posti: int = 100

while True:
    opzioni = input("Inserisci che opzione vuoi scegliere: iscriviti, annulla, visuaizza, elimina, esci: ")
    if opzioni =="iscriviti":
        if max_posti > 0:
            max_posti -= 1
            print("Ti sei iscritto con successo.")
        else:
            print("Non ci sono posti disponibili.")
    elif opzioni == "annulla":
        if max_posti < 100:
            max_posti += 1
            print("Hai annullato la tua iscrizione.")
        else:
            print("Tutti i posti sono già disponibili.")
    elif opzioni == "visualizza":
        print(max_posti)
        print(100 - max_posti)
    elif opzioni == "elimina":
        nomeCorso = input("Inserisci nome del nuovo corso a cui vuoi partecipare: ")
    elif opzioni == "esci":
        break
    

     
