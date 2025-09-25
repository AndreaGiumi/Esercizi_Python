'''
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:

    Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
    Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese

La classe dovrà avere i seguenti metodi:

    Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
    Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
    Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino

Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

'''



class Prodotto:
    _nome: str
    _prezzo: float
    _scorta: int

    def __init__(self, nome: str, prezzo: float, scorta: int) -> None:
        self.set_nome(nome)
        self.set_prezzo(prezzo)
        self.set_scorta(scorta)

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

    def set_prezzo(self, prezzo: float) -> None:
        self._prezzo = prezzo

    def prezzo(self) -> float:
        return self._prezzo

    def set_scorta(self, scorta: int) -> None:
        self._scorta = scorta

    def scorta(self) -> int:
        return self._scorta


class GestoreMagazzino:
    _costo_magazzinaggio: float
    
    def __init__(self, costo_magazzinaggio: float) -> None:
        self._prodotti: dict[str, Prodotto] = {}
        self.set_costo_magazzinaggio(costo_magazzinaggio)

    def set_costo_magazzinaggio(self, costo_magazzinaggio: float) -> None:
        self._costo_magazzinaggio = costo_magazzinaggio

    def costo_magazzinaggio(self) -> float:
        return self._costo_magazzinaggio

    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        self._prodotti[prodotto.nome()] = prodotto

    def rimuovi_prodotto(self, nome_prodotto: str) -> None:
        if nome_prodotto in self._prodotti:
            del self._prodotti[nome_prodotto]

    def calcola_costo_magazzinaggio(self) -> float:
        costi = 0
        for prodotto in self._prodotti.values():
            costi += prodotto.scorta() * self._costo_magazzinaggio
        return costi


if __name__ == "__main__":
    p = Prodotto("Barretta", 2.50, 10)
    p1 = Prodotto("Pane", 1.50, 100)
    p2 = Prodotto("Coca Cola", 2.50, 50)
    p3 = Prodotto("Acqua", 2.50, 150)

    magazzino = GestoreMagazzino(10)

    magazzino.aggiungi_prodotto(p)
    magazzino.aggiungi_prodotto(p1)
    magazzino.aggiungi_prodotto(p2)
    magazzino.aggiungi_prodotto(p3)

    print("Costo totale di magazzinaggio:", magazzino.calcola_costo_magazzinaggio())
