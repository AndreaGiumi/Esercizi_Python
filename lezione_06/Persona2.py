class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def displayData(self)-> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")


# mi consente di impostare un valore per self.name
    def setName(self, name:str)->  None:
        self.name = name
# mi consente di impostare il cognome di una persona
    def setLastname(self, lastname:str)->  None:
        self.lastname = lastname
# mi consente di impostare l'età di una persona
    def setAge(self, age:int)->  None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
# ritorna il valore di self.name
    def getName(self) -> str:
        return self.name
# ritorna il valore di self.lastname
    def getLastname(self) ->str:
        return self.lastname
# ritorna il valore di self.age
    def getAge(self) -> int:
        return self.age

# crea oggetto di tipo persona
ag:Persona = Persona()

# stampa i dati della persona creata
ag.displayData()
# imposta il nome di una persona
ag.setName("Andrea")
# imposta il cognome di una persona
ag.setLastname("Giumi")
# imposta il età di una persona
ag.setAge(-27)

ag.setAge(27)

ag.displayData()
print("-------------------------")
print(ag.getName(), ag.getLastname(), ag.getAge())