#!/usr/bin/python3
""" Amenity module for the HBNB project """
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance."""
        super().__init__(*args, **kwargs)
