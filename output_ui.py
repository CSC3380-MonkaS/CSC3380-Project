from helper_functions import *
import PySimpleGUI as sg
from MandQclasses import myMovie

class output_UI:

    def __init__(self, percents, user_pref, movie_file):
        self.percents = percents
        self.user_pref = user_pref
        self.movie_file = movie_file

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
    # parameters:
    #           myFile [string] The text file containing all the movies
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

    # Creates/Displays congratulations screen
    #
    # function: congratulations
    #
    # returns: N/A
    #
    # parameters: genre [string] String of genres
    #
    # @author MonkaS
    # @since 3/11/2021

    def __congratulations(self):
        max_prefs = convert(self.max_prefs())

        layout_column = [[sg.Input(visible=False)],
                         [sg.Text("Congratulations!", font="Fixedsys 30", justification='center', size=(22,2))],
                         [sg.Text("Your chosen genre(s):", font="Fixedsys 20", justification='center', size=(22, 2))],
                         [sg.Text(max_prefs, justification= 'center', font="Times")],
                         [sg.Button("Continue to Movies", button_color="Blue", pad=(50,50), font="Fixedsys 20", key="-01-")]]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window("Movie Recommendation Demo", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
                break
            elif event == "-01-":
                window.close()
                break

    # Creates/Displays unfortunately screen
    #
    # function: unfortunately
    #
    # returns: N/A
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/11/2021

    @staticmethod
    def __unfortunately(self):
        layout_column = [[sg.Input(visible=False)],
                         [sg.Text("Unfortunately, there are no movies with your favorite generes in our database!", font="Fixedsys 30", justification='center', size=(30, 3))],
                         [sg.Button("OK", button_color="Blue", font="Fixedsys 20", key="-01-")]]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window("Sorry!", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            elif event == "-01-":
                window.close()
                break

    # Creates/Displays user movie reccomendation output screen
    #
    # function: user_movie_output
    #
    # returns: N/A
    #
    # parameters: user_pref [string[]] List of user preferences
    #             percents [float[]] List of user percent match for genres
    #             movie_file File containing movies
    #
    # @author MonkaS
    # @since 3/11/2021

    def user_movie_output(self):

        sg.theme('Dark Grey 5')
        movie_list = self.__read_movie_file()
        max_prefs = self.max_prefs()
        user_picks = []

        for movie in range(len(movie_list)):
            gInMovie = intersect(max_prefs, movie_list[movie].getInfo()[3])
            if len(gInMovie) != 0:
                user_picks.append(movie_list[movie].getInfo()[0] + "\n\n" +
                                  movie_list[movie].getInfo()[4] +
                                  "\nRated: " + movie_list[movie].getInfo()[2] +
                                  "\n\nScore: " + movie_list[movie].getInfo()[1] + "/100"+
                                  "\n\nGenre(s): " + convert(gInMovie) +
                                  "\n---------------------------------------------------------")

        user_picks = sorted(user_picks)

        self.__congratulations()

        if len(user_picks) > 0:
            sg.PopupScrolled(*user_picks, title="Your Specially Selected Movie Recommendations!", button_color="Blue", size=(100, 45))

        else:
            self.__unfortunately()

    def max_prefs(self):
        max_p = []
        max_percent = max(self.percents)

        for p in range(len(self.user_pref)):
            if max_percent == self.percents[p]:
                max_p.append(self.user_pref[p])

        return max_p
