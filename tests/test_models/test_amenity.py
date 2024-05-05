#!/usr/bin/python3
""" Test suite for the Amenity class. """
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity()

    def test_name(self):
        """Test for name attribute"""
        self.assertEqual(self.amenity.name, "")
