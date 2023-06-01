from flask import Flask
from flask_cors import CORS

from controllers.currency_controller import get_currency_game_controller
from controllers.guess_controller import get_guess_game_controller
from controllers.memory_controller import get_memory_game_controller
from controllers.score_controller import get_score_controller, update_score_controller
from queries.score_query import create_and_init_score_table_query

app = Flask(__name__)
CORS(app)

# Init connections to DB
create_and_init_score_table_query()


# Routes
@app.route('/')
def index():
    return 'Welcome to the World of game server.'


app.route('/score', methods=['GET'])(get_score_controller)
app.route('/score/<score>', methods=['PUT'])(update_score_controller)
app.route('/guess', methods=['GET'])(get_guess_game_controller)
app.route('/memory', methods=['GET'])(get_memory_game_controller)
app.route('/currency', methods=['GET'])(get_currency_game_controller)

app.run(host='0.0.0.0', port=5050)
