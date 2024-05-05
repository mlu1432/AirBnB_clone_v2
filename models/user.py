#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """This class defines a user by various attributes"""
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)
        self.validate_user()

    def validate_user(self):
        """Validates the user's information."""
        if not isinstance(self.email, str) or '@' not in self.email:
            raise ValueError("Invalid email format")
        if not isinstance(self.password, str) or len(self.password) < 6:
            raise ValueError("Password must be at least 6 characters long")