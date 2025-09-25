def lista_colori():
    # Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. '
    # 'Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.


    lista_colori: list[str] = []

    while len(lista_colori) <= 9:
        colore: str = str(input("Inserisci un colore: "))

        if colore == "":
            print("Un colore non può essere una stringa vuota.")
            colore: str = str(input("Inserisci un colore: "))
        else:
            lista_colori.append(colore)

    lettera: str = str(input("Inserisci iniziale: "))

    for colore in lista_colori:
        if colore.startswith(lettera) is True:
            print(f"Il colore che inizia con la lettera {lettera.upper()} è: {colore.capitalize()}")



lista_colori()