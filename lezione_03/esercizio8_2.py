valore_A: int = int(input("Inserisci primo valore: "))
valore_B: int = int(input("Inserisci secondo valore: "))

if valore_A < valore_B:
    if valore_A > 0 and valore_B > 0:
        if valore_A % 1 == 0 and valore_B % 1 == 0:
            sum = 0
            i = valore_A
            while i <= valore_B:
                sum += i
                i += 1
            print(sum)
        print(f"{valore_A} e {valore_B} devono essere interi!")
    print(f"{valore_A} e {valore_B} devono essere positivi!")
print(f"{valore_A} deve essere maggiore di {valore_B}")



 