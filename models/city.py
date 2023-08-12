#!/usr/bin/python3
"""Module defining the City class, inheriting from BaseModel."""
from models.base_model import BaseModel

class City(BaseModel):
    """Class representing city objects with inherited attributes."""
    
    name = ""      # Name of the city
    state_id = ""  # ID of the state associated with the city
