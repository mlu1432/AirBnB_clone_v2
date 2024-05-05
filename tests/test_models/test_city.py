import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def test_init_city(self):
        """Test initialization of City."""
        city = City()
        self.assertTrue(hasattr(city, 'id'), "City should have an id attribute")
        self.assertTrue(hasattr(city, 'created_at'), "City should have a created_at attribute")
        self.assertTrue(hasattr(city, 'updated_at'), "City should have an updated_at attribute")
        self.assertTrue(hasattr(city, 'state_id'), "City should have a state_id attribute")
        self.assertTrue(hasattr(city, 'name'), "City should have a name attribute")
        self.assertIsInstance(city.state_id, str, "City state_id should be a string")
        self.assertIsInstance(city.name, str, "City name should be a string")

    def test_city_str(self):
        """Test the string representation of a city."""
        city = City(name="San Francisco")
        expected_str_format = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str_format, "String format mismatch.")

if __name__ == '__main__':
    unittest.main()
