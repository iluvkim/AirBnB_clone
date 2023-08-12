#!/usr/bin/python3
"""Module defining the User class, inheriting from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """Class representing user objects with inherited attributes."""

    email = ""         # User's email address
    password = ""      # User's password
    last_name = ""    # User's last name
    first_name = ""     # User's first name
