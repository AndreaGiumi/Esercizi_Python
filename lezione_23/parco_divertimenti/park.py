from ride import Ride
class Park:
    def __init__(self):
        self.rides: dict[str, Ride] = {}

    def add(self, ride: Ride) -> None:
        if ride.id in self.rides:
            return "Errore, attrazione già presente!"    
        self.rides[ride.id] = ride

    
    def get(self, ride_id: str) -> dict:
        return self.rides[ride_id]

    def list_all(self) -> list[dict[str, str | int]]:
        return [ride.info() for ride in self.rides.values()]
    
            