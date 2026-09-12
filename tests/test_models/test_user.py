#!/usr/bin/python3
"""Unit tests for User class."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class."""

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u, User)

    def test_attributes(self):
        """Test default attributes of User."""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_to_dict(self):
        """Test to_dict method with User."""
        u = User()
        u.email = "airbnb@mail.com"
        u.first_name = "Betty"
        d = u.to_dict()
        self.assertEqual(d["__class__"], "User")
        self.assertEqual(d["email"], "airbnb@mail.com")
        self.assertEqual(d["first_name"], "Betty")


if __name__ == "__main__":
    unittest.main()
