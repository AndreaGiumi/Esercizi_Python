

def sumList():
    '''
    Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.
    '''
    list_num = []

    while len(list_num) <= 9:
        num = int(input("Inserisci numeri nella lista: "))

        list_num.append(num)

        
    print(f"La somma della lista è : {sum(list_num)}")




sumList()


