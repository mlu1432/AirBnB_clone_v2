import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test suite for the Place model."""

    def test_init_place(self):
        """Test initialization of Place."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'), "Place should have a city_id attribute")
        self.assertEqual(place.amenity_ids, [], "amenity_ids should be an empty list by default")

    def test_invalid_number_rooms(self):
        """Test for invalid number of rooms."""
        with self.assertRaises(ValueError):
            Place(number_rooms=-1)

    def test_valid_latitude(self):
        """Test valid latitude range."""
        place = Place(latitude=45.0)
        self.assertEqual(place.latitude, 45.0)

    def test_invalid_latitude(self):
        """Test invalid latitude range."""
        with self.assertRaises(ValueError):
            Place(latitude=100.0)

    # More tests for other attributes and methods...

if __name__ == '__main__':
    unittest.main()
