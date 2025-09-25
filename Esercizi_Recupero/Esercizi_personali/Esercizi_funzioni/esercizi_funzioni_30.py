def reverse(parola: str):
    # Scrivi una funzione a cui passerai come parametro una stringa, e
    # che manderà in print una versione inversa (al contrario) della stessa stringa. Ad esempio "abcd" diventerà "dcba"

    if parola:
        print(parola[::-1])



reverse("Ciao")




def palidrom_string(string: str):

    indice = (len(string) -1)
    new_string: str = ""

    while indice >= 0:
        new_string += string[indice]

        indice -= 1

    if new_string == string:
        print(new_string + ": la parola passata è un palindromo!")
    else:
        print(new_string + ": mi dispiace, la parola inserita non è un palindromo...")


if __name__=="__main__":

    palidrom_string("ciao")