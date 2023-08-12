#!/usr/bin/python3
"""Module defining the Amenity class, inheriting from BaseModel."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class representing amenity objects with inherited attributes."""
    
    name = ""  # Name of the amenity
