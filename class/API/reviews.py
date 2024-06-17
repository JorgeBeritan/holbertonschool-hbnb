#!/usr/bin/python3

import sys
sys.path.insert(0, "/workspaces/holbertonschool-hbnb/class")
from flask import Flask, request, jsonify
from Review import Review
from User import User
from Place import Place
from City import City

app = Flask(__name__)
user1 = User("jorge@gmail.com", "Jorge", "Beritan")
city1 = City("Montevideo", "UY")
place1 = Place("Casa de Jorge", "Es la casa del Joge", 2, 1, 5, 200.0, 25.7, 24.8, user1.id, city1.id)
review1 = Review(place1.id, user1.id, 4, "Es la casa del Jorge GOD")

reviews = [review1.to_dict()]
@app.route("/reviews/<string:review_id>", methods=["GET", "PUT", "DELETE"])
def route(review_id):
    review_dict = next((review for review in reviews if review.get("ID") == review_id), None)

    if not review_dict:
        return jsonify({"message": "Review not found"}), 404
    
    if request.method == "GET":
        return jsonify(review_dict), 200
    
    if request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid Input"}), 400
        
        place_id = data.get("place_id")
        user_id = data.get("user_id")
        rating = data.get("rating")
        comment = data.get("comment")

        if place_id:
            review_dict["place_id"] = place_id
        if user_id:
            review_dict["user_id"] = user_id
        if rating:
            review_dict["rating"] = rating
        if comment:
            review_dict["comment"] = comment

        return jsonify(review_dict), 200

    if request.method == "DELETE":
        reviews.remove(review_dict)
        return jsonify({}), 204


@app.route("/places/<string:place_id>/reviews", methods=["GET", "POST"])
def get_reviews_place(place_id):
    reviews_list = [review for review in reviews if review.get("place_id") == place_id]
    if request.method == "GET":
        if len(reviews_list) == 0:
            return jsonify({"error": "Not found"}), 404
        return jsonify(reviews_list), 200
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid Input"}), 400
        
        place_idr = data.get("place_id")
        user_id = data.get("user_id")
        rating = data.get("rating")
        comment = data.get("comment")

        if place_idr:
            reviews_list["place_id"] = place_idr
        if user_id:
            reviews_list["user_id"] = user_id
        if rating:
            reviews_list["rating"] = rating
        if comment:
            reviews_list["comment"] = comment

        return jsonify(reviews_list), 200


@app.route("/users/<string:user_id>/reviews", methods="")
def get_review_user(user_id):
    review_list = [review for review in reviews if review.get("user_id") == user_id]
    if request.method == "GET":
        if len(review_list) == 0:
            return jsonify({"error": "Review not found"}), 404
        return jsonify(review_list), 200


if __name__ == "__main__":
    print(review1.id)
    app.run(debug=True)