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
BASE_URL = "http://127.0.0.1:5000"

@app.route(BASE_URL + "/")
def description():
    return jsonify({
        "description":"Welcome to Service Center API",
        "links":{
            "devices": url_for(BASE_URL + "/list_devices"),
            "devices_id":url_for(BASE_URL+ "/id_device"),
            "estimate_sample":url_for(BASE_URL + "/estimate_time", factor = 1.0)
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
"-----------   POST ----------------------"




if __name__ == "__main__":
    app.run(debug=True)

