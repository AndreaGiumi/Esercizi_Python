class Specie:
    _nome: str
    _popolazione: int
    _tasso_crescita: float

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        self.set_nome(nome)
        self.set_popolazione(popolazione)
        self.set_tasso_crescita(tasso_crescita)



    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_popolazione(self, popolazione: int) -> None:
        self._popolazione = popolazione

    def popolazione(self) -> int:
        return self._popolazione
    
    def set_tasso_crescita(self, tasso_crescita: float) -> None:
        self._tasso_crescita = tasso_crescita

    def tasso_crescita(self) -> float:
        return self._tasso_crescita
    

    def crescita(self) -> int:
        nuova_popolazione: int = int(self.popolazione() * (1 + self.tasso_crescita()/100))
        return nuova_popolazione
    

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        pass
        

            
    

    def getDensita(self, area_kmq: float) -> int:
        '''
        Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²

        '''
        popolazione: int = self.popolazione()
        anni: int = 0
        densita = popolazione / area_kmq
        while densita < 1:
            densita = popolazione / area_kmq
            anni += 1

        return anni








class BufaloKlingon(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__(BufaloKlingon, popolazione, tasso_crescita)



class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__(Elefante, popolazione, tasso_crescita)
