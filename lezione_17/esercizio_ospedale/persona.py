class Persona:
    '''
    ### CLASSE: Persona

    Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String,
    uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
    - La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non 
    risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe,
      assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.
    setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene
      passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
    setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se
      viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
    setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al
      metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
    getName(): consente di ritornare il nome di una persona.
    getLastname(): consente di ritornare il cognome di una persona.
    getAge(): consente di ritornare l'età di una persona.
    greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
    '''
    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name: str, last_name: str) -> None:
        self.set_first_name(first_name)
        self.set_last_name(last_name)

        if not isinstance(first_name, str) or not isinstance(last_name, str):
            self.__age = None
        else:
            self.__age = 0

    def set_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str) or not first_name:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
        else:
            self.__first_name = first_name

    
    def set_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str) or not last_name:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")
        else:
            self.__last_name = last_name


    
    def set_age(self, age: int) -> None:
        if not isinstance(age, int):
            print("L'età deve essere un numero intero!")
        else:
            self.__age = age


    def get_first_name(self) -> str:
        return self.__first_name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def get_age(self) -> int:
        return self.__age
    
    def greet(self) -> None:
        print(f"Ciao sono {self.get_first_name()} {self.get_last_name()}. Ho {self.get_age()} anni! ")
    

if __name__=="__main__":

    persona: Persona = Persona(5, "Giumi")


    persona.greet()