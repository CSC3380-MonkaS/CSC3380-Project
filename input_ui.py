import PySimpleGUI as sg

#  Creates/Displays start screen
#
# function: startScreen
#
# returns: N/A
#
# parameters: N/A
#
# @author MonkaS
# @since 3/11/2021


class input_UI:

    def startScreen(self):
        sg.theme('Dark Grey 5')
        layout_column = [[sg.Input(visible=False)],
                         [sg.Text("Welcome to MonkaS Movie Recommendation System", font="Fixedsys 30", justification='center', size=(22,2))],
                         [sg.Text()],
                         [sg.Text()],
                         [sg.Text("To get started, press the start button below.", font="Fixedsys 20", justification='center', size=(22, 2))],
                         [sg.Button("More Info", button_color="Red", pad=(25,50), font='Fixedsys 20', key='-01-'),
                          sg.Button("Start", button_color="Blue", pad=(25,0), font="Fixedsys 20", key="-02-")]]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window("Start", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
                break
            elif event == "-01-":
                self.infoScreen()
            elif event == "-02-":
                window.close()
                break


    # Creates/Displays information screen
    #
    # function: infoScreen
    #
    # returns: N/A
    #
    # parameters: N/A
    #
    # @author MonkaS
    # @since 3/11/2021

    @staticmethod
    def infoScreen():
        sg.theme('Dark Grey 5')
        layout_column = [[sg.Input(visible=False)],
                         [sg.Text("More Information", font="Fixedsys 30", justification='center', size=(22,0))],
                         [sg.Text("About MonkaS:", font="Fixedsys 20", justification='left', size=(50, 0))],
                         [sg.Text("MonkaS is a group of 6 LSU students who had a vision of transforming the way movie lovers receive movie recommendations.", font="Fixedsys 15", justification='left', size=(60, 0))],
                         [sg.Text("How to Use:", font="Fixedsys 20", justification='left', size=(50, 0))],
                         [sg.Text("Start by pressing the start button. You will be greeted by two buttons, each containing a movie genre. Choose the genre you prefer. You will continue until you answer all of the questions. After answering all of the questions, you will be rewarded with your own personalized movie recommendations!", font="Fixedsys 15", justification='left', size=(60, 0))],
                         [sg.Button("Back", button_color="Blue", pad=(0, 50), font="Fixedsys 20", key="-03-")]]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window("More Information", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
                break
            elif event == "-03-":
                window.close()
                break
