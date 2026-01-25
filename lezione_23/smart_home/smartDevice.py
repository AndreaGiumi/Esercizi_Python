from abc import ABC, abstractmethod

# --- Classe Astratta SmartDevice ---
class SmartDevice(ABC):
    """
    Classe base astratta per un generico dispositivo IoT.
    Non può essere istanziata direttamente.
    """
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str):
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        """Restituisce il tipo del dispositivo (implementato nelle sottoclassi)."""
        pass

    @abstractmethod
    def energy_consumption(self) -> float| int:
        """Restituisce il consumo in Watt."""
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        """Restituisce un valore da 1 a 10 sulla qualità di connessione richiesta."""
        pass

    def info(self) -> dict[str, float| int| str]:
        """Restituisce un dizionario con i dati del dispositivo."""
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "type": self.device_type()  # Utile per distinguere i tipi nel JSON finale
        }

    def diagnostici_time(self, factor: float = 1.0) -> float:
        """Calcola il tempo stimato per la diagnostica."""
        # Formula: energy_consumption * factor + connection_quality * 10
        return (self.energy_consumption() * factor) + (self.connection_quality() * 10)
