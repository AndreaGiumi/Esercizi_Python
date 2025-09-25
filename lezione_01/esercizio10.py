r: int = int(input("Inserisci retta: "))
m: int = int(input("Inserisci media: "))

if r < 20000 and m > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio non approvata (Motivo: reddito o media insufficenti )")