#!/usr/bin/python3
"""
    FileStorage Class module
"""

import os
import json


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
    instances
    Attributes:
        __file_path (str): private class attribute containing a file path
        __objects (dict): contains the id of all object instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary containing all object instances id """
        if not isinstance(FileStorage.__objects, dict):
            FileStorage.__objects = {}
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): instance of a class Basemodel
        """
        if not isinstance(FileStorage.__objects, dict):
            FileStorage.__objects = {}
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        if not isinstance(FileStorage.__objects, dict):
            FileStorage.__objects = {}
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if (isinstance(self.__file_path, str) and
                os.path.exists(self.__file_path)):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as fi:
                    content = fi.read()
                    if content:
                        obj_dict = json.loads(content)
                        for o in obj_dict.values():
                            cls_name = o.get("__class__")
                            if cls_name in classes:
                                self.new(classes[cls_name](**o))
            except Exception:
                pass
