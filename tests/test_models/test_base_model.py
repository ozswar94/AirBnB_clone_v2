#!/usr/bin/python3
""" Unittest of Base class"""


import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from unittest import mock

class TestBaseModel(unittest.TestCase):
    """ Test of class BaseModel """

    def test_id(self):
        """test for id attribute of BaseModel
        """
        b = BaseModel()
        self.assertEqual(type(b.id), type("a"))

    def test_created_at(self):
        """test for created_at attribute of BaseModel
        """
        b = BaseModel()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(b.created_at)[0:-10], dst)

    def test_updated_at(self):
        """test for updated_at attribute of BaseModel
        """
        b = BaseModel()
        d = datetime.now()
        dst = d.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(str(b.updated_at)[0:-10], dst)

    def test_name(self):
        """test for name attribute of BaseModel
        """
        b = BaseModel()
        b.name = "test"
        self.assertEqual(b.name, "test")

    def test_name2(self):
        """test for name attribute of BaseModel
        """
        b = BaseModel()
        b.name = None
        self.assertEqual(b.name, None)

    def test_name3(self):
        """test for name attribute of BaseModel
        """
        b = BaseModel()
        b.name = ""
        self.assertEqual(b.name, "")

    def test_name4(self):
        """test for name attribute of BaseModel
        """
        b = BaseModel(name="b")
        self.assertEqual(b.name, "b")

    def test_my_number(self):
        """test for my_number attribute of BaseModel
        """
        b = BaseModel()
        b.my_number = 1
        self.assertEqual(b.my_number, 1)

    def test_my_number2(self):
        """test for my_number attribute of BaseModel
        """
        b = BaseModel(my_number=None)
        self.assertEqual(b.my_number, None)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """test for method to_dict of BaseModel
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.created_at.isoformat(), bdic['created_at'])

    def test_to_dict2(self):
        """test for method to_dict of BaseModel
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), bdic['updated_at'])

    def test_to_dict3(self):
        """test for method to_dict of BaseModel
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.id, bdic['id'])

    def test_to_dict4(self):
        """test for method to_dict of BaseModel
        """
        b = BaseModel(name="b")
        bdic = b.to_dict()
        self.assertEqual(b.name, bdic['name'])

    def test_to_dict5(self):
        """test for method to_dict of BaseModel
        """
        b = BaseModel(my_number=1)
        bdic = b.to_dict()
        self.assertEqual(b.my_number, bdic['my_number'])

    def test_str(self):
        """test for method __str__ of BaseModel
        """
        b = BaseModel()
        a = str(b.id)[0:5]
        self.assertEqual(str(b)[0:18], "[BaseModel] ({}".format(a))

    def test_init_kwargs(self):
        """test for method __init__ of BaseModel by kwagrs
        """
        b = BaseModel(name="a", my_number=1)
        bdic = b.to_dict()
        a = BaseModel(**bdic)
        self.assertEqual(a.id, b.id)

    def test_init_kwargs2(self):
        """test for method __init__ of BaseModel by kwagrs
        """
        b = BaseModel()
        bdic = b.to_dict()
        a = BaseModel(**bdic)
        self.assertEqual(a.created_at, b.created_at)


if __name__ == "__main__":
    unittest.main()
