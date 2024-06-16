#!/usr/bin/python3

import sys
sys.path.insert(0, "/workspaces/holbertonschool-hbnb/class")
from flask import Flask, request, jsonify
from Place import Place
from User import User
from City import City 

app = Flask(__name__)
user1 = User("jorge@gmail.com", "Jorge", "Beritan")
city1 = City("Matanzas", "CU")
place1 = Place("Hotel", "Este Hotel esta God", 4, 3, 20, 200.0, 24.6, 25.7, user1.id, city1.id)

places = [place1.to_dict()]

@app.route('/places', methods=["GET", "POST"])
def get_post_places():
    if request.method == "GET":
        if len(places) > 0:
            return jsonify(places)
        else:
            return jsonify({"error": "Not found"}), 404
        
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"message:" "Invalud Input"}), 400

        name = data.get("name")
        description = data.get("description")
        number_of_rooms = data.get("number_of_rooms")
        number_of_bathrooms = data.get("number_of_bathrooms")
        max_guest = data.get("max_guest")
        price_per_night = data.get("price_per_night")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        host_id = data.get("host_id")
        city_id = data.get("city_id")

        place = Place(name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, host_id, city_id)
        places.append(place.to_dict())
        return jsonify(place.to_dict()), 201

@app.route("/places/<string:place_id>", methods=["GET", "PUT", "DELETE"])
def manage_place(place_id):
    place_dict = next((place for place in places if place.get("ID") == place_id), None)
    if not place_dict:
        return jsonify({"message": "Place not found"}), 404
    
    if request.method == "GET":
        return jsonify(place_dict), 200
    
    if request.method == "DELETE":
        places.remove(place_dict)
        return jsonify({}), 204
    
    if request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid input"}), 400
        
        name = data.get("name")
        description = data.get("description")
        number_of_rooms = data.get("number_of_rooms")
        number_of_bathrooms = data.get("number_of_bathrooms")
        max_guest = data.get("max_guest")
        price_per_night = data.get("price_per_night")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        host_id = data.get("host_id")
        city_id = data.get("city_id")

        if name:
            place_dict["name"] = name
        if description:
            place_dict["description"] = description
        if number_of_rooms:
            place_dict["number_of_rooms"] = number_of_rooms
        if number_of_bathrooms:
            place_dict["number_of_bathrooms"] = number_of_bathrooms
        if max_guest:
            place_dict["max_guest"] = max_guest
        if price_per_night:
            place_dict["price_per_night"] = price_per_night
        if latitude:
            place_dict["latitude"] = latitude
        if longitude:
            place_dict["longitude"] = longitude
        if host_id:
            place_dict["host_id"] = host_id
        if city_id:
            place_dict["city_id"] = city_id

        return jsonify(place_dict), 200

if __name__ == "__main__":
    app.run(debug=True)