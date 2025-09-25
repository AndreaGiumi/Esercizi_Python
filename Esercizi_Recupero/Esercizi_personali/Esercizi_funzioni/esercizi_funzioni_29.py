def linguaggio_dei_furfanti():

    # In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket, che significa "linguaggio dei furfanti": 
    # consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".

    # Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket. 
    # Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, 
    # dovrà attendere l'inserimento di una nuova parola da parte dell'utente.
    vocali: str = "aeiou"

    while True:
        frase: str = str(input("Inserisci una frase o una parola che vuoi tradurre: "))
        frase_tradotta: str = ""

        for i in frase:
            if i.lower() in vocali:
                frase_tradotta += i
            elif frase == "":
                print("Inserire una stringa valida")
                frase: str = str(input("Inserisci una frase o una parola che vuoi tradurre: "))
            else:
                frase_tradotta += i + "o" + i

        print(f"Ecco a te la traduzione! '{frase_tradotta}'")

        risposta = str(input("Vuoi tradurre una nuova parola/frase?: ").lower())

        if risposta == "no":
            break




if __name__=="__main__":

    linguaggio_dei_furfanti()