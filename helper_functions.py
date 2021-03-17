# Converts a list to a string
# with spaces between indices
#
#
# function: convert
#
# returns:
#          A string of the indices in the list with spaces
#          placed between each one
#
# parameters:
#          question_file [string] The input question text file
#
# @author MonkaS
# @since 3/11/2021

def convert(l):
    return ', '.join(l)


def intersect(a, b):
    return list(set(a) & set(b))