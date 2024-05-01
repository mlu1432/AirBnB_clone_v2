#!/usr/bin/python3
""" Tests for City model """
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class TestCity(test_basemodel):
    """ Define tests for City model from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialize the TestCity class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test the type of state_id if it exists """
        new = self.value()
        self.assertTrue(hasattr(new, 'state_id'), "City should have a state_id attribute")
        self.assertIsInstance(new.state_id, str, "The 'state_id' attribute should be a string")

    def test_name(self):
        """ Test the type of name """
        new = self.value()
        self.assertIsInstance(new.name, str, "The 'name' attribute should be a string")
