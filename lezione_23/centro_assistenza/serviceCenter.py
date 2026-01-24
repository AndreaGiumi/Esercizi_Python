from smartphone import Smartphone
from laptop import Laptop


class ServiceCenter:
    def __init__(self):
        self.devices: dict[str, Smartphone | Laptop] = {}
    
    def add(self, device: Smartphone | Laptop) -> bool:
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True
    
    def get(self, device_id: str) -> Smartphone | Laptop:
        return self.devices.get(device_id)
    
    def update(self, device_id: str, new_device: Smartphone | Laptop):
        if device_id in self.devices:
            self.devices[device_id] = new_device
            return True
        return False
    
    def patch_status(self, device_id: str, new_status: str):
        device = self.get(device_id)
        if device:
            device.status = new_status
            return True
        return False
    
    def delete(self, device_id: str):
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False
    
    def list_all(self):
        return [device.info() for device in self.devices.values()]
