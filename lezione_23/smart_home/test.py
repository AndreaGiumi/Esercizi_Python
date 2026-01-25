import requests
import json

BASE_URL = "http://localhost:5000"
a_serial_number = "SN-LUMP-777"

if __name__=="__main__":
    
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }


    response = requests.get(f"{BASE_URL}/", headers=headers)
    print("GET/", response.status_code, response.json())
    
    print("\n")
    
    
    response = requests.get(f"{BASE_URL}/devices", headers=headers)
    print(f"/GET/{a_serial_number}", response.status_code, response.json())
    
    print("\n")
    
    
    new_device ={
        "serial_number": a_serial_number,
        "brand": "LIFX",
        "room": "Bedroom",
        "installation_year": 2025,
        "status": "online",
        "type": "bulb",
        "brightness_lumens": 1100,
        "color_capability": True
        }
    
    response = requests.post(f"{BASE_URL}/devices", headers=headers, json=new_device)



    response = requests.get(f"{BASE_URL}/devices/{a_serial_number}", headers=headers)
    print(f"GET/devices/{a_serial_number}", response.status_code, response.json())
    
    print("\n")
    
    new_status = {"status": "offline"}
    
    response = requests.patch(f"{BASE_URL}/devices/{a_serial_number}/status", headers=headers, json=new_status)
    print(f"PATCH/devices/{a_serial_number}/status", response.status_code, response.json())
    
    print("\n")
    
    update_device = new_device.copy()
    
    update_device["room"] = "kitchen"
    
    response = requests.put(f"{BASE_URL}/devices/{a_serial_number}", headers=headers, json=update_device)
    print(f"PUT/{a_serial_number}",  response.status_code,  response.json())
    
    print("\n")
    
    response = requests.delete(f"{BASE_URL}/devices/{a_serial_number}", headers=headers)
    print(f"DELETE/devices/{a_serial_number}", response.status_code, response.json())
    
    print("\n")
    
    response = requests.get(f"{BASE_URL}/devices/{a_serial_number}", headers=headers)
    print(f"GET/devices/{a_serial_number}", response.status_code, response.json())