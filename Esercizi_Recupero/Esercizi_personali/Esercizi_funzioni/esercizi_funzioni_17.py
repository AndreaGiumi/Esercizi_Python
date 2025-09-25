from typing import Any
def indice(lista_casuale: Any):

    '''
    Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.

    Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
    '''

    oggetto = str(input("Inserisci elemento da trovare: "))
    trovato = False

    for el in lista_casuale:
        if el == oggetto:
            trovato = True
            break
    if trovato:
        print(f"{oggetto} è nella lista con indice {lista_casuale.index(oggetto)}")
    else:
        print(f"{oggetto} non è nella lista.")

            



lista_casuale: list[Any] = ["Ciao", "Telefono", "PC", "Roma", "Scarpa", "Sandalo", "Andrea" ]


indice(lista_casuale)