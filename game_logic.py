import string

import random


def word_list_loader():
    with open("mots.txt", "r") as file:
        word_list = file.read().split("\n")
        word_list.pop(-1)
    return word_list


def random_word_select(word_list):
    random_word = random.choice(word_list)
    return random_word


def player_prompt(used_letters):
    letter = input("Une lettre: ")
    return letter

class verify_input:
    def is_letter(letter):
        if letter.isalpha():
            return True


    def is_one_char(letter):
        if len(letter) == 1:
            return True


    def was_used(letter, used_letters):
        if letter in used_letters:
            return True


def convert_to_lowercase(letter):
    letter.lower()
    return letter


def add_to_used_letters(letter, used_letters):
    used_letters.append(letter)
    used_letters.sort()

def is_in_word(letter, random_word):
    if letter in random_word:
        return True

def modify_play_field(letter, play_field, random_word):
    for index, character in enumerate(random_word):
        if letter == character:
            play_field = play_field[:index] + letter + play_field[index + 1 :]
    return play_field

class game_state:
    def play_state(used_letters, count, play_field):
        current_state = f"{count}/7\n{play_field}\n{used_letters}\n"
        return current_state


    def lose_state(count):
        if count == 7:
            return True


    def win_state(play_field, random_word):
        if play_field == random_word:
            return True
