class Resturant:
    def __init__(self, resturant_name:str, cusine_type:str, number_served:int = 0):
        self.resturant_name = resturant_name
        self.cusine_type = cusine_type
        self.number_served = number_served


    def describe_resturant(self):
        print(f"Nome ristorante: {self.resturant_name}\nTipo di cucina: {self.cusine_type}")


    def open_resturant(self):
        print(f"Il ristorante {self.resturant_name} è aperto!")


    def set_number_served(self, number_served:int):
        self.number_served = number_served

    def increment_number_served(self, number_served:int):
        self.number_served += number_served


resturant = Resturant("Il Vicoletto", "Cucina Italiana")

if __name__ == "__main__":

    resturant.set_number_served(67)
    resturant.increment_number_served(2)
    print(f"Il numero di clienti serviti oggi è: {resturant.number_served}")
