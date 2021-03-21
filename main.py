from start_screen import *
from userFile_generator import *
from user_movie_output import *
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
    startScreen()
    preferences, percents = user_file_generator("input_files/questions.txt")
    user_movie_output(preferences, percents, "input_files/movie_list.txt")


if __name__ == "__main__":
    main()