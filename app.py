from flask import Flask

from src.Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


@app.route('/')
def hello():
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            score = f.read()
            return f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>The score is <div id="score">{score}</div></h1>
                    </body>
                </html>
            """
    except Exception as e:
        print(e)
        return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
                </body>
            </html>
        """


app.run(host='0.0.0.0', port=5050, debug=True)

