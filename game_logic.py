import string

import random


class WordHandler:
    @staticmethod
    def word_list_loader():
        with open("mots.txt", "r") as file:
            word_list = file.read().split("\n")
            word_list.pop(-1)
        return word_list

    @staticmethod
    def random_word_select(word_list):
        random_word = random.choice(word_list)
        return random_word


class VerifyInput:
    @staticmethod
    def was_used(letter):
        if letter in LetterHandler.used_letters:
            return True

    @staticmethod
    def is_in_word(letter, random_word):
        if letter in random_word:
            return True


class LetterHandler:
    used_letters = []

    @staticmethod
    def add_to_used_letters(letter):
        LetterHandler.used_letters.append(letter)
        LetterHandler.used_letters.sort()


class GameState:
    @staticmethod
    def lose_state(count):
        if count == 7:
            return True

    @staticmethod
    def win_state(play_field, random_word):
        if play_field == random_word:
            return True


def modify_play_field(letter, play_field, random_word):
    for index, character in enumerate(random_word):
        if letter == character:
            play_field = play_field[:index] + letter + play_field[index + 1 :]
    return play_field
