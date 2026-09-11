#!/usr/bin/python3
"""Unit tests for BaseModel class."""
from datetime import datetime
import os
import time
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModelDocs(unittest.TestCase):
    """Tests for BaseModel documentation and docstrings."""

    def test_module_docstring(self):
        """Test for the module docstring."""
        import models.base_model as bm_module
        self.assertIsNotNone(bm_module.__doc__)
        self.assertTrue(len(bm_module.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the BaseModel class docstring."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_docstrings(self):
        """Test for docstrings in BaseModel methods."""
        for func in [
            BaseModel.__init__,
            BaseModel.save,
            BaseModel.to_dict,
            BaseModel.__str__
        ]:
            self.assertIsNotNone(func.__doc__)
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModelInstantiation(unittest.TestCase):
    """Tests for BaseModel instantiation."""

    def test_no_args_instantiation(self):
        """Test instantiation with no arguments."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_unique_ids(self):
        """Test that each instance has a unique id."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_different_created_at(self):
        """Test that two instances have different created_at timestamps."""
        bm1 = BaseModel()
        time.sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_str_representation(self):
        """Test the __str__ representation of BaseModel."""
        bm = BaseModel()
        expected = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected)

    def test_args_unused(self):
        """Test that *args is not used when creating an instance."""
        bm = BaseModel("123", "test")
        self.assertNotIn("123", bm.__dict__.values())
        self.assertNotIn("test", bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs dictionary."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(
            id="42",
            created_at=dt_iso,
            updated_at=dt_iso,
            name="Test",
            number=89
        )
        self.assertEqual(bm.id, "42")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)
        self.assertEqual(bm.name, "Test")
        self.assertEqual(bm.number, 89)

    def test_instantiation_with_class_in_kwargs(self):
        """Test that __class__ in kwargs is not added as an attribute."""
        bm = BaseModel(__class__="OtherClass", id="99")
        self.assertNotEqual(bm.__class__.__name__, "OtherClass")
        self.assertEqual(bm.__class__.__name__, "BaseModel")


class TestBaseModelMethods(unittest.TestCase):
    """Tests for BaseModel save and to_dict methods."""

    def setUp(self):
        """Set up test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at attribute."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        time.sleep(0.01)
        bm.save()
        self.assertGreater(bm.updated_at, old_updated_at)

    def test_save_creates_file(self):
        """Test that save method creates and persists to file.json."""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("BaseModel.{}".format(bm.id), content)

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_keys(self):
        """Test that to_dict contains expected keys."""
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 89
        d = bm.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], bm.id)
        self.assertEqual(d["name"], "Holberton")
        self.assertEqual(d["my_number"], 89)
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_iso_format(self):
        """Test that created_at and updated_at in to_dict are ISO format."""
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d["created_at"], bm.created_at.isoformat())
        self.assertEqual(d["updated_at"], bm.updated_at.isoformat())

    def test_to_dict_does_not_mutate_dict(self):
        """Test that to_dict returns a copy and does not mutate __dict__."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertNotIn("__class__", bm.__dict__)


if __name__ == "__main__":
    unittest.main()
