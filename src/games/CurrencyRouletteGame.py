# CurrencyRouletteGame.py
# This game will use q free currency api to get the current exchange rate from USD to ILS.
# Will generate a new random number between 1-100 and will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
#
# Properties
# Difficulty: 1 - 50%, 2 - 49.5%, 3 - 49%, 4 - 48.5%, ... 98 - 2%, 99 - 1.5%, 100 - 1%

# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
#
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import numpy as np
from project.utils.games_utils import *
from currency_converter import CurrencyConverter


def calculate_money_interval(difficulty, total_money):
    min_interval = total_money - 5 - difficulty
    max_interval = total_money - 5 + difficulty
    return [min_interval, max_interval]


# Will get the current currency rate from USD to ILS and will generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +(5 - d))
def get_money_interval(difficulty):
    currency_rate = CurrencyConverter()
    exchange_rate = currency_rate.convert(1, 'USD', 'ILS')
    real_amount = np.random.randint(1, 101)
    interval = calculate_money_interval(difficulty, real_amount)
    return [interval, exchange_rate * real_amount, real_amount]


# A method to prompt a guess from the user to enter a guess of value to a given amount of USD
def get_guess_from_user():
    return get_number("Enter your guess for the value in ILS: ")


# Will call the functions above and play the game.
# Will return True / False if the user lost or won.
def play(game_over):
    win = False
    user_want_to_play = True
    print(custom_text("Welcome to Currency Roulette Game!", GameColors.HEADER))

    while user_want_to_play:
        difficulty = get_number_in_range("What is the difficulty from 1 to 10 when 10 is the easier? ", 1, 11)
        interval, exchange_rate, real_amount = get_money_interval(difficulty)
        print(f'The total value in ILS is: {GameColors.OKCYAN}{round(exchange_rate, 2)}')
        user_guess = get_guess_from_user()
        print(f'Your guess is: {GameColors.OKCYAN}{user_guess}{GameColors.ENDC} and the real amount in ILS is: {GameColors.OKCYAN}{real_amount}')
        if interval[0] <= user_guess <= interval[1]:
            win = True
        is_win_output(win)
        win = False
        user_want_to_play = get_boolean('Do you want to play again')
    print(custom_text(THANK_YOU, GameColors.OKGREEN))
    game_over = not get_boolean('Do you want continue to play with one of our games')
    return game_over


