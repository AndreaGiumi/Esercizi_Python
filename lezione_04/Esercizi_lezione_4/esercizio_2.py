import random
def guess_number(num_min: int, num_max: int, attemps: int):

    ran = random.randint(num_min, num_max)

    for _ in range(attemps):
        try:
            num_user = int(input("Inserisci il tuo numero: "))

            if num_user > ran:
                print("Numero troppo grande")
            elif num_user < ran:
                print("Numero troppo piccolo")
            else:
                print("Numero corretto")
                return
        except ValueError:
            print("Inserire un numero valido")
            

    print(f"Il numero da indovinare era {ran}")



guess_number(20, 770, 25)



