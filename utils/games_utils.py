import os
from time import sleep
THANK_YOU = "Thanks for playing!"


class GameColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


Games = {
    1: 'Memory Game',
    2: 'Guess Game',
    3: 'Currency Roulette Game',
}


def custom_text(text, color=None):
    return f'{color}{text}{GameColors.ENDC}' if color else text


def get_number(text):
    number = input(f'{custom_text(text, GameColors.ENDC)}')
    while number.isnumeric() is False:
        number = input(f'{GameColors.FAIL}Invalid number, {GameColors.ENDC} {text}')
    return int(number)


def is_in_range(number, min_value, max_value):
    return min_value <= number <= max_value


def get_boolean(text):
    result = input(custom_text(f'{text}? type (y/n) ', GameColors.ENDC))
    while result.lower() not in ['y', 'n']:
        result = input(f'{GameColors.FAIL}Invalid answer, {GameColors.ENDC}{text}')
    if result.lower() == 'y':
        return True
    return False


def get_number_in_range(text, min_value, max_value):
    valid_number = False
    number = -1
    while not valid_number:
        number = get_number(text)
        valid_number = is_in_range(number, min_value, max_value)
    return number


def is_win_output(win):
    if win:
        return print(custom_text('Congratulations, you win!', GameColors.OKCYAN))
    return print(custom_text('Nice try but you lose this time, good luck next time!', GameColors.ENDC))


def clean_console():
    # FOR MAC OS PLEASE RUN export TERM=xterm OR ADD ENV PARAM:
    # https://softwaretester.info/pycharm-term-environment-variable-not-set/
    print(custom_text('The console will be clear in 2 seconds.', GameColors.WARNING))
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')



