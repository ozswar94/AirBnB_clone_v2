#!/usr/bin/python3
""" Unittest for class State """

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test of class State
    """

    def test_name_type(self):
        """
        testing name type for class State
        """
        s = State()
        self.assertEqual(type(s.name), type("a"))

    def test_name(self):
        """
        testing name attribute for class State
        """
        s = State()
        s.name = None
        self.assertEqual(s.name, None)

    def test_name2(self):
        """
        testing name attribute for class State
        """
        s = State()
        s.name = ""
        self.assertEqual(s.name, "")

    def test_name3(self):
        """
        testing name attribute for class State
        """
        s = State(name="c")
        s.name = self.assertEqual(s.name, "c")

    def test_state_id_type(self):
        """
        testing state id type
        """
        s = State()
        self.assertEqual(type(s.id), type("a"))

    def test_created_at(self):
        """
        test for created_at attribute of State
        """
        s = State()
        d = datetime.now()
        self.assertEqual(str(s.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_updated_at(self):
        """
        test for updated_at attribute of State
        """
        s = State()
        d = datetime.now()
        self.assertEqual(str(s.updated_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_to_dict(self):
        """
        test for method to_dict of State
        """
        s = State()
        sdic = s.to_dict()
        self.assertEqual(s.created_at.isoformat(), sdic['created_at'])

    def test_to_dict2(self):
        """
        test for method to_dict of State
        """
        s = State()
        sdic = s.to_dict()
        self.assertEqual(s.updated_at.isoformat(), sdic['updated_at'])


if __name__ == "__main__":
    unittest.main()
