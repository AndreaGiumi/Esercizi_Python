from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str)-> None:
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self):
        pass
    
    @abstractmethod
    def base_cleaning_time(self):
        pass
    
    @abstractmethod
    def wear_level(self):
        pass

    def info(self):
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status
        }
    
    def estimated_prep_time(self, factor: float = 1.0):
        return f"Tempo di preparazione stimato: {int(self.base_cleaning_time() * factor + self.wear_level()* 15)}"
