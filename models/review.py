#!/usr/bin/python3
"""Module defining the Review class, inheriting from BaseModel."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Class representing review objects with inherited attributes."""
    
    place_id = ""  # ID of the place associated with the review
    text = ""      # Text content of the review
    user_id = ""   # ID of the user who created the review
