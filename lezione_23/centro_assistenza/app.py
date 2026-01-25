from flask import Flask, url_for, request, jsonify
from serviceCenter import ServiceCenter
from smartphone import Smartphone
from laptop import Laptop

center = ServiceCenter()
phone = Smartphone("d1", "iPhone 13", "Mario Rossi", 2022, "received", True, 128)
laptop = Laptop("d2", "ThinkPad X1", "Luigi Verdi", 2021, "diagnosing", True, 15.6)

center.add(phone)
center.add(laptop)

print("Tutti i dispositivi:", center.list_all())
print("Tempo stimato smartphone:", phone.estimated_total_time(1.2))
print("Tempo stimato laptop:", laptop.estimated_total_time())



app = Flask(__name__)

#------------------ GET --------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "description": "Welcome to Service Center API",
        "links": {
            "devices": url_for("list_devices"),
            "devices_id": url_for("id_device", device_id="d1"),
            "estimate_sample": url_for("estimate_time", device_id="d1", factor=1.2)
        }
    })

@app.route("/devices", methods=["GET"])
def list_devices():
    return jsonify(center.list_all())

@app.route("/devices/<string:device_id>", methods=["GET"])
def id_device(device_id: str):
    device = center.get(device_id)

    if device is None:
        return jsonify({"error":"Device non trovato!"}), 404
    return jsonify(device.info())


@app.route("/devices/<string:device_id>/est_time/<float:factor>")
def estimate_time(device_id: str, factor: float =1.0):
    device = center.get(device_id)

    if device is None:
        return jsonify({"error":"Device non trovato!"}), 404
    est_time = device.estimated_total_time(factor)

    return jsonify({
        "id":device_id,
        "device_type":device.device_type(),
        "factor":factor,
        "estimate_total_minutes":est_time
    })
#-----------   POST ----------------------

@app.route("/devices", methods=["POST"])
def post():
    # si prende il body dal json, quindi tutti i dati
    data: dict = request.get_json()
    #--------------------------------------------------------------------

    # si fa una lista di tutti i campi obbligatori
    
    required = ["id", "type", "model", "customer_name", "purchase_year", "status"]

    #--------------------------------------------------------------------

    #  controlliamo che i campi comuni siano tutti inseriti tramite questo ciclo for

    if not all(field in data for field in required):
        return jsonify({"error":"Campi obbligatori mancanti"}), 400
    #--------------------------------------------------------------------

    # contollo del tipo (in questo caso andiamo a controllare direttamente il campo model, 
    #                                                                       che se assente assegna di default il valore che inseriamo dopo)
    device_type = data.get("type", "smartphone").lower()

    #--------------------------------------------------------------------
    
    # andiamo a gestire le due situazioni con il try/except


    try:
        if device_type == "smartphone":
                device = Smartphone(
                id=data["id"],
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_protective_case=data.get("has_protective_case", False), # usa get per sicurezza
                storage_gb=data.get("storage_gb", 64)
            ) # con l'oggetto all'interno
        elif device_type == "laptop":
            device = Laptop(
                id=data["id"],
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_dedicated_gpu=data.get("has_dedicated_gpu", False),
                screen_size_inches=data.get("screen_size_inches", 13.0)
            ) # con l'oggetto all'interno
        else:
            return jsonify({"error":"Tipo non supportato"}), 400
    #--------------------------------------------------------------------
        
        # andiamo a gestire il successo della creazione dell'oggetto, nello specifico:
            # se il device viene aggiunto, ritornano le info (201), altrimenti ritorna error 409

        success = center.add(device)

        if success:
            return jsonify(device.info()), 201
        else:
            return jsonify({"error":"Device già esistente!"}), 409
        
    #--------------------------------------------------------------------
        # andiamo a gesire le eccezzioni, KeyError(400), Exception(500)
    except KeyError as e:
        return jsonify({"error": f"Dati mancanti {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"Errore nella creazione: {e}"}), 500
    

    '''
    NOTA BENE:

    quando nella creazione dell'oggetto utilizzi le parentesi quadre per prendere il valore da assegnare a quel campo,
    nel momento in cui quel dato non viene inserito viene alzata un except KeyError (gestita nel try/except) in automatico.

    Se invece vogliamo dare un valore di default usiamo il .get("campo desiderato", valore di default)

    '''
        
#---------------- PUT-------------------------------

@app.route("/devices/<string:device_id>", methods=["PUT"])
def put(device_id: str):
    data: dict = request.get_json()

    if data is None:
        return jsonify({"error":"error"}), 400
    
    device = center.get(device_id)
    if  device is None:
        return jsonify({"error":"error"})
    
    required = ["model", "customer_name", "purchase_year", "status"]

    if not all(field in data for field in required):
        return jsonify({"error": "Campi obbligatori mancanti!"}), 400
    
    device_type = data.get("device_type", "smartphone").lower()

    new_device = None

    try:
        if device_type == "smartphone":
            new_device =Smartphone(
                id=device_id,
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_protective_case=data.get("has_protective_case", False), # usa get per sicurezza
                storage_gb=data.get("storage_gb", 64)
            )
        elif device_type == "laptop":
            new_device = Laptop(
                id=data["id"],
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_dedicated_gpu=data.get("has_dedicated_gpu", False),
                screen_size_inches=data.get("screen_size_inches", 13.0)
            )
        else:
            return jsonify({"error":"Tipo device non supportato!"}), 400
        
        success = center.update(device_id, new_device)

        if success:
            return jsonify(new_device.info()), 201
        else:
            return jsonify({"error":"error"}), 500
    except KeyError as e:
        return jsonify({"error":f"Dati mancanti: {e}"}), 400
    except Exception as e:
        return jsonify({"error":f"Errore interno: {e}"}), 500
    

#---------------- PATCH-------------------------------

@app.route("/devices/<string:device_id>/status", methods=["PATCH"])
def patch(device_id: str):
    data: dict = request.get_json()

    if data is None:
        return jsonify({"error":"error"}), 404
    
    device = center.get(device_id)

    if device is None:
        return jsonify({"error":"error"}), 404
    

    if "status" not in data:
        return jsonify({"error":"campo status mancante"}), 400
    
    new_status = data["status"]

    valid_status = ["received","diagnosing","repairing", "ready", "delivered"]


    if new_status not in valid_status:
        return jsonify({"error": f"Stato: {new_status} non valido. Validi: {valid_status}"}), 400
    try:
        success = center.patch_status(device_id, new_status)

        if success:
            return jsonify(device.info()), 200
        else:
            return jsonify({"error": "impossibile aggiornare lo stato"}), 500
        
    except Exception as e:
        return jsonify({"error": f"Errore interno: {e}"}), 500
    

#---------------- DELETE---------------------

@app.route("/devices/<string:device_id>", methods=["DELETE"])
def delete(device_id: str):

    device = center.get(device_id)

    if device is None:
        return jsonify({"error":"error"}), 404
    

    center.delete(device_id)

    return jsonify({"delete": True, "id": device_id})



    


if __name__ == "__main__":
    app.run(debug=True)

