# Creo una lista 
lista_num: list[int] = []

for num in range(1, 11):
# Aggiungere i numeri alla lista
    lista_num.append(num)       

    print((num) ** 3)

print(f"The first three items in the list are: {lista_num[0: 3]}")
print(f"Three items from the middle of the list are: {lista_num[4: 7]}")
print(f"The last three items in the list are: {lista_num[8: 10]}")
