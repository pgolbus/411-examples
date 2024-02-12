from __future__ import annotations

import random
from typing import List


class CardModel:
    """Model for concentration game.

    """

    def __init__(self, seed=None) -> None:
        """Initialize ConcentrationModel.

        """
        values = [
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'j',
            'q',
            'k',
            'a'
        ]
        suits = [
            'c',
            'd',
            'h',
            's'
        ]

        cards = []
        for value in values:
            for suit in suits:
                cards.append(value + suit)

        if seed is not None:
            random.seed(seed)
        cards = self._shuffle(cards=cards)

        self._cards = cards
        self._state = ['down'] * 52
        self._matched = [False] * 52

    def _shuffle(self, cards: List[str]) -> List[str]:
        """Shuffle the cards.

        Parameters
        ----------
        cards : List[str]
            The unshuffled cards.

        Returns
        -------
        cards : List[str]
            The shuffled cards.

        """
        random.shuffle(cards)
        return cards

    @property
    def cards(self) -> List[str]:
        """The cards.

        """
        return self._cards

    @cards.setter
    def cards(self, cards: List[str]) -> None:
        """The cards.

        """
        self._cards = cards

    @property
    def state(self) -> List[str]:
        """The state.

        """
        return self._state

    @state.setter
    def state(self, state: List[str]) -> None:
        """The state.

        """
        self._state = state

    @property
    def matched(self) -> List[bool]:
        """The matched.

        """
        return self._matched

    @matched.setter
    def matched(self, matched: List[bool]) -> None:
        """The matched.

        """
        self._matched = matched

    def game_over(self) -> bool:
        """Checks if the game is over.

        Returns
        -------
        status : bool
            `True` if the game is over. `False` otherwise.

        """
        return all(self._matched)
