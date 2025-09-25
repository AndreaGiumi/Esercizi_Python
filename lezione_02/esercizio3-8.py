myfavoritePlaces: list[str] = ["Islanda", "Route 66", "Giappone", "Norvegia", "Hawaii"]

print(f"Questa è la lista iniziale: {myfavoritePlaces}")

print(f"Questa è la lista con sorted: {sorted(myfavoritePlaces)}")

print(f"Questa è la lista con sorted reverse=True: {sorted(myfavoritePlaces, reverse=True)}")

print(f"Questa è la lista iniziale: {myfavoritePlaces}")

myfavoritePlaces.reverse()
print(f"Questa è la lista con reverse: {myfavoritePlaces}")

myfavoritePlaces.reverse()
print(f"Questa è la lista con il secondo reverse: {myfavoritePlaces}")

myfavoritePlaces.sort()
print(f"Questa è la lista con sort: {myfavoritePlaces}")

myfavoritePlaces.sort(reverse=True)
print(f"Questa è la lista con il sort reverse=True: {myfavoritePlaces}")