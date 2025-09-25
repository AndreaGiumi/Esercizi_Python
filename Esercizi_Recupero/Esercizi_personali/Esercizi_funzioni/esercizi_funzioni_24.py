from math import pi
import platform
def geometra():
    '''
    Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:

    un cerchio
    un quadrato
    un rettangolo
    un triangolo

    '''

    calcolo = str(input("Inserisci forma geometrica tra: cerchio, quadrato, rettangolo, triangolo: "))

    if calcolo == "cerchio":
        r = float(input("Inserisci il raggio: "))
        if r > 0:
            area = pi * r**2
        print(f"L'area del cerchio è uguale a {area:.2}")

    
    elif calcolo == "quadrato":
        l = float(input("Inserisci lato del quadrato: "))

        if l > 0:
            area = l**2
        print(f"L'area del quadrato è uguale a {area}")


    elif calcolo == "rettangolo":
        b = float(input("Inserisci base del rettangolo: "))
        h = float(input("Inserisci altezza rettangolo: "))

        if b > 0 and h > 0:
            area = b * h
        print(f"L'area del rettangolo è uguale a {area}")


    elif calcolo == "triangolo":

        b = float(input("Inserisci base del triangolo: "))
        h = float(input("Inserisci altezza triangolo: "))

        if b > 0 and h > 0:
            area = (b * h) / 2
        print(f"L'area del triangolo è uguale a {area}")
    else:
        print("Utilizzare solo le forme geometriche specificate.")


geometra()