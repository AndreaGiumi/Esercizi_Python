import random
import string
import secrets
def generatore_password():
    # Scrivi una funzione generatrice di password.
    # La funzione deve generare una stringa alfanumerica di 8 caratteri 
    # qualora l'utente voglia una password semplice, e di 20 caratteri ASCII qualora desideri una password più complicata.
    lunghezza_password: str = str(input("Vuoi una password semplice o complessa?: ").lower())

    ascii_char = string.ascii_letters + string.digits + string.punctuation
    alpha_char = string.digits + string.ascii_letters

    if lunghezza_password == "semplice":
        lunghezza = 8
        tipo = alpha_char
    else:
        lunghezza = 20
        tipo = ascii_char

    psw = "".join(secrets.choice(tipo) for _ in range(lunghezza))

    print(psw)
        

    
if __name__=="__main__":
    generatore_password()