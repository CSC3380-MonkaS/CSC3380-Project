class myMovie:

    def __init__(self, name, score, rating, genre, des):
        self._name = name                 # name of Movies
        self._score = score               # score/100 of the movie
        self._rating = rating             # rating of the movie
        self._genre = genre.split(", ")   # Genre(s) of movies separated by commas
        self._des = des                   # Description of the movie

    # This method returns information from a movie object
    #
    #
    # function: getInfo
    #
    # returns: self._name - Movie name
    #          self._score - Movie score
    #          self._rating - Movie Rating
    #          self._genre - Movie genre(s)
    #          self._des - Movie description
    #
    #
    # parameters: self [myMovie] A movie object
    #
    #
    # @author MonkaS
    # @since 3/11/2021
    def getInfo(self):
        return self._name, self._score, self._rating, self._genre, self._des



class myQuestion:

    def __init__(self, ques, o, p1, p2):
        self._ques = ques   # Question posed
        self._o = o         # Options for answers
        self._p1 = p1       # Genres to add points to if option 1 chosen
        self._p2 = p2       # Genres to add points to if option 2 chosen

    # is method returns information from a question object
    #
    #
    # function: getQ
    #
    # returns: self._ques - Question
    #          self._o - " or "
    #          self._p1 - First option
    #          self._p2 - Second option
    #
    #
    # parameters: self [myQuestion] A question object
    #
    #
    # @author MonkaS
    # @since 3/11/2021
    def getQ(self):
        return self._ques, self._o, self._p1, self._p2
