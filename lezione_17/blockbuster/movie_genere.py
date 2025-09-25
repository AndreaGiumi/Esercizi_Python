
from film import Film
class Azione(Film):

    '''
    Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Ognuna di queste classi ha un attributo privato di tipo string 
    chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. I film di azione 
    hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

    - Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

    Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py"
    '''
    __genere: str
    __penale: float

    def __init__(self, id: int, titolo: str):
        super().__init__(id, titolo)

        self.__genere = "Azione"

        self.__penale = 3.00
    
    def getGenere(self) -> str:
        return self.__genere
    

    def getPenale(self) -> float:
        return self.__penale
    
    def calcoloPenaleRitardo(self, giorni_ritardo: int):
        penale: float = self.getPenale() * giorni_ritardo
        print("Tariffe penalita giornaliere in base al genere:\nAzione: 3€;\nCommedie: 2.50€;\nDrammatici: 2€")
        print("----------------------------------------------")
        print(f"La penale da pagare per il film: {self.getTitolo()}, con ID: {self.getID()}, genere: {self.getGenere()}, è di: {penale}€")
        return penale
        
class Commedia(Film):
    __genere: str
    __penale: float

    def __init__(self, id: int, titolo: str):
        super().__init__(id, titolo)

        self.__genere = "Commedia"
        self.__penale = 2.50


    def getGenere(self) -> str:
        return self.__genere


    def getPenale(self) -> float:
        return self.__penale
    
    def calcoloPenaleRitardo(self, giorni_ritardo: int):
        penale: float = self.getPenale() * giorni_ritardo
        print("Tariffe penalita giornaliere in base al genere:\nAzione: 3€;\nCommedie: 2.50€;\nDrammatici: 2€")
        print("----------------------------------------------")
        print(f"La penale da pagare per il film: {self.getTitolo()}, con ID: {self.getID()}, genere: {self.getGenere()}, è di: {penale}€")
        return penale


class Drama(Film):
    __genere: str
    __penale: float

    def __init__(self, id: int, titolo: str):
        super().__init__(id, titolo)

        self.__genere = "Drama"
        self.__penale = 2.00


    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcoloPenaleRitardo(self, giorni_ritardo: int):
        penale: float = self.getPenale() * giorni_ritardo
        print("Tariffe penalita giornaliere in base al genere:\nAzione: 3€;\nCommedie: 2.50€;\nDrammatici: 2€")
        print("----------------------------------------------")
        print(f"La penale da pagare per il film: {self.getTitolo()}, con ID: {self.getID()}, genere: {self.getGenere()}, è di: {penale}€")
        return penale

if __name__=="__main__":

    film1: Azione = Azione(27, "Redivivo")
    film2: Drama = Drama(747, "La vita è bella")

    # print(film1.getGenere())
    # print(film1.getPenale())
    # film1.calcoloPenaleRitardo()

    film2.calcoloPenaleRitardo()


