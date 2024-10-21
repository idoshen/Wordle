import math
from guess_handler import GuessHandler

class WordleSolver:
    def __init__(self, word_bank: list):
        '''Initialize WordleSolver'''
        self.current_word_bank = word_bank
        # self.entropy_list = self.get_entropy_list()
        self.entropy_list = []
    
    def update_word_bank(self, word: str, coloring: list):
        '''Update word bank based on user input'''
        word_bank_temp = self.current_word_bank.copy()
        for candidate in self.current_word_bank:
            if not self.matches_coloring(candidate, word, coloring):
                word_bank_temp.remove(candidate)
        
        self.current_word_bank = word_bank_temp
        self.get_entropy_list()
    
    def matches_coloring(self, candidate: str, word: str, coloring: list):
        '''Check if candidate matches coloring'''
        gh = GuessHandler(candidate)
        return gh.mark_guess(word) == coloring

    def get_entropy_list(self):
        '''Get entropy list for current word bank'''
        self.entropy_list = []
        for word_number, word in enumerate(self.current_word_bank):
            print(f"Calculating entropy for word {word_number + 1} of {len(self.current_word_bank)}", end="\r")
            self.entropy_list.append((word, self.calc_entropy(word)))
        print()
        
        self.entropy_list.sort(key=lambda x: x[1])
        reversed_list = self.entropy_list[::-1]
        self.entropy_list = reversed_list

    def calc_entropy(self, word: str):
        '''Calculate entropy for a specific word'''
        entropy = 0
        sum_probabilities = 0
        dict_coloring = self.count_possible_coloring(word)

        for _, count in dict_coloring.items():
            probability = count / len(self.current_word_bank)
            sum_probabilities += probability
            information = -math.log2(probability)
            entropy += probability * information
        
        return entropy
    
    def get_coloring(self, word: str, target_word: str):
        '''Get coloring for a specific word given a target word'''
        gh = GuessHandler(target_word)
        return gh.mark_guess(word)
    
    def count_possible_coloring(self, word:str):
        '''Count possible colorings for a specific word'''
        count_coloring = dict()
        for target in self.current_word_bank:
            coloring = tuple(self.get_coloring(word, target))
            if coloring not in count_coloring.keys():
                count_coloring[coloring] = 1
            else:
                count_coloring[coloring] += 1
        
        return count_coloring
    
    def show_ten_words_with_max_entropy(self):
        '''Show ten words with max entropy'''
        for i in range(min(len(self.entropy_list),10)):
            word, entropy = self.entropy_list[i]
            print(f"{i + 1}. {word} - {entropy}")