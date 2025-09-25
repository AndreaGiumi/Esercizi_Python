def rimario(parole: list[str]):

    # Scrivi una semplice funzione rimario, a cui viene passato un elenco di parole come parametro e che riceva una parola 
    # inserita dall'utente tramite la funzione input.

    # La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco passato, alla ricerca di rime, 
    # intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

    # Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.

    parola: str = str(input("Inserisci la parola da controllare: "))
    # con list comprehension
    rime: list[str] = [el for el in parole if parola[-3:] == el[-3:]]

    # for word in parole:
    #     if word[-3:] == parola[-3:]:
    #         rime.append(word)
        
    if not rime:
        print("Non sono state trovate rime!")
    else:
        output = ", ".join(el for el in rime)
        print(f"Le rime corrispondenti alla parola {parola} sono le seguenti: {output}")


lista_parole = ["cane", "sapore", "frizzante", "colore", "limone"]

rimario(lista_parole)