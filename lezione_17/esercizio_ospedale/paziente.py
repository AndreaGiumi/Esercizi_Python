from persona import Persona

class Paziente(Persona):

    '''
    
    ### CLASSE: Paziente
    Creare un file chiamato "paziente.py".
    In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

    Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
    - Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
    
    '''
    __identificativo: str

    def __init__(self, first_name: str, last_name: str, identificativo: str):
        super().__init__(first_name, last_name)

        self.set_IdCode(identificativo)

    
    def set_IdCode(self, identificativo: str) -> None:
        self.__identificativo = identificativo

    def get_IdCode(self) -> str:
        return self.__identificativo
    

    def patientInfo(self) -> None:
        print(f"Paziente: {self.get_first_name()} {self.get_last_name()}\nID: {self.get_IdCode()}")



if __name__=="__main__":

    paziente: Paziente = Paziente("Angelo", "Binachi", "LDO877DJF")

    paziente.patientInfo()