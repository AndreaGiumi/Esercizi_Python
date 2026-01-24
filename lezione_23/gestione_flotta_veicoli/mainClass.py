
from car import Car
from fleetManager import FleetManager
from van import Van


flotta: FleetManager = FleetManager()

macchina1: Car = Car("HB065CR", "Alfa Romeo Stelvio", "Andrea", "2026", "rented", 5)

van1: Van = Van("FR045DD", "Volkswagen Type 2", None, "1963", "available", 250)


flotta.add(macchina1)
flotta.add(van1)


flotta.get("HB065CR")