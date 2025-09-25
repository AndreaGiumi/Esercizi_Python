class Resturant:
    def __init__(self, resturant_name:str, cusine_type:str):
        self.resturant_name = resturant_name
        self.cusine_type = cusine_type


    def describe_resturant(self):
        print(f"Nome ristorante: {self.resturant_name}\nTipo di cucina: {self.cusine_type}")


    def open_resturant(self):
        print(f"Il ristorante {self.resturant_name} è aperto!")



resturant = Resturant("Il Vicoletto", "Cucina Italiana")
resturant2 = Resturant("Da Andrea", "Cucina Americana")
resturant3 = Resturant("Taiwan", "Cucina Cinese")


resturant.describe_resturant()
resturant2.describe_resturant()
resturant3.describe_resturant()