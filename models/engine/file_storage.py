#!/usr/bin/python3
"""Defines the FileStorage class for serialization and deserialization."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to objects.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to add to __objects.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if file exists.

        If the file does not exist, no exception is raised.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    objdict = json.load(f)
                    for o in objdict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(cls_name)(**o))
                except Exception:
                    pass
        except FileNotFoundError:
            return
