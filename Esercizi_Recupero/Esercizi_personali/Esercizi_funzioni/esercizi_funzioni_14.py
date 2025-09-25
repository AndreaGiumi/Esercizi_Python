def isVocale() -> bool:

    '''
    Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.
    '''
    char = str(input("Inserisci un carattere: "))
    vocali: list[str] = ["a", "e", "i", "o", "u"]

    if char.lower() in vocali:
        print(True)
    else:
        print(False)



isVocale()