#!/usr/bin/python3
"""This script initializes the package and sets up storage."""

# Import the necessary module for file storage
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage for data storage
storage = FileStorage()

# Load data from storage (if available)
storage.reload()
