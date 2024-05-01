#!/usr/bin/python3
""" Test suite for the Amenity class. """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity

class TestAmenity(test_basemodel):
    """ Test cases for the Amenity model. """

    def __init__(self, *args, **kwargs):
        """ Initialize the TestAmenity class. """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_attribute(self):
        """ Test that the Amenity model has a name attribute of type str. """
        amenity = self.value()
        self.assertIsInstance(amenity.name, str, "name should be a string")
        self.assertTrue(hasattr(amenity, 'name'), "Amenity should have a name attribute")
