class Alieno:


    '''
    di un alieno ci interessa la galassia di provenienza
    self.galaxy: str


    '''
    # inizializziare un oggetto della classe Alieno
    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    # definire un metodo per impostare il valore dell'attributo self.galaxy
    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota!")

    # definire un metodo per restituire il valore dell'attributo self.galaxy
    def getGalaxy(self) -> str:
        return self.galaxy
    
    # definire un metodo speak
    def speak(self) ->None:
        print("jifejfiedjkfiefkjedcfkl")


    def __str__(self) -> str:
        return f"Alieno proveniente dalla galassia: {self.getGalaxy()}"