import numpy as np
from flask import jsonify, request


def generate_number(difficulty):
    return np.random.randint(1, difficulty + 1)


def get_guess_game_controller():
    difficult = request.args.get('difficult')
    secret_number = generate_number(difficult)
    return jsonify({'secretNumber': secret_number})
