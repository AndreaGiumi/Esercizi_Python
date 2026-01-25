from smartDevice import SmartDevice

class SmartBulb(SmartDevice):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, 
                 brightness_lumens: int, color_capability: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return 12  # Esempio: 12 Watt

    def connection_quality(self) -> int:
        return 3   # Bassa banda richiesta

    def info(self) -> dict[str, float| int| str]:
        # Recupera il dizionario base e lo estende
        data = super().info()
        data.update({
            "brightness_lumens": self.brightness_lumens,
            "color_capability": self.color_capability
        })
        return data
