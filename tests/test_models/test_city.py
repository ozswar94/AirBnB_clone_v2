#!/usr/bin/python3
""" Unittest for class City """

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """
    Test of class City
    """

    def test_name_type(self):
        """
        testing name type for class City
        """
        c = City()
        self.assertEqual(type(c.name), type("a"))

    def test_name(self):
        """
        testing name attribute for class City
        """
        c = City()
        c.name = None
        self.assertEqual(c.name, None)

    def test_name2(self):
        """
        testing name attribute for class City
        """
        c = City()
        c.name = ""
        self.assertEqual(c.name, "")

    def test_name3(self):
        """
        testing name attribute for class City
        """
        c = City(name="c")
        c.name = self.assertEqual(c.name, "c")

    def test_state_id_type(self):
        """
        testing state id type
        """
        c = City()
        self.assertEqual(type(c.id), type("a"))

    def test_created_at(self):
        """
        test for created_at attribute of City
        """
        c = City()
        d = datetime.now()
        self.assertEqual(str(c.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_updated_at(self):
        """
        test for updated_at attribute of City
        """
        c = City()
        d = datetime.now()
        self.assertEqual(str(c.updated_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_to_dict(self):
        """
        test for method to_dict of City
        """
        c = City()
        cdic = c.to_dict()
        self.assertEqual(c.created_at.isoformat(), cdic['created_at'])

    def test_to_dict2(self):
        """
        test for method to_dict of City
        """
        c = City()
        cdic = c.to_dict()
        self.assertEqual(c.updated_at.isoformat(), cdic['updated_at'])


if __name__ == "__main__":
    unittest.main()
