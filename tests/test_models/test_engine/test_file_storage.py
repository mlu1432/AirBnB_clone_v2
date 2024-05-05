import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        storage._FileStorage__objects.clear()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0, "Storage should be empty initially")

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        storage.new(new)
        self.assertIn('BaseModel.' + new.id, storage.all(), "New object should be in storage")

    def test_all_returns_dict(self):
        """ __objects is properly returned """
        self.assertIsInstance(storage.all(), dict, "All should return a dictionary")

    def test_base_model_instantiation_no_save(self):
        """ File is not created on BaseModel instantiation without save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'), "File should not exist without save method call")

    def test_save_creates_file(self):
        """ Data is saved to file """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'), "File should be created after save")

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        self.assertIn('BaseModel.' + new.id, storage.all(), "Object should be reloaded into storage")

    def test_reload_empty(self):
        """ Loading from an empty file does not raise an exception """
        open('file.json', 'w').close()  # Ensuring the file is empty
        try:
            storage.reload()
        except Exception as e:
            self.fail(f"Reload from an empty file failed with exception {e}")

    def test_reload_from_nonexistent(self):
        """ Reload from a nonexistent file """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        storage.reload()  # Should not raise any exceptions
        self.assertTrue(True, "Reloading from a nonexistent file should be handled gracefully")

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'), "File should exist after BaseModel save")

    def test_key_format(self):
        """ Key format is properly maintained """
        new = BaseModel()
        storage.new(new)
        storage.save()
        expected_key = 'BaseModel.' + new.id
        self.assertIn(expected_key, storage.all(), "Key should be correctly formatted in storage")

    def test_storage_var_created(self):
        """ FileStorage object storage is correctly instantiated """
        self.assertIsInstance(storage, FileStorage, "Storage should be an instance of FileStorage")
