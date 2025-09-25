friend_pizzas: list[str] = ["Diavola", "Salsiccia e funghi porcini",
                            "Margherita"]
pizzas: list[str] = ["Diavola",
                    "Salsiccia e funghi porcini", "Margherita"]

pizzas.append("Ortolana")
friend_pizzas.append("Salsiccia e peperoni")

for pizza in pizzas:
    print(f"My favourite pizzas are: {pizza}")

for pizza in friend_pizzas:
    print(f"My favourite pizzas are: {pizza}")



# Creo una lista vuota
lista_num: list[int] = []
# Inizializzo un ciclo for
for num in range(1, 11):
# Aggiungere i numeri alla lista
    lista_num.append(num)       
# Stampo i numeri della lista elevati al cubo
    print((num) ** 3)

