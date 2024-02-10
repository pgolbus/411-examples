from __future__ import annotations

from flask import Flask, make_response, redirect, render_template, request, Response, url_for
# you could use a database to track scores over time

from mastermind import MastermindModel

app = Flask(__name__)

MODEL = None
SIZE = 4
PATTERN_COLORS = ["red", "green", "blue", "yellow", "orange", "purple"]
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

@app.route('guesses', methods=['POST'])
def guesses() -> Response:
    """Check for a win
    
    """
    data = {
        'message': 'OK',
        'guesses': MODEL.get_guesses(),
        'win': MODEL.check_win(),
        'lose': MODEL.check_lose(),
        'guess_count': MODEL.get_guess_count,
    }
    return make_response(data, 200)

@app.route('/lose', methods=['POST'])
def lose() -> Response:


@app.route('/')
def index():
    try:
        win = MODEL.check_win()
        lose = MODEL.check_lose()
        guess_count = MODEL.get_guess_count()
    except:
        app.logger.info('error')
        win = False
        lose = False
        guess_count = 0
    app.logger.info(f'win: {win}, lose: {lose}, guess_count: {guess_count}')
    return render_template('index.html', size=SIZE, pattern_colors=PATTERN_COLORS, guesses=MODEL.get_guesses(), win=win, lose=lose, guess_count=guess_count)

@app.route('/guess', methods=['POST'])
def guess() -> Response:
    app.logger.info('Guessing.')
    app.logger.info(request.form)
    guess = list([int(color) for color in request.form.values()])
    MODEL.guess(guess)
    return redirect(url_for('index'))

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


    data = {
        'message': 'Game reset.'
    }
    return redirect(url_for('index'))

if __name__ == '__main__':
    MODEL = MastermindModel(SIZE,
                            len(PATTERN_COLORS),
                            MAX_GUESSES,
                            seed=SEED)
    app.run(host='0.0.0.0', port=5000, debug=True)