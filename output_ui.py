import PySimpleGUI as sg
from recommend_list_gen import *

class output_UI:

    def __init__(self, percents, user_pref, movie_file):
        self.percents = percents                            # Calculated genre precentages
        self.user_pref = user_pref                          # User's Preffered genres
        self.movie_file = movie_file                        # Location of movies text file

    # Creates/Displays congratulations screen
    #
    # function: congratulations
    #
    # returns: N/A
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/11/2021

    def __congratulations(self, max_p):

        max_prefs = helper_functions().convert(max_p)

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
    def __unfortunately():
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

    # Creates/Displays user movie recommendation output screen
    #
    # function: user_movie_output
    #
    # returns: N/A
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/11/2021

    def user_movie_output(self):

        sg.theme('Dark Grey 5')

        r_gen = recommendation_list_generator(self.percents, self.user_pref, self.movie_file)
        max_prefs, user_picks = r_gen.generate_list()

        self.__congratulations(max_prefs)

        if len(user_picks) > 0:
            sg.PopupScrolled(*user_picks, title="Your Specially Selected Movie Recommendations!", button_color="Blue", size=(100, 45))

        else:
            self.__unfortunately()
