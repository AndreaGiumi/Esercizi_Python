from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s:str, key:int):
    lettere: list[str] = ascii_lowercase
    lettere_upper: list[str] = ascii_uppercase
    c = ""
    for l in s:
        if l in lettere:
            index_l = (lettere.index(l) + key) % len(lettere)
            c += lettere[index_l] 
        elif l in lettere_upper:
            index_l = (lettere_upper.index(l) + key) % len(lettere_upper)
            c += lettere_upper[index_l]
    print(c)
                
caesar_cypher_encrypt("ciao mamma", 3)


def caesar_cypher_decrypt(s, key):
    lettere: list[str] = ascii_lowercase
    lettere_upper: list[str] = ascii_uppercase
    c = ""
    for l in s:
        if l in lettere:
            index_l = (lettere.index(l) - key) % len(lettere)
            c += lettere[index_l]
        elif l in lettere_upper:
            index_l = (lettere_upper.index(l) - key) % len(lettere_upper)
            c += lettere_upper[index_l]

    print(c)


caesar_cypher_decrypt("fldrpdppd", 3)