# J'importe que la méthode choice du module random
from random import choice

class HangmanLogic:
    def __init__(self):
        self.word_list = self.word_list_loader()
        self.random_word = self.random_word_select()
        self.play_field = "_" * len(self.random_word)
        self.life_count = 0
        self.used_letters = []


    def word_list_loader(self):
        for times in range(2):
            try:
                with open("mots.txt", "r") as file:
                    return file.read().split("\n")[:-1]
            except FileNotFoundError:
                with open("mots.txt", "w") as file:
                    file.write("")
                    return []


    def random_word_select(self):
        return choice(self.word_list)


    def was_used(self, letter):
        if letter in self.used_letters:
            return True


    def is_in_word(self, letter):
        if letter in self.random_word:
            return True


    def add_to_used_letters(self, letter):
        self.used_letters.append(letter)
        self.used_letters.sort()


    def lose_state(self):
        LIFE_LIMIT = 7
        if self.life_count == LIFE_LIMIT:
            return True


    def win_state(self):
        if self.play_field == self.random_word:
            return True

    def modify_play_field(self, letter):
        for index, character in enumerate(self.random_word):
            if letter == character:
                self.play_field = self.play_field[:index] + letter + self.play_field[index + 1 :]

    def add_to_life_count(self):
        self.life_count += 1