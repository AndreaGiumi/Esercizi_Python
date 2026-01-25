import requests
import json

BASE_URL = "http://localhost:5000"
a_id = "dell_xps_luca"
if __name__=="__main__":
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

    print("#1 =======ESEMPIO GET / =========")
    response = requests.get(f"{BASE_URL}/", headers=headers)
    print("GET /", response.status_code, response.json())

    print("\n")
    
    print("#2 ESEMPIO GET/devices")
    
    response = requests.get(f"{BASE_URL}/devices", headers=headers)
    print("GET/devices",response.status_code, response.json())
    
    print("\n")

    print("#3 =======ESEMPIO POST=======")

    device ={
        
        "id": a_id,
        "type": "laptop",
        "model": "Dell XPS 15 9530",
        "customer_name": "Luca Bianchi",
        "purchase_year": 2022,
        "status": "diagnosing",
        "has_dedicated_gpu": True,
        "screen_size_inches": 15.6
    }
    response = requests.post(f"{BASE_URL}/devices", headers=headers, json=device)
    print("POST/devices", response.status_code, response.json())
    
    
    print("\n")

    print("#4 =======ESEMPIO GET / device/id=======")
    
    response = requests.get(f"{BASE_URL}/devices/{a_id}", headers=headers)
    print(f"GET/devices/{a_id}", response.status_code, response.json())
    
    print("\n")
    
    
    print("#5 =======ESEMPIO PATCH======")
    
    new_status = {"status":"repairing"}
    
    response = requests.patch(f"{BASE_URL}/devices/{a_id}/status", headers=headers, json=new_status)
    print(f"PATCH/devices/{a_id}/status", response.status_code, response.json())
    
    print("\n")
    

    print("#6 =======ESEMPIO PUT======")
    
    
    new_customer = device.copy()
    
    new_customer["customer_name"] = "Kristian Lanni"
    
    response = requests.put(f"{BASE_URL}/devices/{a_id}", headers=headers, json=new_customer)
    print(f"PUT/devices/{a_id}", response.status_code, response.json())
    
    print("\n")
    
    
    print("#7 =======ESEMPIO DELETE======")
    
    response = requests.delete(f"{BASE_URL}/devices/{a_id}", headers=headers)
    print(f"DELETE/devices/{a_id}", response.status_code, response.json())
    print("\n")
    
    print("#8 =======ESEMPIO GET dopo DELETE======")
    
    response = requests.get(f"{BASE_URL}/devices/{a_id}", headers=headers)
    print(f"GET/devices/{a_id}", response.status_code, response.json())
    
    print("\n")