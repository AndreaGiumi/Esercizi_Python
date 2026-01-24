from flask import Flask, url_for, jsonify
from main_rifugio import rifugio
app = Flask(__name__)

@app.route("/", methods = ['GET'])
def descrizione():
    return {"message": "Welcome to Animal Shelter API",
            "links": {
                "animals": url_for("list_animals"),
                "animal_id": url_for("id_animal"),
                "animal_food": url_for("food_animal"),
                "animal_adoption": url_for("adoption_animal")
            } }

@app.route("/animals", methods=["GET"])
def list_animals():
    return jsonify(rifugio.list_all())

@app.route("/animals/<string:animal_id>", methods=["GET"])
def id_animal(animal_id:str):
    animal = rifugio.get(animal_id)

    if animal is None:
        return jsonify({"error":"Animal not found"}), 404
    return jsonify(rifugio.get(animal_id).info())

@app.route("/animals/<string:animal_id>/food", methods=["GET"])
def food_animal(animal_id:str):
    animal = rifugio.get(animal_id)

    if animal is None:
        return jsonify({"error":"Animal not found"}), 404
    return jsonify({
        "id":animal.id,
        "specie":animal.species(),
        "cibo giornaliero stimato": animal.daily_food_grams()
    })

@app.route("/animals/<string:animal_id>/adoption", methods=["GET"])
def adoption_animal(animal_id:str):
    animal = rifugio.get(animal_id)
    adoption = rifugio.is_adopted(animal_id)
    adopter = rifugio.adoptions

    if animal is None:
        return jsonify({"error":"Animal not found"}), 404
    
    if not adoption:
        return jsonify({
            "id":animal.id,
            "adopted": False
        })
    else:
        return jsonify({
            "id": animal.id,
            "adopted": adoption,
            "adopter_name": adopter[animal_id]
        })
if __name__=="__main__":
    app.run(debug=True)