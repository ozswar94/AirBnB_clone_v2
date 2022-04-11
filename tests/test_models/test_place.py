#!/usr/bin/python3
""" Unittest of Base class"""


import unittest
from datetime import datetime
import time
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test of class Place """

    def test_id(self):
        """test for id attribute of Place
        """
        p = Place()
        self.assertEqual(type(p.id), type("a"))

    def test_created_at(self):
        """test for created_at attribute of Place
        """
        p = Place()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(p.created_at)[0:-10], dst)

    def test_updated_at(self):
        """test for updated_at attribute of Place
        """
        p = Place()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(p.updated_at)[0:-10], dst)

    def test_city_id(self):
        """test for city_id attribute of Place
        """
        p = Place(city_id="a")
        self.assertEqual(p.city_id, "a")

    def test_city_id2(self):
        """test for city_id attribute of Place
        """
        p = Place()
        self.assertEqual(p.city_id, "")

    def test_user_id(self):
        """test for user_id attribute of Place
        """
        p = Place(user_id="aaaaa")
        self.assertEqual(p.user_id, "aaaaa")

    def test_user_id2(self):
        """test for user_id attribute of Place
        """
        p = Place()
        self.assertEqual(p.user_id, "")

    def test_name(self):
        """test for name attribute of Place
        """
        p = Place(name="test")
        self.assertEqual(p.name, "test")

    def test_name2(self):
        """test for name attribute of Place
        """
        p = Place()
        self.assertEqual(p.name, "")

    def test_description(self):
        """test for description attribute of Place
        """
        p = Place(description="test")
        self.assertEqual(p.description, "test")

    def test_description2(self):
        """test for description attribute of Place
        """
        p = Place()
        self.assertEqual(p.description, "")

    def test_number_rooms(self):
        """test for number_rooms attribute of Place
        """
        p = Place(number_rooms=1)
        self.assertEqual(p.number_rooms, 1)

    def test_number_rooms2(self):
        """test for number_rooms attribute of Place
        """
        p = Place()
        self.assertEqual(p.number_rooms, 0)

    def test_number_bathrooms(self):
        """test for number_bathrooms attribute of Place
        """
        p = Place(number_bathrooms=1)
        self.assertEqual(p.number_bathrooms, 1)

    def test_number_bathrooms2(self):
        """test for number_bathrooms attribute of Place
        """
        p = Place()
        self.assertEqual(p.number_bathrooms, 0)

    def test_max_guest(self):
        """test for max_guest attribute of Place
        """
        p = Place(max_guest=1)
        self.assertEqual(p.max_guest, 1)

    def test_max_guest2(self):
        """test for max_guest attribute of Place
        """
        p = Place()
        self.assertEqual(p.max_guest, 0)

    def test_price_by_night(self):
        """test for price_by_night attribute of Place
        """
        p = Place(price_by_night=1)
        self.assertEqual(p.price_by_night, 1)

    def test_price_by_night2(self):
        """test for price_by_night attribute of Place
        """
        p = Place()
        self.assertEqual(p.price_by_night, 0)

    def test_latitude(self):
        """test for latitude attribute of Place
        """
        p = Place(latitude=1)
        self.assertEqual(p.latitude, 1.0)

    def test_latitude2(self):
        """test for latitude attribute of Place
        """
        p = Place()
        self.assertEqual(p.latitude, 0.0)

    def test_longitude(self):
        """test for longitude attribute of Place
        """
        p = Place(longitude=1)
        self.assertEqual(p.longitude, 1.0)

    def test_longitude2(self):
        """test for longitude attribute of Place
        """
        p = Place()
        self.assertEqual(p.longitude, 0.0)

    def amenity_ids(self):
        """test for amenity_ids attribute of Place
        """
        p = Place()
        self.assertEqual(p.amenity_ids, "")

    def amenity_ids2(self):
        """test for amenity_ids attribute of Place
        """
        p = Place(amenity_ids="a1")
        self.assertEqual(p.amenity_ids, "a1")

    def test_to_dict(self):
        """test for method to_dict of Place
        """
        p = Place(name="a")
        pdic = p.to_dict()
        self.assertEqual(pdic['name'], "a")

    def test_str(self):
        """test for method __str__ of Place
        """
        p = Place()
        self.assertEqual(str(p)[0:7], "[Place]")

    def test_init_kwargs(self):
        """test for method __init__ of Place by kwagrs
        """
        p = Place()
        pdic = p.to_dict()
        c = Place(**pdic)
        self.assertEqual(p.id, c.id)

    def test_init_kwargs2(self):
        """test for method __init__ of Place by kwagrs
        """
        p = Place(name="a")
        pdic = p.to_dict()
        c = Place(**pdic)
        self.assertEqual(p.name, c.name)


if __name__ == "__main__":
    unittest.main()
