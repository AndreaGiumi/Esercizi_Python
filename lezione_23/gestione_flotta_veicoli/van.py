from vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str, max_load_kg: int):
        super().__init__(plate_id, model, driver_name, registration_year, status)

        self.max_load_kg = max_load_kg
        self.require_special_license = False


    def vehicle_type(self):
        return "van"
    
    def base_cleaning_time(self):
        return 60
    
    def wear_level(self):
        return 5
    
    def info(self):
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
            "max_load kg": self.max_load_kg,
            "require_specia_license": self.require_special_license
        }