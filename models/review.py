#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
