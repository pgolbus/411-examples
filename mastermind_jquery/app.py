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

    return jsonify(**data, status=200, mimetype='application/json')

@app.route('/')
def index():

@app.route('/guess', methods=['GET'])
def guess() -> Response:


@app.route('/reset', methods=['POST'])
def reset() -> Response:
    """Reset game.

    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)