# imports
from managerData import ManagerData
from serviceSort import SortMovies

class Movie(SortMovies, ManagerData):

    def __init__(self, path_movies):
        self._path_movies = path_movies
        # call method for upload movies
        self._upload_movies()
    

    @property
    def data_movies(self):
        return self._data_movies

    
    @data_movies.setter
    def data_movies(self, data):
        self._data_movies = data
    

    def _upload_movies(self):
        self._data_movies = self.upload(self._path_movies)
        self.calculated_average_rating(self._data_movies)
    

    def sort_movies(self, option_sort):
        self.sort_to_average([2, 4 ,2 ,5 ,4, 3])



# funtion main for the test sort and upload files
if __name__ == "__main__":

    print("Ingrese la forma de ordenar el archivo: ")
    option_sort = int(input())

    # upload data and calculate averga rating for each movie into the json
    movies = Movie('movies.json')
    movies.sort_movies(option_sort)