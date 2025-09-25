import random
import re

class Creatura:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.setNome(nome)


    def setNome(self, nome: str) -> None:
        if nome:
            self._nome = nome
        else:
            self._nome = "Creatura Generica"
        
    def nome(self) -> str:
        return self._nome
    


    def __str__(self) -> str:
        return f"Creatura: {self._nome}"
    



    '''
    
Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero 
    intero positivo casuale tra 10000 e 90000.

Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
 

    il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi i
      cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.

    il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli.
 Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: "Attenzione! 
 Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

    il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)



    '''
    

class Alieno(Creatura):
    _matricola: int
    _munizioni: list[int]

    def __init__(self,nome) -> None:
        super().__init__(nome)

        self._setMatricola()
        self._setMunizioni()
        self._nome = nome

        if self._nome != "Robot-":
            self._nome ="\"Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!\""
        else:
            self._nome = f"Robot-{self._matricola}"





    def _setMatricola(self) -> int:
        self._matricola = random.randint(10000, 90000)
        return self._matricola


    def _setMunizioni(self) -> list[int]:
        self._munizioni = [i**2 for i in range(15)]
        return self._munizioni

    def get_matricola(self) -> int:
        return self._matricola
    
    def get_munizioni(self) -> list[int]:
        return self._munizioni
    


    def __str__(self):
        return f"Alieno: {self._nome}"
    


class Mostro(Creatura):

    _urlo_vittoria: str
    _gemito_sconfitta: str
    _assalto: list[int]


    def __init__(self, nome, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)
        self.setUrlo_vittoria(urlo_vittoria)
        self.setGemito_sconfitta(gemito_sconfitta)
        self._set_assalto()



    def setUrlo_vittoria(self, urlo_vittoria: str) -> None:
        self._urlo_vittoria = urlo_vittoria


    def setGemito_sconfitta(self, gemito_sconfitta: str) -> None:
        self._gemito_sconfitta = gemito_sconfitta


    def _set_assalto(self) -> list[int]:
        self._assalto = [random.randint(1, 100) for i in range(15)]
        return self._assalto
    
    def get_assalto(self) -> list[int]:
        return self._assalto

    def getUrlo_vittoria(self) -> str:
        return self._urlo_vittoria
    

    def getGemito_sconfitta(self) -> str:
        return self._gemito_sconfitta
    

    def _setVittoria(self, vittoria: str):
        if vittoria:
            self.vittoria = vittoria
        else:
            self.setUrlo_vittoria() == "GRAAAHHH"

    def _setSconfitta(self, sconfitta: str):
        if sconfitta:
            self.sconfitta = sconfitta
        else:
            self.setGemito_sconfitta() == "Uuurghhh"



    def __str__(self):
        new_name = ""
        for index, i in enumerate(self._nome):
            if index % 2 != 0:
                i = i.upper()
            new_name += i
        return f"Mostro: {new_name}"


    
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []

    for i, j in zip(a, b):
        if i % 2 == 0 and j % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c

def combattimento(a: Alieno, m: Mostro) -> None:
    a1 = a.get_munizioni()
    m1 = m.get_assalto()
    p_u = pariUguali(a1, m1)

    print("Combattimento")

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("La/e creatura/e inserita/e non sono valide! ")
        return None
        
    if p_u.count(1) > 4:
        print((f"{m.getUrlo_vittoria()} \n") * 3) 
        return m
    else:
            
        print((f"{m.getGemito_sconfitta()} \n") * 3)
        return a






 
def proclamaVincitore(c):
    testo = str(c)  
    lunghezza = len(testo) + 10 
    altezza = 5  

    for i in range(altezza):
        if i == 0 or i == altezza - 1:
            print("*" * lunghezza)
        elif i == 2:
            
            print("*" + " " * 4, end="")  
            print(testo, end="")         
            spazi_restanti = lunghezza - 1 - (4 + len(testo))
            print(" " * spazi_restanti + "*") 
        else:
            
            print("*" + " " * (lunghezza - 2) + "*")

            

if __name__ == "__main__":


    m: Mostro = Mostro("Gino", "GRAAAHHH", "Uuurghhh")
    a: Alieno = Alieno("Robot-")

    print(a)
    print(a.get_munizioni())
    print(m)
    print(m.get_assalto())
    c = combattimento(a, m)

    proclamaVincitore(c)