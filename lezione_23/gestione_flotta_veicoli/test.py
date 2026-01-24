import json
import requests

BASE_URL = "http://127.0.0.1:5000"

def print_response(title, response):
    """Utility per stampare in modo leggibile le risposte HTTP."""
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Response text:")
        print(response.text)
    print()


    if __name__=="__main__":

        headers = {
            "Content-type": "application/json",
            "Accept":"application/json"
        }

        r = requests.get(f"{BASE_URL}/", headers=headers)
        print_response("GET/vehicles", r)