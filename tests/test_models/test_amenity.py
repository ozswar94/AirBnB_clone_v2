#!/usr/bin/python3
""" Unittest for class Amenity """

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test of class Amenity
    """

    def test_name_type(self):
        """
        testing name type for class Amenity
        """
        a = Amenity()
        self.assertEqual(type(a.name), type("a"))

    def test_name(self):
        """
        testing name attribute for class Amenity
        """
        a = Amenity()
        a.name = None
        self.assertEqual(a.name, None)

    def test_name2(self):
        """
        testing name attribute for class Amenity
        """
        a = Amenity()
        a.name = ""
        self.assertEqual(a.name, "")

    def test_name3(self):
        """
        testing name attribute for class City
        """
        a = Amenity(name="c")
        a.name = self.assertEqual(a.name, "c")

    def test_state_id_type(self):
        """
        testing amenity id type
        """
        a = Amenity()
        self.assertEqual(type(a.id), type("a"))

    def test_created_at(self):
        """
        test for created_at attribute of Amenity
        """
        a = Amenity()
        d = datetime.now()
        self.assertEqual(str(a.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_updated_at(self):
        """
        test for updated_at attribute of Amenity
        """
        a = Amenity()
        d = datetime.now()
        self.assertEqual(str(a.updated_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_to_dict(self):
        """
        test for method to_dict of Amenity
        """
        a = Amenity()
        adic = a.to_dict()
        self.assertEqual(a.created_at.isoformat(), adic['created_at'])

    def test_to_dict2(self):
        """
        test for method to_dict of Amenity
        """
        a = Amenity()
        adic = a.to_dict()
        self.assertEqual(a.updated_at.isoformat(), adic['updated_at'])


if __name__ == "__main__":
    unittest.main()
