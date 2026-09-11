#!/usr/bin/python3
"""Defines the FileStorage class for serialization and deserialization."""
import json
import os


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            k: v.to_dict() for k, v in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if file exists.

        If the file does not exist, no exception is raised.
        """
        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, val in obj_dict.items():
                        cls_name = val.get("__class__")
                        if cls_name in classes:
                            cls = classes[cls_name]
                            FileStorage.__objects[key] = cls(**val)
                except Exception:
                    pass
