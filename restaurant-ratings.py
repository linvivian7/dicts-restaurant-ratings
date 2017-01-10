# your code goes here
import sys


filename = sys.argv[1]


def sort_dicts(dictionary):
    return sorted(dictionary)


def prettify_output(dictionary):
    list_of_tuples = sorted(dictionary.items())

    for tup in list_of_tuples:
        print tup[0], 'is rated at', str(tup[1]) + '.'


def add_user_rating(rest_ratings):
    name = raw_input("Please enter restaurant name: \n")
    score = int(raw_input("Please enter score for {}: \n".format(name)))

    rest_ratings[name] = score


def rate_restaurants(filename):
    score_file = open(filename)

    rest_ratings = {}

    for line in score_file:
        rest_name, rest_rating = line.rstrip().split(":")

        rest_ratings[rest_name] = int(rest_rating)

    return rest_ratings


rest_ratings = rate_restaurants(filename)
prettify_output(rest_ratings)

add_user_rating(rest_ratings)
prettify_output(rest_ratings)
