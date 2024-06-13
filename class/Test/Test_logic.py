#!/usr/bin/python3


import sys
sys.path.append("/workspaces/holbertonschool-hbnb/class")
from Place import Place
from User import User
from City import City

city1 = City("Matanzas", "CU")
user1 = User("jorge@gmail.com", "Jorge", "Beritan")
user2 = User("jorge@gmail.com", "Nico", "Bonilla")
place1 = Place("casa maria", "Esta muy linda esta casas",2, 1, 4, 2000.0, 25.7, 19.6, user1.ID, city1.ID)


print(place1.number_of_rooms)