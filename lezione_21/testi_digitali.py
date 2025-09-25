class Documento:
    _testo: str
    def __init__(self, testo: str) -> None:
        self.setText(testo)



    def setText(self, testo: str) -> None:
        self._testo = testo


    def getText(self) -> str:
        return self._testo
    


    def isInText(self, word: str) -> bool:
        if word in self._testo:
            return True
        return False
    

class Email(Documento):
    _testo: str
    _mittente: str
    _destinatario: str
    _titolo_messaggio: str

    def __init__(self,*, testo, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(testo)

        self.set_mittente(mittente)
        self.set_destinatario(destinatario)
        self.set_titoloMessaggio(titolo_messaggio)

    def set_mittente(self, mittente: str) -> None:
        self._mittente = mittente


    def set_destinatario(self, destinatario: str) -> None:
        self._destinatario = destinatario


    def set_titoloMessaggio(self, titolo_messaggio: str) -> None:
        self._titolo_messaggio = titolo_messaggio


    def mittente(self) -> str:
        return self._mittente
    
    def destinatario(self) -> str:
        return self._destinatario
    
    def titolo_messaggio(self) -> str:
        return self._titolo_messaggio
    

    def getText(self) -> str:
        return f"Da: {self.mittente()}, A: {self.destinatario()}/nTitolo: {self.titolo_messaggio()}\nMessaggio: {super().getText()}"
    

    def writeToFile(self, nomePercorso: str) -> None:
        self.nomePercorso = nomePercorso
        contenuto = self.getText()
        with open(nomePercorso, "w") as file:
            file.write(contenuto)
        return file


class File(Documento):
    _nomePercorso: str
    def __init__(self, nomePercorso: str):
        self._nomePercorso = nomePercorso
        super().__init__(self.leggiTestoDaFile())


    def leggiTestoDaFile(self) -> None:
        with open(self._nomePercorso, "r") as file:
           contenuto = file.readlines()
        return contenuto
    

    def getText(self) -> str:
        return f"Percorso: {self._nomePercorso}\nContenuto: {super().getText()}"




if __name__ == "__main__":


    email: Email = Email(mittente="ale@gmail.com", destinatario="andrea@gmail.com", titolo_messaggio="Ciao bello", testo="Silvia Pesce perde sempre a briscola!")
    file: File = File("/home/its/document.txt")

    print(email.getText())
    print(file.getText())
    
    email.writeToFile("/home/its/email1.txt")

    print(email.isInText("briscolo"))

    print(file.isInText("percorso"))
        

    