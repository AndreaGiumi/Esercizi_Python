def calendario_serie_A(lista_squadre: list[str]):
    n = len(lista_squadre)

    # Se il numero di squadre è dispari, aggiungiamo una squadra fittizia (riposo)
    if n % 2 != 0:
        lista_squadre.append("Riposo")
        n += 1

    calendario: list = []

    # Rotazione round-robin
    squadre = lista_squadre[:]
    for turno in range(n - 1):
        giornata = []

        for i in range(n // 2):
            casa = squadre[i]
            trasferta = squadre[n - 1 - i]

            # Alterniamo casa/trasferta per ogni giornata
            if turno % 2 == 0:
                giornata.append((casa, trasferta))
            else:
                giornata.append((trasferta, casa))

        calendario.append(giornata)

        # Rotazione (fissa la prima squadra)
        squadre = [squadre[0]] + [squadre[-1]] + squadre[1:-1]

    # Calendario di ritorno (inverti casa/trasferta)
    calendario_ritorno = []
    for giornata in calendario:
        invertita = [(trasferta, casa) for casa, trasferta in giornata]
        calendario_ritorno.append(invertita)

    calendario_completo = calendario + calendario_ritorno

    # Stampa il calendario
    for i, giornata in enumerate(calendario_completo, start=1):
        print(f"Giornata {i}:")
        for casa, trasferta in giornata:
            if "Riposo" not in (casa, trasferta):
                print(f"  {casa} - {trasferta}")
        print()


if __name__ == "__main__":
    squadre = ["Atalanta", "Bologna", "Cagliari", "Como", "Fiorentina", "Genoa", "Hellas Verona", "Inter", "Juventus", "Lazio", "Lecce", "Milan", "Napoli", "Parma", "Roma", "Torino", "Udinese"]
    calendario_serie_A(squadre)
