class SortMovies(object):
    """ calss for manage sort funtionalitys
    """

    # methos for sort by average rating
    def _sort_to_average_rating(self):
        return self._merge_sort(self.data_movies.get('movies'))


    # method for sort by similar movie
    def _sort_to_similar_movie(self):
        return []


    # method for sort by same actor
    def _sort_to_same_actor(self):
        return []


    # merge sort methos for order data in sort average rating
    def _merge_sort(self, data_movies):
        if len(data_movies) >1: 
            mid = len(data_movies)//2 # Finding the mid of the array 
            L = data_movies[:mid] # Dividing the array elements  
            R = data_movies[mid:] # into 2 halves 
    
            self._merge_sort(L) # Sorting the first half 
            self._merge_sort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i].get('averageRating') < R[j].get('averageRating'): 
                    data_movies[k] = L[i] 
                    i+= 1
                else: 
                    data_movies[k] = R[j] 
                    j+= 1
                k+= 1
            
            # Checking if any element was left 
            while i < len(L): 
                data_movies[k] = L[i]
                i+= 1
                k+= 1
            
            while j < len(R): 
                data_movies[k] = R[j] 
                j+= 1
                k+= 1
            return data_movies
        else:
            return data_movies
    

    # methos main for execute each option sort
    def sort_data(self, option_sort):
        if option_sort == 1:
            self.data_movies = self._sort_to_average_rating()
            self.data_movies = self.data_movies[::-1]
        elif option_sort == 2:
            self.data_movies = self._sort_to_similar_movie()
        elif option_sort == 3:
            self.data_movies = self._sort_to_same_actor()