from classes import *
from helper_functions import *
from read_methods import read_movie_file
import PySimpleGUI as sg

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
def congratulations(genre):
    layout_column = [[sg.Input(visible=False)],
                     [sg.Text("Congratulations!", font="Fixedsys 30", justification='center', size=(22,2))],
                     [sg.Text("Your chosen genre(s):", font="Fixedsys 20", justification='center', size=(22, 2))],
                     [sg.Text(genre, justification= 'center', font="Times")],
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
def unfortunately():
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
def user_movie_output(user_pref, percents, movie_file):

    sg.theme('Dark Grey 5')
    movie_list = read_movie_file("input_files/movie_list.txt")
    max_percent = max(percents)
    max_prefs = []
    user_picks = []

    for p in range(len(user_pref)):
        if max_percent == percents[p]:
            max_prefs.append(user_pref[p])

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

    congratulations(convert(max_prefs))

    if len(user_picks) > 0:
        sg.PopupScrolled(*user_picks, title="Your Specially Selected Movie Recommendations!", button_color="Blue", size=(100, 50))

    else:
        unfortunately()
