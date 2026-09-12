#!/usr/bin/python3
"""Unit tests for State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State class."""

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        s = State()
        self.assertIsInstance(s, BaseModel)
        self.assertIsInstance(s, State)

    def test_attributes(self):
        """Test default attributes of State."""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

    def test_to_dict(self):
        """Test to_dict method with State."""
        s = State()
        s.name = "California"
        d = s.to_dict()
        self.assertEqual(d["__class__"], "State")
        self.assertEqual(d["name"], "California")


if __name__ == "__main__":
    unittest.main()
