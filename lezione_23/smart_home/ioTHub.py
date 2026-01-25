from smartDevice import SmartDevice
class IoTHub:
    def __init__(self):
        # Dizionario per accesso rapido tramite serial_number
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        """Aggiunge un dispositivo se il seriale non esiste."""
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        """Restituisce il dispositivo o None."""
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        """Sostituisce completamente un dispositivo esistente."""
        if serial_number in self.devices:
            self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        """Aggiorna solo lo stato di un dispositivo."""
        device = self.get(serial_number)
        if device:
            device.status = new_status

    def delete(self, serial_number: str) -> bool:
        """Rimuove un dispositivo dal sistema."""
        if serial_number in self.devices:
            del self.devices[serial_number]
            return True
        return False

    def list_all(self) -> list[dict[str, float| int| str]]:
        """Restituisce la lista delle info di tutti i dispositivi."""
        return [device.info() for device in self.devices.values()]

