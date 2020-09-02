class SortMovies(object):


    def _sort_to_average_rating(self):
        pass


    def _sort_to_similar_movie(self):
        pass


    def _sort_to_same_actor(self):
        pass


    def _merge_sort(self, lista):
        if len(lista) < 2:
            return self.data_movies
        
            # De lo contrario, se divide en 2
        else:
            middle = len(lista) // 2
            right = self._merge_sort(lista[:middle])
            left = self._merge_sort(lista[middle:])
            return self._merge(right, left)
    

    def _merge(self, lista1, lista2):
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado

        # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1

        # Agregamos los resultados a la lista
            result += lista1[i:]
            result += lista2[j:]

            # Retornamos el resultados
            return result



    def sort_to_average(self, option_sort):
        print(option_sort)
        self.data_movies = self._merge_sort(option_sort)
        import pdb; pdb.set_trace()