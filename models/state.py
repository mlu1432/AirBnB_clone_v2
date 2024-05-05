#!/usr/bin/python3
"""State Module for HBNB project"""

from models.base_model import BaseModel

class State(BaseModel):
    """State class to store state information"""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new state instance."""
        super().__init__(*args, **kwargs)
        if not isinstance(self.name, str):
            raise ValueError("name must be a string")
        if self.name == "":
            raise ValueError("name must not be empty")
