from termcolor import colored

class GuessHandler:
    def __init__(self, target_word: str):
        self.target_word = target_word
    
    def mark_guess(self, guess: str):
        target_word_list = [*self.target_word]
        char_list = [*guess]
        color_list = ['WHITE'] * 5
        print(char_list)

        for i, char in enumerate(char_list):
            if char == target_word_list[i]:
                color_list[i] = 'GREEN'
                char_list[i] = ''
        
        for i, char in enumerate(char_list):
            if char in target_word_list and color_list[i] == 'WHITE':
                color_list[i] = 'YELLOW'
                char_list[i] = ''

        print(color_list)

    