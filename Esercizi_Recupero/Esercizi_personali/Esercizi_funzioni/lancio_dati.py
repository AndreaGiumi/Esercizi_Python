import random
def lancio_dadi():
    dado_1 = [1, 2, 3, 4, 5, 6]
    dado_2 = [1, 2, 3, 4, 5, 6]
    lanci = 1

    numero_lanci = int(input("Quanti lanci vuoi fare? "))
    while lanci <= numero_lanci:
        num1 = random.choice(dado_1)
        num2 = random.choice(dado_2)
        somma = num1 + num2
        print(f"I numeri usciti sono: {num1} e {num2}, la somma di essi è: {somma}")

        lanci += 1  
 
if __name__=="__main__":
    lancio_dadi()