from classes import *
from read_methods import read_movie_file
import PySimpleGUI as sg


def congratulations(genre):
    layout = [[sg.Text("Congratulations!", font="Fixedsys 30", size=(20,2))],
              [sg.Text("Your chosen genre is:", font="Fixedsys 20", size=(20, 2))],
              [sg.Text(genre, font="Times")],
              [sg.Button("Continue to movies", button_color="Blue", font="Fixedsys 20", key="-01-")]]
    window = sg.Window("Movie Recommendation Demo", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "-01-":
            window.close()
            break


def user_movie_output(user_pref, percents, movie_file):


    sg.theme('Dark Grey 5')
    movie_list = read_movie_file("input_files/movie_list.txt")
    max_percent = max(percents)
    max_prefs = []

    for p in range(len(user_pref)):
        if max_percent == percents[p]:
            max_prefs.append(user_pref[p])

    if len(max_prefs) > 1:
        layout_str = "layout = [[sg.Text(\"You Seem to like Multiple Genres Equally!\", font=\"Fixedsys\")], [sg.Text(\"Select a category to see movies of that Genre:\", font=\"Fixedsys\")], "

        display_str = """
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        window.close()
        break
"""
        for g in range(len(max_prefs)):
            temp_str = "[sg.Button(\"%s\", button_color=\"Red\", font=\"Fixedsys\", key=\"%s\")], " % (max_prefs[g], max_prefs[g])
            layout_str = layout_str + temp_str

            temp_str = """
    elif event == \"%s\":
        spec_movies%d = []
        for i in range(len(movie_list)):
            if \"%s\" in movie_list[i].getInfo()[3]:
                spec_movies%d.append(movie_list[i].getInfo()[0]+movie_list[i].getInfo()[4])
                
        window.close()
        congratulations(\"%s\")
        sg.PopupScrolled(*spec_movies%d, title="%s")                # Temporary: Need to Display Results in a better way
        
        if len(spec_movies%d) == 0:
            sg.popup("No Movies With This Genre Yet!")
""" \
            % (max_prefs[g], g, max_prefs[g], g, max_prefs[g], g, max_prefs[g], g)
            display_str = display_str + temp_str



        layout_str = layout_str[0:(len(layout_str)-2)]
        layout_str = layout_str + "]"
        window_str = "window = sg.Window(\"Movie Results\", layout)"



        exec(layout_str)
        exec(window_str)

        exec(display_str)

    else:
        spec_movies = []
        for i in range(len(movie_list)):
            if max_prefs[0] in movie_list[i].getInfo()[3]:
                spec_movies.append(movie_list[i].getInfo()[0]+movie_list[i].getInfo()[4])
        congratulations(max_prefs[0])
        sg.PopupScrolled(*spec_movies, title=max_prefs[0])      # Temporary: Need to Display Results in a better way
