class Food:
    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description



pizza = Food("Diavola", 6.00, "Pomodoro, mozzarella, salame piccante")
pasta = Food("Cacio e pepe", 12.00, "Pasta con crema di formaggio cacio e tanto pepe.")
dolce = Food("Cornetto", 2.50, "cornetto ripieno di nutella e cioccolato bianco")



class Menu:
    def __init__(self, foods:list[Food] = []):
        self.foods = foods



    def addFood(self, foods:list[Food]):
        self.foods = foods.append(Food)
        
    

    def removeFood(self, foods:list[Food]):
        self.foods = foods.pop(Food)



    def printPrices(self):
        print(f"Questi solo tutti i prezzi del menù: {self.price}")


    def getAveragePrice(self):
        print({self.price} / len(Menu))



 
