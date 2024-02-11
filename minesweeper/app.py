from __future__ import annotations

from flask import Flask, jsonify, make_response, render_template, request, Response
# you could use a database to track scores over time

from minesweeper import MinesweeperModel

app = Flask(__name__)

MODEL = None

@app.route('/health', methods=['GET'])
def health() -> Response:
    """Health check.

    """
    data = {
        'message': 'OK'
    }
    return make_response(data, 200)

@app.route('/')
def index():
    reset()
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset() -> Response:
    """Reset game.

    """
    # Specify global scope if going to change the value of a global variable.
    global MODEL

    # app.logger.info('Resetting game.')

    MODEL = MinesweeperModel()
    app.logger.info(MODEL)

    data = {
        'message': 'Game reset.'
    }
    return make_response(data, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)