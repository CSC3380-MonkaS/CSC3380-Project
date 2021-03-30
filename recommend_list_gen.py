from helper_functions import *
from MandQclasses import myMovie

class recommendation_list_generator:

    def __init__(self, u_per, u_prefs, m_file):

        self.percents = u_per
        self.user_pref = u_prefs
        self.movie_file = m_file

    #  Reads the movie text file
    #  and loads it into a list
    #  (i.e. movieList)
    #
    # function: __read_movie_file
    #
    # returns:
    #          movieList - A list of all the movies and their details.
    #                      Each index is of myMovie type.
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/11/2021

    def __read_movie_file(self):

        movieList = []

        with open(self.movie_file) as file:
            while True:

                cur_movie = file.readline()

                if not cur_movie:
                    break

                temp_name = cur_movie.strip()
                temp_score = file.readline().strip()
                temp_rating = file.readline().strip()
                temp_genre = file.readline().replace('\n', '')
                temp_des = ""

                while True:
                    cur_line = file.readline()
                    if "$$$$" in cur_line.strip():
                        break
                    temp_des = temp_des + cur_line

                movieList.append(myMovie(temp_name, temp_score, temp_rating, temp_genre, temp_des))

        file.close()

        return movieList


    # Gets the genre(s) with the highest percentage
    #
    # function: __max_prefs
    #
    # returns: N/A
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/29/2021

    def __max_prefs(self):
        max_p = []
        max_percent = max(self.percents)

        for p in range(len(self.user_pref)):
            if max_percent == self.percents[p]:
                max_p.append(self.user_pref[p])

        return max_p

    # Generates a list of recommend movies based
    # of the genre which is most favored
    #
    # function: generate_list
    #
    # returns: max_prefs User's top genres
    #          sorted(user_picks) Sorted list of the user's picked movies
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/29/2021

    def generate_list(self):

        movie_list = self.__read_movie_file()
        max_prefs = self.__max_prefs()
        user_picks = []

        for movie in range(len(movie_list)):
            gInMovie = helper_functions().intersect(max_prefs, movie_list[movie].getInfo()[3])
            if len(gInMovie) != 0:
                user_picks.append(movie_list[movie].getInfo()[0] + "\n\n" +
                                  movie_list[movie].getInfo()[4] +
                                  "\nRated: " + movie_list[movie].getInfo()[2] +
                                  "\n\nScore: " + movie_list[movie].getInfo()[1] + "/100" +
                                  "\n\nGenre(s): " + helper_functions().convert(gInMovie) +
                                  "\n---------------------------------------------------------")

        return max_prefs, sorted(user_picks)

