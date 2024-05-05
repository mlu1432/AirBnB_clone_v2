import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def test_init_no_kwargs(self):
        """Test BaseModel initialization without kwargs."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertIsInstance(model.id, str)

    def test_init_with_kwargs(self):
        """Test BaseModel initialization with kwargs."""
        model = BaseModel(id=str(uuid.uuid4()), created_at=datetime.now().isoformat(), updated_at=datetime.now().isoformat())
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertIsInstance(model.created_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()