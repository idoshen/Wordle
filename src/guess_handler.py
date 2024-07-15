from termcolor import colored


class GuessHandler:
    def __init__(self, guess: str):
        self.char_list = guess.split()

    