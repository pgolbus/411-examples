from __future__ import annotations

from flask import Flask, jsonify, make_response, render_template, request, Response
# you could use a database to track scores over time

from mastermind import MastermindModel

app = Flask(__name__)

MODEL = None
SIZE = 4
PATTERN_COLORS = ["red", "green", "blue", "yellow", "orange", "purple"];
MAX_GUESSES = 10
SEED = 42

@app.route('/health', methods=['GET'])
def health() -> Response:
    """Health check.

    """
    data = {
        'message': 'OK'
    }
    return make_response(data, 200)

@app.route('/guesses', methods=['POST'])
def guesses() -> Response:
    """Check for a win
    
    """
    try:
        win = MODEL.check_win()
        lose = MODEL.check_lose()
        guess_count = MODEL.get_guess_count()
    except:
        win = False
        lose = False
        guess_count = 0
    data = {
        'message': 'OK',
        'guesses': MODEL.get_guesses(),
        'win': win,
        'lose': lose,
        'guess_count': guess_count,
    }
    return jsonify(**data, status=200, mimetype='application/json')

@app.route('/')
def index():
    reset()
    return render_template('index.html', size=SIZE, pattern_colors=PATTERN_COLORS)

@app.route('/guess', methods=['GET'])
def guess() -> Response:
    app.logger.info('Guessing.')
    colors = list([int(color) for color in request.args.to_dict().values()])
    app.logger.info(colors)
                    
    MODEL.guess(colors)
    app.logger.info(MODEL.get_guesses())
    data = {
        'message': 'Guess.'
    }
    return make_response(data, 200)

@app.route('/reset', methods=['POST'])
def reset() -> Response:
    """Reset game.

    """
    # Specify global scope if going to change the value of a global variable.
    global MODEL

    # app.logger.info('Resetting game.')

    MODEL = MastermindModel(SIZE,
                            len(PATTERN_COLORS),
                            MAX_GUESSES,  
                            seed=SEED)
    app.logger.info(MODEL)

    data = {
        'message': 'Game reset.'
    }
    return make_response(data, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)