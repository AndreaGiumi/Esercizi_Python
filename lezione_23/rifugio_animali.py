from abc import ABC, abstractmethod
from typing import Any
class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float)-> None:
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg
        
    @abstractmethod
    def species(self):
        pass

    def daily_food_grams(self):
        pass

    def info(self)->dict[str,Any]:
        return {
            "id":self.id,
            "nome":self.name,
            "anni":self.age_years,
            "chilogrammi":self.weight_kg
        }
    
    def bmi_like(self):
        return self.weight_kg / (self.age_years + 1)


class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool = False)->None:
        super().__init__(id, name, age_years, weight_kg)

        self.breed = breed
        self.is_trained = is_trained

    def species(self)->str:
        return "dog"
    

    def daily_food_grams(self)->str:
        return 200 + self.age_years * 50
    

    def info(self)->dict[str,Any]:
        return {"id":self.id,
            "nome":self.name,
            "specie":self.species(),
            "anni":self.age_years,
            "chilogrammi":self.weight_kg,
            "razza":self.breed,
            "addestrato":self.is_trained
        }

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, favorite_toy: str, indoor_only: bool = False) ->None:
        super().__init__(id, name, age_years, weight_kg)

        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    
    def species(self):
        return "cat"
    

    def daily_food_grams(self):
        return 100 + self.age_years * 30
    

    def info(self)->dict[str,Any]:
        return {"id":self.id,
            "nome":self.name,
            "specie": self.species(),
            "età":self.age_years,
            "chilogrammi":self.weight_kg,
            "gioco preferito": self.favorite_toy,
            "casalingo": self.indoor_only
        }
    
class Shelter:
    def __init__(self) -> None:
        self.animals: dict[str,Animal] = {}
        self.adoptions: dict[str,str] = {}


    def add(self, animal:Animal):
        if animal.id in self.animals:
            return "Esiste già un animale con questo id"
        self.animals[animal.id] = animal
        


    def get(self, animal_id: str) -> Animal | None:
        if animal_id in self.animals:
            return self.animals[animal_id]
        return None
    
    def list_all(self):
        return [animal.info() for animal in self.animals.values()]
    
    def is_adopted(self, animal_id: str) -> bool:
        if animal_id in self.adoptions:
            return True
        return False


    def set_adopted(self, animal_id: str, adopter_name: str):
        if animal_id not in self.animals:
            raise ValueError("Animale insesistente")
        self.adoptions[animal_id] = adopter_name
    



