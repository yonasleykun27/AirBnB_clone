#!/usr/bin/python3
"""Unit tests for Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review class."""

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertIsInstance(r, Review)

    def test_attributes(self):
        """Test default attributes of Review."""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_to_dict(self):
        """Test to_dict method with Review."""
        r = Review()
        r.text = "Great place!"
        d = r.to_dict()
        self.assertEqual(d["__class__"], "Review")
        self.assertEqual(d["text"], "Great place!")


if __name__ == "__main__":
    unittest.main()
