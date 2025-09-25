def seq_num():

    list_seq: list[int] = []
    occorrenze = 0

    try:
        x:int = int(input("Inserisci un numero intero positivo: "))
        if x <= 0:
            raise ValueError("Il numero che hai inserito deve essere positivo!")
    except ValueError as error:
        print(error)

        

    while True:
        try:
            n: int = int(input("Inserisci una serie di numeri interi positivi: "))
        except ValueError as error:
            print(error)
            
        if n == 0:
            break

        list_seq.append(n)
    print(f"La sequenza di numeri è: {list_seq}")

    somma = 0
    for n in list_seq:
        if n != x:
             somma += n
    print(f"La somma dei valori della sequenza diversi da {x} è {somma}")


    for i in list_seq:
        if i == x:
            occorrenze += 1
    print(f"Il numero {x} si ripete: {occorrenze} volte")


    for i in list_seq:
        if x in list_seq:
            print(f"Il numero {x} compare nella sequenza per la prima volta alla poszione {list_seq.index(x)}")
            break



            
    


seq_num()