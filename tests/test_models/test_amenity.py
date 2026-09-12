#!/usr/bin/python3
"""Unit tests for Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class."""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)
        self.assertIsInstance(a, Amenity)

    def test_attributes(self):
        """Test default attributes of Amenity."""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")

    def test_to_dict(self):
        """Test to_dict method with Amenity."""
        a = Amenity()
        a.name = "Wifi"
        d = a.to_dict()
        self.assertEqual(d["__class__"], "Amenity")
        self.assertEqual(d["name"], "Wifi")


if __name__ == "__main__":
    unittest.main()
