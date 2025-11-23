from flask import Flask, url_for, jsonify
from class_main import park
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def description():
    return jsonify({
        "description" : "Welcome to Andrea's API Park",

        "links" : {
            "rides" : url_for("list_rides"),
            "rides_rc1" : url_for("id_ride", ride_id="rc1"),
            "ride_rc1_wait" : url_for("ride_wait_time", ride_id="rc1")
        }
    })

@app.route('/rides', methods=['GET'])
def list_rides():
    return jsonify(park.list_all())

@app.route('/rides/<string:ride_id>', methods=['GET'])
def id_ride(ride_id: str):
    return jsonify(park.get(ride_id).info())

@app.route('/rides/<string:ride_id>/wait', defaults = {"crowd": 1.0}, methods=['GET'])
@app.route('/rides/<string:ride_id>/wait/<float:crowd>', methods=['GET'])
def ride_wait_time(ride_id: str, crowd: float):
    ride = park.get(ride_id)
    wait = ride.wait_time(crowd)
    return jsonify({
        "ride_id" :  ride_id,
        "crowd_factor" : crowd,
        "wait_time_minutes" : wait
    })

if __name__=="__main__":
    app.run(debug=True)