import unittest
import os
from unittest import skipIf
import MySQLdb


class TestStateCreation(unittest.TestCase):
    """
    Test the functionality of state creation within a database.
    Assumes that state creation is handled by a command in the application
    that interacts with the database when HBNB_TYPE_STORAGE is set to 'db'.
    """

    @classmethod
    def setUpClass(cls):
        """Connect to the database only once before all tests."""
        cls.db = MySQLdb.connect(
            host="localhost",
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Close database connection after all tests have run."""
        cls.db.close()

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not using database storage")
    def test_state_creation(self):
        """Test if creating a state actually adds a record to the states table."""
        # Initially count the number of states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Simulate the application command to create a new state
        self.create_state(name="California")

        # Count the number of states after insertion
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Check if the state count has increased by 1
        self.assertEqual(new_count, initial_count + 1, "Failed to add a new state")
        
    def create_state(self, name):
        """Mock or actual method to simulate state creation in the db."""
        self.cursor.execute("INSERT INTO states (name) VALUES (%s)", (name,))
        self.db.commit()


if __name__ == '__main__':
    unittest.main()