from helper_functions import *


class compat_calc:

    def __init__(self, u_p,  u_s, u_f):

        self.user_preferences = u_p         # User genre preferences
        self.user_scores = u_s              # User's scores for each genre
        self.user_file = u_f                # User's profile info

    # calculates the percentages that a user
    # favors each genre and write it to user
    # info file and returns said percentages
    #
    # function: calc_percents
    #
    # returns:
    #          percentages User's percentages of genres liked
    #
    #
    # parameters: N/A
    #
    #
    # @author MonkaS
    # @since 3/11/2021


    def calc_percents(self):

        score_total = sum(self.user_scores)
        percentages = []

        u_pref = sorted(self.user_preferences)
        u_pref = helper_functions().convert(u_pref)
        u_pref = u_pref.split(", ")

        with open("output_files/user_info.txt", "a", encoding='utf8') as file:

            for pf in range(len(u_pref)):
                percentages.append(
                    round((self.user_scores[self.user_preferences.index(u_pref[pf])] / score_total) * 100.0, 2))
                file.write(u_pref[pf] + ": " + str(
                    round((self.user_scores[self.user_preferences.index(u_pref[pf])] / score_total) * 100.0, 2)) + "%\n")

        return percentages
