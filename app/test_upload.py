# imports python packages
import unittest


# imports files owns projects
from managerData import ManagerData

class TestStringMethods(unittest.TestCase):
    """ class for unit test to project
    """

    # method for upload data to test
    def setUp(self):
        self._manager_upload = ManagerData
        self._list_ratings = [1, 5, 10, 8, 7, 5]


    # methos for test upload data to dict python
    def test_upload(self):
        self.assertEqual(len(self._manager_upload.upload('movies.json').get('movies')), 33)


    # method for test instance to calculate_avergage
    def test_average_rating(self):
        movie = self._manager_upload.upload('movies.json').get('movies')[0].get('ratings')
        self.assertIsInstance(self._manager_upload._calculate_average(self, movie), float)


if __name__ == '__main__':
    unittest.main()