from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str, doors: int):
        super().__init__(plate_id, model, driver_name, registration_year, status)

        self.doors = doors
        self.is_cabrio = False

    def vehicle_type(self):
        return "car"
    

    def base_cleaning_time(self):
        return 30
    
    def wear_level(self):
        return 1
    

    def info(self):
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
            "doors": self.doors,
            "is_cabrio": self.is_cabrio
        }