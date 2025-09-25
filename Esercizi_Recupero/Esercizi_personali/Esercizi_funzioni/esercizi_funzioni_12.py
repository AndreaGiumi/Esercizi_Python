def max_tre_num():
    '''
    Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.
    '''

    num1: int = int(input("Inserisci primo numero: "))
    num2: int = int(input("Inserisci secondo numero: "))
    num3: int = int(input("Inserisci terzo numero: "))

    if num1 >= num2 and num1 >= num3:
        print(f"Il numero più grande è il primo: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"Il numero più grande è il secondo: {num2}")
    else:
        print(f"Il numero più grande è il terzo: {num3}")

    
max_tre_num()