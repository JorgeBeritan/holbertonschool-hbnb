#!/usr/bin/python3
import sys
sys.path.insert(0, "/workspaces/holbertonschool-hbnb/class")
from User import User
from flask import Flask, jsonify, request

app = Flask(__name__)
user1 = User("jorge@gmail.com", "Jorge", "Beritan")
users = [user1.to_dict()]
@app.route("/users", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        if len(users) > 0:
            return jsonify(users)
        else:
            return jsonify({"message": "No found"}), 404
    
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid Input"}), 400
        
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        user = User(email,first_name, last_name)
        users.append(user.to_dict())
        return jsonify(user.to_dict()), 201

@app.route("/users/<string:user_id>", methods=["GET", "DELETE", "PUT"])
def manage_user(user_id):
    user_dict = next((user for user in users if user.get("ID") == user_id), None)
    if not user_dict:
        return jsonify({"message": "User not found"}), 404

    if request.method == "GET":
        return jsonify(user_dict), 200

    if request.method == "DELETE":
        users.remove(user_dict)
        return jsonify({}), 204

    if request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid Input"}), 400
        
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        
        if email:
            user_dict["email"] = email
        if first_name:
            user_dict["first_name"] = first_name
        if last_name:
            user_dict["last_name"] = last_name
        
        return jsonify(user_dict), 200

if __name__ == "__main__":
    app.run(debug=True)