class myMovie:
    # This method initializes movie objects
    #
    #
    # function: __init__
    #
    # returns: N/A
    #
    #
    # parameters: self [myMovie] A movie object
    #             name [string] The name of the movie
    #             score [int] The score of the movie
    #             rating [string] The rating of the movie
    #             genre [string[]] The genre(s) of the movie
    #             des [string] A description of the movie
    #
    #
    # @author MonkaS
    # @since 3/11/2021
    def __init__(self, name, score, rating, genre, des):
        self._name = name
        self._score = score
        self._rating = rating
        self._genre = genre.split(", ")
        self._des = des

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
    # This method initializes question objects
    #
    #
    # function: __init__
    #
    # returns: N/A
    #
    #
    # parameters: self [myQuestion] A question object
    #             ques [string] The question
    #             o [string] The " or " between options
    #             p1 [string] First option
    #             p2 [string] Second option
    #
    #
    # @author MonkaS
    # @since 3/11/2021
    def __init__(self, ques, o, p1, p2):
        self._ques = ques
        self._o = o
        self._p1 = p1
        self._p2 = p2

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
