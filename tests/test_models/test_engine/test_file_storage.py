#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """Tests for FileStorage documentation and docstrings."""

    def test_module_docstring(self):
        """Test for the module docstring."""
        import models.engine.file_storage as fs_module
        self.assertIsNotNone(fs_module.__doc__)
        self.assertTrue(len(fs_module.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the FileStorage class docstring."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_methods_docstrings(self):
        """Test for docstrings in FileStorage methods."""
        for func in [
            FileStorage.all,
            FileStorage.new,
            FileStorage.save,
            FileStorage.reload
        ]:
            self.assertIsNotNone(func.__doc__)
            self.assertTrue(len(func.__doc__) > 0)


class TestFileStorageAttributesAndMethods(unittest.TestCase):
    """Tests for FileStorage attributes and methods."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        bm = BaseModel()
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], bm)

    def test_save_creates_json_file(self):
        """Test that save() writes to file.json."""
        bm = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], bm.id)

    def test_reload_loads_objects(self):
        """Test that reload() restores objects from file.json."""
        bm = BaseModel()
        bm_id = bm.id
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "BaseModel.{}".format(bm_id)
        self.assertIn(key, self.storage.all())
        reloaded = self.storage.all()[key]
        self.assertIsInstance(reloaded, BaseModel)
        self.assertEqual(reloaded.id, bm_id)

    def test_reload_no_file_raises_no_exception(self):
        """Test that reload() does not raise error if file does not exist."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        try:
            self.storage.reload()
        except Exception as e:
            self.fail("reload() raised exception unexpectedly: {}".format(e))


if __name__ == "__main__":
    unittest.main()
