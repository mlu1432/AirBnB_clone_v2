#!/usr/bin/python3
"""Review module for the HBNB project"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class to store review information."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""