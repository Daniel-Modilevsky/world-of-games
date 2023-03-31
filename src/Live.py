from project.utils.games_utils import *
from project.games.GuessGame import play as guess_game
from project.games.MemoryGame import play as memory_game
from project.games.CurrencyRouletteGame import play as currency_game


# This function prints out the following text:
# Please choose a game to play:
# 1. Memory Game - a sequence of numbers will appear for 1 second and you have to
# guess it back
# 2. Guess Game - guess a number and see if you chose like the computer
# 3. Currency Roulette - try and guess the value of a random amount of USD in ILS

# Gets an input from the user about the game he chose. After receiving the game number from
# the user, the function will get the level of difficulty with the following text and also save to a
# variable:

# Please choose game difficulty from 1 to 5:
# The function will check the input of the chosen game (the input suppose to be a number between 1 to 3),
# also will check the input of level of difficulty (input should be a number between 1 to 5).
def load_game():
    game_over = False
    while not game_over:
        print(f'''{custom_text('Hello there and welcome to the World of Games (WoG). This is our games:', GameColors.HEADER)}
        {GameColors.OKCYAN}1. Memory Game - {GameColors.WARNING}a sequence of numbers will appear for 1 second and you have guess it back
        {GameColors.OKCYAN}2. Guess Game - {GameColors.WARNING}guess a number and see if you chose like the computer
        {GameColors.OKCYAN}3. Currency Roulette - {GameColors.WARNING}try and guess the value of a random amount of USD in ILS{GameColors.ENDC}''')
        game = get_number_in_range('Please choose a game to play: ', 1, 3)
        if game == 1:
            game_over = memory_game(game_over)
        elif game == 2:
            game_over = guess_game(game_over)
        else:
            game_over = currency_game(game_over)
    print(custom_text('Thank you for playing our games, see you next time!', GameColors.WARNING))
    return



