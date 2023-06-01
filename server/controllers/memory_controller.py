import numpy as np
from flask import jsonify, request


def generate_sequence(difficulty):
    sequence = []
    for index in range(difficulty):
        sequence.append(np.random.randint(1, 101))
    return sequence


def get_memory_game_controller():
    difficult = request.args.get('difficult')
    sequence = generate_sequence(difficult)
    return jsonify({'numbersToGuess': sequence})
