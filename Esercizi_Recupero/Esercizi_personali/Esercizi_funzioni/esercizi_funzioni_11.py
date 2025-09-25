def max_num() -> int:
    '''
Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo
    '''

    num1: int = int(input("Inserisci primo numero: "))
    num2: int = int(input("Inserisci secondo numero: "))

    max_n: int = num1
    if num2 == max_n:
        print("I numeri sono uguali")
    elif num2 > max_n:
        print(f"Il numero più grande è il secondo inserito: {num2}")
    else:
        print(f"Il numero più grande è il primo inserito: {num1}")


max_num()