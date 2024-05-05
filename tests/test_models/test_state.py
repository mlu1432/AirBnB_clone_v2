#!/usr/bin/python3
"""Unit tests for the State class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_state(test_basemodel):
    """Test suite for the State model."""

    def __init__(self, *args, **kwargs):
        """Initialize from test_basemodel."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_initialization(self):
        """Test the initialization of the name attribute."""
        state = self.value()
        self.assertEqual(state.name, "", "Initial name should be an empty string")

    def test_name_validation(self):
        """Test the validation of the name attribute."""
        with self.assertRaises(ValueError):
            State(name=123)  # Not a string

        with self.assertRaises(ValueError):
            State(name="")  # Empty string