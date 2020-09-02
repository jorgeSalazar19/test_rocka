# imports python packages
import unittest


# imports files owns projects
from managerData import ManagerData
from serviceSort import SortMovies


class TestUpload(unittest.TestCase):
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



class TestSortService(unittest.TestCase):


    # method for upload data to test
    def setUp(self):
        self._manager_upload = ManagerData
    

    # method for test merge sort 
    def test_merge_sort_instance(self):
        data_movies = self._manager_upload.upload('movies.json').get('movies')
        self.assertIsInstance(SortMovies()._merge_sort(data_movies), list)


if __name__ == '__main__':
    unittest.main()