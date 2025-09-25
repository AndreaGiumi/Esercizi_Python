'''

Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

'''


class Animale:
    _nome: str
    _specie: str

    def __init__(self, nome: str, specie: str) -> None:
        self.set_nome(nome)
        self.set_specie(specie)



    def set_nome(self, nome: str) -> None:
        self._nome = nome


    def nome(self) -> str:
        return self._nome
    

    def set_specie(self, specie: str) -> None:
        self._specie = specie


    def specie(self) -> str:
        return self._specie
    


    def emetti_suono(self) -> str:
        if self.specie() == "Gatto":
            return "Miao"
        elif self.specie() == "Cane":
            return "Bau"
        else:
            return "Suono sconosciuto!"
        

if __name__=="__main__":
    
    c: Animale = Animale("Bobby", "Cane")

    print(c.emetti_suono())

    
