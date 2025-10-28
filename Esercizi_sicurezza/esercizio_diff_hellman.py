import random
def is_prime(n: int):
    for i in range(n - 1, 1, -1):
        if n % i == 0:  
            return False
        
    return True

def diff_hellman(p: int, g: int):
    if not is_prime(p):
        print(f"Attenzione {p} deve essere un numero primo")
    else:
        # chiave privata Alice
        a = random.randint(2, p-1)
        # chiave pubblica di Alice
        A = pow(g, a, p)
        print(f"Chiave pubblica di Alice: A = {g}**{a} mod {p} = {A}") 
        
        # chiave privata Bob
        b = random.randint(2, p-1)

        #chiave pubblica Bob
        B = pow(g, b, p)
        print(f"Chiave pubblica di Bob: B = {g}**{b} mod {p} = {B}")

        #chiave condivisa

        #Alice usa la chiave pubblica di Bob e la sua chiave privata

        chiave_alice = pow(B, a, p)

        print(f"Alice calcola {B}**{a} mod {p} = {chiave_alice}")

        #Bob usa la chiave pubblica di ALice e la sua chiave privata

        chiave_bob = pow(A, b, p)

        print(f"Bob calcola {A}**{b} mod {p} = {chiave_bob}")

        print("\n--- RISULTATO ---")
        if chiave_alice == chiave_bob:
            print(f"✓ SUCCESSO! Chiave condivisa = {chiave_alice}")
            print(f"  Matematicamente: {g}**({a}*{b}) mod {p} = {chiave_alice}")
        else:
            print("✗ Errore nelle chiavi!")



diff_hellman(23, 9)