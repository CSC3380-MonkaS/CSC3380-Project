class myMovie:
    def __init__(self, name, score, rating, genre, des):
        self._name = name
        self._score = score
        self._rating = rating
        self._genre = genre.split()
        self._des = des

    def getInfo(self):
        return self._name, self._score, self._rating, self._genre, self._des



class myQuestion:
    def __init__(self, ques, o, p1, p2):
        self._ques = ques
        self._o = o
        self._p1 = p1
        self._p2 = p2

    def getQ(self):
        return self._ques, self._o, self._p1, self._p2
