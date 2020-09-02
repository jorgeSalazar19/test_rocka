# imports
import json

class ManagerData(object):
    

    # constructor
    def __init__(self, path_data):
        self._data = self._upload_data(path_data)
    

    # method for upload data
    @classmethod
    def upload(self, path_data):
        with open(path_data) as file:
            data = json.load(file)
        return dict(movies=data)
    

    # method for calculated average rating
    @classmethod
    def calculated_average_rating(self, data_movies):
        for movie in data_movies.get('movies'):
            average_rating = self._calculate_average(self, movie.get('ratings'))
            movie['averageRating'] = average_rating
            del movie['ratings']


    # calculate average rating to movie
    def _calculate_average(self, movie):
        return round(sum(movie) / len(movie), 1)