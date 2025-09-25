# (3-7)

invitati: list[str] = ["Franccesco Totti", "J-Ax", "Bryan Cranston"]

print(f"Caro {invitati[0]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[1]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Dear {invitati[2]}! You are invited to the Christmas dinner at my home!")

print(invitati)

print(f"{invitati[0]} non potrà essere presente alla cena! Recupereremo!")

invitati[0] = "Claudio Ranieri"

print(invitati)

print(f"Caro {invitati[0]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[1]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Dear {invitati[2]}! You are invited to the Christmas dinner at my home!")

print("Con molta fortuna ho ritrovato un tavolo più grande per ospitare altra gente per la cena")

invitati.insert(0, "Gigi Proietti")
invitati.insert(2, "Lazza")
invitati.append("Maradona")


print(invitati)


print(f"Caro {invitati[0]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[1]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[2]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Caro {invitati[3]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Dear {invitati[4]}! You are invited to the Christmas dinner at my home!")
print(f"Dear {invitati[5]}! You are invited to the Christmas dinner at my home!")

print("Con dispiacere devo annunciare che il tavolo più grande non arriverà in tempo, quindi potrò invitare solo due persone.")

print(f"Dear {invitati.pop(5)}, it is with great regret that I have to announce that I will not be able to invite you to dinner!")
print(f"Caro {invitati.pop(1)}, con grande dispiacere devo annunciare che non potrò invitarvi alla cena!")
print(f"Caro {invitati.pop(3)}, con grande dispiacere devo annunciare che non potrò invitarvi alla cena!")
print(f"Caro {invitati.pop(0)}, con grande dispiacere devo annunciare che non potrò invitarvi alla cena!")


print(f"Caro {invitati[0]} sei ancora invitato alla cena!")
print(f"Caro {invitati[1]} sei ancora invitato alla cena!")

del invitati[0]
del invitati[0]

print(invitati)

