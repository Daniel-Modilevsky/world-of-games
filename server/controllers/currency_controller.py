from flask import jsonify, request
import numpy as np


def calculate_money_interval(difficulty, total_money):
    min_interval = total_money - 5 - difficulty
    max_interval = total_money - 5 + difficulty
    return [min_interval, max_interval]


def get_currency_game_controller():
    difficult = request.args.get('difficult')
    dollar = np.random.randint(1, 101)
    shekel_interval = calculate_money_interval(int(difficult), dollar)
    return jsonify({'dolarValue': dollar, 'shekelValue': shekel_interval})
