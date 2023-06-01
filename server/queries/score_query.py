from decorators.decorator_db import with_db_connection
from utils.constans import TableNames, INITIAL_SCORE_INDEX, INITIAL_SCORE_VALUE


@with_db_connection
def create_and_init_score_table_query(cursor):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {TableNames["SCORE"]} (id INTEGER PRIMARY KEY, value INTEGER)')
    cursor.execute(
        f'INSERT OR IGNORE INTO {TableNames["SCORE"]} (id, value) VALUES ({INITIAL_SCORE_INDEX}, {INITIAL_SCORE_VALUE})')


@with_db_connection
def get_score_query(cursor):
    cursor.execute(f'SELECT value FROM {TableNames["SCORE"]} WHERE id = {INITIAL_SCORE_INDEX}')
    result = cursor.fetchone()[0]
    return result


@with_db_connection
def update_score_query(cursor, score):
    cursor.execute(f'UPDATE {TableNames["SCORE"]} SET value = {score} WHERE id = {INITIAL_SCORE_INDEX}')
    cursor.execute(f'SELECT value FROM {TableNames["SCORE"]} WHERE id = {INITIAL_SCORE_INDEX}')
    result = cursor.fetchone()[0]
    return result
