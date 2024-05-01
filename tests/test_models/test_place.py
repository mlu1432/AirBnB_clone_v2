#!/usr/bin/python3
"""Unit tests for the Place class from the HBNB project."""

from test_base_model import test_basemodel
from models.place import Place

class TestPlace(test_basemodel):
    """Defines tests for the Place model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class with Place model info."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_attributes_existence(self):
        """Test that all class attributes are present and initialized correctly."""
        place = self.value()
        self.assertTrue(hasattr(place, 'city_id'), "Missing city_id attribute")
        self.assertTrue(hasattr(place, 'user_id'), "Missing user_id attribute")
        self.assertTrue(hasattr(place, 'name'), "Missing name attribute")
        self.assertTrue(hasattr(place, 'description'), "Missing description attribute")
        self.assertTrue(hasattr(place, 'number_rooms'), "Missing number_rooms attribute")
        self.assertTrue(hasattr(place, 'number_bathrooms'), "Missing number_bathrooms attribute")
        self.assertTrue(hasattr(place, 'max_guest'), "Missing max_guest attribute")
        self.assertTrue(hasattr(place, 'price_by_night'), "Missing price_by_night attribute")
        self.assertTrue(hasattr(place, 'latitude'), "Missing latitude attribute")
        self.assertTrue(hasattr(place, 'longitude'), "Missing longitude attribute")
        self.assertTrue(hasattr(place, 'amenity_ids'), "Missing amenity_ids attribute")

    def test_attributes_type(self):
        """Test the type of each attribute."""
        place = self.value()
        self.assertIsInstance(place.city_id, str, "city_id should be a string")
        self.assertIsInstance(place.user_id, str, "user_id should be a string")
        self.assertIsInstance(place.name, str, "name should be a string")
        self.assertIsInstance(place.description, str, "description should be a string")
        self.assertIsInstance(place.number_rooms, int, "number_rooms should be an int")
        self.assertIsInstance(place.number_bathrooms, int, "number_bathrooms should be an int")
        self.assertIsInstance(place.max_guest, int, "max_guest should be an int")
        self.assertIsInstance(place.price_by_night, int, "price_by_night should be an int")
        self.assertIsInstance(place.latitude, float, "latitude should be a float")
        self.assertIsInstance(place.longitude, float, "longitude should be a float")
        self.assertIsInstance(place.amenity_ids, list, "amenity_ids should be a list")

