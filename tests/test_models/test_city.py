#!/usr/bin/python3
"""Unit tests for City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City class."""

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        c = City()
        self.assertIsInstance(c, BaseModel)
        self.assertIsInstance(c, City)

    def test_attributes(self):
        """Test default attributes of City."""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def test_to_dict(self):
        """Test to_dict method with City."""
        c = City()
        c.state_id = "CA-123"
        c.name = "San Francisco"
        d = c.to_dict()
        self.assertEqual(d["__class__"], "City")
        self.assertEqual(d["state_id"], "CA-123")
        self.assertEqual(d["name"], "San Francisco")


if __name__ == "__main__":
    unittest.main()
