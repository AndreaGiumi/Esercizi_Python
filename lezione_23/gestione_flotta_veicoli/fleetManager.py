from car import Car
from van import Van
class FleetManager:
    def __init__(self) -> None:
        self.vehicles: dict[str, Car | Van] = {}

    def add(self, vehicle: Car | Van) -> bool:
        if vehicle.plate_id in self.vehicles:
            print("Il veicolo già esiste")
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        print("Veicolo aggiunto con successo!")
        return True
    
    def get(self, plate_id: str) -> Car | Van | None:
        if plate_id not in self.vehicles:
            print("Il veicolo non esiste")
            return None
        return self.vehicles.get(plate_id)
    
    def update(self, plate_id: str, new_vehicle: Car | Van) -> None:
        if plate_id not in self.vehicles:
            print("Il veicolo non esiste")
        else:
            self.vehicles[plate_id] = new_vehicle
    
    def patch_status(self, plate_id: str, new_status: str) -> None:
        v = self.vehicles.get(plate_id)

        if v in None:
            return
        v.status = new_status
        

    def delete(self, plate_id: str) -> bool:
        if plate_id not in self.vehicles:
            print("Il veicolo non esiste")
            return False
        del self.vehicles[plate_id]
        print("Il veicolo è stato eliminato con successo!")
        return True
    
    def list_all(self):
        return [vehicle.info() for vehicle in self.vehicles.values()]
