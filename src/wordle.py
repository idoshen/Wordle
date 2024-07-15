import random

def load_words():
    with open("../data/allowed_words.txt") as f:
        words = f.read().splitlines()
    return words 

def main():
    new_game = Wordle()

class Wordle:
    def __init__(self):
        self.word_bank = load_words()
        self.target_word = random.choice(self.word_bank)
        self.current_guess = self.input_validator()

    def input_validator(self):
        user_input = ''
        while (user_input not in self.word_bank):
            print('insert 5 letter word:')
            user_input = input()

        return user_input

if __name__ == "__main__":
    main()