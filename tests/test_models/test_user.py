#!/usr/bin/python3
"""Unit tests for the User class."""
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class test_User(test_basemodel):
    """Test suite for the User model."""

    def __init__(self, *args, **kwargs):
        """Initialize from test_basemodel."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email_validation(self):
        """Test the email validation logic."""
        with self.assertRaises(ValueError):
            User(email="invalidemail")  # Missing '@'

    def test_password_validation(self):
        """Test the password validation logic."""
        with self.assertRaises(ValueError):
            User(password="123")  # Too short

    def test_valid_user(self):
        """Test creating a valid user."""
        user = User(email="test@example.com", password="123456")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "123456")

if __name__ == '__main__':
    unittest.main()