def rubrica_telefonica():
    rubrica: dict[str, int] = {}
    # aggiunge contatti alla rubrica
    while True:
        risposta = str(input("Vuoi aggiungere un numero di telefono alla rubrica? S/N ")).upper()
        if  risposta == "S":

            nome: str = str(input("Inserisci nome: ")).capitalize()

            num_tel: int = int(input("Inserisci numero di telefono: "))

            rubrica[nome] = num_tel
    
        elif risposta == "N":
            print("Fine inserimento!")
            break
        else:
            print("Risposta non valida. Inserisci S o N.")

    # stampa i contatti della rubrica in ordine alfabetico
    for nome in sorted(rubrica.keys()):
        print(f"{nome} : {rubrica[nome]}")
    return rubrica
    
def cerca_contatto(rubrica: dict[str, int]):
    # cerca un contatto (tramite il nome) all'interno della rubrica
    risposta = str(input("Vuoi cercare un contatto specifico nella rubrica? S/N ")).upper()
    while True:
        if risposta == "S":           
            contatto_da_cercare:str = str(input("Inserisci nome contatto: ")).capitalize()

            if contatto_da_cercare in rubrica:
                return f"{contatto_da_cercare}: {rubrica[contatto_da_cercare]}"
            else:
                return "Il contatto che stai cercando non è in rubrica!"
        elif risposta == "N":
             print("Fine ricerca")
             break
        else:
            print("Risposta non valida. Inserisci S o N.")
        
    for nome in sorted(rubrica.keys()):
        print(f"{nome} : {rubrica[nome]}")
    

def elimina_contatto(rubrica: dict[str, int]):
    # elimina un contatto dalla rubrica
    risposta = str(input("Vuoi eliminare un contatto? S/N ")).upper()
    while True:
        if risposta == "S":
            contatto_da_eliminare: str = str(input("Inserisci nome contatto: ")).capitalize()
        
        if contatto_da_eliminare in rubrica:
            rubrica.pop(contatto_da_eliminare)
            return rubrica
        elif risposta == "N":
            print("Fine")
        else:
            print("Risposta non valida. Inserisci S o N.")
    
        
    

if __name__=="__main__":

    rubrica = rubrica_telefonica()

    print(cerca_contatto(rubrica))
    print(elimina_contatto(rubrica))