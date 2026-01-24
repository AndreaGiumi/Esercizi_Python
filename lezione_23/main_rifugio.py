from rifugio_animali import *
rifugio: Shelter = Shelter()


leone: Dog = Dog("ln01", "Leone", 4, 20.0, "Beagle")

cannella: Cat = Cat("cn01", "Cannella", 12, 5.40, "pallina")




rifugio.add(leone)
rifugio.add(cannella)

rifugio.set_adopted("ln01", "Andrea Giumi")
rifugio.set_adopted("cn01", "Martina Giumi")

print(leone.daily_food_grams())
print(rifugio.list_all())
print(rifugio.adoptions)