#!/usr/bin/python3

import sys
sys.path.insert(0, "/workspaces/holbertonschool-hbnb/class")
from flask import Flask, request, jsonify
from Review import Review
from User import User
from Place import Place

app = Flask(__name__)

@app.route("/places/<string:place_id>/reviews", methods=["GET", "POST"])
def manage_review_place(place_id):
    if request.method == "GET":
        pass