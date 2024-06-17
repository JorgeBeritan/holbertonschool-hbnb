from flask import Flask, jsonify, request
from amenities import Amenity

app = Flask(__name__)

amenities = []

@app.route("/amenities", methods=["GET", "POST"])
def manage_amenities():
 
    if request.method == "GET":
        # Convertir cada objeto Amenity a un diccionario y retornar como JSON
        return jsonify(amenities)

    if request.method == "POST":
        data = request.get_json()
        if 'name' not in data or data['name'] == "":
            return jsonify({"error": "Name is required"}), 400
        amenity = Amenity(data['name'])
        amenities.append(amenity)
        return jsonify(amenity.to_dict()), 201

# Ruta para gestionar una amenity específica por su ID
@app.route("/amenities/<string:amenity_id>", methods=["GET", "DELETE", "PUT"])
def manage_amenity(amenity_id):
    # Buscar la amenity específica por ID
    amenity = next((a for a in amenities if a.id == amenity_id), None)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    if request.method == "GET":
        return jsonify(amenity)

    if request.method == "DELETE":
        amenities.remove(amenity)
        return jsonify({}), 204

    if request.method == "PUT":
        data = request.get_json()
        if 'name' in data:
            try:
                amenity.name = data['name']
            except (TypeError, ValueError) as e:
                return jsonify({"error": str(e)}), 400
        return jsonify(amenity)

# Verificar si el script es el punto de entrada principal y ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)  # Iniciar el servidor en modo depuración
