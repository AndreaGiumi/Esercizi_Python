friend_pizzas: list[str] = ["Diavola", "Salsiccia e funghi porcini", "Margherita"]
pizzas: list[str] = ["Diavola", "Salsiccia e funghi porcini", "Margherita"]

pizzas.append("Ortolana")
friend_pizzas.append("Salsiccia e peperoni")

for pizza in pizzas:
    print(f"My favourite pizzas are: {pizza}")

for pizza in friend_pizzas:
    print(f"My favourite pizzas are: {pizza}")
