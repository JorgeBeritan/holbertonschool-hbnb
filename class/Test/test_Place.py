#!/usr/bin/python3
import sys
sys.path.append("/workspaces/holbertonschool-hbnb/class")
import unittest
from Place import Place

class TestPlaceClass(unittest.TestCase):
    def setUp(self):
        self.p1 = Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7)

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
            Place(123, "Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7)

    def test_name_exception_none(self):
        with self.assertRaises(ValueError):
            Place("","Esta bueno el Hotel", 4, 3, 20, 200.0, 24.6, 25.7)

    def test_description_bool(self):
        self.assertTrue(isinstance(self.p1.description, str))

    def test_description_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", 123, 4, 3, 20, 200.0, 24.6, 25.7)

    def test_description_exception_none(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "", 4, 3, 20, 200.0, 24.6, 25.7)

    def test_number_of_rooms_bool(self):
        self.assertTrue(isinstance(self.p1.number_of_rooms, int))

    def test_number_of_rooms_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", "4", 3, 20, 200.0, 24.6, 25.7)

    def test_number_of_rooms_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", -4, 3, 20, 200.0, 24.6, 25.7)

    def test_number_of_bathrooms_bool(self):
        self.assertTrue(isinstance(self.p1.number_of_bathrooms, int))
    
    def test_numbert_of_bathrooms_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, "3", 20, 200.0, 24.6, 25.7)

    def test_numbert_of_bathrooms_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, -3, 20, 200.0, 24.6, 25.7)

    def test_max_guest_bool(self):
        self.assertTrue(isinstance(self.p1.max_guest, int))

    def test_max_guest_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, "20", 200.0, 24.6, 25.7)

    def test_max_guest_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, -20, 200.0, 24.6, 25.7)

    def test_price_per_night_bool(self):
        self.assertTrue(isinstance(self.p1.price_per_night, float))

    def test_price_per_night_exception(self):
        with self.assertRaises(TypeError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, "200.0", 24.6, 25.7)

    def test_price_per_night_exception_negative(self):
        with self.assertRaises(ValueError):
            Place("Hotel", "Esta bueno el Hotel", 4, 3, 20, -200.0, 24.6, 25.7)

        