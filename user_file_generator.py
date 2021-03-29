from helper_functions import *

# Generates the User's info file
# regarding which genre of movies
# he/she would be most interested in
#
#
# function: user_file_generate
#
# returns: N/A
#
#
# parameters: question_file [string] The input text file containing the questions
#
#
# @author MonkaS
# @since 3/11/2021


class user_file_generator:

    def __init__(self, u_prefs, u_scores):
        self.user_preferences = u_prefs
        self.user_scores = u_scores

    def user_file_generate(self):

        score_total = sum(self.user_scores)
        percentages = []

        with open("output_files/user_info.txt", "w", encoding='utf8') as file:
            file.write("Generated by The Movie Recommender\n")
            file.write("Developed by MonkaS\n")
            file.write("Copyright 2021\n\n\n")
            u_pref = sorted(self.user_preferences)
            u_pref = convert(u_pref)
            file.write("Genre List: " + u_pref + "\n\n\n")
            u_pref = u_pref.split(", ")

            file.write("Movie Genre Percent Matches\n\n")

            for pf in range(len(u_pref)):
                percentages.append(round((self.user_scores[self.user_preferences.index(u_pref[pf])] / score_total) * 100.0, 2))
                file.write(u_pref[pf] + ": " + str(
                    round((self.user_scores[self.user_preferences.index(u_pref[pf])] / score_total) * 100.0, 2)) + "%\n")

        file.close()

        return u_pref, percentages
