from flask import Flask, url_for, jsonify, request
import json

# Assumiamo che queste classi siano salvate nei rispettivi file o presenti nel contesto
# Se sono nello stesso file, rimuovi gli import
from smartDevice import SmartDevice
from ioTHub import IoTHub
from smartBulb import SmartBulb
from securityCamera import SecurityCamera

# 1. Creazione dell'Hub
my_hub = IoTHub()

# 2. Creazione dei dispositivi iniziali
bulb1 = SmartBulb("SN-LUMP-001", "Philips Hue", "Salotto", 2024, "online", 800, True)
cam1 = SecurityCamera("SN-CAM-99X", "Arlo", "Ingresso", 2023, "offline", "4K", True)

# 3. Aggiunta all'Hub
my_hub.add(bulb1)
my_hub.add(cam1)

# 4. Test diagnostica (Console)
print(f"Tempo diagnostica Lampadina: {bulb1.diagnostici_time()} sec")
print(f"Tempo diagnostica Telecamera: {cam1.diagnostici_time()} sec")

# 6. Lista completa (Console)
print("\n--- Lista Dispositivi ---")
print(json.dumps(my_hub.list_all(), indent=2))

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "description": "Smart Home Hub API",
        "links": {
            "dev_list": url_for("devices_list", _external=True),
            "devi_id": url_for("devices_id", serial_number="SN-LUMP-001", _external=True),
            "devi_cam": url_for("devices_id", serial_number="SN-CAM-99X", _external=True),
            "dev_diagn": url_for("devices_diagnostic", serial_number="SN-LUMP-001", factor=1.0, _external=True),
        }
    }

@app.route("/devices", methods=["GET"])
def devices_list():
    return jsonify(my_hub.list_all())

@app.route("/devices/<string:serial_number>")
def devices_id(serial_number: str):
    device = my_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device non trovato!"}), 404
    return jsonify(device.info())

@app.route("/devices/<string:serial_number>/diagnostic/<float:factor>", methods=["GET"])
def devices_diagnostic(serial_number: str, factor: float):
    device = my_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device non trovato!"}), 404
    
    diagnostic_time = device.diagnostici_time(factor)
    return jsonify({
        "id": serial_number,
        "device_type": device.device_type(),
        "factor": factor,
        "diagnostic_seconds": diagnostic_time
    })

@app.route("/devices", methods=["POST"])
def post():
    data: dict = request.get_json()
    
    if data is None:
        return jsonify({"error": "Nessun dato JSON inviato"}), 400
    
    # Campi comuni obbligatori
    required = ["serial_number", "brand", "room", "installation_year", "status", "type"]
    if not all(field in data for field in required):
        return jsonify({"error": f"Campi obbligatori mancanti. Richiesti: {required}"}), 400
    
    device_type = data.get("type")
    
    try:
        if device_type == "bulb":
            # Controllo campi specifici per Bulb
            if "brightness_lumens" not in data or "color_capability" not in data:
                 return jsonify({"error": "Mancano campi specifici per Bulb (brightness_lumens, color_capability)"}), 400
            
            # CREAZIONE CORRETTA DELL'OGGETTO
            device = SmartBulb(
                serial_number=data["serial_number"],
                brand=data["brand"],
                room=data["room"],
                installation_year=int(data["installation_year"]),
                status=data["status"],
                brightness_lumens=int(data["brightness_lumens"]),
                color_capability=bool(data["color_capability"])
            )
            
        elif device_type == "camera":
            # Controllo campi specifici per Camera
            if "resolution" not in data or "night_vision" not in data:
                 return jsonify({"error": "Mancano campi specifici per Camera (resolution, night_vision)"}), 400

            # CREAZIONE CORRETTA DELL'OGGETTO
            device = SecurityCamera(
                serial_number=data["serial_number"],
                brand=data["brand"],
                room=data["room"],
                installation_year=int(data["installation_year"]),
                status=data["status"],
                resolution=str(data["resolution"]),
                night_vision=bool(data["night_vision"])
            )
        else:
            return jsonify({"error": "Tipo inserito non supportato (usa 'bulb' o 'camera')"}), 400
        
        success = my_hub.add(device)
        
        if success:
            return jsonify(device.info()), 201
        else:
            return jsonify({"error": "Device con questo Serial Number già esistente"}), 409
    
    except ValueError as e:
        return jsonify({"error": f"Errore nel formato dei dati: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Errore interno: {str(e)}"}), 500


@app.route("/devices/<string:serial_number>", methods=["PUT"])
def put(serial_number: str):
    data: dict = request.get_json()
    
    if data is None:
        return jsonify({"error": "Nessun dato JSON inviato"}), 400

    # Verifichiamo se il device esiste PRIMA di provare a crearlo
    existing_device = my_hub.get(serial_number)
    if existing_device is None:
        return jsonify({"error": "Device non trovato, impossibile aggiornare"}), 404
    
    required = ["brand", "room", "installation_year", "status", "type"]
    if not all(field in data for field in required):
        return jsonify({"error": "Campi obbligatori mancanti"}), 400
    
    device_type = data.get("type")
    new_device = None
    
    try:
        # Nota: Usiamo serial_number dell'URL per garantire coerenza
        if device_type == "bulb":
            new_device = SmartBulb(
                serial_number=serial_number,
                brand=data["brand"],
                room=data["room"],
                installation_year=int(data["installation_year"]),
                status=data["status"],
                brightness_lumens=int(data.get("brightness_lumens", 0)),
                color_capability=bool(data.get("color_capability", False))
            )
        elif device_type == "camera":
            new_device = SecurityCamera(
                serial_number=serial_number,
                brand=data["brand"],
                room=data["room"],
                installation_year=int(data["installation_year"]),
                status=data["status"],
                resolution=str(data.get("resolution", "1080p")),
                night_vision=bool(data.get("night_vision", False))
            )
        else:
            return jsonify({"error": "Tipo non supportato"}), 400

        # Eseguiamo l'update (il metodo update dell'hub non restituisce valori, modifica in loco)
        my_hub.update(serial_number, new_device)
        
        # Verifichiamo che l'update sia avvenuto recuperando il device
        updated_device = my_hub.get(serial_number)
        return jsonify(updated_device.info()), 200

    except Exception as e:
        return jsonify({"error": f"Errore interno: {e}"}), 500


@app.route("/devices/<string:serial_number>/status", methods=["PATCH"]) 
def patch(serial_number: str):
    # NOTA: methods deve essere una lista [], non un set {}
    data: dict = request.get_json()
    
    device = my_hub.get(serial_number)
    
    if data is None:
        return jsonify({"error": "Nessun dato JSON"}), 400
    
    if device is None:
        return jsonify({"error": "Device non trovato"}), 404
    
    # Corretto il typo "statis" in "status"
    if "status" not in data:
        return jsonify({"error": "Campo 'status' mancante"}), 400
    
    new_status = data["status"] # Corretto: prendiamo il valore dal dizionario
    
    valid_status = ["online", "offline", "updating", "error"]
    
    if new_status not in valid_status:
        return jsonify({"error": f"Status: {new_status} non valido. Status validi: {valid_status}"}), 400
    
    try:
        # IoTHub.patch_status è void (ritorna None), modifica l'oggetto in memoria
        my_hub.patch_status(serial_number, new_status)
        
        # Ritorniamo le info aggiornate
        return jsonify(device.info()), 200
        
    except Exception as e:
        return jsonify({"error": f"Errore interno: {e}"}), 500


@app.route("/devices/<string:serial_number>", methods=["DELETE"])
def delete(serial_number: str):
    # my_hub.delete restituisce True se cancellato, False se non trovato
    success = my_hub.delete(serial_number)
    
    if not success:
        return jsonify({"error": "Device non trovato"}), 404
    
    return jsonify({"delete": True, "serial_number": serial_number}), 200

if __name__ == "__main__":
    app.run(debug=True)
