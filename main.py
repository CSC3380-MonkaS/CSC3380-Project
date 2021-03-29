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

    iui = input_UI()      # Make a input_UI object
    iui.startScreen()     # Display the Start Screen

    q_eng = question_engine(question_file)     # Make a question_engine object
    user_prefs, user_scores = q_eng.gen_ques_database() # Get the user's genre preferences and scores each genre

    ufg = user_file_generator(user_prefs, user_scores)
    string_user_prefs, percents = ufg.user_file_generate() # Generate User Info File

    oui = output_UI(percents, string_user_prefs, movie_file)

    oui.user_movie_output()

if __name__ == "__main__":
    main()