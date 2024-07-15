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
        print(self.target_word)

if __name__ == "__main__":
    main()