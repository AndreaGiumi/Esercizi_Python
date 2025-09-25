# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
# Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction



def atm_machine_simulator() -> int|float:
    bilance: float = 50

    while True:
        print("Depositare = 1\nRitirare = 2\nControllare saldo = 3\nUscire = 4")
        atm = str(input("Cosa vuoi fare? "))

        if atm == "1":
            depositare = int(input("Inserisci la somma che vuoi depositare: "))

            bilance += depositare


        elif atm == "2":
            ritirare = int(input("Inserisci somma che vuoi ritirare: "))
            if bilance < ritirare:
                raise RuntimeError("Transazione negata! La somma da ritirare è maggiore della somma del conto.")

            bilance -= ritirare

        
        elif atm == "3":
            print(f"Saldo disponibile: ${bilance:.2f}")


        elif atm == "4":
            break

        else:
            raise RuntimeError("Operazione scelta non valida!")





    




    

atm_machine_simulator()
