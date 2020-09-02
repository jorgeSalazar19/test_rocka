# imports python packages
import unittest
import sys
sys.path.append("/test_movies/app/")


# imports files owns projects
import ManagerData

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self._manager_upload = ManagerData

    def test_upload(self):
        self.assertEqual(len(self._manager_upload.upload('./files/movies.json')), 33)


if __name__ == '__main__':
    unittest.main()