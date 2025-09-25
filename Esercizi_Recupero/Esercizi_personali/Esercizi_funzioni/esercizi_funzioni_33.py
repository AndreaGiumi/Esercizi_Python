def vendi_libri(libreria: dict[str, int]):

    # Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri in una libreria:

    # Controlla se il libro richiesto è presente sugli scaffali della libreria
    # Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
    # Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato che la vendita non ha avuto successo

    # La funzione deve restituire valore booleanoTrue o False in base all'esito della vendita

    elenco_libiri_da_ordinare: list[int] = []

    libro: str = str(input("Inserisci libro da cercare nella libreria: "))
    vendita = False
    if libro in libreria:
        vendita = True
        libreria[libro] -= 1
        print("La vendita ha avuto successo!")
        if libreria[libro] == 0:
            del libreria[libro]
            
    else:
        elenco_libiri_da_ordinare.append(libro)
        print(f"Elenco di libri da ordinare: {elenco_libiri_da_ordinare}")
        print("La vendita non ha avuto successo!")
    print("Di seguito un elenco aggiornato dei volumi presenti nel nostro scaffale:")
    print(libreria)
    return vendita



if __name__=="__main__":

    libreria: dict[str, int] = {"Harry Potter": 5, "Alice in the wonderland": 1, "Cappuccetto Rosso" : 7, "Red": 1}

    print(vendi_libri(libreria))