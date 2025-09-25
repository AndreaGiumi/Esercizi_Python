class Persona:
    '''
    
    Di una persona noi dobbiamo sapere delle informazioni
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età
    

    Come li rappresento in python?

    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)

    '''
    # costruttore della classe Persona
    def __init__(self, name:str, lastname:str, age:int):
        self.name:str = name
        self.lastname:str = lastname
        self.age:int = age


    # funzione che mostri in output tutti i dati di una persona
    def displayData(self)-> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")



ag:Persona = Persona("Andrea", "Giumi", 27)

print(ag)

# mostra i dati di una persona

ag.displayData()