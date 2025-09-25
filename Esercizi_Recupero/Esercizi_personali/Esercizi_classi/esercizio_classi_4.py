'''
Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e
 “stipendio”. Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10%
   e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

'''


class Impiegato:
    _nome: str
    _cognome: str
    _matricola: str
    _stipendio: float


    def __init__(self, nome: str, cognome: str, matricola: str, stipendio: float) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_matricola(matricola)
        self.set_stipendio(stipendio)


    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def cognome(self) -> str:
        return self._cognome
    
    def set_matricola(self, matricola: str) -> None:
        self._matricola = matricola


    def matricola(self) -> str:
        return self._matricola
    

    def set_stipendio(self, stipendio: float) -> None:
        self._stipendio = stipendio


    def stipendio(self) -> float:
        return self._stipendio
    

    def aumenta_stipendio(self) -> float:
        self._stipendio *= 1.1
        # return f"stipendio aumentato: {new_stip:.2f}"
    
    def stampa_dettagli(self) -> str:
        return f"Impiegato: {self.nome()} {self.cognome()}, matricola: {self.matricola()}, stipendio: {self.stipendio():.2f} €"
    

if __name__=="__main__":
    c:Impiegato = Impiegato("Andri", "Giumi", "GM54I", 3000)

    print(c.stampa_dettagli())
    c.aumenta_stipendio()
    print(c.stampa_dettagli())
