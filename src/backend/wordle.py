import random
from guess_handler import GuessHandler
from wordle_solver import WordleSolver
import os

def load_words():
    '''Load words from file'''
    print(os.getcwd())
    with open("./data/allowed_words.txt") as f:
        words = f.read().splitlines()
    return words 

class Wordle:
    def __init__(self):
        '''Initialize game'''
        self.word_bank = load_words()
        self.target_word = random.choice(self.word_bank)
        self.guess_handler = GuessHandler(target_word=self.target_word)

    def input_validator(self):
        '''Validate user input'''
        print('insert 5 letter word:')
        user_input = input()
        
        while user_input not in self.word_bank:
            print('invalid input, please enter 5 letter word:')
            user_input = input()

        return user_input
    
    def run_game(self):
        '''Run game'''
        guess_counter = 1
        current_guess = ''
        ws = WordleSolver(self.word_bank)

        while guess_counter <= 6 and current_guess != self.target_word:
            print(f'guess number {guess_counter}')
            current_guess = self.input_validator()
            self.guess_handler.print_guess(current_guess)

            if current_guess == self.target_word:
                break

            ws.update_word_bank(current_guess, self.guess_handler.mark_guess(current_guess))
            ws.show_ten_words_with_max_entropy()
            guess_counter += 1

        if current_guess == self.target_word:
            print('winner')
        else:
            print(f'loser, target word is {self.target_word}')

        print('new game? y/n')
        
        return input() == 'y'


def main():
    '''Entry point'''
    new_game = Wordle()
    is_running = True
    while is_running:
        is_running = new_game.run_game()
        new_game.__init__()

if __name__ == "__main__":
    main()