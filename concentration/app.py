from __future__ import annotations

from concentration import CardModel


MODEL = None
SEED = 42
# The face up card indices
INDICES_UP = []
# The number of guesses
GUESSES = 0



def health() -> Response:
    """Health check.

    """

def reset() -> Response:
    """Reset game.

    """
    # Specify global scope if going to change the value of a global variable.
    global MODEL, INDICES_UP, GUESSES

    app.logger.info('Resetting game.')

    MODEL = CardModel(seed=SEED)
    INDICES_UP = []
    GUESSES = 0


def card(index: int) -> Response:
    """Get card info.

    """
    data = {
        'card': MODEL.cards[index],
        'match': MODEL.matched[index],
        'state': MODEL.state[index]
    }

def select(index: int) -> Response:
    """Select a card.

    """
    app.logger.info(f'Selecting card {index}')
    # Specify global scope if going to change the value of a global variable.
    global MODEL, INDICES_UP, GUESSES

    if len(INDICES_UP) == 2:
        INDICES_UP = []
        MODEL.state = ['down'] * 52

    # Edge cases: Selecting a matched card or selected card.
    if MODEL.matched[index] is True:
        data = {
            'message': 'Card already matched. Try again.'
        }
    elif MODEL.state[index] == 'up':
        data = {
            'message': 'Card already selected. Try again.'
        }

    state = MODEL.state
    state[index] = 'up'
    MODEL.state = state
    INDICES_UP.append(index)

    if len(INDICES_UP) == 2:
        GUESSES += 1
        index1 = INDICES_UP[0]
        index2 = INDICES_UP[1]
        card1 = MODEL.cards[index1]
        card2 = MODEL.cards[index2]

        if card1[0] == card2[0]:
            matched = MODEL.matched
            matched[index1] = True
            matched[index2] = True
            MODEL.matched = matched
    data = {
        'message': 'OK'
    }

def get_guesses() -> Response:
    """Select a card.
    """
    matches = sum([1 if matched else 0 for matched in MODEL.matched]) / 2
    data = {
        'guesses': GUESSES,
        'matches': matches
    }


def index():
    reset()


if __name__ == '__main__':
    pass