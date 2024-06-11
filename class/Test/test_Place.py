#!/usr/bin/python3
import sys
sys.path.append("/workspaces/holbertonschool-hbnb/class")
from User import User
import unittest
import datetime
import uuid
from Place import Place

class TestPlaceClass(unittest.TestCase):
    def setUp(self):
        self.u1 = User("Jorge@gmail.com", "Jorge", "Beritan")
        self.u2 = User("nico@gmail.com", "Nico", "Bonilla")
        self.p1 = Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)
        self.p2 = Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7, self.u2.ID)


    def test_name(self):
        self.assertEqual(self.p1.name, "Hotel")

    def test_description(self):
        self.assertEqual(self.p1.description, "Esta bueno el Hotel")
    
    def test_number_of_rooms(self):
        self.assertEqual(self.p1.number_of_rooms, 4)

    def test_number_of_bathrooms(self):
        self.assertEqual(self.p1.number_of_bathrooms, 3)
    
    def test_max_guest(self):
        self.assertEqual(self.p1.max_guest, 20)

    def test_price_per_night(self):
        self.assertEqual(self.p1.price_per_night, 200.0)

    def test_latitude(self):
        self.assertEqual(self.p1.latitude, 24.6)

    def test_longitude(self):
        self.assertEqual(self.p1.longitude, 25.7)

    def test_name_bool(self):
        self.assertTrue(isinstance(self.p1.name, str))
    
    def test_name_exception(self):
        with self.assertRaises(TypeError):
            Place(123, "Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_name_exception_none(self):
        with self.assertRaises(ValueError):
            Place("","Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_description_bool(self):
        self.assertTrue(isinstance(self.p1.description, str))

    def test_description_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", 123, 4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_description_exception_none(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "", 4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_number_of_rooms_bool(self):
        self.assertTrue(isinstance(self.p1.number_of_rooms, int))

    def test_number_of_rooms_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", "4", 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_number_of_rooms_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", -4, 3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_number_of_bathrooms_bool(self):
        self.assertTrue(isinstance(self.p1.number_of_bathrooms, int))
    
    def test_numbert_of_bathrooms_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, "3", 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_numbert_of_bathrooms_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, -3, 20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_max_guest_bool(self):
        self.assertTrue(isinstance(self.p1.max_guest, int))

    def test_max_guest_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, "20", 200.0, 24.6, 25.7, self.u1.ID)

    def test_max_guest_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, -20, 200.0, 24.6, 25.7, self.u1.ID)

    def test_price_per_night_bool(self):
        self.assertTrue(isinstance(self.p1.price_per_night, float))

    def test_price_per_night_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, "200.0", 24.6, 25.7, self.u1.ID)

    def test_price_per_night_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, -200.0, 24.6, 25.7, self.u1.ID)

    def test_create_at(self):
        self.assertTrue(isinstance(self.p1.create_at, datetime.datetime))

    def test_update_at(self):
        self.assertTrue(isinstance(self.p1.update_at, datetime.datetime))

    def test_id(self):
        self.assertTrue(isinstance(self.p1.id, uuid.UUID))

    def test_host_id(self):
        self.assertTrue(isinstance(self.p1.host_id, uuid.UUID))

    def test_city_id(self):
        self.assertTrue(isinstance(self.p1.city_id, uuid.UUID))

    def test_amenity_id(self):
        self.assertTrue(isinstance(self.p1.amenity_id, uuid.UUID))

    def test_unique_id_place(self):
        self.assertTrue(self.p1.id, self.p2.id)

    def test_unique_host_id_and_host_id_place(self):
        self.assertEqual(self.p1.host_id, self.u1.ID)

    def test_unique_host_id_and_host_id_place_2(self):
        self.assertEqual(self.p2.host_id, self.u2.ID)
    
    def test_unique_id_user(self):
        self.assertNotEqual(self.u1.ID, self.u2.ID)

    def test_unique_id_user1_bool(self):
        self.assertTrue(isinstance(self.u1.ID, uuid.UUID))
    
    def test_unique_id_user2_bool(self):
        self.assertTrue(isinstance(self.u2.ID, uuid.UUID))

    def test_attributes_user(self):
        self.assertTrue(isinstance(self.u1.Email, str))

    def test_attributes_user_first_name(self):
        self.assertTrue(isinstance(self.u1.First_name, str))

    def test_attributes_user_last_name(self):
        self.assertTrue(isinstance(self.u1.Last_name, str))

    def test_exception_user_name(self):
        with self.assertRaises(TypeError):
            User("Jorge@gmail.com", 12, "Beritan")

    def test_exception_user_last_name(self):
        with self.assertRaises(TypeError):
            User("Jorge@gmail.com", "Jorge", 12)

    def test_exception_user_first_name_none(self):
        with self.assertRaises(ValueError):
            User("Jorge@gmail.com", "", "Beritan")

    def test_exception_user_last_name_none(self):
        with self.assertRaises(ValueError):
            User("Jorge@gmail.com", "Jorge", "")
