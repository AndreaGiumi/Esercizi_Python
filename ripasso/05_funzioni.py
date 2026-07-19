"""
Sezione 5 - Funzioni (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 5.1 - Calcolatrice
# Quattro funzioni con parametri tipizzati. La divisione gestisce
# il divisore uguale a zero. Poi un menu che chiede operazione e numeri.
def somma(a: float, b: float) -> float:
    return a + b


def sottrazione(a: float, b: float) -> float:
    return a - b


def moltiplicazione(a: float, b: float) -> float:
    return a * b
    


def divisione(a: float, b: float) -> float | None:
    if b == 0:
        return "Errore divisone per 0"
    else:
        return a / b
        


def menu_calcolatrice() -> None:
    while True:
        print("Scegli l'operazione che vuoi eseguire tra: Addizione, Sottrazione, Moltiplicazione e Divisione. Altrimenti Esc per usicre!")

        operazione: str = input("Inserisci l'operazione scelta: ").lower()

        if operazione == "addizione":
            print("Qauli numeri vuoi addizionare: ")

            add1: float = float(input("Primo numero: "))
            add2: float = float(input("Secondo numero: "))
            risultato: float = somma(add1, add2)
            print(f"Il risultato è {risultato}") 

        elif operazione == "sottrazione":
            print("Qauli numeri vuoi sottrarre: ")
            sott1: float = float(input("Primo numero: "))
            sott2: float = float(input("Secondo numero: "))
            risultato: float = sottrazione(sott1, sott2)
            print(f"Il risultato è {risultato}") 
            
        elif operazione == "moltiplicazione":
            print("Qauli numeri vuoi moltiplicare: ")
            molt1: float = float(input("Primo numero: "))
            molt2: float = float(input("Secondo numero: "))
            risultato: float = moltiplicazione(molt1, molt2)
            print(f"Il risultato è {risultato}") 
        elif operazione == "divisione":
            print("Qauli numeri vuoi dividere (ATTENZIONE ALLO ZERO): ")
            div1: float = float(input("Primo numero: "))
            div2: float = float(input("Secondo numero: "))
            risultato: float | str = divisione(div1, div2)
            print(f"Il risultato è {risultato}")

        elif operazione == "esc":
            break


# Esercizio 5.2 - Validatore password
# Ritorna True solo se la password: >= 8 caratteri, almeno una maiuscola,
# almeno un numero.
def valida_password(password: str) -> bool:
    char_cap: bool = False
    char_numeric: bool = False
    len_char_psw: bool = False

    for i in password:
        if i.isupper():
            char_cap = True
        if i.isdigit():
            char_numeric = True
    if len(password) >= 8:
        len_char_psw = True

    return char_cap and char_numeric and len_char_psw
        

        


# Esercizio 5.3 - Funzioni con valori di default (difficile)
# Applica prima lo sconto (in %) e poi aggiunge l'IVA.
# Testala con 1, 2 e 3 argomenti, anche con keyword arguments.
def calcola_prezzo(prezzo_base: float, sconto: float = 0, iva: float = 22) -> float:
    sconto_app: float = prezzo_base * sconto / 100
    tot_con_sconto: float = prezzo_base - sconto_app
    tot_con_iva: float = tot_con_sconto * (1 + iva / 100)

    return tot_con_iva

if __name__ == "__main__":
    # menu_calcolatrice()
    # print(valida_password("paFswor1"))
    print(calcola_prezzo(100))
    print(calcola_prezzo(100, sconto=10))
    print(calcola_prezzo(100, sconto=10, iva=4))
