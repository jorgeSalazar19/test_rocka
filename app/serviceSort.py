class SortMovies(object):
    """ calss for manage sort funtionalitys
    """

    # methos for sort by average rating
    def _sort_to_average_rating(self):
        return self._merge_sort_average(self.data_movies.get('movies'))


    # method for sort by similar movie
    def _sort_to_similar_movie(self):
        return []


    # method for sort by same actor
    def _sort_to_same_actor(self):
        return self._sort_by_actor(self.data_movies.get('movies'))
    

    # method for sor by actor
    def _sort_by_actor(self, data_movies):
        list_result = []
        list_tmp_titles_movies = []
        for index in range(len(data_movies)):
            for index_aux in range(len(data_movies)):
                if len(set(data_movies[index].get('actors')).union(set(data_movies[index_aux].get('actors')))) < len(data_movies[index].get('actors')) + len(data_movies[index_aux].get('actors')):
                    if data_movies[index_aux].get('title') not in list_tmp_titles_movies:
                        list_result.append(data_movies[index_aux])
                        list_tmp_titles_movies.append(data_movies[index_aux].get('title'))
            if data_movies[index].get('title') not in list_tmp_titles_movies:
                list_result.append(data_movies[index])
                list_tmp_titles_movies.append(data_movies[index].get('title'))
        print(list_tmp_titles_movies, len(list_tmp_titles_movies))
        return list_result




    # merge sort methos for order data in sort average rating
    def _merge_sort_average(self, data_movies):
        if len(data_movies) >1: 
            mid = len(data_movies)//2 # middle list 
            left_list = data_movies[:mid] # Dividing the array in two list, left and right
            right_list = data_movies[mid:] #
    
            self._merge_sort_average(left_list) # Sorting the left list
            self._merge_sort_average(right_list) # Sorting the right list
    
            i = j = k = 0
            
            # Copy data to temp arrays left_list[] and right_list[] 
            while i < len(left_list) and j < len(right_list): 
                if left_list[i].get('averageRating') > right_list[j].get('averageRating'): 
                    data_movies[k] = left_list[i] 
                    i+= 1
                else: 
                    data_movies[k] = right_list[j] 
                    j+= 1
                k+= 1
            
            # Checking if any element was left 
            while i < len(left_list): 
                data_movies[k] = left_list[i]
                i+= 1
                k+= 1
            
            while j < len(right_list): 
                data_movies[k] = right_list[j] 
                j+= 1
                k+= 1
            return data_movies
        else:
            return data_movies
    

    # methos main for execute each option sort
    def sort_data(self, option_sort):
        if option_sort == 1:
            self.data_movies = self._sort_to_average_rating()
        elif option_sort == 2:
            self.data_movies = self._sort_to_similar_movie()
        elif option_sort == 3:
            self.data_movies = self._sort_to_same_actor()