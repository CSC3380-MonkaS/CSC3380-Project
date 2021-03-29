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


# Finds the intersect between two sets of data
#
#
# function: intersect
#
# returns:
#          A list of the intersect of two sets of data
#
# parameters:
#          a [string[]] The first set of data
#          b [string[]] The isecond set of data
#
# @author MonkaS
# @since 3/11/2021
def intersect(a, b):
    return list(set(a) & set(b))

#  Converts list to string
#
# function: list_to_string
#
# returns:
#           str - A string
#
# parameters:
#           s [list] A list
#
# @author MonkaS
# @since 3/11/2021


def listToString(s):

    str = ""

    for i in s:
        str += i

    return str
