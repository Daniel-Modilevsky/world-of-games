from flask import jsonify
import threading

from queries.score_query import get_score_query, update_score_query

# Initialize the lock
counter_lock = threading.Lock()


def get_score_controller():
    with counter_lock:
        score = get_score_query()
        return jsonify({'score': score})


def update_score_controller(score):
    with counter_lock:
        new_score = update_score_query(int(score))
        return jsonify({'score': new_score})
