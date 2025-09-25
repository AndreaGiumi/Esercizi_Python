class Persona:
    __nome: str
    __eta: int
    __sesso: str

    '''
    Definire la classe Persona con attributi nome, età e sesso (M/F). La funzione di __init__ della classe deve prendere come argomento solo il nome della persona,
    mentre l'età va impostata automaticamente a ZERO e il sesso a "M" (o "F", scegliete voi).

    Aggiungere i metodi invecchia (aggiunge un anno di età) e saluta (restituisce "signore" o "signora" a seconda del sesso della persona).

    Definire 2 persone: "Augusto", maschio di 47 anni e "Marianna", femmina di 44 anni. Utilizzare i metodi invecchia e saluta per entrambi, 

    procedere poi a visualizzare gli attributi di entrambi.
    '''

    def __init__(self, nome: str, eta: int = 0, sesso: str = "M") -> None:
        self.set_nome(nome)
        self.__eta = eta
        self.__sesso = sesso



    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    
    def nome(self) -> str:
        return self.__nome
    

    def invecchia(self) -> None:
        self.__eta += 1

    def saluta(self) -> str:
        if self.__sesso == "M":
            return f"Signore"
        if self.__sesso == "F":
            return f"Signora"
        
    def __str__(self) -> str:
        return f"{self.__nome}, {self.__sesso} di {self.__eta} anni"
    

if __name__=="__main__":
        a: Persona = Persona("Augusto", 47, "M")
        print(a)
        a.invecchia()
        print(a)
        print(a.saluta())
        m: Persona = Persona("Marianna", 44, "F")
        print(m)
        m.invecchia()
        print(m)
        print(m.saluta())