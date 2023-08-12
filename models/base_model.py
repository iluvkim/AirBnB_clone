#!/usr/bin/python3
"""This script defines the base model class."""

import uuid
from models import storage
from datetime import datetime

class BaseModel:
    """Base class for model inheritance."""

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes.

        Args:
            *args: List of arguments
            **kwargs: Dictionary of key-value arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                # Check and parse 'created_at' and 'updated_at' attributes
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    # Set other attributes from kwargs
                    self.__dict__[key] = value
        else:
            # Generate new attributes for a fresh instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the official string representation."""

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute 'updated_at' and save."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
