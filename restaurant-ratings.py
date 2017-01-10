# your code goes here
import sys

filename = sys.argv[1]


def prettify_output(ratings):
    """ Sorts dictionary and makes the output pretty ;P"""

    tuples = sorted(ratings.items())

    for tup in tuples:
        print "{} is rated at {}.".format(tup[0], tup[1])


def add_user_rating(rest_ratings):
    """ Prompts user for restaurant name and rating and adds input to dict

    If restaurant is already in dictionary, user's input overwrites items
    """

    name = raw_input("Please enter restaurant name: \n")
    score = int(raw_input("Please enter score for {}: \n".format(name)))

    rest_ratings[name] = score


def update_rest_rating(rest_ratings):
    """ Updates dictionary with user's new rating for exisiting restaurant """

    rest_choice = raw_input("Which restaurant rating would you like to change?\n ")

    if rest_choice not in rest_ratings:
        print "This restaurant is not already in our database, if you would like to add it, type 2"
        return

    print "{} is currently rated {}.".format(rest_choice, rest_ratings[rest_choice])
    new_rating = raw_input("Enter new rating here: \n")

    rest_ratings[rest_choice] = new_rating


def rate_restaurants(filename):
    """ Reads file info and creates dictionary from restaurant names and ratings
    """

    score_file = open(filename)

    rest_ratings = {}

    for line in score_file:
        rest_name, rest_rating = line.rstrip().split(":")

        rest_ratings[rest_name] = int(rest_rating)

    score_file.close()

    return rest_ratings


def initial_user_choice():
    """ Prompts user for choice of what function the program should run or to
    quit :(
    """

    rest_ratings = rate_restaurants(filename)

    while True:
        print
        print """Would you like to (1) see the rated restaurants, (2) add one of
        your own, (3) update a restaurant rating, or (4) quit? \n"""

        choice = raw_input("""To see ratings, type 1; to add your own, type 2;
            to update, type 3; to quit, type 4 \n""")

        if choice == '2':
            add_user_rating(rest_ratings)
        if choice in ['1', '2', '3']:
            prettify_output(rest_ratings)
        if choice == '3':
            update_rest_rating(rest_ratings)
            prettify_output(rest_ratings)
        elif choice == '4':
            break
        else:
            print "Please enter valid input"


initial_user_choice()
