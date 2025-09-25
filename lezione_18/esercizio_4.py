from datetime import datetime, date
from typing import Any

class DatabaseDates:
    def __init__(self,  date_str: str):
        try:
            self.date:date = datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(f"Fromato data non valido: {date_str}, usare 'gg.mm.aaaa'. ")


    def __str__(self):
        return self.date.strftime("%d.%m,%Y")
        
    

    def __eq__(self, other: Any):
        if isinstance(other, DatabaseDates) and self.date == other.date:
            return True
        else:
            return False
        


class ManageDate:
    def __init__(self):
        self.date: list[DatabaseDates] = []

    
    def add_date(self, date_str: str) -> None:
        new_date: DatabaseDates = DatabaseDates(date_str)
        self.date.append(new_date)        
        
    def delete_date(self, date_str: str) -> None:
        delelte_date: DatabaseDates = DatabaseDates(date_str)
        if delelte_date in self.date:
            self.date.remove(delelte_date)

    def modify_date(self, old_date_str: str, new_date_str:str) -> None:
        old_date:DatabaseDates = DatabaseDates(old_date_str)
        new_date:DatabaseDates = DatabaseDates(new_date_str)

        if old_date_str in self.date:
            indice: int = self.date.index(old_date)
            self.date[indice] = new_date
        else:
            print("Data da modificare non trovata")


    def find_date(self, date_str:str) -> bool:
        find_date:DatabaseDates = DatabaseDates(date_str)
        return find_date in self.date
    


    def view_date(self) ->list[str]:
        for d in self.date:
            return str(d)
        


gestore:ManageDate = ManageDate()                              # Crea un nuovo gestore
gestore.add_date("11.04.2025")                                # Aggiunge la data 11 aprile 2025
gestore.add_date("01.01.2024")                                # Aggiunge la data 1 gennaio 2024
gestore.modify_date("01.01.2024", "02.01.2024")                  # Modifica la seconda data
gestore.delete_date("11.04.2025")     
print("Date attuali:", ManageDate.view_date())                      # Stampa tutte le date memorizzate
print("La data 02.01.2024 è presente?")
print(ManageDate.find_date("02.01.2024")) 