myfavoriteCities: list[str] = ["Roma", "Cassino", "Napoli", "Lecce", "Bolzano"]

#aggiungo una città alla fine della lista
myfavoriteCities.append("Agrigento")

print(myfavoriteCities)

#aggiungo una città all'indice 1 della lista
myfavoriteCities.insert(1, "Milano")

print(myfavoriteCities)


#elimino la città all'indice 5 della lista
myfavoriteCities.pop(5)
print(myfavoriteCities)

 #elimino un'altra città all'indice 1 della lista
del myfavoriteCities[1]

print(myfavoriteCities)



print(f"Questa è la lista con sorted: {sorted(myfavoriteCities)}")

print(myfavoriteCities)


myfavoriteCities.reverse()
print(f"Questa è la lista con reverse: {myfavoriteCities}")

myfavoriteCities.sort()
print(f"Questa è la lista con sort: {myfavoriteCities}")