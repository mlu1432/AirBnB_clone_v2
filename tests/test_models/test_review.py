#!/usr/bin/python3
"""Unit tests for the Review class."""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
    """Test suite for the Review model."""

    def __init__(self, *args, **kwargs):
        """Initialize from TestBaseModel."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_initial_attributes(self):
        """Test the initial attributes of Review."""
        review = self.value()
        self.assertEqual(review.place_id, "", "place_id should be initialized as an empty string")
        self.assertEqual(review.user_id, "", "user_id should be initialized as an empty string")
        self.assertEqual(review.text, "", "text should be initialized as an empty string")

    def test_types(self):
        """Test the type of Review attributes."""
        review = self.value()
        self.assertIsInstance(review.place_id, str, "place_id should be a string")
        self.assertIsInstance(review.user_id, str, "user_id should be a string")
        self.assertIsInstance(review.text, str, "text should be a string")

if __name__ == '__main__':
    unittest.main()
