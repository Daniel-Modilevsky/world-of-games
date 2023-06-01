from enum import Enum


class HttpMethod(Enum):
    GET = 'GET'
    PUT = 'PUT'


TableNames = {
    "SCORE": "score",
}

DEFAULT_IP = '127.0.0.1'
INITIAL_SCORE_VALUE = 0
INITIAL_SCORE_INDEX = 1
MAXIMUM_SCORE = 1000
EnvironmentModes = {
    'DEVELOPMENT': 'development',
    'TESTING': 'testing',
}