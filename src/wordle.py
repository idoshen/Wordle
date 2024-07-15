import random

def load_words():
    with open("../data/allowed_words.txt") as f:
        words = f.read().splitlines()
    return words 

class Wordle:
    def __init__(self):
        self.word_bank = load_words()
        self.target_word = random.choice(self.word_bank)

    def input_validator(self):
        user_input = ''
        while (user_input not in self.word_bank):
            print('insert 5 letter word:')
            user_input = input()

        return user_input
    
    def run_game(self):
        print(self.target_word)
        guess_counter = 0
        current_guess = ''

        while guess_counter < 6 and current_guess != self.target_word:
            current_guess = self.input_validator()
            guess_counter += 1

        if current_guess == self.target_word:
            print('winner')
        else:
            print('loser')

def main():
    new_game = Wordle()
    new_game.run_game()



if __name__ == "__main__":
    main()