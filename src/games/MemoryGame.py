# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.
# Properties
# 1. Difficulty
#
# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user.
# The list length will be in the size of difficulty.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will return True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
import functools
import numpy as np

from src.Scores import add_score
from src.utils.games_utils import *


#   ----------------------------------------------------------------
#   Function: generate_sequence - Will get the difficulty of the game.
#   Function: get_list_from_user - Will get the difficulty of the game.
#   ----------------------------------------------------------------


# Will generate a list of random numbers between 1 to 101.
# The list length will be difficulty.
def generate_sequence(difficulty):
    sequence = []
    for index in range(difficulty):
        sequence.append(np.random.randint(1, 101))
    return sequence


# Will return a list of numbers prompted from the user.
# # The list length will be in the size of difficulty.
def get_list_from_user(difficulty):
    user_choices = []
    print(f"{GameColors.ENDC}The amount of numbers you remember is {GameColors.OKCYAN}{difficulty}")
    for index in range(difficulty):
        user_choice = get_number_in_range(f"What is number {index + 1} of the list? ", 1, 101)
        user_choices.append(user_choice)
    return user_choices


# A function to compare two lists if they are equal.
# The function will return True / False.
def is_list_equal(list1, list2):
    if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, list1, list2), True):
        print(custom_text("The lists are the same.", GameColors.HEADER))
        return True
    print(custom_text("The lists are not the same.", GameColors.HEADER))
    return False


# Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(game_over):
    win = False
    user_want_to_play = True
    # TODO REMOVE THIS ONE FILE ABOVE
    print(custom_text("Welcome to Memory Game!", GameColors.HEADER))
    while user_want_to_play:
        difficulty = get_number_in_range("How many numbers do you want in the sequence from 1 to 100? ", 1, 101)
        sequence = generate_sequence(difficulty)
        print(f"{GameColors.ENDC}The sequence is: {GameColors.OKCYAN}{sequence}")
        clean_console()
        users_choices = get_list_from_user(difficulty)
        print(f"{GameColors.ENDC}The user choices are: {GameColors.OKCYAN}{users_choices}{GameColors.ENDC} and the sequence is: {GameColors.OKCYAN}{sequence}")
        win = is_list_equal(sequence, users_choices)
        if win:
            add_score(difficulty)
        is_win_output(win)
        win = False
        user_want_to_play = get_boolean('Do you want to play again')
    print(custom_text(THANK_YOU, GameColors.OKGREEN))
    game_over = not get_boolean('Do you want continue to play with one of our games')
    return game_over
