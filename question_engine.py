from MandQclasses import *
from helper_functions import *
import PySimpleGUI as sg

class question_engine:

    def __init__(self, question_file):
        self.q_file = question_file

    # Reads the question text files
    # and stores it in a list (i.e. qs)
    #
    #
    # function: __read_question_file
    #
    # returns:
    #           qs - A list of all the questions.
    #                Each index is of myQuestion type
    # parameters:
    #           myFile [string] The input text file of questions
    #
    # @author MonkaS
    # @since 3/11/2021

    def __read_question_file(self):

        qs = []

        with open(self.q_file) as file:
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


    # Displays the questions to the user and
    # records his/her input through the UI
    # into two lists (i.e. userPref, userScore)
    #
    # function: gen_ques_database
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

    def gen_ques_database(self):
        sg.theme('Dark Grey 5')
        userPref = []
        userScore = []

        questions = self.__read_question_file()

        for idx in range(len(questions)):

            layout_column = [[sg.Input(visible=False)],
                             [sg.Text(questions[idx].getQ()[0], justification='center', font="Fixedsys 20")],
                             [sg.Button(questions[idx].getQ()[1][0], button_color='Blue', key="-O1-", font="Fixedsys 20", size=(20, 10)),
                              sg.Button(questions[idx].getQ()[1][1], button_color="red", key="-O2-", font="Fixedsys 20", size=(20, 10))]]

            layout = [[sg.Column(layout_column, element_justification='center')]]

            window = sg.Window("MonkaS Movie Recommendation System", layout)

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    quit()
                # This occurs when the user selects the first option and updates the users prefrences with the selected genre
                elif event == "-O1-":
                    for genre in range(len(questions[idx].getQ()[2])):
                        if questions[idx].getQ()[2][genre] not in userPref:
                            userPref.append(questions[idx].getQ()[2][genre])
                            userScore.append(0)
                        userScore[userPref.index(questions[idx].getQ()[2][genre])] += 1
                    break

                # This occurs when the user selects the second option and updates the users prefrences with the selected genre
                elif event == "-O2-":
                    for genre in range(len(questions[idx].getQ()[3])):
                        if questions[idx].getQ()[3][genre] not in userPref:
                            userPref.append(questions[idx].getQ()[3][genre])
                            userScore.append(0)
                        userScore[userPref.index(questions[idx].getQ()[3][genre])] += 1
                    break

            window.close()

        return userPref, userScore
