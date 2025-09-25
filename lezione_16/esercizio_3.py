class Veicolo:
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
    
    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca()}\nModello: {self.modello()}\nAnno: {self.anno()}")




class Auto(Veicolo):
    _numero_porte: int
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.set_numeroPorte(numero_porte)

    def set_numeroPorte(self, numero_porte:int) -> None:
        self._numero_porte = numero_porte

    def numero_porte(self) -> int:
        return self._numero_porte


    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca()}\nModello: {self.modello()}\nAnno: {self.anno()}\nNumero Porte: {self.numero_porte()}")


class Moto(Veicolo):
    _tipo: str
    def __init__(self, marca: str, modello: str, anno: str, tipo: str):
        super().__init__(marca, modello, anno)

        self.set_tipo(tipo)

    def set_tipo(self, tipo: str) -> None:
        self._tipo = tipo

    def tipo(self) -> str:
        return self._tipo
    

    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca()}\nModello: {self.modello()}\nAnno: {self.anno()}\nTipo: {self.tipo()}")

        
if __name__=="__main__":
    # compass: Veicolo = Veicolo("Jeep", "Compass", 2021)

    compass: Auto = Auto("Jeep", "Compass", 2021, 5)
    compass.descrivi_veicolo()