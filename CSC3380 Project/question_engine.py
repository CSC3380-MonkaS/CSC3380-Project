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

    userPref = []
    userScore = []

    questions = read_question_file(question_file)

    for idx in range(len(questions)):

        layout = [[sg.Text(questions[idx].getQ()[0])],
                  [sg.Button(questions[idx].getQ()[1][0], key="-O1-", button_color='blue'),
                   sg.Button(questions[idx].getQ()[1][1], key="-O2-", button_color='red')]]

        window = sg.Window("Movie Recommendation Demo", layout)

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