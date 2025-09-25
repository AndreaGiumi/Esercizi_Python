car: str = "ferrari"
color: str = "Red"
number: int = 10

cars: list[str] = ["ferrari", "audi", "bmw", "fiat"]


print("Is car == ferrari? I predict True.")
print(car == 'ferrari')
print("Is car == 'bmw'? I predict False.")
print(car == 'bmw')
print("Is color == red.lower()? I predict True.")
print(color == 'red'.lower())
print("Is color == 'Red'? I predict False.")
print(color == 'Red')
print("Is number == 10? I predict True.")
print(number == 10)
print("Is number != '10? I predict False.")
print(number != 10)
print("Is number > 5? I predict True.")
print(number > 5)
print("Is number < 2 ? I predict False.")
print(number < 2)
print("Is number >= 5? I predict True.")
print(number >= 5)
print("Is number >= 9 ? I predict False.")
print(number >= 9)
print("Is number > 5 and number % 2 == 0? I predict True.")
print(number > 5 and number % 2 == 0)
print("Is number > 9 and number % 2 != 0? I predict False.")
print(number > 9 and number % 2 != 0)
print("Is number > 5 or number % 2 != 0? I predict True.")
print(number > 5 or number % 2 != 0)
print("Is number > 10 or number % 2 == 0? I predict False.")
print(number > 10 or number % 2 != 0)
print("Is car in cars? I predict True.")
print(car in cars)
print("Is lamborghini in cars? I predict False.")
print( "lamborghini"in cars)
print("Is lamborghini not in cars? I predict True.")
print("lamborghini" not in cars)
print("Is car not in cars? I predict False.")
print( car not in cars)

