'''
Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

'''


class Persona:

    _nome: str
    _età: int
    _sesso: str

    def __init__(self, nome: str, età: int, sesso: str) -> None:
        self.set_nome(nome)
        self.set_età(età)
        self.set_sesso(sesso)


    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    
    def nome(self) -> str:
        return self._nome
    

    def set_età(self, età: int) -> None:
        self._età = età


    def età(self) -> int:
        return self._età
    

    def set_sesso(self, sesso: str) -> None:
        self._sesso = sesso


    def sesso(self) -> str:
        return self._sesso
        
    def presentati(self) -> str:
        return  f"Ciao, mi chiamo {self.nome()} ed ho {self.età()} anni!"
    


if __name__=="__main__":
    p: Persona = Persona("Andrea", 28, "Maschio")


    print(p.presentati())