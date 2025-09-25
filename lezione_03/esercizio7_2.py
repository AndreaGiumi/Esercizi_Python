cont = 0
sum = 0
scelta: str = str(input("Vuoi inserire un voto? "))

while scelta.lower() == "si":
    voto: int = int(input("Inserisci voto: "))
    scelta: str = str(input("Vuoi inserire un'altro voto? "))
    if voto > 0:
        cont  += 1
        sum += voto
    else:
        print("Errore")
if scelta.lower() == "no":
    if cont > 0:
        media: int = sum / cont
        print(f"Questa è la media dei tuoi voti: {media}")
    else:
        print("Nssun voto inserito")