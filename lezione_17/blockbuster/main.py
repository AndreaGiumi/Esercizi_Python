from film import Film
from movie_genere import Azione, Commedia, Drama
from noleggio import Noleggio

if __name__=="__main__":
        
    film1:Azione = Azione(1, "Matrix")
    film2: Azione = Azione(2, "John Wick")
    film3: Azione = Azione(3, "Mad Max")
    film4: Azione = Azione(4, "Gladiator")
    film5: Azione = Azione(5, "Inception")

    film6: Commedia = Commedia(6, "The Mask")
    film7: Commedia = Commedia(7, "Una notte da leoni")
    film8: Commedia = Commedia(8, "Mamma ho perso l’aereo")
    film9: Commedia = Commedia(9, "Scary Movie")

    film10: Drama = Drama(10, "La vita è bella")

    lista_film: list[Film] = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film10]

    noleggio_film: Noleggio = Noleggio(lista_film)

    print("Quale film vuoi noleggiare?")
    

    noleggio_film.rentAMovie(film2, 101)
    noleggio_film.rentAMovie(film3, 101)
    noleggio_film.rentAMovie(film3, 102)
    noleggio_film.rentAMovie(film10, 102)
    noleggio_film.giveBack(film3, 101, 4)
    noleggio_film.printMovies()