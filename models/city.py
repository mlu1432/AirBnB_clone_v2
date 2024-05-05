#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel

class City(BaseModel):
    """Representation of a City"""
    state_id: str = ""  # Will store the id of the State
    name: str = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City instance."""
        super().__init__(*args, **kwargs)
        if type(self.state_id) is not str or type(self.name) is not str:
            raise TypeError("state_id and name must be strings")
