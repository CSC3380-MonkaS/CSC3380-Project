from read_methods import *
import PySimpleGUI as sg


# Displays the questions to the user and
# records his/her input through the UI
# into two lists (i.e. userPref, userScore)
#
# function: question_engine
#
# returns:
#          userPref - Generes that the User may like
#          userScore - Number of "points" the user has
#                      for each genre
#
# parameters:
#             question_file [string]  Text file containing the questions
#
# @author MonkaS
# @since 3/11/2021

def question_engine(question_file):
    sg.theme('Dark Grey 5')
    userPref = []
    userScore = []

    questions = read_question_file(question_file)

    for idx in range(len(questions)):

        layout_column = [[sg.Input(visible=False)],
                        [sg.Text()],
                        [sg.Text()],
                        [sg.Text(questions[idx].getQ()[0], justification='center', font="Fixedsys 30")],
                        [sg.Text()],
                        [sg.Text()],
                        [sg.Text()],
                        [sg.Text()],
                        [sg.Button(questions[idx].getQ()[1][0], button_color='Blue', key="-O1-", font="Fixedsys 20", size=(13, 8)),
                        sg.Button(questions[idx].getQ()[1][1], button_color="red", key="-O2-", font="Fixedsys 20", size=(13, 8))]]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window("MonkaS Movie Recommendation System", layout, size=(800, 500))

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                quit()

            elif event == "-O1-":
                for genre in range(len(questions[idx].getQ()[2])):
                    if questions[idx].getQ()[2][genre] not in userPref:
                        userPref.append(questions[idx].getQ()[2][genre])
                        userScore.append(0)
                    userScore[userPref.index(questions[idx].getQ()[2][genre])] += 1
                break

            elif event == "-O2-":
                for genre in range(len(questions[idx].getQ()[3])):
                    if questions[idx].getQ()[3][genre] not in userPref:
                        userPref.append(questions[idx].getQ()[3][genre])
                        userScore.append(0)
                    userScore[userPref.index(questions[idx].getQ()[3][genre])] += 1
                break

        window.close()

    return userPref, userScore
