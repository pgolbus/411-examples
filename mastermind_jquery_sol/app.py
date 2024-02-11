from __future__ import annotations

# you could use a database to track scores over time

from mastermind import MastermindModel

app = Flask(__name__)

MODEL = None
SIZE = 4
PATTERN_COLORS = ["red", "green", "blue", "yellow", "orange", "purple"];
MAX_GUESSES = 10
SEED = 42

def health() -> Response:
    """Health check.

    """

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

def index():
    reset()

def guess() -> Response:
    app.logger.info('Guessing.')
    colors = list([int(color) for color in request.args.to_dict().values()])
    app.logger.info(colors)
                    
    MODEL.guess(colors)
    app.logger.info(MODEL.get_guesses())
    data = {
        'message': 'Guess.'
    }

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

if __name__ == '__main__':
    pass