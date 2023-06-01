# The purpose of guess game is to start a new game,
# cast a random number between 1 to a variable called difficulty.
# The game will get a number input from the Properties:
# 1. Difficulty
# 2. Secret number
#
# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and return the number.
# 3. compare_results - Will compare the the secret generated number to the one prompted
# by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import numpy as np

from server.src.Scores import add_score
from server.src.utils.games_utils import *


# Will generate number between 1 to difficulty and save it to secret_number
# -1 will be invalid value
def generate_number(difficulty):
    if type(difficulty) != int:
        return -1
    if not 0 < difficulty < 11:
        return -1
    return np.random.randint(1, difficulty + 1)


# Will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user(difficulty):
    return get_number(f"Guess a number between 1 to {difficulty}: ")


# Will compare the secret generated number to the one prompted by the get_guess_from_user.
def compare_results(secret_number, guess_number):
    print(f"{GameColors.ENDC} The secret number is {GameColors.OKCYAN}{secret_number} {GameColors.ENDC}and the guess number is {GameColors.OKCYAN}{guess_number}")
    return secret_number == guess_number


# Will call the functions above and play the game.
# Will return True / False if the user lost or won.
def play(game_over):
    win = False
    user_want_to_play = True
    print(custom_text("Welcome to Guess the Number Game!", GameColors.HEADER))
    while user_want_to_play:
        user_difficulty = get_number_in_range(f"{GameColors.ENDC}Choose a difficulty between {GameColors.OKCYAN}1 and 10: {GameColors.ENDC}", 1, 10)
        game_guess = generate_number(user_difficulty)
        user_guess = get_guess_from_user(user_difficulty)
        win = compare_results(user_guess, game_guess)
        if win:
            add_score(user_difficulty)
        is_win_output(win)
        win = False
        user_want_to_play = get_boolean('Do you want to play again')
    print(custom_text(THANK_YOU, GameColors.OKGREEN))
    game_over = not get_boolean('Do you want continue to play with one of our games')
    return game_over