#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
import models
import uuid

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs of attributes.
        """
        if kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(val, str):
                        try:
                            self.__dict__[key] = datetime.strptime(
                                val, TIME_FORMAT
                            )
                        except ValueError:
                            self.__dict__[key] = datetime.fromisoformat(val)
                    else:
                        self.__dict__[key] = val
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at with current datetime and saves to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__.

        Includes key __class__ and ISO formatted datetimes.
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        if isinstance(self.created_at, datetime):
            res["created_at"] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            res["updated_at"] = self.updated_at.isoformat()
        return res

    def __str__(self):
        """Returns string representation: [<class name>] (<id>) <dict>."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
