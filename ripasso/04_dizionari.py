"""
Sezione 4 - Dizionari (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 4.1 - Classifica pari/dispari
# Funzione che prende una lista di numeri e ritorna un dizionario con
# le chiavi "pari" e "dispari", ognuna con la lista dei numeri corrispondenti.
def classifica_numeri(lista: list[int]) -> dict[str, list[int]]:
    pari: list[int] = []
    dispari: list[int] = []
    diz: dict[str, list[int]] = {"pari": pari, "dispari" : dispari}

    for n in lista:
        if n % 2 == 0:
            pari.append(n)
        else:
            dispari.append(n)
    
    return diz




# Esercizio 4.2 - Conta lettere
# Data una frase, costruisci un dizionario che conta quante volte compare
# ogni lettera (ignora gli spazi). Stampa la lettera più frequente.
def conta_lettere(frase: str) -> dict[str, int]:
    diz:dict[str, int] = {}
    new_frase: str = frase.replace(" ", "")
    for p in new_frase:
        if p in diz:
            diz[p] += 1
        else:
            diz[p] = 1
    print(diz)

    max: int = 0
    lettera: str | None = None

    for key, value in diz.items():
        if value > max:
            max = value
            lettera = key
    return f"La lettera più frequente è la \'{lettera}\', con un conteggio di {max} "


    
        



# Esercizio 4.3 - Rubrica telefonica (difficile)
# Rubrica come dizionario {nome: telefono} con menu testuale in un while:
#   1. Aggiungi contatto   2. Cerca contatto   3. Elimina contatto
#   4. Mostra tutti        5. Esci
# Gestisci contatto già esistente o inesistente.
def rubrica() -> None:
    contatti: dict[str, str] = {}



    while True:
        print("Scegli azione:\n1. Aggiungi contatto  2. Cerca contatto\n3. Elimina contatto  4. Mostra tutti\n5. Esci")

        azione: int = int(input("Inserisci il numero dell'azione che vuoi fare: "))

        if azione == 1:
            nome: str = input("Inserisci nome contatto: ").title()
            telefono: str = input("Inserisci numero di telefono: ")

            if nome not in contatti:
                contatti[nome] = telefono
            else:
                print(f"Il contatto {nome} è già presente nei tuoi contatti")
                    


        elif azione == 2:
            nome: str = input("Quale contatto vuoi cercare? ").title()

            if nome not in contatti:
                print(f"Il contatto {nome} non è presente nei tuoi contatti. Aggiungilo!!")
            else:
                print(f"Il telefono del contatto {nome} è {contatti[nome]}")
            

        elif azione == 3:
            nome: str = input("Inserisci il nome del contatto che vuoi eliminare dai tuoi contatti: ").title()

            if nome not in contatti:
                print("Il contatto che vuoi eliminare non esiste")
            else:
                del contatti[nome]


        elif azione == 4:
            for c, t in contatti.items():
                print(c, t)


        elif azione == 5:
            break

if __name__ == "__main__":
    # print(classifica_numeri([1, 2, 3, 4, 5, 6]))
    # print(conta_lettere("porco di dioooooo"))1
    rubrica()
