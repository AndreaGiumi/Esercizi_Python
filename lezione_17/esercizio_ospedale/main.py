from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

if __name__=="__main__":
    ### Codice Driver

# Scrivere, infine, il codice driver che gestisca due dottori e due liste di pazienti. La prima lista di pazienti deve contenere 3 pazienti, 
# mentre la seconda 1 solo paziente.

#     Impostare l'età di ogni medico, affinché i due medici risultino validi!
#     Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().
#     Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.
#     Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.
#     Stampare in output il salario di ogni singolo dottore. Ad esempio:

#       "Salario Dottore1: ... euro!
#        Salario Dottore2: ... euro!"

#     Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.
#     Stampare in output il salario di ogni dottore.
#     Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore. Esempio:

# "In totale, l'ospedale ha incassato: tot euro!"

    dottore1: Dottore = Dottore("kristian", "Lanni", "Generale", 14.00)
    dottore2: Dottore = Dottore("Matteo", "Azzoli", "Pediatra", 10.00)

    paziente1: Paziente = Paziente("Marco", "Rossi", "MRS514")
    paziente2: Paziente = Paziente("Luca", "Verdi", "LVR285")
    paziente3: Paziente = Paziente("Lucia", "Bianchi", "LCB258")
    paziente4: Paziente = Paziente("Simona", "Ricci", "SMR741")

    lista_pazienti1: list[Paziente] = [paziente1, paziente2, paziente3]
    lista_pazienti2: list[Paziente] = [paziente4]

    dottore1.set_age(41)
    dottore2.set_age(30)
    dottore1.isAValidDoctor()
    dottore2.isAValidDoctor()

    dottore1.doctorGreet()
    dottore2.doctorGreet()

    fattura1: Fattura = Fattura(lista_pazienti1, dottore1)
    fattura2: Fattura = Fattura(lista_pazienti2, dottore2)

    print(f"Salario Dottor {dottore1.get_first_name()} {dottore1.get_last_name()}: {fattura1.getSalary()} euro")

    print(f"Salario Dottor {dottore2.get_first_name()} {dottore2.get_last_name()}: {fattura2.getSalary()} euro")

    fattura1.removePatient(paziente1.get_IdCode())
    fattura2.addPatient(paziente1)


    print(f"Salario Dottor {dottore1.get_first_name()} {dottore1.get_last_name()}: {fattura1.getSalary()} euro")

    print(f"Salario Dottor {dottore2.get_first_name()} {dottore2.get_last_name()}: {fattura2.getSalary()} euro")


    print(f"In totale, l'ospedale ha incassato: {fattura1.getSalary() + fattura2.getSalary()} euro!")