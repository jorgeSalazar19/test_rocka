# import python package
import json

# imports
from managerData import ManagerData
from serviceSort import SortMovies


class Movie(SortMovies, ManagerData):
    """ class main for execute logic for upload and sort data 
    """
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
    

    # methos for upload data movies
    def _upload_movies(self):
        self._data_movies = self.upload(self._path_movies)
        self.calculated_average_rating(self._data_movies)
    

    # method to sort data movies
    def sort_movies(self, option_sort):
        self.sort_data(option_sort)
    

    # method to save json result data sort
    def save_data_json(self):
        with open('result.json', 'w') as fp:
            json.dump(self.data_movies, fp, indent=4)



# funtion main for the test sort and upload files
if __name__ == "__main__":

    print("Ingrese la forma de ordenar el archivo: ")
    print("1. Ordenar por puntuacion")
    print("2. Ordenar por peliculas similares")
    print("3. Ordenar por actor")
    option_sort = int(input())

    # upload data and calculate averga rating for each movie into the json
    movies = Movie('movies.json')
    movies.sort_movies(option_sort)
    movies.save_data_json()
    
    index = 0
    print("lista de reproduccion, pelicula actual")
    print("Titulo: {} calificacion: {}".format(movies.data_movies[index].get('title'), movies.data_movies[index].get('averageRating')))
    
    while True:

        if index == 0:
            print("siguiente pelicula (1)")
            print("Salir (2)")
            option = int(input())
            if option == 1:
                index +=1
                print("Titulo: {} calificacion: {}".format(movies.data_movies[index].get('title'), movies.data_movies[index].get('averageRating')))
            elif option == 2:
                break
            else:
                print("error 1")
                break
        if index > 0:
            print("Siguiente pelicula (1)")
            print("Anterior pelicula (2)")
            print("Salir (3)")
            option = int(input())
            if option == 1:
                index +=1
                print("Titulo: {} calificacion: {}".format(movies.data_movies[index].get('title'), movies.data_movies[index].get('averageRating')))
            elif option == 2:
                index -=1
                print("Titulo: {} calificacion: {}".format(movies.data_movies[index].get('title'), movies.data_movies[index].get('averageRating')))
            elif option == 3:
                break
            else:
                print("error")
                break
