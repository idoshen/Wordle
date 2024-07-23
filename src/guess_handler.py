from termcolor import colored

class GuessHandler:
    def __init__(self, target_word: str):
        '''Initialize GuessHandler'''
        self.target_word = target_word
        self.current_coloring = []
    
    def mark_guess(self, guess: str):
        '''Mark guess based on target word'''
        target_word_list = [*self.target_word]
        char_list = [*guess]
        color_list = ['white'] * 5

        for i, char in enumerate(char_list):
            if char == target_word_list[i]:
                color_list[i] = 'green'
                target_word_list[i] = ''
        
        for i, char in enumerate(char_list):
            if char in target_word_list and color_list[i] == 'white':
                color_list[i] = 'yellow'
                target_word_list[target_word_list.index(char)] = ''
        
        return color_list
    
    def print_guess(self, guess: str):
        '''Print guess with colors'''
        char_list = [*guess]
        color_list = self.mark_guess(guess)
        for i, char in enumerate(char_list):
            print(colored(char, color_list[i]), end='')
            
        print()

    