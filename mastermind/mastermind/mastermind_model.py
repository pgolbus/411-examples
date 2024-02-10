import random

from . import logger


logger = logger.get_logger(__name__)


class MastermindModel():

    def __init__(self, size, pattern_color_count, maxGuesses, seed):
        self.size = size
        self.pattern_color_count = pattern_color_count
        self.maxGuesses = maxGuesses
        if seed is not None:
            random.seed(seed)
        self.secret_code = self.create_secret_code()
        logger.info(f"Secret code: {self.secret_code}")
        # we need to know how many times each color appears in the pattern
        # so we can check the number of correct colors in the wrong position
        self.color_counts = self.count_colors()
        logger.info(f"Color counts: {self.color_counts}")
        self.guesses = []

    def create_secret_code(self):
        # randomly sample size choices from [0..pattern_color_count]
        return [random.randint(0, self.pattern_color_count - 1) for _ in range(self.size)] 

    def count_colors(self):
        color_counts = [0] * self.pattern_color_count
        for color in self.secret_code:
            color_counts[color] += 1
        return color_counts

    def guess(self, guess):
        result = self.evaluate_guess(guess)
        self.guesses.append(guess + result)
        return result

    def evaluate_guess(self, guess):
        result = [0, 0]
        color_counts = self.color_counts.copy()
        # check for correct colors in the correct position
        for i in range(self.size):
            if guess[i] == self.secret_code[i]:
                result[0] += 1
                color_counts[guess[i]] -= 1

        # now check for correct colors in the wrong position
        for i in range(self.size):
            if guess[i] != self.secret_code[i] and color_counts[guess[i]] > 0:
                result[1] += 1
                color_counts[guess[i]] -= 1
        logger.info(f"Guess {guess} result: {result}")
        return result

    def get_guesses(self):
        return self.guesses

    def get_guess_count(self):
        return len(self.guesses)

    def check_win(self):
        return self.guesses[-1][self.size] == self.size
    
    def check_lose(self):
        return self.get_guess_count() >= self.maxGuesses