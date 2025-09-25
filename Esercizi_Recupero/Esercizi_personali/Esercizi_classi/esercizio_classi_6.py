class Veicolo:
    '''

Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. Aggiungi poi i metodi accellera e frena. 
Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore().

'''
    __marca: str
    __modello: str
    __anno: int

    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_anno(anno)


    def set_marca(self, marca: str) -> None:
        self.__marca = marca

    def marca(self) -> str:
        return self.__marca
    
    def set_modello(self, modello: str) -> None:
        self.__modello = modello

    def modello(self) -> str:
        return self.__modello
    
    def set_anno(self, anno: int) -> None:
        self.__anno = anno

    def anno(self) -> int:
        return self.__anno
    

    def accellera(self) -> str:
        return "Sto accellerando!"
    

    def freno(self) -> str:
        return "Sto frenando!"
    
    def __str__(self) -> str:
        return f"Marca: {self.marca()}\n Modello: {self.modello()}\nAnno: {self.anno()}\n"
        
    

class Auto(Veicolo):
    __colore: str

    def __init__(self, marca, modello, anno, colore: str):
        super().__init__(marca, modello, anno)

    def set_colore(self, colore: str) -> None:
        self.__colore = colore
    
    def colore(self) -> str:
        return self.__colore
    

    def cambia_colore(self, new_colore: str) -> None:
        self.__colore = new_colore


    def __str__(self):
        return super().__str__() + f"Colore: {self.colore()}"
    

if __name__=="__main__":
    