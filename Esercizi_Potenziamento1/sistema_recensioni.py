
from __future__ import annotations

class Media:


    '''
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe
 derivata Film che rappresenti specificamente un film e ne specifichi il titolo. Gli studenti dovranno anche creare 
 oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.
 
Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
 
Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero 
mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3,
 "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio 
e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
 aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

'''
    _title: str
    _reviews: list[int]

    def __init__(self, title: str, reviews: list[int] = []):
        self.set_title(title)
        self._reviews = reviews



    def set_title(self, title: str) -> None:
        self._title = title

    def title(self) -> str:
        return self._title
    

    def aggiungiValutazione(self, voto: int) -> None:
        if voto in range(1,6):
            self._reviews.append(voto)
        else:
            raise KeyError("Il voto inserito non è valido!")


    def getMedia(self) -> float:
        sum_m = 0
        for i in self._reviews:
            sum_m += i
            media = sum_m/len(self._reviews)
        return f"{media:.2f}"
        
    
    def getRate(self) -> str:

            # if self.getMedia() <= 1:
            #     return f"Giudizio Terribile"
            # if 1 <= self.getMedia() <= 2:
            #     return f"Giudizio Brutto"
            # if 2 <= self.getMedia() <= 3:
            #     return f"Giudizio Normale"
            # if 3 <= self.getMedia() <= 4:
            #     return f"Giudizio Bello"
            # if 4 <= self.getMedia() <= 5:
            #     return f"Giudizio Grandioso"

            match self.getMedia():
                 
                 case 1:
                      return 



    def ratePercentage(self, voto):
        sum_v = 0
        for v in self._reviews:
            if v == voto:
                sum_v += v
                perc = (sum_v * len(self._reviews))/100
        return perc
    
    def recensione(self) -> str:
        return f"Titolo del Film: {self.title()}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(self.getRate())}\Brutto: {self.ratePercentage(self.getRate())}\nNormale: {self.ratePercentage(self.getRate())}\nBello: {self.ratePercentage({self.getRate()})}/nGrandioso: {self.ratePercentage(self.getRate())}"

class Film(Media):
    pass
if __name__== "__main__":


        film: Media = Media("Ciao", [])
        film1: Media = Media("Ciao2", [])

        film.set_title("Bonne")

        film.aggiungiValutazione(1)
        film.aggiungiValutazione(1)
        film.aggiungiValutazione(4)
        film.aggiungiValutazione(5)
        film.aggiungiValutazione(4)
        film.aggiungiValutazione(5)



        print(film.getMedia())

        print(film.recensione())