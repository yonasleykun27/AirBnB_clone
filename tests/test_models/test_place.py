#!/usr/bin/python3
"""Unit tests for Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for Place class."""

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        p = Place()
        self.assertIsInstance(p, BaseModel)
        self.assertIsInstance(p, Place)

    def test_attributes(self):
        """Test default attributes of Place."""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

    def test_to_dict(self):
        """Test to_dict method with Place."""
        p = Place()
        p.name = "Cozy Cottage"
        d = p.to_dict()
        self.assertEqual(d["__class__"], "Place")
        self.assertEqual(d["name"], "Cozy Cottage")


if __name__ == "__main__":
    unittest.main()
