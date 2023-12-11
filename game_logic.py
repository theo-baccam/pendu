import string

import random

class WordHandler:
    def word_list_loader():
        with open("mots.txt", "r") as file:
            word_list = file.read().split("\n")
            word_list.pop(-1)
        return word_list


    def random_word_select(word_list):
        random_word = random.choice(word_list)
        return random_word


class VerifyInput:
    def is_letter(letter):
        if letter.isalpha():
            return True


    def is_one_char(letter):
        if len(letter) == 1:
            return True


    def was_used(letter, used_letters):
        if letter in used_letters:
            return True

    def is_in_word(letter, random_word):
        if letter in random_word:
            return True

class LetterHandler:
    def add_to_used_letters(letter, used_letters):
        used_letters.append(letter)
        used_letters.sort()


class GameState:
    def lose_state(count):
        if count == 7:
            return True


    def win_state(play_field, random_word):
        if play_field == random_word:
            return True


def modify_play_field(letter, play_field, random_word):
    for index, character in enumerate(random_word):
        if letter == character:
            play_field = play_field[:index] + letter + play_field[index + 1 :]
    return play_field
