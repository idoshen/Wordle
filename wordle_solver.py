import math
import re

COLOR_VARIATIONS = math.pow(3,5) - 1

class WordleSolver:

    class TrinaryCounter:
        def __init__(self):
            self.current_coloring = [0] * 5
        
        def next_color(self):
            for i, value in list(enumerate(self.current_coloring))[::-1]:
                if value == 0 or value == 1:
                    self.current_coloring[i] += 1
                    return  
                else:
                    self.current_coloring[i] = 0

    def __init__(self, word_bank: list):
        self.current_word_bank = word_bank
        # self.entropy_list = self.get_entropy()

    def get_entropy(self):
        
        for word in self.current_word_bank:
            self.entropy_list.append((word, self.calc_entropy(word)))

    def calc_entropy(self, word: str):
        entropy = 0
        for coloring in range(COLOR_VARIATIONS):
            possible_words = self.get_possible_words(word, coloring)
            probability = possible_words / len(self.current_word_bank)
            information = -math.log2(probability)
            entropy += probability * information

    def get_possible_words(self, word: str, coloring: list):
        
        word_bank_temp = self.current_word_bank.copy()
        set_list = []
        
        for i, color in enumerate(coloring):
            
            if color == 0:
                set_list.append(set([filtered_word for filtered_word in word_bank_temp if word[i] not in filtered_word]))
            
            elif color == 1:
                set_list.append(set([filtered_word for filtered_word in word_bank_temp if word[i] in filtered_word and filtered_word[i] != word[i]]))
            
            elif color == 2:
                set_list.append(set([filtered_word for filtered_word in word_bank_temp if filtered_word[i] == word[i]]))
    
        new_set = set_list[0]
        for item in set_list:
            new_set = item & new_set
        return new_set



if __name__== '__main__':
    word_bank = [
    "apple", "charm", "crane", "brick", "sweet", "brave", "grace", "clear", "dance", "shine"
    ]
    ws = WordleSolver(word_bank)
    print(ws.get_possible_words('clasm', [0,0,0,1,0]))
