# from __future__ import annotations
from film import Film
from movie_genere import *
class Noleggio:
    '''
    ### CLASSE: Noleggio
    In un file "noleggio.py", creare una classe Noleggio.
    Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), un dizionario (rented_film) che ha come chiave
    un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
 
    - Definire i seguenti metodi:

    init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
    isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario.
      Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!".
        Se il film non è disponibile in negozio stampare: "Il film scelto non è disponibile: {titolo_film}!".
    rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del
      cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto,
        il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile,
          rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
        la chiave sarà l'id del cliente che noleggia (id_client)
        il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
    Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati
      dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!".
        Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".
    giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio,
      ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, 
      il numero dei giorni in cui il cliente ha tenuto il film per se.
     Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, 
     deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, 
     il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. Stampare la penale che 
     il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
    printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
    printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.

    
    '''
    __film_list: list[Film]
    __rented_film : dict[int, list[Film]]

    def __init__(self, film_list: list[Film]):
        self.setFilmList(film_list)
        self.__rented_film: dict[int, list[Film]] = {}

    
    def setFilmList(self, film_list: list[Film]) -> None:
        self.__film_list = film_list

    def getFilmList(self) -> list[Film]:
        return self.__film_list
    
    def getRentedFilm(self) -> dict[int, list[Film]]:
        return self.__rented_film
    

    def isAvailable(self, film: Film) -> bool:
        
        if film in self.getFilmList():
            print(f"Il film scelto è disponibile: {film.getTitolo()}")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitolo()}")
            return False
            
    def rentAMovie(self, film: Film, clientID: int) -> None:
        if self.isAvailable(film):
            self.getFilmList().remove(film)
            if clientID not in self.__rented_film:
                self.__rented_film[clientID] = []
            self.__rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitolo()}")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitolo()}")

    def giveBack(self, film: Azione | Commedia | Drama, clientID: int, days: int) -> None:
        if clientID in self.__rented_film and film in self.__rented_film[clientID]:
            self.__rented_film[clientID].remove(film)
            self.getFilmList().append(film)
        if days > 0:
            penale: float = film.getPenale() * days
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitolo()} e' di {penale} euro!")
        
        
    def printMovies(self) -> None:
        if not self.__film_list:
            print("Nessun film disponibile in negozio.")
        else:
            for film in self.__film_list:
                    print(f"{film.getTitolo()} - {film.getGenere()}")

    def printRentMovies(self, clientID: int) -> None:
        if clientID not in self.__rented_film or not self.__rented_film[clientID]:
            print(f"Cliente {clientID} non ha noleggiato alcun film")
        else:
            print(f"Film noleggiati dal cliente {clientID}:\n")
            for film in self.__rented_film[clientID]:
                print(f"{film.getTitolo()} - {film.getGenere()}")

if __name__=="__main__":


    # Creo dei film
    f1 = Azione(1, "Matrix")
    f2 = Drama(2, "Titanic")
    f3 = Azione(3, "Avatar")

    # Creo la videoteca con una lista iniziale
    videoteca = Noleggio([f1, f2])

    # Cliente 101 prova a noleggiare Matrix
    videoteca.rentAMovie(f1, 101)

    # Cliente 102 prova a noleggiare lo stesso film (non più disponibile)
    videoteca.rentAMovie(f1, 102)

    # Cliente 103 prova a noleggiare Avatar (mai stato disponibile)
    videoteca.rentAMovie(f3, 103)

    videoteca.giveBack(f1, 102, 4)

    # Stato attuale
    videoteca.printMovies()

    videoteca.printRentMovies(101)

    # print("\nFilm noleggiati dai clienti:")









