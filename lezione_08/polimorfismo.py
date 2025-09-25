from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona
p: Persona = Persona("Andrea", "Giumi", 28)

# visualizzare le informazioni dell'oggetto p della classe Persona
print(p) 

# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")
print("\n")

# visualizzare le informazioni dell'oggetto et della classe Alieno
print(et)
print("\n")

# invocare il metodo speak() della classe Persona
p.speak()
print("\n")
# invocare il metodo speak() della classe Alieno
et.speak()
