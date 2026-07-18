"""
Sezione 3 - Liste e stringhe (difficoltà: media / difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""


# Esercizio 3.1 - Analisi lista
# Senza usare min(), max() o sum():
#   - trova il valore minimo e il massimo
#   - calcola la media
#   - crea una nuova lista con i soli numeri maggiori della media
def esercizio_3_1() -> None:
    numeri: list[int] = [12, 5, 8, 21, 3, 16, 9]

    max: int = numeri[0]
    min: int = numeri[0]

    for i in numeri:
        if i > max:
            max = i
        elif i < min:
            min = i

    media = sum(numeri)/len(numeri)

    num_max_media: list[int] = []

    for i in numeri:
        if i > media:
            num_max_media.append(i)

    print(f"Il numero maggiore è {max}\nIl numero minore è {min}\nLa media è {media}\nNuova lista: {num_max_media}")


# Esercizio 3.2 - Palindromo
# Chiedi una parola e dì se è palindroma (ignora maiuscole/minuscole).
# Prova sia con lo slicing [::-1] sia con un ciclo.
def esercizio_3_2() -> None:
    parola: str = input("Inserisci una parola/frase: ").lower()

    new_parola: str = parola.replace(" ", "")
    # if new_parola == new_parola[::-1]:
    #     print("La parola è palindroma")
    # else:
    #     print("La parola NON è palindroma")

    palindromo: str = ""

    for i in new_parola:
        palindromo = i + palindromo
    
    new_pal: str = palindromo.replace(" ", "")
    if new_pal == new_parola:
        print("La parola è palindroma")
    else:
        print("La parola NON è palindroma")




# Esercizio 3.3 - Matrice (difficile)
# Crea una matrice 3x3 (lista di liste) chiedendo i valori all'utente. Poi:
#   - stampala riga per riga in modo leggibile
#   - calcola la somma di ogni riga e di ogni colonna
#   - calcola la somma della diagonale principale
def esercizio_3_3() -> None:
    matrice: list[list[int]] = []

    row: list[int] = []
    while len(row) < 3:
        numeri: int = int(input("Inserisci i numeri nella matrice: "))

        row.append(numeri)
    matrice.append(row)
    print(matrice)


if __name__ == "__main__":
    # esercizio_3_1()
    # esercizio_3_2()
    esercizio_3_3()
