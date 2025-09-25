from paziente import Paziente
from dottore import Dottore

class Fattura:
    '''
        ### CLASSE: Fattura
    Creare un file chiamato "fatture.py".
    In tale file, creare una classe chiamata Fattura.

    - Definire i seguenti metodi:

    init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, 
    richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, 
    mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un 
    messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di 
    pazienti.
    getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
    addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
    richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
    removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente 
    da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è
      stato rimosso il paziente {codice_identificativo}".

    '''

    __fatture: int
    __salary: int

    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:
        if doctor.isAValidDoctor():
            self.__patient = patient
            self.__doctor = doctor
            self.__fatture = len(patient)
            self.__salary = 0
        else:
            self.__patient = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def setPatient(self, patient: list[Paziente]) -> None:
        if patient is not None:
            self.__patient = patient

    def getPatient(self) -> list[Paziente]:
        return self.__patient
    
    def setDoctor(self, doctor: Dottore) -> None:
        self.__doctor = doctor

    def getDoctor(self) -> Dottore:
        return self.__doctor
        
    def setFatture(self, fatture: int) -> None:
        self.__fatture = fatture

    def getFatture(self) -> int:
        if self.__patient is not None:
            self.__fatture = len(self.__patient)
        return self.__fatture
    
    def setSalary(self, salary: int) -> None:
        self.__salary = salary

    def getSalary(self) -> int:
        if self.__doctor is not None and self.__patient is not None:
            self.__salary = self.__doctor.get_parcel() * len(self.__patient)
        return self.__salary

    def addPatient(self, newPatient: Paziente) -> None:
        self.__patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.__doctor.get_last_name()} è stato aggiunto il paziente {newPatient.get_IdCode()}")


    def removePatient(self, IdCode) -> None:
        for paziente in self.getPatient():
            if paziente.get_IdCode() == IdCode:
                self.__patient.remove(paziente)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.__doctor.get_last_name()} è stato rimosso il paziente {IdCode}")
        return
