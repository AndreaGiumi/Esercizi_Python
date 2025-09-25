'''
Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo 
“descrivi” che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.

'''



class Automobile:
    _marca: str
    _modello: str
    _anno: int

    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_anno(anno) 


    def set_marca(self, marca: str) -> None:
        self._marca = marca

    def marca(self) -> str:
        return self._marca
    

    def set_modello(self, modello: str) -> None:
        self._modello = modello

    def modello(self) -> str:
        return self._modello
    
    def set_anno(self, anno: int) -> None:
        self._anno = anno

    def anno(self) -> int:
        return self._anno
    

    def descrivi(self) -> str:
        return f"Questa è una {self.marca()} {self.modello()} del {self.anno()}"
    


if __name__=="__main__":
    m: Automobile = Automobile("Fiat", "Freemont", 2018)


    print(m.descrivi())