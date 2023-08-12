#!/usr/bin/python3
"""Module defining the State class, inheriting from BaseModel."""
from models.base_model import BaseModel

class State(BaseModel):
    """Class representing state objects with inherited attributes."""
    
    name = ""  # Name of the state
