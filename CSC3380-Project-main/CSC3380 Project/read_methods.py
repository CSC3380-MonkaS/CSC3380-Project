from classes import *

#  Reads the movie text file
#  and loads it into a list
#  (i.e. movieList)
#
# function: read_movie_file
#
# returns:
#          movieList - A list of all the movies and their details.
#                      Each index is of myMovie type.
#
# parameters:
#           myFile [string] The text file containing all the movies
#
# @author MonkaS
# @since 3/11/2021


def read_movie_file(myFile):

    movieList = []

    with open(myFile) as file:
        while True:

            cur_movie = file.readline()

            if not cur_movie:
                break

            temp_name = cur_movie.strip()
            temp_score = file.readline().strip()
            temp_rating = file.readline().strip()
            temp_genre = file.readline()
            temp_des = ""

            while True:
                cur_line = file.readline()
                if "$$$$" in cur_line.strip():
                    break
                temp_des = temp_des + cur_line

            movieList.append(myMovie(temp_name, temp_score, temp_rating, temp_genre, temp_des))

    file.close()

    return movieList

# Reads the question text files
# and stores it in a list (i.e. qs)
#
#
# function: read_question_file
#
# returns:
#           qs - A list of all the questions.
#                Each index is of myQuestion type
# parameters:
#           myFile [string] The input text file of questions
#
# @author MonkaS
# @since 3/11/2021


def read_question_file(myFile):

    qs = []

    with open(myFile) as file:
        while True:
            temp_cur_ques = file.readline()

            if not temp_cur_ques:
                break

            temp_cur_ques = temp_cur_ques.strip()
            temp_options = file.readline().strip().split(" or ")
            temp_points = file.readline().strip().split(" # ")
            temp_p1 = temp_points[0].split(", ")
            temp_p2 = temp_points[1].split(", ")

            qs.append(myQuestion(temp_cur_ques, temp_options, temp_p1, temp_p2))
            file.readline()

    file.close()

    return qs

