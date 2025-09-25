from persona import Persona
from studente import Studente

# creo un oggetto della classe Persona
ag: Persona = Persona("Andrea", "Giumi", 28)

# visualizzare e informazione relative all'oggetto ag
print(ag)


# creo un oggetto della classe studente
studente1: Studente = Studente("Mario", "Rossi", 20, "01223444")


# visualizzare e informazione relative all'oggetto studente
print(studente1)


# controllo se studente1 sia istanza della classe Studente
# isistance(obj.Class)--> controlla se l'oggetto sia un istanza della classe Class
# in caso affermativo -->True
# in caso negatovo -->False
if isinstance(studente1, Studente):
    print(f"\nstudente1 è istanza della classe Studente")
    
# controllo se studente1 è anche istanza della classe Persona
if isinstance(studente1, Persona):
    print(f"\nstudente1 è anche istanza della classe Persona")

# controllare se l'oggetto ag sia istanza della classe Persona
if isinstance(ag, Persona):
    print(f"\nl'ggetto ag è istanza della classe Persona")

if isinstance(ag, Studente):
    print(f"\nl'oggetto ag è istanza della classe Persona e anche istanza della classe Studente")
else:
    print(f"\nl'oggetto ag è istanza della classe Persona ma non è istanza della classe Studente")


# conrrollare se la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1,Class2) -> controllo se Class1 sia sottoclasse di Class2
# in caso afferamtivo -> True
# in caso negativo -> False
if issubclass(Studente, Persona):
    print(f"\nla classe Studente è sottoclasse della classe Persona")
