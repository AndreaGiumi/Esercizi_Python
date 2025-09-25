class RecipeManager:
    def __init__(self) -> None:
        self.recipe_ing: dict[str, list[str]] = {}
        
    def create_recipe(self,name: str, ingredients: list[str]) -> dict[str,list[str]]:
        if name not in self.recipe_ing:
            self.recipe_ing[name] = ingredients
        else:
           raise KeyError("Errore questa ricetta è già presente!")
        return self.recipe_ing
    

    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        if recipe_name in self.recipe_ing:
            if ingredient not in self.recipe_ing[recipe_name]:
                self.recipe_ing[recipe_name].append(ingredient)
            else:
                raise KeyError("L'ingrediente è già presente nella ricetta")
        return self.recipe_ing
    

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        if recipe_name in self.recipe_ing and ingredient in self.recipe_ing[recipe_name]:
            self.recipe_ing[recipe_name].remove(ingredient)
        if not self.recipe_ing[recipe_name]:
            del self.recipe_ing[recipe_name]
        return self.recipe_ing
        
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]:

        if recipe_name not in self.recipe_ing:
            raise ValueError("La ricetta non esiste!")
        
        if old_ingredient not in self.recipe_ing[recipe_name]:
            raise ValueError("L'ingrediente non è presente!")
        
        index: int = self.recipe_ing[recipe_name].index(old_ingredient)
        self.recipe_ing[recipe_name][index] = new_ingredient
        
        return {recipe_name: self.recipe_ing[recipe_name]}
    
    def  list_recipes(self) -> list[str]:
        return list(self.recipe_ing.keys())
    
    def  list_ingredients(self, recipe_name: str):
        if recipe_name not in self.recipe_ing:
            raise ValueError("La ricetta non esiste!")
        return self.recipe_ing[recipe_name]
    
    def  search_recipe_by_ingredient(self, ingredient: str) -> list[str]:
        rec_list: list[str] = []

        for name, recipe in self.recipe_ing.items():
            if ingredient in recipe:
                rec_list.append(name)

            if rec_list == []:
                raise Exception("Nessuna ricetta trovata con questo ingrediente!")
            return self.recipe_ing
        
if __name__=="__main__":
    



     	

    manager = RecipeManager()
    print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
    print(manager.add_ingredient("Torta di mele", "Zucchero"))
    print(manager.list_recipes()) # ['Torta di mele']
    print(manager.list_ingredients("Torta di mele"))
    print(manager.search_recipe_by_ingredient("Uova"))




