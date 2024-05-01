import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""  # Corrected indentation

    def setUp(self):
        """Set up test cases for the BaseModel."""
        with patch('models.base_model.storage.new') as mocked_new:
            self.model = BaseModel()

    def test_instance_creation_with_kwargs(self):
        """Test initialization with kwargs including datetime conversion."""
        date_str = '2022-01-01T00:00:00.000000'
        model = BaseModel(created_at=date_str, updated_at=date_str)
        self.assertEqual(model.created_at, datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.updated_at, datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f'))

    @patch('models.base_model.open', mock_open(), create=True)
    @patch('models.base_model.json.dump')
    def test_save_to_file(self, mocked_json_dump):
        """Test saving the model's state to a file."""
        self.model.save()
        mocked_json_dump.assert_called_once()

    def test_initial_time_setup(self):
        """Test the initial setup of created_at and updated_at attributes."""
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str_representation(self):
        """Test the string representation of the model."""
        expected_format = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_format)

if __name__ == '__main__':
    unittest.main()