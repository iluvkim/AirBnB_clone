#!/usr/bin/python3
"""Module defining the FileStorage class for storing and retrieving data."""
import datetime
import os
import json

class FileStorage:
    """Class for managing data storage and retrieval."""
    __file_path = "file.json"  # Path to the JSON file for data storage
    __objects = {}  # Dictionary to hold stored objects

    def all(self):
        """Return the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add the object to the stored objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize and save the objects to the JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def classes(self):
        """Return a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reload and populate objects from the JSON file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Return valid attributes and their types for each class."""
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str, "user_id": str, "name": str, "description": str,
                "number_rooms": int, "number_bathrooms": int, "max_guest": int,
                "price_by_night": int, "latitude": float, "longitude": float,
                "amenity_ids": list
            },
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
        return attributes
