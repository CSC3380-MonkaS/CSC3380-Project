from input_ui import *
from question_engine import *
from user_file_generator import *
from output_ui import *

# Main Function
#
# function: main
#
# returns: N/A
#
# parameters: N/A
#
#
# @author MonkaS
# @since 3/11/2021


def main():

    movie_file = "input_files/movies.txt"
    question_file = "input_files/questions.txt"

    input_ui = input_UI()
    input_ui.startScreen()

    q_eng = question_engine(question_file)
    

    user_prefs, user_scores = q_eng.gen_ques_database()

    u_file_gen = user_file_generator(user_prefs, user_scores)
    output_UI = output_UI()



if __name__ == "__main__":
    main()