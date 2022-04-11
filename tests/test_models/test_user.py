#!/usr/bin/python3
""" Unittest of Base class"""


import unittest
from datetime import datetime
import time
from models.user import User


class TestUser(unittest.TestCase):
    """ Test of class User """

    def test_id(self):
        """test for id attribute of User
        """
        u = User()
        self.assertEqual(type(u.id), type("a"))

    def test_created_at(self):
        """test for created_at attribute of User
        """
        u = User()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(u.created_at)[0:-10], dst)

    def test_updated_at(self):
        """test for updated_at attribute of User
        """
        u = User()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(u.updated_at)[0:-10], dst)

    def test_email(self):
        """test for email attribute of User
        """
        u = User(email="a@gmail.com")
        self.assertEqual(u.email, "a@gmail.com")

    def test_email2(self):
        """test for email attribute of User
        """
        u = User()
        self.assertEqual(u.email, "")

    def test_password(self):
        """test for password attribute of User
        """
        u = User(password="aaaaa")
        self.assertEqual(u.password, "aaaaa")

    def test_password2(self):
        """test for password attribute of User
        """
        u = User()
        self.assertEqual(u.password, "")

    def test_first_name(self):
        """test for first name attribute of User
        """
        u = User(first_name="test")
        self.assertEqual(u.first_name, "test")

    def test_first_name2(self):
        """test for first name attribute of User
        """
        u = User()
        self.assertEqual(u.first_name, "")

    def test_last_name(self):
        """test for last name attribute of User
        """
        u = User(last_name="test")
        self.assertEqual(u.last_name, "test")

    def test_last_name2(self):
        """test for last name attribute of User
        """
        u = User()
        self.assertEqual(u.last_name, "")

    def test_to_dict(self):
        """test for method to_dict of User
        """
        u = User(email="a")
        udic = u.to_dict()
        self.assertEqual(udic['email'], "a")

    def test_str(self):
        """test for method __str__ of User
        """
        u = User()
        self.assertEqual(str(u)[0:6], "[User]")

    def test_init_kwargs(self):
        """test for method __init__ of User by kwagrs
        """
        u = User()
        udic = u.to_dict()
        c = User(**udic)
        self.assertEqual(u.id, c.id)

    def test_init_kwargs2(self):
        """test for method __init__ of User by kwagrs
        """
        u = User(email="a")
        udic = u.to_dict()
        c = User(**udic)
        self.assertEqual(u.email, c.email)


if __name__ == "__main__":
    unittest.main()
