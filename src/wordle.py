import random
from guess_handler import GuessHandler
from wordle_solver import WordleSolver

def load_words():
    with open("../data/allowed_words.txt") as f:
        words = f.read().splitlines()
    return words 

class Wordle:
    def __init__(self):
        self.word_bank = load_words()
        self.target_word = random.choice(self.word_bank)
        self.guess_handler = GuessHandler(target_word=self.target_word)

    def input_validator(self):
        print('insert 5 letter word:')
        user_input = input()
        
        while user_input not in self.word_bank:
            print('invalid input, please enter 5 letter word:')
            user_input = input()

        return user_input
    
    def run_game(self):
        # print(self.target_word)
        guess_counter = 0
        current_guess = ''
        ws = WordleSolver(self.word_bank)

        while guess_counter < 6 and current_guess != self.target_word:
            current_guess = self.input_validator()
            ws.update_word_bank(current_guess, self.guess_handler.mark_guess(current_guess))
            print(ws.get_ten_words_with_max_entropy())
            self.guess_handler.print_guess(current_guess)
            guess_counter += 1

        if current_guess == self.target_word:
            print('winner')
        else:
            print(f'loser, target word is {self.target_word}')

        print('new game? y/n')
        
        return input() == 'y'


def main():
    new_game = Wordle()
    is_running = True
    while is_running:
        is_running = new_game.run_game()
        new_game.__init__()



if __name__ == "__main__":
    main()