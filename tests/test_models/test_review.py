#!/usr/bin/python3
""" Unittest of Base class"""


import unittest
from datetime import datetime
import time
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test of class Review """

    def test_id(self):
        """test for id attribute of Review
        """
        r = Review()
        self.assertEqual(type(r.id), type("a"))

    def test_created_at(self):
        """test for created_at attribute of Review
        """
        r = Review()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(r.created_at)[0:-10], dst)

    def test_updated_at(self):
        """test for updated_at attribute of Review
        """
        r = Review()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(r.updated_at)[0:-10], dst)

    def test_place_id(self):
        """test for place_id attribute of Review
        """
        r = Review(place_id="a")
        self.assertEqual(r.place_id, "a")

    def test_place_id2(self):
        """test for place_id attribute of Review
        """
        r = Review()
        self.assertEqual(r.place_id, "")

    def test_user_id(self):
        """test for user_id attribute of Review
        """
        r = Review(user_id="a")
        self.assertEqual(r.user_id, "a")

    def test_user_id2(self):
        """test for user_id attribute of Review
        """
        r = Review()
        self.assertEqual(r.user_id, "")

    def test_text(self):
        """test for text attribute of Review
        """
        r = Review(text="test")
        self.assertEqual(r.text, "test")

    def test_text2(self):
        """test for text attribute of Review
        """
        r = Review()
        self.assertEqual(r.text, "")

    def test_to_dict(self):
        """test for method to_dict of Review
        """
        r = Review(text="a")
        rdic = r.to_dict()
        self.assertEqual(rdic['text'], "a")

    def test_str(self):
        """test for method __str__ of Review
        """
        r = Review()
        self.assertEqual(str(r)[0:8], "[Review]")

    def test_init_kwargs(self):
        """test for method __init__ of Review by kwagrs
        """
        r = Review()
        rdic = r.to_dict()
        c = Review(**rdic)
        self.assertEqual(c.id, r.id)

    def test_init_kwargs2(self):
        """test for method __init__ of Review by kwagrs
        """
        r = Review(text="a")
        rdic = r.to_dict()
        c = Review(**rdic)
        self.assertEqual(r.text, c.text)


if __name__ == "__main__":
    unittest.main()
