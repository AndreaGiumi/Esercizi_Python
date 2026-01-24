from flask import Flask, url_for, jsonify, request
from mainClass import flotta
from car import Car
from van import Van

app = Flask(__name__)

@app.route("/")
def descrizione():
    return {
        "message": "Welcome to Rent Service API",
        "links": {
            "vehicles": url_for("list_vehicles", _external=False),
            "id_vehicle": url_for("vehicle_id", id_vehicle="HA014AS", _external=False),
            "estimate_sample": url_for("extimate_time", id_vehicle="HA014AS", factor=2.0, _external=False)
        }
    }


@app.route("/vehicles")
def list_vehicles():
    return jsonify(flotta.list_all())


@app.route("/vehicles/<string:id_vehicle>")
def vehicle_id(id_vehicle: str):
    vehicle = flotta.get(id_vehicle)
    if vehicle is None:
        return jsonify({"error": "veicolo non trovato"}), 404
    return jsonify(vehicle.info()) 


@app.route("/vehicles/<string:id_vehicle>/prep_time/<float:factor>")
def extimate_time(id_vehicle: str, factor: float):
    vehicle = flotta.get(id_vehicle)
    if vehicle is None:
        return jsonify({"error": "veicolo non trovato!"}), 404
    
    prep_time = vehicle.base_cleaning_time() * factor + vehicle.wear_level() * 15
    
    return jsonify({
        "id": id_vehicle,
        "vehicle_type": vehicle.vehicle_type(),
        "factor": factor,
        "estimated_total_minutes": int(prep_time) 
    })



@app.route("/vehicles/", methods=["POST"])
def create_vehicle():
    data = request.get_json()
    
    required = ["plate_id", "model", "driver_name", "registration_year", "status"]
    
    if not all(field in data for field in required):
        return jsonify({"error": "Campi obbligatori mancanti"}), 400
    
    vehicle_type = data.get("vehicle_type", "car")  
    
    try:
        if vehicle_type == "car":
            vehicle = Car(
                plate_id=data["plate_id"],
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                doors=data.get("doors", 4)
            )
        elif vehicle_type == "van":
            vehicle = Van(
                plate_id=data["plate_id"],
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                max_load_kg=data["max_load_kg"]
            )
        else:
            return jsonify({"error": "Tipo veicolo non supportato!"}), 400  
        
        success = flotta.add(vehicle)
        
        if success:
            return jsonify(vehicle.info()), 201
        else:
            return jsonify({"error": "Veicolo già esistente!"}), 409
            
    except KeyError as e:
        return jsonify({"error": f"Dati mancanti: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"Errore creazione: {e}"}), 500



if __name__ == "__main__":
    app.run(debug=True)
